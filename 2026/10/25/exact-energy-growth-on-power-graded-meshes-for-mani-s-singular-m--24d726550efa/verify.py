"""Reproducibility checks for the power-graded Manià interpolation law.
Uses only Python's standard library. The proof of the all-r theorem is in RESULT.md.
"""
from fractions import Fraction as Q
from math import isclose


def padd(a, b):
    c = [Q(0)] * max(len(a), len(b))
    for i, x in enumerate(a): c[i] += x
    for i, x in enumerate(b): c[i] += x
    return c


def pscale(a, c):
    return [x*c for x in a]


def pmul(a, b):
    c = [Q(0)] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): c[i+j] += x*y
    return c


def pint(a, lo, hi):
    return sum((c*(hi**(k+1)-lo**(k+1))/Q(k+1)
                for k, c in enumerate(a)), Q(0))


def F_rho_r3(i):
    """Exact F(rho_i) for r=3, where rho_i=((i-1)/i)^3."""
    rho = Q(i-1, i)**3
    root = Q(i-1, i)
    slope = (1-root)/(1-rho) if rho != 1 else Q(1, 3)
    # phi(t)=intercept+slope*t, and phi^3-t is a polynomial.
    intercept = root-slope*rho
    phi = [intercept, slope]
    phi3 = pmul(pmul(phi, phi), phi)
    residual = padd(phi3, [Q(0), Q(-1)])
    square = pmul(residual, residual)
    return slope**6 * pint(square, rho, Q(1))


def direct_cell_energy_r3(N, i):
    """Integrate the actual affine-cell energy exactly for r=3."""
    a, b = Q(i-1, N)**3, Q(i, N)**3
    ua, ub = Q(i-1, N), Q(i, N)
    slope = (ub-ua)/(b-a)
    # u(x)=intercept+slope*x, so u^3-x is polynomial in x.
    intercept = ua-slope*a
    u = [intercept, slope]
    u3 = pmul(pmul(u, u), u)
    residual = padd(u3, [Q(0), Q(-1)])
    square = pmul(residual, residual)
    return slope**6 * pint(square, a, b)


def main():
    assert pint([Q(0), Q(0), Q(1), Q(0), Q(-2), Q(0), Q(1)], Q(0), Q(1)) == Q(8,105)
    assert F_rho_r3(1) == Q(8,105)
    for N in range(2, 8):
        total_direct = sum((direct_cell_energy_r3(N, i) for i in range(1, N+1)), Q(0))
        total_scaled = Q(N)**3 * sum((Q(1, i**3)*F_rho_r3(i) for i in range(1, N+1)), Q(0))
        assert total_direct == total_scaled, (N, total_direct, total_scaled)
    # Approximate C_r using a stable floating-point polynomial integral; diagnostic only.
    def F_float(rho):
        if rho == 0.0: return 8.0/105.0
        import math
        root = rho**(1.0/3.0)
        h = 1.0-rho
        s = (1.0-root)/h
        # With t=rho+h*y, the constant residual vanishes exactly:
        # (root+(1-root)y)^3-(rho+h*y)=c1*y+c2*y^2+c3*y^3.
        b = 1.0-root
        c = [0.0, 3.0*root*root*b-h, 3.0*root*b*b, b**3]
        sq=[0.0]*7
        for j,x in enumerate(c):
            for k,y in enumerate(c): sq[j+k]+=x*y
        return s**6*h*sum(sq[k]/(k+1) for k in range(1,7))
    for r in (0.5, 1.0, 2.0, 3.0):
        c=sum(i**(-r)*F_float(((i-1.0)/i)**r) for i in range(1,2001))
        assert c > 8.0/105.0
        print(f"C_{r:g} partial sum (2000 terms) = {c:.14f}")
    print("VERIFY_OK: exact rational cell-scaling checks for r=3, N=2..7; first-cell constant 8/105")

if __name__ == "__main__":
    main()
