"""Finite exact-algebra verification for the two-thermal-inertia phase theorem.

Run: python verify.py   (requires SymPy >=1.11)
The continuum assertions are proved in RESULT.md, not by this finite replay.
"""
import math
import sympy as sp

r,m,x=sp.symbols('r m x', real=True)
C=1+r-m
B=(r+1)*m**2-(r**2+1)*m+r*(r+1)
A=r*m*((r+1)*m-r)
Q=-(r+1)*m**2+(r**2-6*r+1)*m-r*(r+1)
D=sp.expand(B**2-4*A*C)
n=0
assert sp.expand(D-(r-m)*(m-1)*(r+1)*Q)==0;n+=1
assert sp.expand(B+Q+6*r*m)==0;n+=1
assert sp.factor(sp.discriminant(Q,m)-(r-1)**2*(r*r-14*r+1))==0;n+=1
z=sp.symbols('z',positive=True)
assert sp.factor(Q.subs({r:z*z,m:z})-z*(z+1)**2*(z*z-4*z+1))==0;n+=1
assert sp.factor((C+B*x+A*x*x).subs({r:sp.Integer(20),m:sp.Integer(5)}))!=0;n+=1
# The original rational transfer and three arctangent derivatives match exactly.
w=sp.symbols('w',real=True)
a,b,f=sp.symbols('a b f',positive=True)
mu=f*b+(1-f)*a
H=f/(1+sp.I*w*a)+(1-f)/(1+sp.I*w*b)
assert sp.simplify(H-(1+sp.I*w*mu)/((1+sp.I*w*a)*(1+sp.I*w*b)))==0;n+=1
phi_der=a/(1+a*a*w*w)+b/(1+b*b*w*w)-mu/(1+mu*mu*w*w)
poly=(C+B*x+A*x*x)/((1+x)*(1+r*r*x)*(1+m*m*x))
assert sp.factor(phi_der.subs({b:r*a,mu:m*a,w:sp.sqrt(x)/a})/a-poly)==0;n+=1
for rr in [sp.Rational(11,10),2,3,5,12,13,14,15,16,20,50,100]:
    for k in range(1,10):
        mm=1+(rr-1)*sp.Rational(k,10)
        aa=sp.factor(A.subs({r:rr,m:mm})); bb=sp.factor(B.subs({r:rr,m:mm})); cc=sp.factor(C.subs({r:rr,m:mm}))
        dd=sp.factor(D.subs({r:rr,m:mm})); qq=sp.factor(Q.subs({r:rr,m:mm}))
        assert aa>0 and cc>0;n+=1
        assert sp.sign(dd)==sp.sign(qq);n+=1
        assert (qq>0)==(dd>0 and bb<0);n+=1
        for xx in [sp.Rational(1,100),sp.Rational(1,10),1,10,100]:
            v=aa*xx*xx+bb*xx+cc
            vp=sp.factor(phi_der.subs({a:1,b:rr,f:(mm-1)/(rr-1),w:sp.sqrt(xx)}))
            assert sp.sign(v)==sp.sign(vp);n+=1
# The exact double-root threshold at the extremal first-order mixture.
t=2+sp.sqrt(3)
rr=t*t
mm=t
assert sp.factor(Q.subs({r:rr,m:mm}))==0;n+=1
assert sp.factor(B.subs({r:rr,m:mm})**2-4*A.subs({r:rr,m:mm})*C.subs({r:rr,m:mm}))==0;n+=1
assert sp.simplify(-B.subs({r:rr,m:mm})/(2*A.subs({r:rr,m:mm}))-1/rr)==0;n+=1
# Numeric illustration, with two genuine turning frequencies.
rr=20.0;mm=math.sqrt(rr)
aa=rr*mm*((rr+1)*mm-rr)
bb=(rr+1)*mm*mm-(rr*rr+1)*mm+rr*(rr+1)
cc=rr+1-mm
d=bb*bb-4*aa*cc
assert d>0 and bb<0;n+=1
freq=[math.sqrt((-bb+s*math.sqrt(d))/(2*aa)) for s in [-1,1]]
phase=lambda w:math.atan(w)+math.atan(rr*w)-math.atan(mm*w)
assert 0<freq[0]<freq[1];n+=1
assert phase(freq[0])>phase(freq[1]);n+=1
assert abs(freq[0]-.14196407209494566)<1e-12;n+=1
assert abs(freq[1]-.3522017878337553)<1e-12;n+=1
print('VERIFY_OK assertions=',n)
print('r_c=',float(7+4*sp.sqrt(3)))
print('r=20, m=sqrt(20) turning frequencies:',freq)
print('phase-drop-degrees=', (phase(freq[0])-phase(freq[1]))*180/math.pi)
