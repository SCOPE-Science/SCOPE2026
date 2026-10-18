#!/usr/bin/env python3
"""Exact-rational joint-cell and Fourier-cycle tests for integer expansion maps.
Only finite cases are checked; the general theorem is supplied by its mathematical proof.
"""
from fractions import Fraction
from math import log


def direct_joint(b_power, q, i, j):
    """Integrate interval intersections branch-by-branch using rational endpoints."""
    xlo, xhi = Fraction(i, q), Fraction(i+1, q)
    total = Fraction(0)
    for branch in range(b_power):
        ylo = Fraction(q*branch+j, q*b_power)
        yhi = Fraction(q*branch+j+1, q*b_power)
        total += max(Fraction(0), min(xhi, yhi)-max(xlo, ylo))
    return total


def formula_joint(b_power, q, i, j):
    d, r = divmod(b_power, q)
    return Fraction(d + (1 if (j - (b_power*i)%q)%q < r else 0), q*b_power)


def orbit_spectrum_cycles(b, q):
    seen, cycles = set(), []
    for v in range(1, q):
        if v in seen:
            continue
        path, index = [], {}
        u = v
        while u not in seen and u not in index and u != 0:
            index[u] = len(path)
            path.append(u)
            u = b*u % q
        if u in index:
            cycles.append(tuple(path[index[u]:]))
        seen.update(path)
    return cycles


def check():
    count = 0
    for q in range(2, 10):
        for B in range(1, 26):
            for i in range(q):
                for j in range(q):
                    assert direct_joint(B,q,i,j)==formula_joint(B,q,i,j),(B,q,i,j)
                    count += 1
            assert all(sum(formula_joint(B,q,i,j) for j in range(q)) == Fraction(1,q) for i in range(q))
            assert all(sum(formula_joint(B,q,i,j) for i in range(q)) == Fraction(1,q) for j in range(q))
            diff=[formula_joint(B,q,i,j)-Fraction(1,q*q) for i in range(q) for j in range(q)]
            tv=sum(map(abs,diff))/2
            chi=sum(v*v*q*q for v in diff)
            r=B%q
            assert tv==Fraction(r*(q-r),q*B)
            assert chi==Fraction(r*(q-r),B*B)
            if r==0:
                assert all(v==0 for v in diff)
            else:
                assert any(v!=0 for v in diff)
    # The nonzero Fourier cycles use multiplication by b modulo q;
    # for each cycle verify the complex weight product telescopes to b^(-length).
    import cmath
    for b in range(2, 8):
        for q in range(2, 26):
            zeta=cmath.exp(2j*cmath.pi/q)
            for cyc in orbit_spectrum_cycles(b,q):
                prod=1+0j
                for m in cyc:
                    cm=sum(zeta**(m*j) for j in range(b))/b
                    prod*=cm
                assert abs(prod - b**(-len(cyc)))<1e-8, (b,q,cyc,prod)
    # Separately calculate finite transition matrices and their full characteristic
    # polynomials over Q, then compare to the predicted Fourier-cycle factorization.
    import sympy as sp
    z=sp.Symbol('z')
    charchecks=0
    for b in range(2,6):
        for q in range(2,13):
            transition=sp.Matrix(q,q,lambda j,i: sp.Rational(
                sum((b*i+a)%q == j for a in range(b)), b))
            cycles=orbit_spectrum_cycles(b,q)
            retained=sum(map(len, cycles))
            target=(z-1)*z**(q-1-retained)
            for cyc in cycles:
                target *= z**len(cyc)-sp.Rational(1,b**len(cyc))
            assert sp.Poly(transition.charpoly(z).as_expr()-target,z).is_zero,(b,q)
            # A separate divisor/order formula gives all algebraic multiplicities.
            qc=q
            for p, _ in sp.factorint(q).items():
                if b % p == 0:
                    while qc % p == 0:
                        qc //= p
            divisor_target=(z-1)*z**(q-qc)
            for d in sp.divisors(qc):
                if d==1:
                    continue
                ell=int(sp.n_order(b,d))
                divisor_target *= (z**ell - sp.Rational(1,b**ell))**(int(sp.totient(d))//ell)
            assert sp.Poly(target-divisor_target,z).is_zero,(b,q)
            charchecks += 1
    # Example of three strictly distinct subsequential constants: base 2, 7 bins.
    assert [(pow(2,n,7)*(7-pow(2,n,7)))/2 for n in (1,2,3)] == [5,6,3]
    # Test asymptotic coefficient for fixed q and each residue subsequence.
    for n in (12,13,14,15,16,17):
        B=2**n
        q=7
        L,r=divmod(B,q)
        I=(r*(L+1)/B)*log(q*(L+1)/B) + ((q-r)*L/B)*log(q*L/B)
        assert abs(B*B*I-r*(q-r)/2)<0.1,(n,I)
    print('VERIFY_OK direct_cells=',count,'; exact_characteristic_polynomials=',charchecks,'; Fourier_cycles=verified; periodic_limits=verified')

if __name__=='__main__':
    check()
