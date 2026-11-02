"""Exact-rational verification of the two-site pausing-exclusion counting law.

Requires Python and SymPy. Run: python verify.py
"""
import itertools
import sympy as S

k,u,t,c=S.symbols('k u t c',positive=True)
states=list(itertools.product(('0','A','P'),repeat=2))
Q=S.zeros(9); B=S.zeros(9)
for i,x in enumerate(states):
    def transition(y,rate,counted=False):
        j=states.index(tuple(y))
        Q[i,j]+=rate
        Q[i,i]-=rate
        if counted: B[i,j]+=rate
    if x[0]=='0': transition(('A',x[1]),1)
    if x[0]=='A' and x[1]=='0': transition(('0','A'),1)
    if x[1]=='A': transition((x[0],'0'),1,True)
    for pos in range(2):
        if x[pos]=='A':
            y=list(x);y[pos]='P';transition(y,k)
        if x[pos]=='P':
            y=list(x);y[pos]='A';transition(y,u)
M=Q.T.copy();M[8,:]=S.ones(1,9)
pi=M.inv()*S.Matrix([0]*8+[1])
exit_intensity=B*S.ones(9,1)
J=S.factor((pi.T*exit_intensity)[0])
A=Q.copy();A[8,:]=pi.T
rhs=J*S.ones(9,1)-exit_intensity
rhs[8]=0
h=A.inv()*rhs
F2=S.factor(1+2*(pi.T*B*h)[0]/J)
D=(4*k**4+20*k**3*u+12*k**3+38*k**2*u**2+40*k**2*u+7*k**2+
   32*k*u**3+47*k*u**2+15*k*u+10*u**4+20*u**3+10*u**2)
P=(8*k**8+(80*u+56)*k**7+(336*u**2+464*u+158)*k**6+
   (792*u**3+1576*u**2+1060*u+220)*k**5+
   (1164*u**4+2912*u**3+2836*u**2+1172*u+145)*k**4+
   (1104*u**5+3220*u**4+3918*u**3+2364*u**2+620*u+36)*k**3+
   (664*u**6+2168*u**5+2989*u**4+2210*u**3+845*u**2+120*u)*k**2+
   (232*u**7+836*u**6+1220*u**5+940*u**4+404*u**3+80*u**2)*k+
   36*u**8+144*u**7+216*u**6+144*u**5+36*u**4)
assert S.cancel(F2-P/D**2)==0
assert S.cancel(J-u*(k+2*u+2)*(2*k**2+4*k*u+k+2*u**2+2*u)/D)==0
F1=(k**2+2*k*u+2*k+2*u**2)/(k+2*u)**2
C=S.factor((F2-F1)*(k+2*u)**2*D**2)
coeff=S.Poly(C,k).all_coeffs()
expected=[
-8,
-8*(10*u+9),
-2*(184*u**2+312*u+117),
-4*(262*u**3+608*u**2+417*u+87),
-4*(522*u**4+1426*u**3+1282*u**2+481*u+60),
-2*(1532*u**5+4540*u**4+4511*u**3+2111*u**2+474*u+31),
-2*u*(1660*u**5+5168*u**4+5172*u**3+2314*u**2+587*u+78),
-2*u**2*(1284*u**5+4200*u**4+4211*u**3+1409*u**2+83*u+13),
-2*u**3*(u+1)*(664*u**4+1644*u**3+839*u**2-161*u-100),
-8*u**4*(u+1)**2*(3*u-1)*(17*u**2+35*u+15),
-56*u**6*(u+1)**4]
assert len(coeff)==11
assert all(S.expand(a-b)==0 for a,b in zip(coeff,expected))
assert S.cancel(S.limit(F2.subs(k,c*u*u),u,0)-(20*c+9)/25)==0
assert S.cancel(S.limit(F1.subs(k,c*u*u),u,0)-(c+1)/2)==0
G2=4*t*(9*t*t+30*t+20)/(7*t*t+15*t+10)**2
G1=2*t/(t+2)**2
assert S.cancel(S.limit(u*F2.subs(k,t*u),u,0)-G2)==0
assert S.cancel(S.limit(u*F1.subs(k,t*u),u,0)-G1)==0
assert S.cancel(S.diff(G2,t)+4*(63*t**4+285*t**3+150*t**2-300*t-200)/(7*t**2+15*t+10)**3)==0
assert S.cancel(G2-G1+2*t*(31*t**4+78*t**3+13*t**2-100*t-60)/((t+2)**2*(7*t**2+15*t+10)**2)) == 0
# Verify the two positive-root sign changes for 0<u<=1/10.
assert all(S.expand(a).subs(u,S.Rational(1,10))<0 for a in coeff[:8])
assert coeff[8].subs(u,S.Rational(1,10))>0
assert coeff[9].subs(u,S.Rational(1,10))>0
assert coeff[10].subs(u,S.Rational(1,10))<0
# The preceding signs are uniform because the relevant factors have fixed signs.
R=S.factor((F2-F1).subs(k,u*u))
assert R.subs(u,S.Rational(1,10))>0
assert S.limit(R,u,0)>0
# Exact reconstruction at multiple positive rational rate pairs.
for U in (S.Rational(1,100),S.Rational(1,20),S.Rational(1,10),S.Rational(1,4)):
    for K in (S.Rational(1,1000),S.Rational(1,100),S.Rational(1,10),1):
        assert F2.subs({u:U,k:K})>0
        assert J.subs({u:U,k:K})>0
p=S.Poly(63*t**4+285*t**3+150*t**2-300*t-200,t)
q=S.Poly(31*t**4+78*t**3+13*t**2-100*t-60,t)
tmax=float(next(S.re(z) for z in S.nroots(p) if abs(float(S.im(z)))<1e-8 and float(S.re(z))>0))
tcross=float(next(S.re(z) for z in S.nroots(q) if abs(float(S.im(z)))<1e-8 and float(S.re(z))>0))
assert 1<tmax<1.01 and 1.11<tcross<1.12
print('PASS: full two-site tilted-generator stationary and Poisson identities')
print('PASS: rational current, exact long-window Fano polynomial and difference coefficients')
print('PASS: both slow-pause boundary layers, limiting profiles and derivative identities')
print('PASS: positive-rate rational systems and root isolation')
print('t_max = %.12f, g2(t_max) = %.12f, t_cross = %.12f' % (tmax,float(G2.subs(t,tmax)),tcross))
