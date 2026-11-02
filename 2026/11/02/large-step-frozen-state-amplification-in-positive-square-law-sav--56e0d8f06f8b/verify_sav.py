"""Standalone supplementary checks for the scalar square-law SAV recurrence.
The universal asymptotic statement is established analytically in RESULT.md;
finite checks here are diagnostics rather than an infinite-dimensional proof.
"""
import math
import random


def iterate(tau, C, x0, steps=160):
    x = float(x0)
    r = math.sqrt(C + x*x/2.0)
    q0 = r
    max_mod_identity = 0.0
    max_pos_violation = 0
    for n in range(steps):
        q = math.sqrt(C+x*x/2)
        c = x/q
        rp = r/math.sqrt(1+tau*c*c)
        xp = x-tau*c*rp
        # scale the equation to avoid subtraction precision cancellation
        lhs = r*r-rp*rp
        rhs = tau*c*c*rp*rp
        err = abs(lhs-rhs)/max(1.0,abs(lhs),abs(rhs))
        max_mod_identity=max(err,max_mod_identity)
        max_pos_violation += int(not (rp>=0 and rp<=r))
        x,r=xp,rp
    return x,r,q0,max_mod_identity,max_pos_violation


# 300 independent parameter sets: positive root and exact dissipative energy law.
rng=random.Random(61573)
for j in range(300):
    C=10**rng.uniform(-2,2)
    x0=rng.choice((-1.0,1.0))*10**rng.uniform(-2,2)
    tau=10**rng.uniform(-3,3)
    x,r,q,err,nv=iterate(tau,C,x0,30)
    assert nv==0, (j,'nonpositive or increasing auxiliary',nv)
    assert err<2e-12,(j,'discrete dissipation residual',err)

# A robust explicit large-timestep example: negative, wrong limiting state.
x,r,q,err,nv=iterate(100,1,1,120)
assert -11<x<-9.125,('large-step limit',x)
assert r<1e-80
assert x*x/2 > 40
assert math.isclose(q*q, 1.5, rel_tol=1e-14)

# Large-step asymptotic including its constant term.
for C,x0 in [(1.,1.),(.2,2.),(4.,.35),(1.,-1.)]:
    q0=math.sqrt(C+x0*x0/2)
    errs=[]
    for tau in (1e3,1e4,1e5):
        x,r,_,_,_=iterate(tau,C,x0,120)
        target=-math.copysign(1,x0)*q0*math.sqrt(tau)+x0+q0*q0/x0
        errs.append(abs(x-target))
    assert errs[1]<.41*errs[0] and errs[2]<.41*errs[1],(C,x0,errs)

print('PASS: 300 dissipative checks, explicit wrong-attractor case, 12 large-step expansion checks')
