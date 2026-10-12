"""Exact arithmetic checks for the two-point stochastic extragradient coupling law.

Run: python3 verify.py
Only the Python standard library is required.
Finite arithmetic tests supplement, and do not replace, the written universal proof.
"""
from fractions import Fraction as F
from itertools import product

checks = 0

def ok(condition):
    global checks
    if not condition:
        raise AssertionError(f"exact test #{checks + 1} failed")
    checks += 1


def raw_second_factor(a, b, p, t, u):
    # Probability table: (a,a), (a,b), (b,a), (b,b).
    def factor(x, y):
        return (1 - u*x*y)**2 + u*y*y
    return ((1-p-t)*factor(a,a) + t*factor(a,b)
            + t*factor(b,a) + (p-t)*factor(b,b))


def moments(a, b, p):
    return (1-p)*a*a + p*b*b, (1-p)*a**4 + p*b**4


def predicted_factor(a, b, p, t, u):
    m2, m4 = moments(a, b, p)
    return (1-u*m2+u*u*m4
            +t*u*(b-a)**2*(2-u*(a+b)**2))


def contraction_margin(a,b,p,t):
    m2,m4 = moments(a,b,p)
    return (m2-2*t*(b-a)**2,m4-t*(b*b-a*a)**2)

for a in [F(1,4), F(1,2), F(1), F(2)]:
    for b in [F(5,2),F(3),F(7)]:
        if a >= b:
            continue
        for p in [F(1,5),F(1,2),F(4,5)]:
            d=min(p,1-p)
            for t in [F(0),d/3,2*d/3,d]:
                for u in [F(1,100),F(1,9),F(1,3),F(4,3)]:
                    q0 = raw_second_factor(a,b,p,t,u)
                    q1 = predicted_factor(a,b,p,t,u)
                    ok(q0 == q1)
                    m,c = contraction_margin(a,b,p,t)
                    ok(c > 0)
                    ok((q0 < 1) == (m > 0 and u < m/c))
                    ok((q0 == 1) == (m > 0 and u == m/c))
            u0=F(2)/(a+b)**2
            # All admissible couplings have the same mean-square factor at the crossover.
            ok(raw_second_factor(a,b,p,F(0),u0)
                == raw_second_factor(a,b,p,d,u0))
            for u in [u0/2,2*u0]:
                qs=raw_second_factor(a,b,p,F(0),u)
                qa=raw_second_factor(a,b,p,d,u)
                ok(qs < qa if u < u0 else qa < qs)

# Every marginal in the three extremal Bernoulli samplers is exactly one half.
a,b,p=F(1),F(2),F(1,2)
u=F(1,3)
for t in [F(0),F(1,4),F(1,2)]:
    aa=1-p-t; ab=ba=t; bb=p-t
    ok(aa+ab==1-p)
    ok(aa+ba==1-p)
    ok(ba+bb==p)
    ok(ab+bb==p)

qs=raw_second_factor(a,b,p,F(0),u)
qi=raw_second_factor(a,b,p,F(1,4),u)
qa=raw_second_factor(a,b,p,F(1,2),u)
ok((qs,qi,qa)==(F(10,9),F(37,36),F(17,18)))
for n in range(1,12):
    # Distribute over four steps exactly; outer sampling independence
    # gives q^n. This is a finite check, not the proof of independence.
    ok(qs**n > 1)
    ok(qi**n > 1)
    ok(qa**n < 1)

# All three exact nonzero-step mean-square convergence ceilings.
def ceiling(t):
    m,c=contraction_margin(a,b,p,t)
    return m/c if m>0 else F(0)
ok((ceiling(F(0)),ceiling(F(1,4)),ceiling(F(1,2)))
   ==(F(5,17),F(8,25),F(3,8)))

# The general stability-ceiling derivative has constant sign,
# with the sign encoded by the same crossing condition as q(u,t).
for a,b,p in [(F(1),F(2),F(1,2)),(F(1),F(6),F(1,2)),
              (F(1),F(3),F(1,5)),(F(1),F(4),F(4,5))]:
    d=min(p,1-p)
    m2,m4=moments(a,b,p)
    lhs=(a+b)**2*m2-2*m4
    def num(t):return m2-2*t*(b-a)**2
    def den(t):return m4-t*(b*b-a*a)**2
    # Multiplication avoids division and is valid even if the numerator is nonpositive.
    difference=num(d)*den(F(0))-num(F(0))*den(d)
    ok((difference > 0)==(lhs>0))
    ok((difference == 0)==(lhs==0))

print(f"PASS {checks} exact rational checks; required no external dependencies")
