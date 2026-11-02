"""Dependency-free, supplementary finite checks for four-site shadow fibers.

The sharp all-parameter statements are proved analytically in RESULT.md.
"""
import math
import random
import itertools
from fractions import Fraction


def determinant_invariants(x, y, z):
    # Coefficient of st and (st)^2 in tridiagonal path determinant.
    return x + y + z, x * z


def moment2_moment4(S, P):
    return S / 20, (S * S - P) / 210


def profile(S, P):
    rho = math.sqrt(P)
    assert P > 0 and S >= 2 * rho - 1e-12
    lower_norm = rho if S <= 3 * rho else (S + math.sqrt(S * S - 8 * P)) / 4
    upper_norm = (S + math.sqrt(S * S - 4 * P)) / 2
    lower_fourth = (S * S - 4 * S * rho + 6 * P) if S <= 4 * rho else (S * S / 2 - 2 * P)
    upper_fourth = S * S - 2 * P
    return lower_norm, upper_norm, lower_fourth, upper_fourth


def sample_weights(S, P, u):
    d = max(0.0, u * u - 4 * P)
    return (u + math.sqrt(d)) / 2, S - u, (u - math.sqrt(d)) / 2


def audit():
    checks = 0
    # Exact determinant expansion in Q[s,t] by permutation, including boundaries.
    def det_coeffs(a, b, c):
        M = [[{(0,0): Fraction(1)} if i==j else {} for j in range(4)] for i in range(4)]
        for i, w in enumerate([a,b,c]):
            M[i][i+1] = {(1,0): Fraction(-w)}
            M[i+1][i] = {(0,1): Fraction(-w)}
        ans = {}
        for perm in itertools.permutations(range(4)):
            inv=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
            terms={(0,0): Fraction(-1 if inv % 2 else 1)}
            for i,j in enumerate(perm):
                nxt={}
                for (e1,e2),v1 in terms.items():
                    for (f1,f2),v2 in M[i][j].items():
                        idx=(e1+f1,e2+f2)
                        nxt[idx]=nxt.get(idx,Fraction(0))+v1*v2
                terms=nxt
            for term,val in terms.items():
                ans[term]=ans.get(term,Fraction(0))+val
        return {k:v for k,v in ans.items() if v}

    for a in range(1,5):
        for b in range(0,5):
            for c in range(1,5):
                S,P=determinant_invariants(a*a,b*b,c*c)
                expected={(0,0): Fraction(1), (1,1): Fraction(-S), (2,2): Fraction(P)}
                assert det_coeffs(a,b,c)==expected
                assert math.isclose(moment2_moment4(S,P)[0],float(Fraction(S,20)),abs_tol=1e-14)
                assert math.isclose(moment2_moment4(S,P)[1],float(Fraction(S*S-P,210)),abs_tol=1e-14)
                checks+=2

    # Algebraic phase-point checks, independent of numerical grid maxima.
    for S, P, a, b, c in [(Fraction(3),Fraction(1),Fraction(1),Fraction(1),Fraction(1)),
                          (Fraction(6),Fraction(1),Fraction(1),Fraction(2),Fraction(1))]:
        assert determinant_invariants(a*a,b*b,c*c)==(S,P)
        checks+=1

    phi = (1 + math.sqrt(5)) / 2
    rstar = 2 + math.sqrt(2)
    assert math.isclose((3 + math.sqrt(5)) / 2, phi * phi, abs_tol=1e-14)
    assert math.isclose((rstar * rstar - 2) / (rstar * rstar - 4*rstar + 6), 1 + math.sqrt(2), abs_tol=1e-14)
    checks += 2

    random.seed(477312)
    for i in range(12000):
        P = 10 ** random.uniform(-3, 3)
        rho = math.sqrt(P)
        r = 2 + 80 * random.random()
        S = r * rho
        u = 2*rho + (S-2*rho)*random.random()
        x,y,z = sample_weights(S,P,u)
        L,U,Qmin,Qmax = profile(S,P)
        norm_sq = max(x,y,z)
        Q=x*x+y*y+z*z
        tolerance = 1e-9*(1+S*S)
        assert x > 0 and z > 0 and y >= -tolerance
        assert abs(x+y+z-S) <= tolerance
        assert abs(x*z-P) <= tolerance
        assert abs(determinant_invariants(x,y,z)[0]-S)<=tolerance
        assert L - tolerance <= norm_sq <= U+tolerance
        assert Qmin-tolerance <= Q <= Qmax+tolerance
        assert U / L <= phi * phi+1e-11
        assert Qmax/Qmin <= 1+math.sqrt(2)+1e-11
        checks += 8
    return checks


if __name__ == '__main__':
    print('PASS: %d finite assertions; analytic proof required for all-parameter theorem.' % audit())
