"""Independent finite-field checks of unit commutativity in truncated quiver algebras.
Run with Python 3, no third-party dependencies.
"""
from itertools import product,combinations
from math import gcd


def fortuin_kasteleyn(q,n,edges):
    Q=(q-1)**2
    m=len(edges)
    total=0
    for mask in range(1<<m):
        parent=list(range(n))
        def find(i):
            while parent[i]!=i:
                i=parent[i]
            return i
        selected=0
        for j,(u,v) in enumerate(edges):
            if mask>>j&1:
                selected+=1
                ru,rv=find(u),find(v)
                parent[ru]=rv
        components=len({find(i) for i in range(n)})
        total+=(q-1)**selected*Q**components
    return q**m*total


def brute_commuting(q,n,edges):
    m=len(edges)
    diag=list(product(range(1,q),repeat=n))
    units=[(d,a) for d in diag for a in product(range(q),repeat=m)]
    ans=0
    for (d,a) in units:
        for (e,b) in units:
            if all((d[u]*b[i]+a[i]*e[v]-e[u]*a[i]-b[i]*d[v])%q==0
                    for i,(u,v) in enumerate(edges)):
                ans+=1
    return ans,len(units)


def test():
    cases=[
        (2,3,[(0,1),(1,2),(2,0)]),
        (3,2,[(0,1)]),
        (5,2,[(0,1)]),
        (3,2,[(0,1),(0,1)]),
        (3,3,[(0,1),(1,2)]),
        (3,3,[(0,1),(1,2),(2,0)]),
        (3,3,[(0,1),(1,2),(0,2)]),
        (3,2,[(0,0),(0,1)]),
        (3,3,[(0,1),(2,1)]),
        (2,4,[(0,1),(1,2),(2,3),(3,0),(0,2)]),
    ]
    for q,n,edges in cases:
        actual,size=brute_commuting(q,n,edges)
        expect=fortuin_kasteleyn(q,n,edges)
        assert actual==expect,(q,n,edges,actual,expect)
        assert actual%size==0
        print('q=',q,'vertices=',n,'arrows=',len(edges),'units=',size,
              'commuting_pairs=',actual,'classes=',actual//size)
    for q in [3,5,7]:
        for ell in [3,4,5]:
            edges=[(i,(i+1)%ell) for i in range(ell)]
            total=fortuin_kasteleyn(q,ell,edges)
            group_size=(q-1)**ell*q**ell
            # Formula P=(q-1)^(-ell)*(1+(q-2)*q^(1-ell))
            # exact cleared-denominator check
            assert total*(q-1)**ell*q**(ell-1)==group_size**2*(q**(ell-1)+q-2)
    print('VERIFY_OK')


if __name__=='__main__':
    test()
