#!/usr/bin/env python3
"""Reproducible finite tests for the two-ray polynomial ambiguity census.

Requires Python 3.10+ and numpy. These tests corroborate, rather than
replace, the invariant-field and multiplicity arguments in the proof.
"""
import cmath
import itertools
import math
import numpy as np


def roots_of_orbit(q, lam):
    return [cmath.exp((cmath.log(lam) + 2j*math.pi*j)/q) for j in range(q)]


def exhaustive_zero_flips(q, lambdas, t_samples=None):
    """Enumerate *all* individual conjugate flips of the specified simple roots."""
    original_roots = [z for lam in lambdas for z in roots_of_orbit(q, lam)]
    original_coeffs = np.poly(original_roots)
    if t_samples is None:
        t_samples = np.linspace(-1.37, 1.53, 2*len(original_roots)+3)
    phi = math.pi/q
    admissible = {}
    for flags in itertools.product((0,1), repeat=len(original_roots)):
        roots = [z.conjugate() if b else z for z,b in zip(original_roots,flags)]
        candidate_coeffs = np.poly(roots)
        good = True
        for t in t_samples:
            x = t*cmath.exp(1j*phi)
            a = np.polyval(original_coeffs,x)
            b = np.polyval(candidate_coeffs,x)
            if abs(abs(a)**2-abs(b)**2) > 2e-7*(1+abs(a)**2+abs(b)**2):
                good = False
                break
        if good:
            key = tuple((round(z.real,7),round(z.imag,7)) for z in candidate_coeffs)
            admissible[key] = candidate_coeffs
    return len(admissible), len(original_roots), len(t_samples)


def test_product_formula(q, params):
    """Compare the multiplicity product with all zero-flipped candidates."""
    roots=[]
    product=1
    for lam, a, b in params:
        assert lam.imag > 0 and a >= 0 and b >= 0
        roots += roots_of_orbit(q,lam)*a
        roots += roots_of_orbit(q,lam.conjugate())*b
        product *= a+b+1
    coeff0=np.poly(roots)
    theta=math.pi/q
    t_samples=np.linspace(-1.13,1.42,2*len(roots)+3)
    found={}
    for flags in itertools.product((0,1),repeat=len(roots)):
        candidate=np.poly([r.conjugate() if b else r for r,b in zip(roots, flags)])
        if all(abs(abs(np.polyval(coeff0,t*cmath.exp(1j*theta)))**2 -
                   abs(np.polyval(candidate,t*cmath.exp(1j*theta)))**2)
               < 2e-7*(1+abs(np.polyval(coeff0,t*cmath.exp(1j*theta)))**2)
               for t in t_samples):
            key=tuple((round(z.real,6),round(z.imag,6)) for z in candidate)
            found[key]=True
    assert len(found)==product,(q,params,len(found),product)
    return len(roots),product


def check_nontrivial_numerator(p, q, r):
    """Check angles pi*p/q with p>1 coprime to q."""
    assert p>1 and math.gcd(p,q)==1
    lambdas=[(2+j)+1j*(j+1) for j in range(r)]
    roots=[z for lam in lambdas for z in roots_of_orbit(q,lam)]
    base=np.poly(roots)
    count=0
    for flips in itertools.product((0,1),repeat=len(roots)):
        trial=np.poly([z.conjugate() if flipped else z for z,flipped in zip(roots,flips)])
        if all(abs(abs(np.polyval(base,t*cmath.exp(1j*math.pi*p/q)))**2-
                   abs(np.polyval(trial,t*cmath.exp(1j*math.pi*p/q)))**2)
               < 1e-7*(1+abs(np.polyval(base,t*cmath.exp(1j*math.pi*p/q)))**2)
               for t in np.linspace(-1.25,1.65,2*len(roots)+3)):
            count+=1
    assert count==2**r,(p,q,r,count)
    return count


def main():
    tests=0
    for q in (2,3,4):
        for r in (1,2):
            lambdas=[(j+2)+1j*(j+1) for j in range(r)]
            got,n,nt=exhaustive_zero_flips(q,lambdas)
            expected=2**r
            assert got==expected,(q,r,got,expected)
            assert expected<=2**(n//q)
            print(f'simple q={q} r={r} degree={n} candidates={2**n} count={got}')
            tests+=1
    for q,params in [
        (2,[(1+1j,2,1)]),
        (2,[(1+1j,1,1),(2+1j,1,0)]),
        (3,[(2+1j,1,1)]),
        (2,[(1+1j,3,0)]),
        (2,[(1+1j,0,3)]),
    ]:
        degree,count=test_product_formula(q,params)
        print(f'multiplicity q={q} degree={degree} exact_count={count}')
        tests+=1
    for p,q,r in [(2,3,1),(2,5,1),(3,5,1),(3,4,1)]:
        count=check_nontrivial_numerator(p,q,r)
        print(f'rational angle p={p} q={q} r={r} count={count}')
        tests+=1
    # A generic degree-7 polynomial has no full rotational orbit, hence one class.
    rs=[0.71+0.42j, -0.18+1.12j, 2.13+0.13j, 0.26-0.79j,
        -1.37-0.42j, 1.74-1.01j, -.91+.31j]
    original=np.poly(rs)
    flipped=0
    for flags in itertools.product((0,1),repeat=7):
        trial=np.poly([r.conjugate() if b else r for r,b in zip(rs,flags)])
        if all(abs(abs(np.polyval(original,t*1j))**2 -
                   abs(np.polyval(trial,t*1j))**2)<1e-6*(1+abs(np.polyval(original,t*1j))**2)
               for t in np.linspace(-1.4,2.2,17)):
            flipped+=1
    assert flipped==1,flipped
    print(f'generic q=2 degree=7 count={flipped}')
    tests+=1
    print(f'PASS: {tests} exhaustive finite configurations, all full zero-flip choices tested')

if __name__=='__main__':main()
