"""Standalone exact characteristic-two identities and F2 sanity checks for the Hasse-osculating quartic."""
import itertools
import sympy as sp
x0,x1,x2,x3,x4,t,s,r=sp.symbols('x0 x1 x2 x3 x4 t s r')
xx=(x0,x1,x2,x3,x4)
def z(f):
    return all(int(v)%2==0 for _,v in sp.Poly(sp.expand(f)).terms())
F=x0**2*x3**4+x1**4*x4**2+x0*x2**4*x4+x0**3*x4**3
G=x2**2+x0*x4
H=x0*x3**2+x1**2*x4
K=x0*x3+x1*x2
L=x1*x4+x2*x3
# Pullback to osculating plane on the x0=1 chart
coordinates={x0:1,x1:t+s,x2:t*t+r,x3:t**3+s*t*t+r*t,x4:t**4}
assert z(F.subs(coordinates, simultaneous=True))
assert z(F-(H**2+x0*x4*G**2)) # NOTE verify if identity true
assert z(K*K - (x0*H+x1*x1*G))
assert z(x0*L-(x1*G+x2*K))
assert z(F.diff(x0)-x4*G**2)
assert z(F.diff(x4)-x0*G**2)
for xi in (x1,x2,x3):assert z(F.diff(xi))
# Ideal of the projected-Veronese cubic scroll
u,v,w=sp.symbols('u v w')
Scoord={x0:u*u,x1:u*v,x2:u*w,x3:v*w,x4:w*w}
for f in (G,K,L):assert z(f.subs(Scoord, simultaneous=True))
# Chart x0!=0: x4=x2^2, x3=x1*x2 in char 2
for f in (G,K,L):assert z(f.subs({x0:1,x3:x1*x2,x4:x2*x2}, simultaneous=True))
# Chart x4!=0: x0=x2^2, x1=x2*x3
for f in (G,K,L):assert z(f.subs({x4:1,x0:x2*x2,x1:x2*x3}, simultaneous=True))
# Chart x3!=0: x2=x1*x4, x0=x1^2*x4
for f in (G,K,L):assert z(f.subs({x3:1,x2:x1*x4,x0:x1*x1*x4}, simultaneous=True))
# Chart x1!=0: x2=x0*x3, x4=x0*x3^2
for f in (G,K,L):assert z(f.subs({x1:1,x2:x0*x3,x4:x0*x3*x3}, simultaneous=True))
# The affine incidence map has generic differential rank three
jac=sp.Matrix([[1,0,1],[0,1,2*t],[t*t,t,t*t+r]])
assert z(jac.det()-r)
# Every F2 projective point: verify singular locus exactly P union S
points=list(itertools.product((0,1),repeat=5))[1:]
def ev(f,a):return int(f.subs(dict(zip(xx,a))))%2
ptP={p for p in points if p[0]==p[4]==0}
ptS={p for p in points if not any(ev(f,p) for f in (G,K,L))}
ptSing={p for p in points if ev(F,p)==0 and not any(ev(F.diff(x),p) for x in xx)}
assert ptSing == ptP|ptS
assert len(ptP)==7 and len(ptS)==9 and len(ptP&ptS)==3
print('PASS polynomial identities, four smooth scroll charts, and complete P4(F2) singular-point check')
print('F2 counts P=',len(ptP),'S=',len(ptS),'intersection=',len(ptP&ptS),'union=',len(ptSing))
