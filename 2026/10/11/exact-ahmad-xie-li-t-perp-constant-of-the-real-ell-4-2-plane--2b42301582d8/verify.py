import sympy as sp

t,r,z=sp.symbols('t r z', positive=True)
G=(1+t**12)*r**4-(1+t**4)
A=(t+r)**4+(1-r*t**3)**4
B=(2*t-r)**4+(2+r*t**3)**4
P=sp.expand(A*B)
Pm=sp.expand(P.subs(r,-r))
diff=sp.factor(P-Pm)
expected=8*r**3*t*(t-1)*(t+1)*(t**2+1)*(t**4+1)**2*(r**4*t**8-r**4*t**4+r**4-12*r**2*t**2-14)
assert sp.expand(diff-expected)==0

# Constrained derivative of P/(1+t^4)^2 along G=0.
Ft=sp.diff(P,t)*(1+t**4)-8*t**3*P
Fr=sp.diff(P,r)*(1+t**4)
H=sp.expand(Ft*sp.diff(G,r)-Fr*sp.diff(G,t))
Hsmall=sp.cancel(H/(-16*r*(1+t**4)**3))
res=sp.factor(sp.resultant(G,sp.together(Hsmall),r))
Q=(28561*z**14-12324932*z**13+214007730*z**12-1563667459*z**11+6135906104*z**10-15047504769*z**9+25081174393*z**8-29615229256*z**7+25081174393*z**6-15047504769*z**5+6135906104*z**4-1563667459*z**3+214007730*z**2-12324932*z+28561)
expected_res=-(t**4+1)**18*(t**8-t**4+1)**2*Q.subs(z,t**4)
assert sp.expand(res-expected_res)==0

poly=sp.Poly(Q,z)
assert poly.count_roots(0,1)==2
assert poly.count_roots(sp.Rational(24169,10_000_000),sp.Rational(24171,10_000_000))==1
assert poly.count_roots(sp.Rational(8255,10000),sp.Rational(8256,10000))==1

# High precision evaluation of the original, pre-elimination stationarity numerator.
# The small resultant root is extraneous; the large root is compatible.
roots=[q for q in sp.nroots(Q,n=60,maxsteps=300) if abs(sp.im(q))<sp.Float('1e-50') and 0<float(sp.re(q))<1]
assert len(roots)==2
zs=sorted([sp.re(q) for q in roots], key=float)
def eval_H(zv):
    tv=zv**sp.Rational(1,4)
    rv=((1+zv)/(1+zv**3))**sp.Rational(1,4)
    return sp.N(H.subs({t:tv,r:rv}),50)
h0=eval_H(zs[0]); h1=eval_H(zs[1])
assert abs(float(h0))>1
assert abs(float(h1))<1e-30

# There is no other possible interior critical point. Signs on each side fix the maximum.
def h_at(q):
    tv=sp.Rational(q[0],q[1]); rv=((1+tv**4)/(1+tv**12))**sp.Rational(1,4)
    return sp.N(H.subs({t:tv,r:rv}),40)
assert h_at((1,2))>0
assert h_at((99,100))<0

zstar=zs[1]
tstar=zstar**sp.Rational(1,4)
rstar=((1+zstar)/(1+zstar**3))**sp.Rational(1,4)
A4=((tstar+rstar)**4+(1-rstar*tstar**3)**4)/(1+tstar**4)
B4=((2*tstar-rstar)**4+(2+rstar*tstar**3)**4)/(1+tstar**4)
T=sp.N((A4*B4)**sp.Rational(1,8),30)
assert abs(float(T)-2.0703790182255246)<2e-15
print('VERIFY_OK roots_Q_0_1=2 compatible=1 z*=%.16f Tperp=%.16f'%(float(zstar),float(T)))
