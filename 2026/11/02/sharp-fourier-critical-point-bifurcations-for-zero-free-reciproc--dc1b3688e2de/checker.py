"""Symbolic and exact rational consistency checks for the reciprocal-trinomial theorem."""
import sympy as sp

m, x, u, X, t = sp.symbols('m x u X t', real=True)
S = -2*X**3+(m-3)*u*X**2+(4*m-2-u**2)*X+(m-1)*u
A = m**2-6*m+1
B = -4*m**4+32*m**3-52*m**2+48*m-8
C = -16*(2*m-1)**3
assert sp.expand(sp.discriminant(S,X)-(u**2-4)*(A*u**4+B*u**2+C)) == 0
assert sp.factor((A*t*t+B*t+C).subs(t,4)) == -16*m**4
assert sp.factor((A*t*t+B*t+C).subs(t,0)) == -16*(2*m-1)**3
assert sp.factor(S.subs(u,2)+2*(X+1)**2*(X-(m-1)))==0
for M in (2,4,6,8,10,12):
    p=x**(2*M)+u*x**M+1
    l=sp.diff(sp.diff(p,x)/p,x)
    expected=M*x**(M-2)*S.subs({m:M,X:x**M})/p**2
    assert sp.factor(l-expected) == 0
    for U, number in ((sp.Rational(-3,2),2), (sp.Rational(-1,2),2), (sp.Rational(0),1), (sp.Rational(1,2),1), (sp.Rational(2),1), (sp.Rational(3),1)):
        r=sp.Poly(S.subs({m:M,u:U}),X)
        assert r.count_roots(0,sp.oo)-(1 if r.eval(0)==0 else 0) == number, (M,U,r)
    if M in (2,4):
        assert (A*t*t+B*t+C).subs(m,M).as_poly(t).discriminant()<0
    if M>=6:
        T=sp.solve((A*t*t+B*t+C).subs(m,M),t)
        threshold=[z for z in T if z.is_positive][0]
        assert threshold>4
        for U in (sp.Rational(10),sp.Rational(20),sp.Rational(40),sp.Rational(100),sp.Rational(1000)):
            number=3 if U**2>threshold else 1
            assert sp.Poly(S.subs({m:M,u:U}),X).count_roots(0,sp.oo)==number,(M,U,threshold)
print('CHECK_OK: symbolic identity, discriminant, root counts, threshold and multiplicity controls')
