#!/usr/bin/env python3
"""Independent finite-field projective orbit and Kummer-support census.
Scientific references: Nevins--Pumpluen, arXiv:2610.30921; Brown--Pumpluen,
arXiv:1703.00718; Pumpluen, arXiv:2403.03263.
"""
from collections import Counter
from math import gcd

def expected_degree_four(q):
    N = (q**4-1)//(q-1)
    return Counter({
        (4,N): (q-1)*(q+1)**2//4,
        (4,2*N): (q-1)//2,
        (4,4*N): 2,
        (8,2*N): (q-1)//2,
        (8,4*N): 1,
    })

def by_kummer_support(q,n):
    assert (q-1)%n == 0
    N=(q**n-1)//(q-1)
    out=Counter()
    for mask in range(1,1<<n):
        S=[i for i in range(n) if mask&(1<<i)]
        if S==[0]: continue
        g=n
        for i in S: g=gcd(g,i)
        r=n//g
        h=n
        for i in S: h=gcd(h,i-S[0])
        e=n//h
        projective=(q-1)**(len(S)-1)
        assert projective%e==0
        out[(n*n//r,N*n//e)] += projective//e
    return out

def by_cyclic_projective_orbits(q,n):
    N=(q**n-1)//(q-1)
    order=q**n-1
    seen=set()
    out=Counter()
    for k in range(1,N):
        if k in seen: continue
        orbit=[]
        v=k
        while v not in seen:
            orbit.append(v)
            seen.add(v)
            v=(q*v)%N
        assert v==k
        e=len(orbit)
        # Primitive field generator g, a=g**k:
        # sigma**r(a)=a iff order | k*(q**r-1).
        r=next(r for r in range(1,n+1) if n%r==0 and (k*(q**r-1))%order==0)
        out[(n*n//r,N*n//e)]+=1
    assert len(seen)==N-1
    return out

def main():
    for q,n in ((5,4),(9,4),(13,4),(17,4),(7,6)):
        left=by_kummer_support(q,n)
        right=by_cyclic_projective_orbits(q,n)
        assert left==right,(q,n,left,right)
        if n==4:
            assert left==expected_degree_four(q),(q,left)
            assert sum(left.values())==(q**3+q**2+3*q+7)//4
            assert sum(c for (dim,autom),c in left.items() if autom==4*((q**4-1)//(q-1)))==3
        print('checked',q,n,'classes',sum(left.values()),'strata',len(left))
    print('VERIFY_OK')
if __name__=='__main__':
    main()
