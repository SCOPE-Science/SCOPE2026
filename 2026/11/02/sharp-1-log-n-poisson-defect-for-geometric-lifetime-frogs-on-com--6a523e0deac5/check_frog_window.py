#!/usr/bin/env python3
"""Exact finite-size consistency checks for geometric-lifetime frogs on K_n.

Uses only Python standard library; no simulation or floating-point rounding
for finite-n distribution identities.
"""
from fractions import Fraction
from functools import lru_cache
from math import comb, factorial, exp, log


def terminal_law(n, p):
    """Absorbing active-count/discovery-count recursion, with holding removed."""
    @lru_cache(None)
    def f(a, v):
        if a == 0:
            return tuple(Fraction(int(j == v)) for j in range(1, n + 1))
        if v == n:
            return tuple(Fraction(int(j == n)) for j in range(1, n + 1))
        hold = p * Fraction(v - 1, n - 1)
        death = (1 - p) / (1 - hold)
        birth = p * Fraction(n - v, n - 1) / (1 - hold)
        x = f(a - 1, v)
        y = f(a + 1, v + 1)
        return tuple(death * x[j] + birth * y[j] for j in range(n))
    return f(1, 1)


def closure_law(n, p):
    """Independent-trajectories/closed-reachable-set recursion."""
    ans = [Fraction(0)] * n
    for s in range(1, n):
        q = (1-p) / (1 - p * Fraction(s - 1, n - 1))
        p_inside = p * Fraction(s - 1, n - 1)
        if s == 1:
            full_s = Fraction(1)
        else:
            full_s = terminal_law(s, p_inside)[-1]
        ans[s-1] = comb(n-1,s-1) * (q**s) * full_s
    ans[-1] = 1 - sum(ans)
    return tuple(ans)


def zero_incoming_factorial(n, k, mu):
    """Exact falling factorial moment of vertices with no incoming frog arc."""
    if k > n-1:
        return Fraction(0)
    ff = factorial(n-1) // factorial(n-1-k)
    return (Fraction(ff) / (1 + mu*Fraction(k-1,n-1))**k
            / (1 + mu*Fraction(k,n-1))**(n-k))


def main():
    checks = 0
    for n in range(2, 11):
        for p in (Fraction(1,3), Fraction(1,2), Fraction(2,3), Fraction(4,5)):
            direct = terminal_law(n, p)
            alternate = closure_law(n,p)
            assert direct == alternate, (n,p,direct,alternate)
            checks += n
            assert sum(direct) == 1
            assert all(x >= 0 for x in direct)
            checks += n+1
            assert direct[0] == 1-p
            checks += 1
    assert terminal_law(3,Fraction(1,2))[-1] == Fraction(5,18)
    checks += 1
    # Exact first factorial moment, also directly derivable per targeted vertex.
    for n in range(2,41):
        mu = Fraction(3,2)
        assert zero_incoming_factorial(n,1,mu) == Fraction(n-1) * (
            1 + mu*Fraction(1,n-1))**(-(n-1))
        checks += 1
    # Large-n diagnostic (not a proof of the Poisson theorem).
    target = exp(-0.4)
    vals = []
    for n in (200,2000,20000,200000):
        mu = log(n)+0.4
        mean = (n-1)*exp(-(n-1)*log(1+mu/(n-1)))
        vals.append((n,mean))
    assert abs(vals[-1][1]-target) < abs(vals[0][1]-target)
    checks += 1
    print('exact assertions:',checks)
    print('K3 p=1/2 coverage:',terminal_law(3,Fraction(1,2))[-1])
    print('limiting mean for c=0.4:',target)
    print('finite-n zero-incoming means:', vals)
    print('PASS')

if __name__ == '__main__':
    main()


def factorial_moment_no_root(n,k,mu):
    """Independent-no-root-arc factorial moment, on nonroot targets."""
    if k > n-1:
        return Fraction(0)
    ff = factorial(n-1)//factorial(n-1-k)
    return (Fraction(ff)/(1+mu*Fraction(k-1,n-1))**k
            /(1+mu*Fraction(k,n-1))**(n-k-1))


def inverted_factorial_law(n,mu,omit_root):
    """Recover exact distribution by inclusion/exclusion, not simulation."""
    f = factorial_moment_no_root if omit_root else zero_incoming_factorial
    result=[]
    for k in range(n):
        value=sum(((-1)**j)*f(n,k+j,mu)/Fraction(factorial(k)*factorial(j))
                  for j in range(n-k))
        result.append(value)
    return tuple(result)


def extended_tests():
    checks=0
    for n in range(2,14):
        for p in (Fraction(1,4),Fraction(1,2),Fraction(3,4)):
            mu=p/(1-p)
            z=inverted_factorial_law(n,mu,False)
            z0=inverted_factorial_law(n,mu,True)
            assert sum(z)==sum(z0)==1
            assert all(a>=0 for a in z+z0)
            checks+=2*n+2
            # The root can only turn otherwise-isolated targets into nonisolated ones.
            assert sum((k*z[k] for k in range(n))) <= sum(k*z0[k] for k in range(n))
            checks+=1
            # Probability of complete failure is exactly the no-first-jump event.
            observed=terminal_law(n,p)
            assert observed[0]==1-p
            checks+=1
            # One-source component has an exact first moment.
            assert zero_incoming_factorial(n,1,mu)==(n-1)/(1+mu/Fraction(n-1))**(n-1)
            checks+=1
    print('additional exact assertions:',checks)
    return checks

if __name__ == '__main__':
    extended_tests()
