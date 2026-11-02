#!/usr/bin/env python3
"""Deterministic consistency checks for resetting-induced radial order.

All formulas are dimensionless and refer to the normalized stationary
mean-field density. Tests are supplementary to the analytical proof.
Uses only Python's standard library.
"""

from math import exp, log, sqrt

COUNT = 0


def check(condition, message):
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(message)


def h(u, m):
    """Smaller inverse of R(h)=h-h*h/m, with u in (0,m/4]."""
    return 2 * u / (1 + sqrt(max(0.0, 1 - 4*u/m)))


def R(x, m):
    return x * (1 - x/m)


def J(a, b, m):
    """Exact integral from a to b of du/h(u)."""
    ha, hb = h(a, m), h(b, m)
    return log(hb/ha) - 2*(hb-ha)/m


def quantile(s, q, m, branch="selected"):
    """Upper survival quantile for Y=chi*abs(X)."""
    check(0 < s < 1 and q > 0 and m >= 4, "quantile domain")
    if branch == "gas":
        check(q <= m/4, "gas existence")
        return J(q*s, q, m)
    check(branch == "selected", "branch")
    if q <= 1:
        return J(q*s, q, m)
    if s >= 1/q:
        return log(1/s)/m
    return log(q)/m + J(q*s, 1, m)


def gas_profile(y, q, m):
    """Independent inversion of the source implicit gas ODE."""
    initial = h(q, m)
    if y == 0:
        return initial
    target = log(initial) - 2*initial/m - y
    lo, hi = 0.0, initial
    for _ in range(110):
        mid = (lo + hi)/2
        if log(mid) - 2*mid/m < target:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def survivor(y, q, m, branch="selected"):
    if branch == "gas" or q <= 1:
        g = gas_profile(y, q, m)
        return R(g, m)/q
    L = log(q)/m
    if y <= L:
        return exp(-m*y)
    g = gas_profile(y-L, 1, m)
    return R(g, m)/q


def density(y, q, m, branch="selected"):
    if branch == "gas" or q <= 1:
        return gas_profile(y, q, m)/q
    L = log(q)/m
    if y <= L:
        return m*exp(-m*y)
    return gas_profile(y-L, 1, m)/q


def simpson(fn, a, b, steps):
    check(steps % 2 == 0 and b > a, "integration grid")
    delta = (b-a)/steps
    total = fn(a)+fn(b)
    for i in range(1,steps):
        total += (4 if i%2 else 2)*fn(a+i*delta)
    return delta*total/3


def main():
    for m in (4.0, 5.0, 10.0, 20.0):
        qseq = (.001, .04, .3, .8, .9999, 1., 1.0001, 1.1, 1.3, 2., 4., 10., 100.)
        for s in (.00001, .0001, .005, .03, .25, .5, .8, .96, .999):
            scaled = [quantile(s,q,m) for q in qseq]
            physical = [y/q for y,q in zip(scaled,qseq)]
            for a,b in zip(scaled,scaled[1:]):
                check(a>=b-1e-11, "scaled quantile monotonicity")
            for a,b in zip(physical,physical[1:]):
                check(a>b+1e-14, "strict physical radial order")
            for q,y in zip(qseq,scaled):
                check(abs(survivor(y,q,m)-s)<1e-8, "independent profile and quantile")
            for q in qseq:
                if q>=1/s:
                    check(abs(scaled[qseq.index(q)]-log(1/s)/m)<1e-10,
                          "exact exponential core quantile")
        # The one-sided condensation-quantile slope gap is independent
        # of the survival level; at m=4 its convergence is square-root.
        for s in (.0001, .05, .5, .9, .99):
            eps = 1e-7
            at = quantile(s, 1., m)
            left = (at-quantile(s,1.-eps,m))/eps
            right = (quantile(s,1.+eps,m)-at)/eps
            exact = (h(1.,m)+1.-m)/m
            check(abs(right-left-exact)<.0003,
                  "universal condensation quantile derivative jump")
        if m>4:
            for q in (1.0001, (1+m/4)/2, m/4):
                for s in (.00001, .01, .2, .5, .8, .99, .9999):
                    check(quantile(s,q,m,"gas")>quantile(s,q,m),
                          "droplet is more concentrated than supersaturated gas")
        for q in (.1, .5, 1., 1.01, 1.5, 3., 30.):
            check(abs(survivor(0,q,m)-1.)<1e-12, "normalization at zero")
            check(survivor(30.,q,m)<1e-11, "tail normalization")
            check(density(0.,q,m)>0, "positive radial density")
        # For q>1 the two densities agree exactly on the core and their
        # difference in the exterior is an exact 1/q translate and rescale.
        for z in (.002, .05, .2, .9, 2., 5.):
            d1 = density(z,1.,m)
            for q in (1.05, 2., 10., 100.):
                L = log(q)/m
                check(abs(q*density(L+z,q,m)-d1)<2e-12,
                      "translated one-sided gas is independent of q")
                check(abs(q*m*exp(-m*(L+z))-m*exp(-m*z))<2e-12,
                      "translated exponential reference")
        delta = simpson(lambda z:abs(density(z,1.,m)-m*exp(-m*z)), 0.,25.,10000)/2
        check(0.01<delta<1., "nonzero sharp high-rate TV coefficient")
        # The small-q limit is Exp(1) with first-order TV coefficient 1/(4m).
        for q in (.004, .002):
            tv = simpson(lambda y:abs(density(y,q,m)-exp(-y)),0.,25.,10000)/2
            check(abs(tv/(q/(4*m))-1)<.02, "sharp low-rate TV expansion")
        print(f"m={m:g}: radial order, branch comparison, two exponential limits passed; "
              f"high-rate TV coefficient delta={delta:.9f}")
    print("PASS", COUNT, "deterministic assertions")


if __name__ == "__main__":
    main()
