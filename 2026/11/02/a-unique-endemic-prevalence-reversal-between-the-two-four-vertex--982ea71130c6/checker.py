#!/usr/bin/env python3
"""Reproduce exact equilibrium identities for the four-vertex-tree SIS model.

Requires Python 3 and SymPy (tested on SymPy 1.13+); no external data.
"""
import math
import random
import sympy as sp

t = sp.symbols('t', positive=True)
root = sp.sqrt(t*(t+1))
x = (3*t*t-1)/(t*(1+3*t))
y = (3*t*t-1)/(3*t*(t+1))
u = 1-1/root
v = (root-1)/t
S = sp.factor(x+3*y)
P = sp.simplify(2*(u+v))
B = (3*t*t+2*t+1)/((t+1)*(3*t+1))

checks = 0

def check(q, description):
    global checks
    checks += 1
    if not q:
        raise AssertionError(description)

# Exact polynomial/radical identities; no numerical approximation involved.
check(sp.cancel(y-t*x/(1+t*x)) == 0, 'star leaf')
check(sp.cancel(x-3*t*y/(1+3*t*y)) == 0, 'star center')
check(sp.simplify(u-t*v/(1+t*v)) == 0, 'path leaf')
check(sp.simplify(v-t*(u+v)/(1+t*(u+v))) == 0, 'path inner')
check(sp.simplify(S-(2-2/t+2*B)) == 0, 'star expression')
check(sp.simplify(P-(2-2/t+2*sp.sqrt(t/(t+1)))) == 0, 'path expression')
check(sp.factor(B*B-t/(t+1)-
      ((t+1)**3-4*t**3)/((t+1)**2*(3*t+1)**2)) == 0, 'difference factorization')
check(sp.simplify(S.subs(t, 1)-sp.Rational(3,2)) == 0, 'star at 1')
check(sp.simplify(P.subs(t, 1)-sp.sqrt(2)) == 0, 'path at 1')
check(sp.simplify(S.subs(t, 2)-sp.Rational(55,21)) == 0, 'star at 2')
check(sp.simplify(P.subs(t, 2)-1-2*sp.sqrt(sp.Rational(2,3))) == 0,
      'path at 2')
check(sp.limit(t*(P-S),t,sp.oo) == sp.Rational(1,3), 'high-rate gap')
check(sp.limit(S,t,sp.oo) == 4 and sp.limit(P,t,sp.oo) == 4,
      'prevalences saturate')
critical = 1/(2**(sp.Rational(2,3))-1)
check(critical > 1, 'crossover larger than one')
check(sp.simplify(((critical+1)/critical)**3-4) == 0,
      'crossover exact')

# Equilibrium residuals checked numerically from the closed formulas.
random.seed(701243)
for _ in range(20000):
    tau = 0.63 + 100.0*random.random()
    # star positive for tau > 1/sqrt(3)
    xx = float(x.subs(t,tau)) if _ < 12 else (3*tau*tau-1)/(tau*(1+3*tau))
    yy = (3*tau*tau-1)/(3*tau*(tau+1))
    zz = math.sqrt(tau*(tau+1))
    uu = 1-1/zz
    vv = (zz-1)/tau
    check(max(abs(xx-3*tau*yy/(1+3*tau*yy)),
              abs(yy-tau*xx/(1+tau*xx)),
              abs(uu-tau*vv/(1+tau*vv)),
              abs(vv-tau*(uu+vv)/(1+tau*(uu+vv)))) < 1e-12,
          'numeric equilibrium residual')
    Ss = xx+3*yy
    Pp = 2*(uu+vv)
    if tau < float(critical)-1e-8:
        check(Ss > Pp, 'lower-rate ordering')
    elif tau > float(critical)+1e-8:
        check(Ss < Pp, 'higher-rate ordering')
    else:
        check(abs(Ss-Pp)<1e-7, 'threshold')

# Independent full-vector fixed-point iteration, not using the closed formulas.
for j in range(1, 201):
    tau = 0.7 + j/30
    for edges, solution in [([(0,1),(0,2),(0,3)],
                              ((3*tau*tau-1)/(tau*(3*tau+1)),)+
                              ((3*tau*tau-1)/(3*tau*(tau+1)),)*3),
                            ([(0,1),(1,2),(2,3)],
                              (1-1/math.sqrt(tau*(tau+1)),
                               (math.sqrt(tau*(tau+1))-1)/tau,
                               (math.sqrt(tau*(tau+1))-1)/tau,
                               1-1/math.sqrt(tau*(tau+1))))]:
        state = [0.9]*4
        for k in range(12000):
            forces = [0.0]*4
            for a, b in edges:
                forces[a] += state[b]
                forces[b] += state[a]
            next_state = [tau*f/(1+tau*f) for f in forces]
            if max(abs(x-y) for x,y in zip(next_state,state))<1e-14:
                state=next_state
                break
            state=next_state
        check(max(abs(x-y) for x,y in zip(state,solution)) < 1e-10,
              'full-vector iteration confirms endemic state')

# Check endemic-free subcritical thresholds and critical ordering.
for j in range(1,10001):
    tau = j/10000.0
    st = 0 if tau <= 1/math.sqrt(3) else (3*tau*tau-1)*(4*tau+2)/(tau*(tau+1)*(3*tau+1))
    if tau <= (math.sqrt(5)-1)/2:
        pa = 0
    else:
        pa = 2+2*math.sqrt(tau/(tau+1))-2/tau
    check(st>=-1e-12 and pa>=-1e-12, 'physical nonnegative state')
    check(st>=pa-1e-12, 'ordering through threshold branches')

print(f'PASS {checks} assertions; critical_tau={float(critical):.15f}')
