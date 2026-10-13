"""Standalone checks for bounded-count graded modalities on finite equivalence frames."""
from itertools import product, combinations
from collections import Counter
from math import comb

def poly_mul(a,b,cap):
    z=[0]*(cap+1)
    for i,x in enumerate(a[:cap+1]):
        if x:
            for j,y in enumerate(b[:cap-i+1]):
                z[i+j]+=x*y
    return z

def poly_pow(a,k,cap):
    z=[1]+[0]*cap
    for _ in range(k): z=poly_mul(z,a,cap)
    return z

def exponent_poly(S,q,K):
    M=max(S)
    b=[1]*(K+1); c=[0]+[1]*K
    b0=[1]*K; c0=[0]+[1]*(K-1)
    n=poly_mul(c,poly_pow(b,q-1,M),M)
    a=poly_mul(c0,poly_pow(b0,q-1,M),M)
    return q*(sum(a[s] for s in S if s<=M)+sum(n[i]-a[i] for i in range(M+1)))

def exemplar_types(S,q,K):
    observed=set()
    for n in S:
        for col in product(range(q),repeat=n):
            freq=Counter(col)
            t=tuple(min(K,freq.get(j,0)) for j in range(q))
            observed.update((j,t) for j in set(col))
    return observed

def type_formula(S,q,K):
    M=max(S); out=set()
    for t in product(range(K+1),repeat=q):
        capped=K in t
        if capped:
            eligible=sum(t)<=M
        else:
            eligible=sum(t) in S
        if eligible:out.update((c,t) for c in range(q) if t[c]>=1)
    return out

def refinement(block_sizes,q,K):
    n=sum(block_sizes)
    groups=[]; cursor=0
    for b in block_sizes:
        groups.append(tuple(range(cursor,cursor+b))); cursor+=b
    group_for={u:g for g in groups for u in g}
    states=[]
    for col in product(range(q),repeat=n):
        for u in range(n): states.append((col,u))
    classes=[col[u] for col,u in states]
    def compress(v):
        m={}; a=[]
        for t in v:
            if t not in m:m[t]=len(m)
            a.append(m[t])
        return a
    classes=compress(classes)
    for depth in range(n+2):
        new=[]
        for col,u in states:
            prev=[classes[states.index((col,v))] for v in group_for[u]]
            ct=Counter(prev)
            new.append((classes[states.index((col,u))],tuple(sorted((j,min(K,v)) for j,v in ct.items()))))
        new=compress(new)
        if new==classes:break
        classes=new
    oracle=[(col[u],tuple(min(K,sum(col[v]==j for v in group_for[u])) for j in range(q))) for col,u in states]
    for i in range(len(states)):
        for j in range(i):
            assert (classes[i]==classes[j]) == (oracle[i]==oracle[j])
    return len(set(classes)),len(states)

def complete_term_algebra(block_sizes,K):
    n=sum(block_sizes); units=[]; gs=[]; z=0
    for b in block_sizes:
        gs.append(tuple(range(z,z+b)));z+=b
    for col in product((0,1),repeat=n):
        for u in range(n):units.append((col,u))
    N=len(units); top=(1<<N)-1
    seed=sum(1<<i for i,(col,u) in enumerate(units) if col[u])
    def diamond_j(mask,j):
        out=0
        for i,(col,u) in enumerate(units):
            block=next(g for g in gs if u in g)
            hit=sum(bool(mask & (1<<units.index((col,v)))) for v in block)
            if hit>=j: out|=1<<i
        return out
    algebra={0,top,seed,top^seed};iteration=0
    while True:
        iteration+=1; current=list(algebra);new=set(current)
        for a in current:
            new.add(top^a)
            for j in range(1,K+1):new.add(diamond_j(a,j))
            for b in current:new.add(a&b)
        if new==algebra:break
        assert iteration<15 and len(new)<=4096
        algebra=new
    return len(algebra),N

def run():
    direct=0; formula=0; stable=0; clos=0
    for M in range(1,6):
        for mask in range(1,1<<M):
            if not mask&(1<<(M-1)):continue
            S=tuple(i+1 for i in range(M) if mask&(1<<i))
            for q in range(1,5):
                for K in range(1,5):
                    expected=type_formula(S,q,K)
                    assert len(expected)==exponent_poly(S,q,K), (S,q,K)
                    formula+=1
                    if sum(q**s for s in S) <=50000:
                        assert expected==exemplar_types(S,q,K),(S,q,K)
                        direct+=sum(q**s for s in S)
    for parts in [(1,),(2,),(3,),(1,1),(1,2),(2,1),(2,2),(1,3),(1,1,2),(1,2,1)]:
        for K in (1,2,3):
            for q in (1,2,3):
                if q**sum(parts)>400:continue
                count,states=refinement(parts,q,K)
                assert count==exponent_poly(set(parts),q,K)
                stable+=states
    for parts,K in [((1,),1),((2,),1),((3,),1),((1,1),1),((1,2),1),((2,1),2),((1,2),2),((3,),2),((1,1,1),2)]:
        count,states=complete_term_algebra(parts,K)
        exp=exponent_poly(set(parts),2,K)
        assert count==2**exp,(parts,K,count,exp)
        clos+=states
    # Distinct cluster-size spectra produce different clone exponents for sufficiently large arity.
    for K in (1,2,3):
        for M in range(1,6):
            allS=[set(i+1 for i in range(M) if mask&(1<<i)) for mask in range(1,1<<M)]
            for a,b in combinations(allS,2):
                same=(max(a)==max(b)) if K==1 else (a==b)
                assert (exponent_poly(a,32,K)==exponent_poly(b,32,K))==same,(a,b,K)
    print('VERIFY_OK formula_cases',formula,'exhaustive_valuations',direct,'partition_refinement_states',stable,'term_algebra_instances',9,'term_algebra_pointed_states',clos,'spectral_reconstruction_checked',True)
    for S in [{2},{1,2},{1,3},{2,3},{1,2,3}]:
        print('S',sorted(S),'E_ordinary_q4',exponent_poly(S,4,1),'E_two_q4',exponent_poly(S,4,2))
if __name__=='__main__': run()
