"""Standalone exact and numerical checks of the harmonic rRKN 2.5 result."""
import math, random
import sympy as S
z,u,x,v,h,w=S.symbols('z u x v h w', real=True)
check=0

def yes(condition):
    global check
    if not condition: raise AssertionError(f'check {check} failed')
    check+=1

# Derive the source rRKN update directly from its force calls.
fminus=-w**2*x
fplus=-w**2*(x+u*h*v+u**2*h**2*fminus/2)
qnew=x+h*v+h**2*fminus/2+h**2*(fplus-fminus)/(6*u)
qtarget=(1-z/2+u*z**2/12)*x+h*(1-z/6)*v
yes(S.simplify((qnew-qtarget).subs(w**2,z/h**2))==0)
a0=1-z/2; a1=z**2/12; a=a0+a1*u
E=lambda degree:S.factor(sum(S.binomial(degree,j)*a0**(degree-j)*a1**j*S.Rational(2,j+2) for j in range(degree+1)))
E2=E(2);E4=E(4)
D=1-S.Rational(13,36)*z+z**2/18-z**3/288
R=S.factor((1-z/6)**2/D)
yes(S.simplify(1-E2-z*D)==0)
yes(S.simplify(R-1-z*(z**2-8*z+8)/(288*D))==0)
yes(S.simplify(S.rem(E4-1,z**2-8*z+8,z)-2*(159*z-758)/1215)==0)
yes(S.simplify(S.diff(D,z)+(3*z**2-32*z+104)/288)==0)
yes(S.discriminant(3*z**2-32*z+104,z)<0)
rho=float(S.nroots(D)[0])
yes(7<rho<7.1)
rminus=4-2*S.sqrt(2);rplus=4+2*S.sqrt(2)
yes(float(rminus)>0 and float(rplus)<rho)
yes(S.simplify(R.subs(z,rminus)-1)==0)
yes(S.simplify(R.subs(z,rplus)-1)==0)
yes(float(E4.subs(z,rminus))<1)
yes(float(E4.subs(z,rplus))>1)
yes(float(E2.subs(z,6))<1)
yes(S.simplify(R.subs(z,6))==0)
# Independently integrate raw moments of beta(2,1) and compare exact polynomial formula.
for j in range(30):
    val=S.Rational(j+1,13)
    if j<25:
        s2=S.integrate(2*u*(a.subs(z,val))**2,(u,0,1))
        yes(S.simplify(s2-E2.subs(z,val))==0)
    else:
        s4=S.integrate(2*u*(a.subs(z,val))**4,(u,0,1))
        yes(S.simplify(s4-E4.subs(z,val))==0)
# Independent exact variance-recursion tests for hundreds of rational step sizes.
for j in range(1,200):
    t=S.Rational(j,30)
    B=1-t/6
    rec=S.factor((1-E2.subs(z,t))*R.subs(z,t)-t*B**2)
    yes(rec==0)
# Reproducible simulation under the first (finite-fourth-moment) calibration.
rr=random.Random(20261029);step=float(S.sqrt(rminus)); omega=1.;zv=float(rminus)
state=0.;sample=[]
for i in range(210000):
    U=math.sqrt(rr.random()) # density 2u
    xi=rr.gauss(0,1)
    state=(1-zv/2+U*zv*zv/12)*state+step*(1-zv/6)*xi
    if i>=10000:sample.append(state)
mu=sum(sample)/len(sample);var=sum(t*t for t in sample)/len(sample)-mu*mu
yes(abs(mu)<0.018)
yes(abs(var-1.)<0.04)
print(f'PASS: {check} checks; numerical variance {var:.6f}; harmonic stability root {rho:.10f}')
