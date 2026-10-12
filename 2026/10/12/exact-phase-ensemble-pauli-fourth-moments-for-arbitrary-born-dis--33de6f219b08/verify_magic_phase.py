"""Reproduce finite phase-ensemble checks of a Pauli-fourth-moment identity.
Python >=3.9; standard library only."""
import cmath
import itertools
import math
import random


def theoretical(p):
    n=len(p)
    assert n>1 and n&(n-1)==0
    c=[sum(p[x]*p[x^a] for x in range(n)) for a in range(n)]
    return 4*sum(x*x for x in c[1:])-2*c[0]**2+3*sum(x**4 for x in p)


def direct_phases(p,roots):
    n=len(p)
    total=0.
    for z in itertools.product(roots, repeat=n):
        v=[math.sqrt(p[x])*z[x] for x in range(n)]
        moment=0.
        for a in range(n):
            for b in range(n):
                expectation=sum(v[x].conjugate()*v[x^a]*(-1 if (x&b).bit_count()%2 else 1) for x in range(n))
                moment+=abs(expectation)**4/n
        total+=moment
    return total/len(roots)**n


def orbit_moment(p):
    n=len(p)
    out=0.
    for a in range(n):
        if a==0:
            out+=sum(sum(p[x]*p[x^t] for x in range(n))**2 for t in range(n))
        else:
            q=[p[x]*p[x^a] for x in range(n) if x<(x^a)]
            out+=6*sum(x*x for x in q)+24*sum(x*y for i,x in enumerate(q) for y in q[i+1:])
    return out


def main():
    roots=[cmath.exp(2j*math.pi*k/5) for k in range(5)]
    checked=0
    cases=[[0.5,0.5],[0.1,0.9],[.25]*4,[.1,.2,.3,.4],[1.,0.,0.,0.], [0.,0.5,0.5,0.]]
    for p in cases:
        lhs=direct_phases(p,roots)
        rhs=theoretical(p)
        assert abs(lhs-rhs)<1e-10,(p,lhs,rhs)
        assert abs(orbit_moment(p)-rhs)<1e-10
        checked+=1
    rng=random.Random(28027)
    for n in (2,4,8):
        for _ in range(150):
            r=[rng.random()**2 for x in range(n)]
            if _%5==0:r[0]=0
            p=[x/sum(r) for x in r]
            lhs=orbit_moment(p)
            rhs=theoretical(p)
            assert abs(lhs-rhs)<1e-11,(n,lhs,rhs)
            checked+=1
    for n in range(1,9):
        N=2**n
        p=[1./N]*N
        exact=theoretical(p)
        expected=(4*N*N-6*N+3)/N**3
        assert abs(exact-expected)<1e-11
        assert expected*N/4<=1+1e-12
        checked+=1
    print(f'VERIFY_OK: {checked} ensemble/orbit/flat-dimensional checks; six exhaustive fifth-root phase-grid ensembles')

if __name__=='__main__':main()
