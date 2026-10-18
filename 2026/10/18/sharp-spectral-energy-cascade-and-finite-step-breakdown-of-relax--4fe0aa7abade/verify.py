"""Standalone numerical and rational checks for a relaxation-free SSPRK(2,2) oscillator theorem.

Only the standard library is required. Finite tests supplement, not replace,
the infinite-step argument supplied in RESULT.md.
"""
from fractions import Fraction as Q
from math import sqrt, isclose, log
from random import Random

N = 0

def check(ok):
    global N
    N += 1
    if not ok:
        raise AssertionError(f'check {N} failed')

def stage_coeffs(w, data):
    # w is a vector of squared timestep frequencies; data are modal energies.
    first = sum((s * e for s, e in zip(w, data)), Q())
    second = sum((s * s * e for s, e in zip(w, data)), Q())
    # h = 1. These are exactly the A*, B*, C* in source equations (2.12).
    return second, 2 * first - second, second / 4

def delta_direct(w, data, eps):
    c = Q(1, 2) - eps
    return sum((e * (s * (1 - 2 * c + c * c * s))
                for s, e in zip(w, data)), Q())

r = Random(47019)
for _ in range(1200):
    m = r.randint(1, 7)
    w = [Q(r.randint(1, 27), r.randint(3, 29)) for j in range(m)]
    e = [Q(r.randint(1, 17), r.randint(1, 19)) for j in range(m)]
    eps = Q(r.randint(-9, 9), r.randint(1, 19))
    a, b, c0 = stage_coeffs(w, e)
    check(a * eps * eps + b * eps + c0 == delta_direct(w, e, eps))
    first = sum((s * x for s, x in zip(w, e)), Q())
    second = sum((s * s * x for s, x in zip(w, e)), Q())
    check(b*b-4*a*c0 == 4*first*(first-second))
    check((first >= second) == (sum((x*s*(1-s) for s,x in zip(w,e)), Q()) >= 0))

# A rational two-frequency witness: correction exists at the first step,
# energy is preserved, but no real correction is possible next step.
u, v = Q(1,4), Q(9,4)
e1, e2 = Q(1), Q(1,16)
q = e1*u + e2*v
rr = e1*u*u + e2*v*v
check(q == Q(25,64))
check(rr == Q(97,256))
check(q-rr == Q(3,256))
c = 10/(10+sqrt(3))
f1, f2 = (1-c*float(u))**2+float(u), (1-c*float(v))**2+float(v)
check(.5 < c < 1.)
check(isclose(float(e1)*f1+float(e2)*f2,float(e1+e2),rel_tol=1e-13))
check(f1 <= float(1+u) and f2 >= float(v))
check(Q(1,16)*Q(9,5) > Q(1,15))
check(float(e2)*f2/(float(e1)*f1) > 1/15)
check(float(e1)*f1*float(u)*(1-float(u))+float(e2)*f2*float(v)*(1-float(v)) < 0)

# Repeat the source method with independently constructed stage vectors
# for random oscillator frequencies, and compare their A*,B*,C* to the modal expression.
def dot(a,b): return sum((x*y for x,y in zip(a,b)), Q())
for _ in range(800):
    m=r.randint(1, 6)
    omega=[Q(r.randint(1,9),r.randint(1,11)) for j in range(m)]
    z=[(Q(r.randint(-8,8),r.randint(1,9)),Q(r.randint(-8,8),r.randint(1,9))) for j in range(m)]
    f1v=[]; f2v=[]; modal=[]; energies=[]
    for om,(x,y) in zip(omega,z):
        f1v.extend([-om*y,om*x])
        # h=1, f2=J(u+f1)
        f2v.extend([-om*y-om*om*x,om*x-om*om*y])
        modal.append(om*om); energies.append(x*x+y*y)
    # explicit source method tableau: a21=1, b=(1/2,1/2), k=(1,-1)
    A=dot([a-b for a,b in zip(f1v,f2v)], [a-b for a,b in zip(f1v,f2v)])
    B=2*dot(f2v,f1v)+dot(f1v,f1v)-dot(f2v,f2v)
    C=-dot(f1v,f2v)+dot([Q(1,2)*(a+b) for a,b in zip(f1v,f2v)],
                                [Q(1,2)*(a+b) for a,b in zip(f1v,f2v)])
    a,b,c0=stage_coeffs(modal,energies)
    check((A,B,C)==(a,b,c0))

# Global modal filtering: test independent direct midpoint-stage updates.
for _ in range(100):
    m=r.randint(2,7)
    w=sorted((r.uniform(.01,.96) for j in range(m)))
    en=[r.uniform(.01,2) for j in range(m)]
    total=sum(en)
    top_initial=en[-1]
    for k in range(100):
        q=sum(s*x for s,x in zip(w,en))
        rr=sum(s*s*x for s,x in zip(w,en))
        check(rr < q)
        c=1/(1+sqrt(1-rr/q))
        f=[(1-c*s)**2+s for s in w]
        check(isclose(sum(a*b for a,b in zip(en,f)),total,rel_tol=3e-13,abs_tol=3e-13))
        check(all(f[-1]>fi for fi in f[:-1]))
        old=en[-1]/en[0]
        en=[a*b for a,b in zip(en,f)]
        check(en[-1]/en[0]>old)
        if k==99: check(en[-1] > top_initial)
print(f'REPRODUCIBLE_CHECKS_OK {N}')
