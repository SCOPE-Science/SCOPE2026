#!/usr/bin/env python3
import itertools, collections, cmath, math

PRIMES=(11,13,17,19,23,29,31)
EXPECTED={(3,2,1):19.0,(2,2,1,1):20.0,(2,1,1,1,1):24.0,(1,1,1,1,1,1):28.0}

def profile(A,p):
    cnt=collections.Counter()
    A=list(A)
    for i in range(4):
        for j in range(i+1,4):
            d=(A[i]-A[j])%p
            key=min(d,(-d)%p)
            cnt[key]+=1
    return tuple(sorted(cnt.values(), reverse=True))

def moment(A, coeff, p):
    R={}
    for i,a in enumerate(A):
        for j,b in enumerate(A):
            d=(a-b)%p
            R[d]=R.get(d,0j)+coeff[i]*coeff[j].conjugate()
    return sum(abs(v)**2 for v in R.values())

def affine_ap_order(A,p):
    S=set(A)
    for x in A:
        for d in range(1,p):
            seq=[(x+j*d)%p for j in range(4)]
            if set(seq)==S:
                return seq
    return None

counts={}
representative={}
for p in PRIMES:
    c=collections.Counter()
    for A in itertools.combinations(range(p),4):
        lam=profile(A,p)
        assert lam in EXPECTED, (p,A,lam)
        c[lam]+=1
        representative.setdefault((p,lam),A)
        if lam==(3,2,1):
            assert affine_ap_order(A,p) is not None
    counts[p]=dict(c)

# Representatives: brute-force fourth-root phases attain the minima for all non-AP profiles.
roots=[1+0j,-1+0j,1j,-1j]
for p in PRIMES:
    for lam,target in EXPECTED.items():
        A=representative.get((p,lam))
        if A is None:
            continue
        if lam==(3,2,1):
            seq=affine_ap_order(A,p)
            z=-7/8+1j*math.sqrt(15)/8
            y=-2*(1+z)
            phase_by_point={seq[0]:1+0j,seq[1]:1+0j,seq[2]:y,seq[3]:y*z}
            coeff=[phase_by_point[a] for a in A]
            val=moment(A,coeff,p)
            assert abs(val-19.0)<1e-10,(p,A,val)
        else:
            best=1e9
            for tail in itertools.product(roots, repeat=3):
                coeff=(1+0j,)+tail
                best=min(best,moment(A,coeff,p))
            assert abs(best-target)<1e-10,(p,A,lam,best,target)

# Exact one-variable progression reduction: min of (r-1)^2+r^2 is 1/2 at r=1/2.
for r in [j/1000 for j in range(2001)]:
    assert (r-1)**2+r*r >= 0.5-1e-12
assert abs((0.5-1)**2+0.5**2-0.5)<1e-15

print('VERIFY_OK', 'profile_counts=', counts)
