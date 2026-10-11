#!/usr/bin/env python3
"""Exact additive-convolution checks for phase-only moments on F_3^2.

Run with Python 3. No third-party dependencies. Finite checks supplement,
not replace, the algebraic classification in the accompanying manuscript.
"""
from itertools import product
from collections import Counter

P=3
SUPPORT=((1,0),(2,0),(0,1),(0,2))

def counts(m):
    o=Counter()
    for I in product(range(4),repeat=m):
        t=tuple(sum(SUPPORT[j][k] for j in I)%P for k in (0,1))
        o[t]+=1
    return o

def moment(z,m):
    """Exact moment for Gaussian-integer phases on unit circle."""
    o={t:0j for t in product(range(P),repeat=2)}
    for I in product(range(4),repeat=m):
        t=tuple(sum(SUPPORT[j][k] for j in I)%P for k in (0,1))
        v=1+0j
        for j in I:v*=z[j]
        o[t]+=v
    return int(round(sum(v.real*v.real+v.imag*v.imag for v in o.values())))

def main():
    for m in range(1,9):
        c=counts(m)
        target=(4**(2*m)+4*(2**(2*m))+4)//9
        assert sum(v*v for v in c.values()) == target,(m,c,target)
        assert sum(c.values())==4**m
    assert sum(counts(2).values()) == 16
    assert counts(2)[(0,0)] == 4
    assert counts(3)[(0,0)] == 4
    # The fourth-moment optimizing torus contains phases outside cube roots.
    z=(1+0j,-1+0j,1+0j,-1+0j)
    assert moment(z,2)==36
    assert moment(z,3)<484
    # Check every fourth-root phase vector, hence many nontrivial equality cases.
    mu4=(1+0j,-1+0j,0+1j,0-1j)
    count4=count6=0
    for z in product(mu4,repeat=4):
        s2=moment(z,2);s3=moment(z,3)
        assert s2<=36 and s3<=484
        if s2==36:
            count4+=1
            assert z[0]*z[1]==z[2]*z[3]
        if s3==484:
            count6+=1
            assert len(set(z))==1
    assert count4==64,(count4,count6)
    assert count6==4,(count4,count6)
    # Exhaustive cube-root phase arithmetic as exponents modulo 3.
    # Equality at m=3 iff all cube phases agree and opposite-pair products match.
    complete=[]
    for r in product(range(3),repeat=4):
        all_match=(r[0]+r[1]-r[2]-r[3])%3==0
        if all_match:complete.append(r)
    assert len(complete)==27
    normalized={(tuple((x-r[0])%3 for x in r)) for r in complete}
    assert len(normalized)==9
    for x,y in product(range(3),repeat=2):
        r=(x,-x,y,-y)
        assert tuple(t%3 for t in r) in complete
    print('PASS: exact convolution identities m=1..8; fourth-root phases=256;')
    print('      optimizing phase classes: fourth-root L4=64, L6=4; cube-root projective L6=9')

if __name__ == '__main__': main()
