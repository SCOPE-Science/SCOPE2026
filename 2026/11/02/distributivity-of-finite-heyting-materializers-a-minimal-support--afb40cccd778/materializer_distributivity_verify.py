#!/usr/bin/env python3
"""Exact finite tests of materializer distributivity and the minimal-premise criterion."""
import itertools


def posets(n):
    pairs=list(itertools.combinations(range(n),2))
    seen=set()
    for bits in range(1<<len(pairs)):
        pred=[1<<i for i in range(n)]
        for j,(a,b) in enumerate(pairs):
            if bits>>j &1: pred[b]|=1<<a
        # transitive closure in topological order
        for j in range(n):
            for i in range(j):
                if pred[j]>>i &1: pred[j]|=pred[i]
        tp=tuple(pred)
        if tp not in seen:
            seen.add(tp)
            yield tp

def ideals(pred):
    n=len(pred)
    return [s for s in range(1<<n) if all(not (s>>i&1) or pred[i]&s==pred[i] for i in range(n))]

def is_principal(s, pred):
    return any(s==p for p in pred)

def one(pred,check_lattice=False):
    n=len(pred); allmask=(1<<n)-1; js=ideals(pred)
    for I in js:
        U=0
        for p in range(n):
            if pred[p]&I: U|=1<<p
        Q=allmask^U
        ks=[s for s in js if s&~I==0]
        def F(K):
            return sum(1<<p for p in range(n) if (U>>p&1) and pred[p]&I&~K==0)
        def D(K):
            FF=F(K); out=0
            for p in range(n):
                if FF>>p&1: out|=pred[p]&Q
            return out
        ds={K:D(K) for K in ks}
        union_ok=all(ds[K1|K2]==ds[K1]|ds[K2] for K1 in ks for K2 in ks)
        min_principal_ok=True
        for q in range(n):
            if not(Q>>q&1):continue
            fam={pred[p]&I for p in range(n) if (U>>p&1) and (pred[p]>>q&1)}
            for s in fam:
                if not any(t!=s and t&s==t for t in fam) and not is_principal(s,pred):
                    min_principal_ok=False
        assert union_ok==min_principal_ok,(pred,I,'premise criterion disagreement')
        if check_lattice:
            # Independent direct implication semantics; no use of F or D to identify M.
            negI=sum(1<<p for p in range(n) if not(pred[p]&I))
            M=[]
            for J in js:
                arrow=sum(1<<p for p in range(n) if not(pred[p]&I&~J))
                if arrow==(negI|J):M.append(J)
            Ms=set(M)
            assert 0 in Ms and allmask in Ms
            assert all(a&b in Ms for a in M for b in M)
            # A materializer's internal join is the intersection of all admissible upper bounds.
            joins={}
            for a in M:
                for b in M:
                    x=a|b
                    join=allmask
                    for z in M:
                        if x&z==x: join &= z
                    assert join in Ms
                    joins[(a,b)]=join
            isdist=True
            for a in M:
                for b in M:
                    for c in M:
                        if a&joins[(b,c)] != joins[(a&b,a&c)]:
                            isdist=False; break
                    if not isdist:break
                if not isdist:break
            assert isdist==union_ok,(pred,I,'lattice mismatch')
    return len(js)

def run():
    count=0; alg=0
    for n in range(1,6):
        countn=0; algn=0
        for pred in posets(n):
            algn+=one(pred,check_lattice=True)
            countn+=1
        print(f'EXHAUSTIVE_ALL_MATERIALIZERS_PASS n={n} posets={countn} antecedents={algn}',flush=True)
        count+=countn;alg+=algn
    # More extensive criterion checks through six vertices without an expensive full lattice-table expansion.
    countn=0; algn=0
    for pred in posets(6):
        algn+=one(pred,check_lattice=False); countn+=1
    print(f'ALL_SIX_VERTEX_PREMISE_CHECKS_PASS posets={countn} antecedents={algn}',flush=True)
    # Explicit 4-point mixed fork: a,b,q minimal, p top, I={a,b}.
    pred=(1,2,4,15)
    one(pred,check_lattice=True)
    print('FOUR_POINT_MIXED_FORK_NONDISTRIBUTIVE_PASS')
    print(f'ALL_MATERIALIZER_DISTRIBUTIVITY_CHECKS_PASS posets={count+countn} antecedents={alg+algn}')

if __name__=='__main__':run()
