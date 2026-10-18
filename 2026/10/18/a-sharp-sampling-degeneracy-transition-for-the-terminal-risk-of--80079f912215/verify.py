"""Reproduce exact symbolic and finite-step checks of the stationary SPPM-NS risk theorem.
Requires Python 3 and SymPy. All domain-wide assertions use the proof in RESULT.md.
"""
import sympy as S

p, g = S.symbols('p g', real=True)
q1 = p/(p+g)
q2 = 2*(1-p)/(2*(1-p)+g)
d = 1-q2
A = p*q1+(1-p)*q2
B = (1-p)*d
C = p*q1**2+(1-p)*q2**2
D = 2*(1-p)*q2*d
E = (1-p)*d**2
m = S.cancel(B/(1-A))
s = S.cancel((D*m+E)/(1-C))
R = S.cancel(s-S.Rational(2, 3)*m+S.Rational(1, 9))
F = -g**3+g**2*(-3*p**2+8*p-4)+9*g*p**2*(1-p)+12*p**2*(1-p)**2
H = g**3+2*g**2*(2-p)+3*g*p*(1-p)*(4-p)+12*p**2*(1-p)**2
P = 100*g**5+5829*g**4-3240*g**3+2112*g**2-8064*g-8448
assert S.cancel(R-S.Rational(1,9)+(1-p)*(g+p)*F/(3*(g+3*p*(1-p))*H)) == 0
assert S.factor(S.resultant(F,S.diff(F,p),p)) == -324*g**4*(3*g+2)**2*P
assert S.factor(F.subs({p:S.Rational(4,5),g:1})) == S.Rational(587,625)
assert S.factor(R.subs({p:S.Rational(4,5),g:1})) == S.Rational(105400,1091241)
assert S.factor(R.subs({p:S.Rational(2,3),g:1})) == S.Rational(2,21)
assert S.factor(R.subs({p:S.Rational(2,3),g:2})) == S.Rational(2,15)
assert P.subs(g,1) == -11711 and P.subs(g,2) == 54416
assert S.factor(S.diff(P,g) - (500*g**4+g**2*(23316*g-9720)+4224*g-8064)) == 0
assert S.factor(F.subs(p,0)) == -g**2*(g+4)
assert S.expand(F.subs(p,1)-g**2*(1-g)) == 0
F2 = S.Poly(S.expand(F.subs(g,2)),p)
bernstein = [S.factor(sum(F2.nth(j)*S.binomial(i,j)/S.binomial(4,j) for j in range(i+1))) for i in range(5)]
assert bernstein == [-24,-16,-5,-S.Rational(3,2),-4]
assert S.factor(S.limit(R,p,0)) == S.Rational(4,9)
assert S.factor(S.limit(R,p,1)) == S.Rational(1,9)

# Check moment recurrences against exact symbolic stationary solutions.
for prob in [S.Rational(1,5),S.Rational(1,2),S.Rational(2,3),S.Rational(4,5),S.Rational(9,10)]:
    for step in [S.Rational(1,10),S.Rational(1,2),S.Integer(1),S.Integer(2),S.Integer(5)]:
        vq1 = q1.subs({p:prob,g:step});vq2 = q2.subs({p:prob,g:step});vd = 1-vq2
        mm = S.Rational(1,7);ss = mm**2
        for k in range(350):
            mm2 = S.expand(prob*vq1*mm+(1-prob)*(vq2*mm+vd))
            ss2 = S.expand(prob*vq1**2*ss+(1-prob)*(vq2**2*ss+2*vq2*vd*mm+vd**2))
            mm,ss = mm2,ss2
        stationary_m = m.subs({p:prob,g:step});stationary_s=s.subs({p:prob,g:step})
        assert abs(float(mm-stationary_m))<1e-16
        assert abs(float(ss-stationary_s))<1e-16
        assert abs(float(ss-S.Rational(2,3)*mm+S.Rational(1,9)-R.subs({p:prob,g:step})))<1e-16

roots = S.nroots(P, n=32, maxsteps=300)
pos = [r for r in roots if abs(float(S.im(r)))<1e-15 and float(S.re(r))>0]
assert len(pos)==1
assert abs(float(S.re(pos[0]))-1.4333451253134435)<1e-13
print('PASS: exact recurrence, rational witnesses, resultant, Bernstein certificate, limiting endpoints, and 25 moment recursions.')
print('Positive polynomial root:', pos[0])
