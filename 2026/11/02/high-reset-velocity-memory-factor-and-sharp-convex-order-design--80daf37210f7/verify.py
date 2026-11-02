#!/usr/bin/env python3
"""Finite algebraic/numerical consistency checks for the documented diffusion theorem.
No simulation or finite grid substitutes for its mathematical proof.
"""
from math import sqrt, exp, cosh, sinh, isclose
from fractions import Fraction

checks = 0

def ck(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

# Drift-only absorption Laplace transform; this is a solvable limiting comparator,
# not a surrogate for the active velocity diffusion.
for D in (0.4, 1., 2.):
    for d in (0.25, 0.7, 1.1):
        for v in (-2., -1., 0., 0.5, 1.8):
            seq=[]
            for r in (16., 64., 256., 1024., 4096.):
                k=sqrt(r/D)
                q=exp(-d*(v+sqrt(v*v+4*D*r))/(2*D))
                scaled=q*exp(d*k)
                target=exp(-d*v/(2*D))
                ck(0<q<1, "constant-drift Laplace range")
                ck(scaled<=target*(1+1.e-10),"constant-drift asymptotic upper bound")
                seq.append(scaled)
            ck(all(seq[j]<seq[j+1]+1.e-12 for j in range(len(seq)-1)),"monotonic asymptotic ratio")
            ck(abs(seq[-1]/target-1)<.04,"drift asymptotic convergence")

# Exact mixed-boundary Brownian discounted first-hitting resolvent;
# verify boundary values and finite-difference differential equation.
for D in (0.5, 1., 2.):
    for L in (1.5, 3.0):
        for r in (0.5, 3., 20., 200.):
            k=sqrt(r/D)
            h=lambda x:cosh((L-x)*k)/cosh(L*k)
            ck(isclose(h(0),1,rel_tol=1e-12),"zero boundary")
            ck(h(L)>0,"upper boundary")
            for x in (L*.2,L*.4,L*.7):
                dx=1.e-4
                numer=D*(h(x+dx)-2*h(x)+h(x-dx))/dx**2-r*h(x)
                ck(abs(numer)<.00003,"Brownian resolvent equation")
            dhL=(h(L)-h(L-1e-4))/1e-4
            ck(abs(dhL)<.02,"Neumann boundary")

# Exact convexity bounds for finite rational velocity laws on [-V,V].
for V in (0.5, 1., 3.):
    for c in (0.1,0.4,1.2):
        a,b=-V,V
        for j in range(41):
            m=a+(b-a)*j/40
            endpoint=(b-m)/(b-a)*exp(-c*a)+(m-a)/(b-a)*exp(-c*b)
            ck(endpoint+1e-12>=exp(-c*m),"Jensen/chord feasibility")
            for w in range(21):
                # Three-point law with fixed mean: convex blend of delta_m
                # and the extremal endpoints law.
                t=w/20
                C=(1-t)*exp(-c*m)+t*endpoint
                ck(exp(-c*m)-1e-12<=C<=endpoint+1e-12,"convex design envelope")
        ck(isclose((exp(-c*V)+exp(c*V))/2,cosh(c*V),rel_tol=1e-13),"symmetric end point factor")

# Renewal exact identity: for an attempt success probability p and independent
# Exp(r) restart, duration expected (1-p)/r; geometric number attempts.
for p0 in (Fraction(1,100),Fraction(1,5),Fraction(2,3),Fraction(99,100)):
    for r0 in (Fraction(1,2),Fraction(3,1),Fraction(17,2)):
        direct=(1-p0)/(r0*p0)
        renewal=(1-p0)/r0 + (1-p0)*direct
        ck(renewal==direct,"renewal fixed point")
print('PASS',checks,'deterministic checks')
