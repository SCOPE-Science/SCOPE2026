#!/usr/bin/env python3
"""Independent finite checks of the cubic-modulus parabola fourth-moment formulas.

Uses exact Gaussian-integer arithmetic for character-orthogonality fiber sums.
The analytic theorem is not inferred from the finite tests.
"""
from collections import defaultdict
from itertools import product
from math import isclose, pi
from cmath import exp
import random


def mul(z, w):
    a,b=z; c,d=w
    return a*c-b*d, a*d+b*c


def plus(z,w):
    return z[0]+w[0],z[1]+w[1]


def squared(z):
    return z[0]*z[0]+z[1]*z[1]


def conv(a,b):
    p=len(a)
    out=[(0,0) for _ in range(p)]
    for i in range(p):
        for j in range(p):
            out[(i+j)%p]=plus(out[(i+j)%p],mul(a[i],b[j]))
    return out


def direct_moment(f):
    N=len(f); fibers=defaultdict(lambda:(0,0))
    for a in range(N):
        for b in range(N):
            key=((a+b)%N,(a*a+b*b)%N)
            fibers[key]=plus(fibers[key],mul(f[a],f[b]))
    return sum(squared(z) for z in fibers.values())


def block_moment(f,p):
    blocks=[[[f[r+p*u+p*p*l] for l in range(p)] for u in range(p)] for r in range(p)]
    mass=[sum(squared(z) for sub in blocks[r] for z in sub) for r in range(p)]
    energy=4*sum(mass[r]*mass[s] for r in range(p) for s in range(r+1,p))
    for r in range(p):
        for u in range(p):
            energy+=sum(map(squared,conv(blocks[r][u],blocks[r][u])))
            for v in range(u+1,p):
                energy+=4*sum(map(squared,conv(blocks[r][u],blocks[r][v])))
    return energy,mass


def spectral_deficit(f,p):
    blocks=[[[complex(*f[r+p*u+p*p*l]) for l in range(p)] for u in range(p)] for r in range(p)]
    masses=[sum(abs(z)**2 for g in rr for z in g) for rr in blocks]
    mixed=(4*p-6)*sum(masses[r]*masses[s] for r in range(p) for s in range(r+1,p))
    frequency=balance=0.0
    for rr in blocks:
        A=[[abs(sum(g[l]*exp(-2j*pi*xi*l/p) for l in range(p)))**2 for xi in range(p)] for g in rr]
        S=[sum(A[u][xi] for u in range(p)) for xi in range(p)]
        frequency+=(2*p-1)/(p*p)*sum(S[xi]*S[eta] for xi in range(p) for eta in range(p) if xi!=eta)
        balance+=sum((sum(A[u][xi]**2 for u in range(p)) - S[xi]**2/p)/p for xi in range(p))
    return mixed+frequency+balance


def test():
    rnd=random.Random(270318)
    nr=0; ne=0; ns=0
    for p,cases in [(3,12),(5,8),(7,3)]:
        N=p**3
        for _ in range(cases):
            f=[(rnd.randrange(-2,3),rnd.randrange(-2,3)) for i in range(N)]
            E=direct_moment(f)
            Eb,mass=block_moment(f,p)
            assert E==Eb,('fiber/block mismatch',p,E,Eb)
            M=sum(mass)
            D=(2*p-1)*M*M-E
            assert D>=0,('sharp bound',p,D)
            assert isclose(spectral_deficit(f,p),D,rel_tol=5e-10,abs_tol=1e-6),(p,D,spectral_deficit(f,p))
            nr+=1
        # All extremizing packet phases are unconstrained across the middle digit.
        for r in range(p):
            f=[(0,0)]*N
            for u in range(p):
                z=[(1,0),(0,1),(-1,0),(0,-1)][(u+2*r)%4]
                for l in range(p):
                    f[r+p*u+p*p*l]=z
            E=direct_moment(f); M=sum(squared(z) for z in f)
            assert E==(2*p-1)*M*M,('packet',p,r,E,M)
            ne+=1
        # Frequency-misaligned packet blocks cannot saturate (use p=3,5,7).
        f=[(0,0)]*N
        for u in range(p):
            for l in range(p):
                f[p*u+p*p*l] = (1,0) if u==0 or l==0 else (0,0)
        E=direct_moment(f); M=sum(squared(z) for z in f)
        assert E<(2*p-1)*M*M
        ns+=1
    print(f'VERIFY_OK Gaussian_integer_fiber_cases={nr} exact_extremizer_packets={ne} strict_nonextremizers={ns} spectral_deficit_checks={nr}')

if __name__=='__main__':
    test()
