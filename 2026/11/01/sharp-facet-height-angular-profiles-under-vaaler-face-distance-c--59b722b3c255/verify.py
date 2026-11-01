#!/usr/bin/env python3
"""Reproducible algebraic and numerical consistency checks for a facet-height Gaussian comparison.
Python standard library only. This is not a substitute for the analytic argument.
"""
from fractions import Fraction
from math import pi, sqrt, atan, asin, gamma, isclose
from random import Random


def positive_part(x):
    return max(x, 0)


def star(s, n):
    """Boundary Gaussian coefficients for s=h^2>=1."""
    assert s >= 1 and n >= 2
    return [s] + [positive_part(j-s)-positive_part(j-1-s) for j in range(2, n+1)]


def gaussian_baseline(n):
    return pi**(n/2)/(2**(n/2)*gamma(n+1))


def high_coefficient(n):
    return n * 2**(n-1) * gamma(n/2) / pi**(n/2)


def integral_two(q1, q2):
    assert q1 > 0 and q2 >= 0
    if q2 == 0:
        return 1/q1
    return atan(sqrt(q2/q1))/sqrt(q1*q2)


def psi_two(h):
    s=h*h
    q2=max(0, 2-s)
    return h*integral_two(s,q2)/(pi/4)


def closed_two(h):
    s=h*h
    if s >= 2:
        return 4/(pi*h)
    return 4/(pi*sqrt(2-s))*asin(sqrt((2-s)/2))


def run():
    rng=Random(20261031)
    count=0
    for n in range(2,14):
        for num in range(1,90):
            s=Fraction(1)+Fraction(num,17)
            q=star(s,n)
            assert q[0] == s and all(v>=0 for v in q)
            prefixes=[sum(q[:k]) for k in range(1,n+1)]
            assert all(prefixes[k-1] == max(Fraction(k),s) for k in range(1,n+1))
            for j in range(2,n+1):
                assert q[j-1] == positive_part(Fraction(j)-s)-positive_part(Fraction(j-1)-s)
            # Every feasible sequence has no smaller prefix sums.
            feasible=list(q)
            for j in range(1,n):
                feasible[j] += Fraction(rng.randint(1,7),17)
            sums=[sum(feasible[:k]) for k in range(1,n+1)]
            assert all(sums[k-1]>=prefixes[k-1] for k in range(1,n+1))
            # Abel summation on an ordered nonnegative squared-coordinate vector.
            zs=sorted([Fraction(rng.randint(1,300),101) for _ in range(n)],reverse=True)
            def quad(v): return sum(a*z*z for a,z in zip(v,zs))
            excess=quad(feasible)-quad(q)
            telescoping=sum((sums[k-1]-prefixes[k-1])*(zs[k-1]**2-(zs[k]**2 if k<n else 0)) for k in range(1,n+1))
            assert excess==telescoping and excess>=0
            count+=1
    for step in range(1,500):
        h=1+step/150
        assert isclose(psi_two(h),closed_two(h),rel_tol=2e-13,abs_tol=2e-13)
        assert 0<psi_two(h)<1
        q2=max(0,2-h*h)
        for delta in [0.01,0.2,2,10]:
            assert integral_two(h*h,q2+delta)<integral_two(h*h,q2)
        count+=1
    assert isclose(psi_two(1),1,rel_tol=2e-15)
    for n in range(2,14):
        c=high_coefficient(n)
        for h in [sqrt(n),sqrt(n)+0.1,2*sqrt(n),4*sqrt(n)]:
            formula=c*h**(1-n)
            i_raw=2**(n/2-1)*gamma(n/2)/(gamma(n)*h**n)
            value=h*i_raw/gaussian_baseline(n)
            assert isclose(value,formula,rel_tol=2e-13)
            # Exact conversion of the high-height local bound to radial Jacobian.
            angle_coefficient=(n*2**n)/value
            radial=2*pi**(n/2)*h**(n-1)/gamma(n/2)
            assert isclose(angle_coefficient,radial,rel_tol=2e-13)
            count+=1
    # Phase switch: derivative in h drops across h=sqrt(2).
    eps=1e-5
    critical=sqrt(2)
    left=(psi_two(critical)-psi_two(critical-eps))/eps
    right=(psi_two(critical+eps)-psi_two(critical))/eps
    assert right<left-0.35
    count+=1
    # Planar trapezoids attain the local coefficient for every 1<=h<sqrt(2).
    for j in range(0,400):
        h=1+(sqrt(2)-1)*(j/401)
        b=sqrt(2-h*h)
        u=(h-b)/2
        v=(h+b)/2
        assert isclose(u*u+v*v,1,rel_tol=3e-14)
        assert isclose(u*h+v*b,1,rel_tol=3e-14)
        # The new right-hand edge has endpoints of radius sqrt(2).
        assert isclose(h*h+b*b,2,rel_tol=3e-14)
        # Normalized angular cone mass is atan(b/h)/pi.
        omega=atan(b/h)/pi
        coefficient=2*b/omega
        assert isclose(coefficient,8/psi_two(h),rel_tol=3e-13)
        count+=1
    # Square-to-cut-corner degeneration; the new-facet area/angle is sharp in n=2.
    for h in [sqrt(2),2,5,13]:
        for eps in [1e-2,1e-3,1e-4]:
            a=h/sqrt(2)+eps
            b=sqrt(2)*h-a
            length=sqrt(2)*(a-b)
            omega=(atan(a/b)-atan(b/a))/(2*pi)
            ratio=length/omega
            expected=2*pi*h
            assert ratio>=expected*(1-2e-12)
            assert ratio/expected < 1+2e-3
            count+=1
    # General-dimension sharpness via max-radius sandwich on the shrinking facet.
    for n in range(2,11):
        for h in [sqrt(n),sqrt(n)+0.5,3*sqrt(n)]:
            for eps in [1e-2,1e-3]:
                rmax=sqrt(h*h+n*(n-1)*eps*eps)
                relative_upper=(rmax/h)**n
                assert 1<=relative_upper<1+0.03
                count+=1
    print(f"PASS: {count} exact-algebra and numerical consistency checks; no infinite proof is inferred")

if __name__=='__main__':
    run()
