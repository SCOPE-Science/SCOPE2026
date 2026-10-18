#!/usr/bin/env python3
"""Exact algebraic identities for period-four orbits of a piecewise-affine planar map."""
import sympy as S

a,b,t=S.symbols('a b t', real=True)
q=a-b-1
D=a**4+(1-b*b)**2
E=(a*a-b*b+1)*(a*a+b*b-1)
P=a**3+a*a*b-a*a+a*b*b-a-b**3+b*b+b-1
V=a**3+a*a*b-a*a-a*b*b+a+b**3-b*b-b+1
U=a**3-a*a*b+a*a+a*b*b-a+b**3-b*b-b+1
R=a**3-a*a*b+a*a-a*b*b+a-b**3+b*b+b-1
sols={
    '+++-':[q*V/D,q*q*(a-b+1)*(a+b-1)/D,q*U/D,-q*q*(a*a+(b-1)**2)/D],
    '++--':[q*P/E,q*R/E,-q*U/E,-q*V/E],
    '+---':[q*(a+b+1)*(a*a+(b-1)**2)/D,-q*R/D,-q*(a-b+1)*(a+b-1)*(a+b+1)/D,-q*P/D],
    '+-+-':[q*(a+b+1)/(a*a+(b+1)**2),-q*q/(a*a+(b+1)**2)]*2,
}
for word,x in sols.items():
    for i in range(4):
        sig=1 if word[i]=='+' else -1
        eq=S.cancel(x[(i+1)%4]+a*sig*x[i]+b*x[(i-1)%4]-q)
        assert eq==0,(word,i,eq)
    for i in range(4):
        assert S.simplify(x[(i+4)%4]-x[i])==0

assert S.factor(P.subs(a,1+b+t)-(
    t**3+(4*b+2)*t**2+(6*b*b+6*b)*t+2*(b+1)*(b*b+2*b-1)))==0
assert S.factor(V.subs(a,1+b+t)-(
    t**3+(4*b+2)*t**2+(4*b*b+6*b+2)*t+2*(b**3+b*b+b+1)))==0
assert S.factor(U.subs(a,1+b+t)-(
    t**3+(2*b+4)*t**2+(2*b*b+6*b+4)*t+2*(b**3+b*b+b+1)))==0
assert S.factor(R.subs(a,1+b+t)-(
    t**3+(2*b+4)*t**2+(6*b+6)*t+2*(1+3*b+b*b-b**3)))==0

J={'+':S.Matrix([[-a,-b],[1,0]]),'-':S.Matrix([[a,-b],[1,0]])}
for word in ['+++-','++--','+---']:
    M=S.eye(2)
    for c in word:M=J[c]*M
    trace=S.factor(S.trace(M))
    assert trace==(-a**4+2*b*b if word!='++--' else a**4+2*b*b)
    assert S.factor(S.det(M)-b**4)==0

# Nonempty sign regimes tested with exact rational arithmetic.
for aa,bb,count in [(S.Rational(11,10),S.Rational(1,20),1),
                     (S.Rational(2,1),S.Rational(1,5),3),
                     (S.Rational(9,5),S.Rational(1,2),3)]:
    good=[]
    for word,x in sols.items():
        z=[v.subs({a:aa,b:bb}) for v in x]
        if all((v>0 if c=='+' else v<0) for v,c in zip(z,word)):
            if len(set(z))==4:good.append(word)
    assert len(good)==count,(aa,bb,good)
print('PASS: exact recurrences, positivity polynomials, Floquet traces, three rational sign tests')
