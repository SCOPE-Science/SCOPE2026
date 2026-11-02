#!/usr/bin/env python3
"""Independent finite spectral-quadrature checks for magnetic-cycle Krylov spreading.

Only the Python standard library is needed.  This checker is finite evidence:
the all-size and infinite-time statements are proved separately in RESULT.md.
"""
import cmath
import math
from fractions import Fraction

PI = math.pi

def predicted(n, phase):
    if phase == 'generic':
        return (n - 1) / 2, [1 / n] * n
    if n % 2:
        p0 = (2*n-1)/(n*n)
        return ((n-1)*(n*n-1))/(4*n*n), [p0]+[2*(n-1)/(n*n)]*((n-1)//2)
    if phase == 'pi':
        return n/4-0.5, [2/n]*(n//2)
    return n/4, [2*(n-1)/(n*n)]+[2*(n-2)/(n*n)]*(n//2-1)+[2*(n-1)/(n*n)]

def spectral_krylov(n,phi):
    # Fourier eigenvectors give root projection masses, independently of formulas.
    lam = sorted(2*math.cos((2*PI*k + phi)/n) for k in range(n))
    atoms=[]
    groups=[]
    for x in lam:
        if atoms and abs(x-atoms[-1]) < 2e-9:
            groups[-1] += 1
        else:
            atoms.append(x);groups.append(1)
    w=[k/n for k in groups]
    d=len(atoms)
    prev=[0.0]*d
    p=[1.0]*d
    beta=0.0
    populations=[]
    polynomials=[]
    for j in range(d):
        pop=sum(w[i]**2 * p[i]**2 for i in range(d))
        populations.append(pop)
        polynomials.append(p[:])
        aa=sum(w[i]*atoms[i]*p[i]*p[i] for i in range(d))
        v=[(atoms[i]-aa)*p[i]-beta*prev[i] for i in range(d)]
        bn=math.sqrt(sum(w[i]*v[i]*v[i] for i in range(d)))
        if j < d-1:
            if bn < 1e-10:
                raise RuntimeError((n, phi, j, 'early Krylov termination'))
            prev,p,beta=p,[z/bn for z in v],bn
        elif bn > 1e-6:
            raise RuntimeError((n, phi, j, 'nonzero last Lanczos coefficient', bn))
    return atoms,w,populations,polynomials

def average_by_finite_time(atoms, w, polys, T, slices):
    # Independent quadrature of observable dynamics (rather than spectral dephasing).
    probs=[0.0]*len(polys)
    for it in range(slices):
        t=(it+0.5)*T/slices
        es=[cmath.exp(-1j*x*t) for x in atoms]
        for j,p in enumerate(polys):
            amp=sum(w[i]*p[i]*es[i] for i in range(len(atoms)))
            probs[j]+=abs(amp)**2/slices
    return probs

def check():
    ntests=0
    for n in range(3,28):
        # Noncritical values are separated from exact zero and half-flux.
        for label,phi in [('zero',0.0),('pi',PI),('generic',0.27),('generic',1.17)]:
            target, target_prob=predicted(n,label)
            E,w,probs,polys=spectral_krylov(n,phi)
            # For N>=20 avoid reporting numerical polynomial-conditioning drift as proof.
            accuracy=2e-4 if n>=20 else 2e-7
            assert abs(sum(probs)-1)<accuracy,(n,label,'norm',sum(probs))
            assert len(probs)==len(target_prob),(n,label,len(probs),len(target_prob))
            assert max(abs(a-b) for a,b in zip(probs,target_prob))<accuracy,(n,label,probs,target_prob)
            assert abs(sum(j*p for j,p in enumerate(probs))-target)<3*n*accuracy,(n,label,'complexity')
            ntests+=4
    for n in range(3,150):
        # Exact integer/rational identities for every branch and parity.
        if n%2:
            ps=[Fraction(2*n-1,n*n)]+[Fraction(2*(n-1),n*n)]*((n-1)//2)
            expected=Fraction((n-1)*(n*n-1),4*n*n)
            assert sum(ps)==1
            assert sum(Fraction(j)*v for j,v in enumerate(ps))==expected
        else:
            ps=[Fraction(2*(n-1),n*n)]+[Fraction(2*(n-2),n*n)]*(n//2-1)+[Fraction(2*(n-1),n*n)]
            assert sum(ps)==1
            assert sum(Fraction(j)*v for j,v in enumerate(ps))==Fraction(n,4)
            half=[Fraction(2,n)]*(n//2)
            assert sum(half)==1
            assert sum(Fraction(j)*v for j,v in enumerate(half))==Fraction(n-2,4)
        # Degeneracy splitting always yields a strictly positive complexity jump.
        for label in ('zero','pi'):
            special=Fraction((n-1)*(n*n-1),4*n*n) if n%2 else (Fraction(n,4) if label=='zero' else Fraction(n-2,4))
            assert Fraction(n-1,2)>special
            ntests+=3
    # Finite-time quadrature checks, using oscillatory dynamics rather than dephased formula.
    for n in (3,4,5,6,7,8):
        for label,phi in [('zero',0.0),('pi',PI),('generic',0.89)]:
            E,w,pr,poly=spectral_krylov(n,phi)
            avg=average_by_finite_time(E,w,poly,T=2500.,slices=20000)
            assert max(abs(x-y) for x,y in zip(avg,pr))<0.005,(n,label,avg,pr)
            ntests+=1
    print('PASS:',ntests,'independent finite checks; all-cycle proof remains analytic')

if __name__ == '__main__':
    check()
