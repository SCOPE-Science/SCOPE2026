"""Finite consistency checks of Möbius-ladder absorption and parity-resonance formulas."""
import numpy as np
from math import cos, pi
from fractions import Fraction
from scipy.linalg import expm, eigh, svdvals
from sympy import Poly, cyclotomic_poly, symbols


def predicted(m):
    defect = int(m % 4 == 2 or m % 6 == 3)
    return m + 1 - defect, m + 1, defect


def graph(m):
    n = 2*m
    a=np.zeros((n,n))
    for j in range(n):
        for k in ((j+1)%n,(j-1)%n,(j+m)%n):
            a[j,k]=1
    assert np.allclose(a,a.T)
    assert (a.sum(axis=1)==3).all()
    return a


def distinct_numeric(v,tol=1e-8):
    eig=np.linalg.eigvalsh(v)
    return 1+sum(abs(eig[i+1]-eig[i])>tol for i in range(len(eig)-1))


def bright_rank(a,sinks):
    # Compute the detector rank in each exact-eigenspace cluster;
    # avoids exponentially ill-conditioned raw powers of A.
    eig,V=eigh(a)
    rank=0
    i=0
    while i<len(eig):
        j=i+1
        while j<len(eig) and abs(eig[j]-eig[i])<1e-8:
            j+=1
        T=V[sinks,i:j]
        s=svdvals(np.atleast_2d(T))
        rank+=sum(x>1e-8 for x in s)
        i=j
    return rank


def exact_spectral_collisions(m):
    # exact rational cyclotomic remainder, no floating equality
    z=symbols('z'); N=2*m
    ph=Poly(cyclotomic_poly(N,z),z,domain='ZZ')
    rem=[]
    for k in range(m+1):
        f=Poly(z**k+z**(N-k)+(-1)**k,z,domain='ZZ')
        q=f.rem(ph)
        rem.append(tuple(int(q.nth(i)) for i in range(ph.degree())))
    groups={}
    for k,c in enumerate(rem):
        groups.setdefault(c,[]).append(k)
    r=Fraction(0); a=Fraction(0)
    for group in groups.values():
        w=lambda k: 1 if k in (0,m) else 2
        mass=sum(w(k) for k in group)
        anti=sum((-1)**k*w(k) for k in group)
        r+=Fraction(mass*mass,(2*m)**2)
        a+=Fraction(anti*anti,(2*m)**2)
    return len(groups),[(i,j) for i in range(m+1) for j in range(i+1,m+1) if rem[i]==rem[j]],r,a


def run():
    combos=0
    for m in range(3,31):
        one,two,defect=predicted(m)
        a=graph(m)
        num=distinct_numeric(a)
        assert num==one,(m,num,one)
        if m<=14:
            ar=bright_rank(a,[0]); ar2=bright_rank(a,[0,m]);
            assert ar==one and ar2==two,(m,ar,ar2,one,two)
        if m<=35:
            exact,collisions,r,a=exact_spectral_collisions(m)
            assert exact==one,(m,exact,one)
            assert len(collisions)==defect,(m,collisions,defect)
            base=Fraction(2*m-1,2*m*m)
            adjust=Fraction(2,m*m) if m%6==3 else Fraction(1,m*m) if m%4==2 else Fraction(0)
            assert r==base+adjust and a==base-adjust,(m,r,a,base,adjust)
            assert r-a==(Fraction(4,m*m) if m%6==3 else Fraction(2,m*m) if m%4==2 else 0)
            if defect:
                expected=(m//3,2*m//3) if m%6==3 else (m//2,m)
                assert collisions==[expected],(m,collisions,expected)
        combos+=1
    tests=0
    for m in (3,4):
        a=graph(m)
        for sinks in ([0],[0,m]):
            K=a.astype(complex)
            for j in sinks: K[j,j]-=0.43j
            # Explicit positivity of decay: K=H-i * 0.43*projector.
            at=expm(-1j*K*1200)
            actual=np.trace(at@at.conj().T).real/(2*m)
            expected=1-predicted(m)[0 if len(sinks)==1 else 1]/(2*m)
            assert abs(actual-expected)<2e-5,(m,sinks,actual,expected)
            tests+=1
    print(f'VERIFY_OK graph_numeric={combos} exact_cyclotomic={combos} asymmetry_rational={combos} detector_rank_cases=24 long_time_cases={tests}')
if __name__=='__main__': run()
