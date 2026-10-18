"""Standalone exact finite-state checks for a critical sum/min tree and its sparse-leaf clock.
Run: python verify.py
"""
from fractions import Fraction as Q
from math import sqrt

checks = 0

def check(flag, message):
    global checks
    assert flag, message
    checks += 1

def full_step(p):
    out = {}
    for a,pa in p.items():
        for b,pb in p.items():
            out[a+b] = out.get(a+b,Q(0)) + pa*pb/2
            m = min(a,b)
            out[m] = out.get(m,Q(0)) + pa*pb/2
    return {k:v for k,v in out.items() if v}

def conditional_step(mu,r):
    out = {a:(1-r)*pa for a,pa in mu.items()}
    for a,pa in mu.items():
        for b,pb in mu.items():
            out[a+b] = out.get(a+b,Q(0)) + r*pa*pb/2
            m=min(a,b)
            out[m] = out.get(m,Q(0)) + r*pa*pb/2
    return {k:v for k,v in out.items() if v}

for r in (Q(1,5),Q(1,3),Q(1,2),Q(3,4),Q(1)):
    full={0:1-r,1:r}
    mu={1:Q(1)}
    for level in range(6):
        check(sum(full.values()) == 1, f'full mass r={r} step={level}')
        check(full.get(0,Q(0))==1-r,f'zero mass r={r} step={level}')
        check(sum(mu.values())==1, f'conditional mass r={r} step={level}')
        check({k:v/r for k,v in full.items() if k>0} == mu,
              f'conditional-exact identity r={r} step={level}')
        for k in range(1,8):
            cdf=sum(v for j,v in mu.items() if j<=k)
            check(Q(0)<=cdf<=Q(1),'CDF positivity')
        if level<5:
            full=full_step(full)
            mu=conditional_step(mu,r)

# The exact scalar CDF recursion follows from two independent original branches.
for r in (Q(1,7),Q(2,5),Q(1)):
    mu={1:Q(1)}
    for level in range(7):
        for k in range(1,9):
            before=sum(v for j,v in mu.items() if j<=k)
            convolution=sum(va*vb for a,va in mu.items()
                            for b,vb in mu.items() if a+b<=k)
            predicted=before+r*(convolution-before**2)/2
            after=sum(v for j,v in conditional_step(mu,r).items() if j<=k)
            check(predicted==after, f'Cdf Euler r={r} level={level} k={k}')
        mu=conditional_step(mu,r)

# Exact order monotonicity of the entire conditional distribution at finite depths.
for r in (Q(1,5),Q(1,2),Q(1)):
    mu={1:Q(1)}
    for level in range(7):
        nxt=conditional_step(mu,r)
        for k in range(1,15):
            check(sum(v for j,v in nxt.items() if j<=k) <=
                  sum(v for j,v in mu.items() if j<=k),
                  f'stochastic monotonicity r={r} level={level} k={k}')
        mu=nxt

# Independent scalar analysis: Pr(Z_s=1)=2/(2+s), and CDF through value two
# solves z'=1+z-z*z in log(1+s/2) time.
phi=(1+sqrt(5))/2
psi=(1-sqrt(5))/2
for theta in (0.5,1.0,2.0,5.0):
    n=2500
    r=theta/n
    u1=u2=1.0
    for _ in range(n):
        u2 += r*(u1*u1-u2*u2)/2
        u1 -= r*u1*u1/2
    target_u1=2/(2+theta)
    R=((1-phi)/(1-psi))*(1+theta/2)**(-sqrt(5))
    z=(phi-R*psi)/(1-R)
    target_u2=target_u1*z
    check(abs(u1-target_u1)<0.00025,'kinetic atom at one')
    check(abs(u2-target_u2)<0.00035,'golden-ratio two-point CDF')
    check(target_u1<target_u2<1,'strictly nontrivial crossover')

print(f'PASS: {checks} exact/finite-check assertions and kinetic diagnostics')
