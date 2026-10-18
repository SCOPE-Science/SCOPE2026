"""Exact finite-field checks for a cubic-graph Gabor window.

Run with Python 3; no third-party dependencies. Fourier zeros are checked
exactly by prime-cyclotomic coefficient counts, not floating-point tolerances.
"""
from math import isqrt

PRIMES = (5, 7, 11, 13, 17, 19, 23, 29, 31, 37)

def prime(p):
    return p >= 2 and all(p % t for t in range(2, isqrt(p)+1))

def residues(p):
    return {u*u % p for u in range(p)}

def curve(p):
    return {(t,t**3 % p) for t in range(p)}

def zero_cyclotomic(exponents,p):
    """A sum of p-th roots vanishes iff all p multiplicities are equal."""
    counts = [0]*p
    for a in exponents:
        counts[a%p]+=1
    return len(set(counts)) == 1

def verify_one(p):
    assert prime(p) and p >= 5
    C=curve(p)
    assert len(C)==p
    squares=residues(p)
    z=0
    empty=single=double=0
    for h in range(p):
        for k in range(p):
            match=[(x,y) for (x,y) in C if ((x-h)%p,(y-k)%p) in C]
            m=len(match)
            predicted=0
            if h==0:
                predicted=p if k==0 else 0
            else:
                inv=lambda a: pow(a,-1,p)
                t=((k-(h**3 * inv(4))%p)*inv(3*h))%p
                predicted=0 if t not in squares else (1 if t==0 else 2)
            assert m==predicted,(p,h,k,m,predicted)
            if m==0: empty+=1
            elif m==1: single+=1
            elif m==2: double+=1
            elif m!=p: raise AssertionError((p,h,k,m))
            # One or two distinct pth roots cannot cancel for odd p.
            if m in (1,2):
                assert all(not zero_cyclotomic([a*x+b*y for x,y in match],p)
                           for a in range(p) for b in range(p))
            if m==p:
                for a in range(p):
                    for b in range(p):
                        vanish=zero_cyclotomic([a*x+b*y for x,y in match],p)
                        expected=(b==0 and a!=0) or (p%3==2 and a==0 and b!=0)
                        assert vanish==expected,(p,a,b,vanish,expected)
                        z+=not vanish
    assert empty==(p*p-1)//2, (p,empty)
    assert single==p-1,(p,single)
    assert double==(p-1)*(p-1)//2,(p,double)
    expected_rank=p*p*(p*p+1)//2-(p-1)*(1+(p%3==2))
    observed= (single+double)*p*p+z
    assert observed==expected_rank,(p,observed,expected_rank)
    # Double intersections have each phase difference with multiplicity p.
    # For each double shift, 2 is present p times; every
    # 2 cos(pi*j/p), 1 <= j <= (p-1)/2, is present 2p times.
    h=1; k=((h**3*pow(4,-1,p))+3*h)%p
    points=[(x,y) for x,y in C if ((x-h)%p,(y-k)%p) in C]
    assert len(points)==2
    counts={j:0 for j in range(p)}
    (x0,y0),(x1,y1)=points
    for a in range(p):
        for b in range(p):
            j=(a*(x0-x1)+b*(y0-y1))%p
            counts[j]+=1
    assert set(counts.values())=={p}
    print('p=',p,'shift populations=',(empty,single,double),
          'zero-shift nonzeros=',z,'rank=',observed,
          'nullity=',p**4-observed)

if __name__=='__main__':
    for p in PRIMES: verify_one(p)
    print('ALL EXACT CHECKS PASSED')
