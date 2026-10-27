"""Independent numerical and rational checks for periodically pulsed group contagion.

Run with Python 3: python verify.py
No external dependencies.
"""
from fractions import Fraction as Q
from random import Random
from math import isclose


def prod(it):
    v=1
    for x in it:v*=x
    return v


def active(p,r,eta):
    return [r*p[i]+eta*(1-p[i])*prod(p[j] for j in range(len(p)) if j!=i) for i in range(len(p))]


def period(p,r,eta,gaps):
    z=p[:]
    for a in gaps:
        z=active(z,r,eta)
        for _ in range(a):z=[r*t for t in z]
    return z


def scalar(x,n,r,eta,gaps):
    for a in gaps:
        x=r**a*(r*x+eta*x**(n-1)*(1-x))
    return x


def mval(n):
    return Q((n-2)**(n-2),(n-1)**(n-1))


def critical(n,r,a):
    return (r**(-a)-r)/mval(n)


def check():
    rng=Random(20261021)
    num=0
    for n in range(3,9):
        for gaps in ((1,1),(0,2),(2,0),(1,0,2),(0,0,3),(1,1,1),(0,1,2)):
            for _ in range(15):
                r=rng.uniform(.3,.995)
                eta=rng.uniform(.001,1)
                p=[rng.random() for _ in range(n)]
                out=period(p,r,eta,gaps)
                d=max(p)-min(p)
                q=max(r,abs(r-eta))
                predicted=d*(q**len(gaps))*(r**sum(gaps))
                assert max(out)-min(out)<=predicted+4e-14
                assert all(0<=v<=1 for v in out)
                x=rng.random()
                y=period([x]*n,r,eta,gaps)
                assert max(abs(v-scalar(x,n,r,eta,gaps)) for v in y)<5e-14
                num+=1
    r=Q(9,10); eta=Q(38,45);x=Q(1,2)
    assert critical(3,r,1)==eta
    assert scalar(x,3,r,eta,(1,1))==x
    assert scalar(x,3,r,eta,(0,2))==Q(8081,16200)
    assert x-scalar(x,3,r,eta,(0,2))==Q(19,16200)
    # A nonuniform schedule has strict gain deficit at the uniform threshold.
    for n in range(3,9):
        rr=0.995; a=2; e=float(critical(n,Q(995,1000),a))
        if e>1:continue
        for gaps in ((0,4),(1,3),(0,1,3),(0,0,4)):
            if sum(gaps)!=a*len(gaps):continue
            vals=[scalar(j/1000,n,rr,e,gaps)-j/1000 for j in range(1,1001)]
            assert max(vals)<1e-12
    r=Q(99,100); e=Q(1,2); a=2
    assert critical(7,r,a)<e<critical(8,r,a)
    # Deterministic orbit checks away from the saddle-node, not proofs of global claims.
    for gaps,expect in [((1,1),'persist'),((0,2),'extinct')]:
        rr=.9; ee=float(eta)+0.00001
        z=[0.8]*3
        for _ in range(25000):z=period(z,rr,ee,gaps)
        if expect=='persist':assert z[0]>.4
        else:assert max(z)<1e-6
    print('CHECK_OK: %d direct schedule/symmetry/contraction tests; rational witnesses; group-size cutoff; trajectory checks'%num)


if __name__=='__main__':check()
