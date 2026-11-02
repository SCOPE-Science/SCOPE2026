#!/usr/bin/env python3
"""Exact independent cycle-graph partition checks (no external packages)."""
from collections import defaultdict
from itertools import permutations


def poly_add(a,b,scale=1):
    c=a.copy()
    for k,v in b.items():
        c[k]=c.get(k,0)+scale*v
        if not c[k]: del c[k]
    return c


def poly_mul(a,b):
    c=defaultdict(int)
    for (d,e),v in a.items():
        for (f,g),w in b.items(): c[d+f,e+g]+=v*w
    return {k:v for k,v in c.items() if v}


def det_one_minus_transition(kind):
    states=[(1,1),(1,2),(2,1),(2,2)] if kind=='two' else [(1,),(2,)]
    m=len(states)
    entries=[]
    for i,p in enumerate(states):
        row=[]
        for j,q in enumerate(states):
            a=p[0]; c=q[0]
            if kind=='two':
                b=p[1]; e=q[1]
                okay=not (a==c==2 and b==1) and not (b==e==2 and c==1)
                val={(a+b,b):1} if okay else {}
            else:
                val={}
                for b in (1,2):
                    if not (a==c==2 and b==1): val[(a+b,b)]=1
            row.append(poly_add({(0,0):1} if i==j else {},val,-1))
        entries.append(row)
    answer={}
    for perm in permutations(range(m)):
        inversion=sum(perm[i]>perm[j] for i in range(m) for j in range(i+1,m))
        product={(0,0):1}
        for i,j in enumerate(perm): product=poly_mul(product,entries[i][j])
        answer=poly_add(answer,product,-1 if inversion%2 else 1)
    return answer


def coefficients_from_det(det,max_n):
    """If D=det(I-T), then F=-z D_z/D; return coefficient dicts."""
    assert det.get((0,0))==1
    terms={(d,e):-v for (d,e),v in det.items() if d>0}
    f=[{} for _ in range(max_n+1)]
    for n in range(1,max_n+1):
        row=defaultdict(int)
        for (d,e),weight in terms.items():
            if d==n: row[e]+=d*weight
            if d<=n:
                for t,v in f[n-d].items():row[e+t]+=weight*v
        f[n]={t:v for t,v in row.items() if v}
    return f


def ld_set(s,n):
    # Independent, direct open-neighborhood identity test.
    outside=[i for i in range(n) if not ((s>>i)&1)]
    signatures=[]
    for i in outside:
        neighbors=tuple(j for j in ((i-1)%n,(i+1)%n) if ((s>>j)&1))
        if not neighbors: return False
        signatures.append(neighbors)
    return len(set(signatures))==len(outside)


def dominates(s,n):
    for i in range(n):
        if not ((s>>i)&1) and not ((s>>((i-1)%n))&1) and not ((s>>((i+1)%n))&1):
            return False
    return True


def brute(n):
    both=defaultdict(int); one=defaultdict(int)
    total=(1<<n)-1
    for s in range(1<<n):
        # 1=LD part, 0=dominating part.
        if not ld_set(s,n):continue
        d=total^s
        if not dominates(d,n):continue
        one[s.bit_count()]+=1
        if ld_set(d,n):both[s.bit_count()]+=1
    return dict(one),dict(both)


def forbidden_equivalence(n):
    # Compare direct graph predicates to independently implemented cyclic-word exclusions.
    for s in range(1<<n):
        w=''.join(str((s>>i)&1) for i in range(n))
        one=ld_set(s,n) and dominates(((1<<n)-1)^s,n)
        cyc=w*3
        predicted=not any(p in cyc for p in ('000','111','00100'))
        if one!=predicted:raise AssertionError(('forbidden',n,s))
        both=one and ld_set(((1<<n)-1)^s,n)
        predicted2=predicted and '11011' not in cyc
        if both!=predicted2:raise AssertionError(('two-sided forbidden',n,s))


def main():
    A={(0,0):1,(2,1):-1,(3,2):-1,(4,2):-1,(5,2):-1,(6,3):-1}
    B={(0,0):1,(2,1):-1,(4,2):-1,(5,2):-1,(5,3):-1,(6,3):-1,(8,4):-1}
    assert det_one_minus_transition('one')==A
    assert det_one_minus_transition('two')==B
    f=coefficients_from_det(A,16); g=coefficients_from_det(B,16)
    for n in range(5,17):
        a,b=brute(n)
        assert f[n]==a,(n,'one',f[n],a)
        assert g[n]==b,(n,'two',g[n],b)
        forbidden_equivalence(n)
        print('n=%d DLDS=%d both_LD=%d'%(n,sum(a.values()),sum(b.values())))
    print('VERIFY_OK n=5..16 all labelled 2^n subsets; determinants via permutations; independent neighborhood and forbidden-word checks')

if __name__=='__main__':main()
