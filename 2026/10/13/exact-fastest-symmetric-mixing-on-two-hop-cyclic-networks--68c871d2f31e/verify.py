"""Reproduce spectral and optimization checks for a five-diagonal cyclic Markov kernel.

Python 3 standard library only. Finite checks supplement the written proof.
"""
from math import sin, pi, cos, floor, isclose
from fractions import Fraction


def design(n):
    assert n >= 5
    t = [sin(pi*k/n)**2 for k in range(1,n//2+1)]
    ell, r = t[0], t[-1]
    j = (n+2)//4
    u = t[j-1]
    d = ell*r + u*(ell+r-u)
    a = (ell+r-1)/(2*d)
    b = 1/(8*d)
    holding = 1-2*(a+b)
    rho = (u*(ell+r-u)-ell*r)/d
    return t,j,ell,r,u,a,b,holding,rho


def mode(t,a,b):
    return 1-4*a*t-16*b*t*(1-t)


def checks():
    assert Fraction(1,4)+Fraction(1,1)==Fraction(5,4)
    t,j,ell,r,u,a,b,h,rho = design(6)
    assert all(isclose(x,1/5,rel_tol=0,abs_tol=3e-15) for x in (a,b,h,rho))
    assert design(5)[-1] < 2e-14
    count_spectra = count_alternatives = count_eigenvectors = 0
    for n in range(5,100):
        t,j,ell,r,u,a,b,h,rho=design(n)
        assert a>0 and b>0 and h>0 and rho>=-1e-13
        assert abs(2*a+2*b+h-1)<1e-13
        g=[v*(ell+r-v) for v in t]
        assert max(g)-g[j-1]<1e-12
        f=[mode(v,a,b) for v in t]
        assert max(map(abs,f))-rho<1e-12
        assert abs(f[0]-rho)<1e-12 and abs(f[-1]-rho)<1e-12
        assert abs(f[j-1]+rho)<1e-12
        count_spectra += len(t)
        if n<=40:
            # Compare 861 legal symmetric orbit-constant alternatives per size.
            for i in range(41):
                for m in range(41-i):
                    alt_a=i/80
                    alt_b=m/80
                    r_alt=max(abs(mode(v,alt_a,alt_b)) for v in t)
                    assert r_alt >= rho-1e-12, (n,alt_a,alt_b,r_alt,rho)
                    count_alternatives+=1
        if n<=21:
            # Compare circulant physical matrix with independent Fourier predictions.
            for k in range(n):
                freq=2*pi*k/n
                v=[cos(freq*i) for i in range(n)]
                lam=1-2*a*(1-cos(freq))-2*b*(1-cos(2*freq))
                for i in range(n):
                    pv=h*v[i] + a*(v[(i+1)%n]+v[(i-1)%n]) + b*(v[(i+2)%n]+v[(i-2)%n])
                    assert abs(pv-lam*v[i])<1e-12
                    count_eigenvectors+=1
    for n in [100,201,402,801,1600]:
        rho=design(n)[-1]
        scaled=(1-rho)*n*n/(8*pi*pi)
        assert abs(scaled-1)<0.025, (n,scaled)
    print(f'VERIFY_OK spectra={count_spectra} feasible_grid_comparisons={count_alternatives} eigenvector_entries={count_eigenvectors} asymptotic_cases=5')


if __name__=='__main__':
    checks()
