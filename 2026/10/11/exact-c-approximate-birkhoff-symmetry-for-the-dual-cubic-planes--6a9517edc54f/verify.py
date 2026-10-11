import math
import sympy as s

k=s.symbols('k',real=True)
H=k**3*(1-k**2)/(1+k**2)**2
Hp=k**2*(3-6*k**2-k**4)/(1+k**2)**3
assert s.factor(s.diff(H,k)-Hp)==0
w0=2*s.sqrt(3)-3
k0=s.sqrt(w0)
target=(78*s.sqrt(3)-135)/16
assert s.simplify(H.subs(k,k0)**2-target)==0
assert 0<float(w0)<1
assert s.simplify((3-6*w0-w0**2))==0

chi=float(s.N(target**s.Rational(1,6),35))
t0=float(s.N(((1-k0)/(1+k0))**s.Rational(1,3),35))
assert abs(chi-0.42916063195784049)<1e-14
assert abs(t0-0.57447695420733808)<1e-14

def norm(z,p):
    return (sum(abs(a)**p for a in z))**(1/p)

def j(z,p):
    n=norm(z,p)
    return [math.copysign(abs(a)**(p-1),a)/n**(p-1) for a in z]

def dot(x,y): return sum(a*b for a,b in zip(x,y))

checks=0
for t in [0,0.001,0.08,0.3,t0,0.9,1,1.4,2,3.5,30,1000]:
    a=(1+t**3)**(1/3)
    b=(1+t**6)**(1/3)
    x=[1/a,t/a]; y=[-t*t/b,1/b]
    assert abs(norm(x,3)-1)<1e-12
    assert abs(norm(y,3)-1)<1e-12
    jx=j(x,3); jy=j(y,3)
    assert abs(dot(jx,y))<3e-12
    residual=abs(dot(jy,x))
    formula=abs(t-t**4)/((1+t**3)**(1/3)*(1+t**6)**(2/3))
    assert abs(residual-formula)<3e-12
    # A dual Birkhoff pair is obtained by reversing the duality maps.
    dx=jy; dy=jx
    assert abs(norm(dx,1.5)-1)<3e-12
    assert abs(norm(dy,1.5)-1)<3e-12
    assert abs(dot(j(dx,1.5),dy))<3e-12
    assert abs(abs(dot(j(dy,1.5),dx))-residual)<3e-12
    assert residual<=chi+1e-11
    checks+=1
assert abs(abs(dot(j([-t0*t0/(1+t0**6)**(1/3),1/(1+t0**6)**(1/3)],3),[1/(1+t0**3)**(1/3),t0/(1+t0**3)**(1/3)]))-chi)<1e-12
# Numerical scans are supplementary, not evidence of a global continuum bound.
scanmax=max((u*abs(1-u)**3/((1+u)*(1+u*u)**2))**(1/3) for u in [i/20000 for i in range(20001)])
assert scanmax<=chi+1e-9 and scanmax>=chi-2e-6
print(f'VERIFY_OK symbolic_derivative=1 exact_radical=1 dual_pairs={checks} chi={chi:.17f} t0={t0:.17f}')
