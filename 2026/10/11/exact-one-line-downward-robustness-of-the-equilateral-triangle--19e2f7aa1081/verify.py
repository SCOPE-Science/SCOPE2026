import sympy as s

t,u=s.symbols('t u', positive=True)
r3=s.sqrt(3)
A=s.Matrix([0,r3]); B=s.Matrix([-1,0]); C=s.Matrix([1,0])
P=A+t*(B-A); Q=A+u*(C-A)
p=t*u
GT=(A+B+C)/3
Gc=(A+P+Q)/3
G=s.simplify((GT-p*Gc)/(1-p))

def lam(X,Y,Z):
    d=Y-X
    return s.factor((Z-X).dot(d)/d.dot(d))

expected={
 'BC':-(t**2*u-t*u**2-3*t*u+3)/(6*(t*u-1)),
 'CQ':(t**2*u+2*t*u**2-6*t*u+3)/(6*(u-1)*(t*u-1)),
 'QP':(2*t**3*u-3*t**2*u**2+4*t*u**3+3*t*u-3*t-6*u**2+3*u)/(6*(t*u-1)*(t**2-t*u+u**2)),
 'PB':(4*t**2*u-t*u**2-6*t+3)/(6*(t-1)*(t*u-1)),
}
for name,X,Y in [('BC',B,C),('CQ',C,Q),('QP',Q,P),('PB',P,B)]:
    assert s.factor(lam(X,Y,G)-expected[name])==0

G2=(A+P+Q)/3
cap_expected={
 'PQ':(4*t**2-3*t*u+2*u**2)/(6*(t**2-t*u+u**2)),
 'QA':-(t-4*u)/(6*u),
 'AP':(2*t+u)/(6*t),
}
for name,X,Y in [('PQ',P,Q),('QA',Q,A),('AP',A,P)]:
    assert s.factor(lam(X,Y,G2)-cap_expected[name])==0

L=t**2*u-4*t*u**2+6*u-3
R=-4*t**2*u+t*u**2+6*t-3
lqp=expected['QP']
N,D=s.together(lqp).as_numer_denom()
M,_=s.together(1-lqp).as_numer_denom()
assert s.factor(N-((t/2-u)*L+s.Rational(3,2)*t*(t**2*u-1)))==0
assert s.factor(M.subs(u,1)-(t-1)*(4*t**2-5*t+3))==0
assert s.factor(4*M.subs(u,s.Rational(1,2))-(8*t**3-27*t**2+19*t-6))==0
assert s.factor(s.diff(M,u,2)-6*t*(2*u-t))==0

s0=(s.sqrt(5)-1)/2
vals=[s.simplify(expected[n].subs({t:s0,u:s0})) for n in ['BC','CQ','QP','PB']]
assert vals==[s.Rational(1,2),1,s.Rational(1,2),0]
assert s.simplify(s0**2-(3-s.sqrt(5))/2)==0
assert s.factor((2*s.Symbol('x')-s.Symbol('x')**3-1)+(s.Symbol('x')-1)*(s.Symbol('x')**2+s.Symbol('x')-1))==0

# Deterministic rational stress test of the logical lower bound.
for ti in range(1,40):
    for ui in range(1,40):
        tv=s.Rational(ti,40); uv=s.Rational(ui,40); pv=tv*uv
        Lv=L.subs({t:tv,u:uv}); Rv=R.subs({t:tv,u:uv})
        if Lv>0 and Rv>0:
            assert pv > (3-s.sqrt(5))/2
print('VERIFY_OK')
