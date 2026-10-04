#!/usr/bin/env python3
from fractions import Fraction
from math import comb

def f(n,k,p):
    return Fraction(comb(n,k)) * (p**k) * ((1-p)**(n-k))

def U(n,k,mu):
    a = Fraction(k-1,n-1)
    b = Fraction(k,n-1)
    if k > 1 and mu <= a:
        return mu * f(n,k,a) / a
    if mu <= b:
        return f(n,k,mu)
    return (1-mu) * f(n,k,b) / (1-b)

def logder_value(n,k,p):
    # f'(p) expressed exactly as f(p)*(k/p-(n-k)/(1-p)).
    return f(n,k,p) * (Fraction(k,1)/p - Fraction(n-k,1)/(1-p))

def qpoly(n,k,p):
    return Fraction(n*(n-1))*p*p - Fraction(2*k*(n-1))*p + Fraction(k*(k-1))

def upper_law(n,k,mu):
    a = Fraction(k-1,n-1)
    b = Fraction(k,n-1)
    if k > 1 and mu < a:
        return {Fraction(0): 1-mu/a, a: mu/a}
    if mu <= b:
        return {mu: Fraction(1)}
    return {b: (1-mu)/(1-b), Fraction(1): 1-(1-mu)/(1-b)}

def eval_mixture(n,k,law):
    return sum(w*f(n,k,p) for p,w in law.items())

def mean_mixture(law):
    return sum(p*w for p,w in law.items())

def two_atom_value(n,k,mu,x,y):
    if x == y:
        if mu != x:
            return None
        return f(n,k,x)
    if not (x <= mu <= y):
        return None
    wy = (mu-x)/(y-x)
    wx = 1-wy
    if wx < 0 or wy < 0:
        return None
    return wx*f(n,k,x) + wy*f(n,k,y)

def run():
    tangent_checks = 0
    majorant_checks = 0
    concavity_checks = 0
    construction_checks = 0
    two_atom_checks = 0

    for n in range(2, 61):
        for k in range(1, n):
            a = Fraction(k-1,n-1)
            b = Fraction(k,n-1)

            if k > 1:
                lhs = logder_value(n,k,a)
                rhs = f(n,k,a)/a
                assert lhs == rhs
                tangent_checks += 1
            if k < n-1:
                lhs = logder_value(n,k,b)
                rhs = -f(n,k,b)/(1-b)
                assert lhs == rhs
                tangent_checks += 1

            # Central concavity certificate at endpoints and dense rational points.
            for j in range(81):
                p = a + (b-a)*Fraction(j,80)
                assert qpoly(n,k,p) <= 0
                concavity_checks += 1

            for j in range(101):
                p = Fraction(j,100)
                val = f(n,k,p)
                up = U(n,k,p)
                assert val <= up
                majorant_checks += 1

                law = upper_law(n,k,p)
                assert sum(law.values(),Fraction(0)) == 1
                assert mean_mixture(law) == p
                assert eval_mixture(n,k,law) == up
                construction_checks += 1

                low = {Fraction(0):1-p, Fraction(1):p}
                assert mean_mixture(low) == p
                assert eval_mixture(n,k,low) == 0
                construction_checks += 1

    # Finite stress test: rational two-atom directing laws.
    grid = [Fraction(i,12) for i in range(13)]
    means = [Fraction(i,12) for i in range(13)]
    for n in range(2, 13):
        for k in range(1,n):
            for mu in means:
                bound = U(n,k,mu)
                for ix,x in enumerate(grid):
                    for y in grid[ix:]:
                        val = two_atom_value(n,k,mu,x,y)
                        if val is not None:
                            assert val <= bound
                            two_atom_checks += 1

    print(
        "VERIFY_OK "
        f"tangent_checks={tangent_checks} "
        f"majorant_checks={majorant_checks} "
        f"concavity_checks={concavity_checks} "
        f"construction_checks={construction_checks} "
        f"two_atom_checks={two_atom_checks}"
    )

if __name__ == "__main__":
    run()
