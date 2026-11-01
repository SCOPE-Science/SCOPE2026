"""Independent finite diagnostics and exact identities for regular-pentagon containment in an ellipse.
Run: python3 verify.py. Finite diagnostics are not a substitute for the proof.
"""
import math
from itertools import combinations
import sympy as S

x=S.symbols('x', positive=True)
h=(1+S.sqrt(5))/4
p=(1+h)/2
q=(1-h)/2
R0sq=(10+5*x+1/x)/16
Rm=p+q*x
switch=(13+7*S.sqrt(5)-S.sqrt(358+158*S.sqrt(5)))/4
cross=S.factor(x*(16*R0sq-16*Rm**2),extension=S.sqrt(5))
assert S.simplify(cross.subs(x,switch))==0
assert S.simplify(cross.subs(x,1))==0
assert S.simplify(S.diff(R0sq,x)-(5-1/x**2)/16)==0
assert 0.4955<float(switch)<0.4956
assert S.simplify(S.sin(2*S.pi/5)**2-(5+S.sqrt(5))/8)==0
assert S.simplify(S.cos(S.pi/5)-h)==0
# Four-contact endpoint: radial equality of the four off-axis pentagon vertices.
t=S.sqrt(x)
center0=(1-x)/(4*t)
y1=S.sin(2*S.pi/5);u1=S.cos(2*S.pi/5)
y2=S.sin(S.pi/5);u2=-S.cos(S.pi/5)
r1=S.simplify((t*u1-center0)**2+y1**2)
r2=S.simplify((t*u2-center0)**2+y2**2)
assert S.simplify(r1-R0sq)==0 and S.simplify(r2-R0sq)==0
assert S.simplify(R0sq-(t-center0)**2)==5*(1-x)/4
# Three-contact endpoint with its other two vertices strictly inside.
center1=(1-x)*(1-h)/2
assert S.simplify((1-center1)-Rm)==0
assert S.simplify((t*S.sin(S.pi/5))**2+(-h-center1)**2-Rm**2)==0
other=S.simplify(Rm**2-(x*S.cos(S.pi/10)**2+(S.sin(S.pi/10)-center1)**2))
assert S.simplify(other.subs(x,1))==0
assert S.simplify(other/(1-x))>0
# Key analytical certificate: strict concavity of the circumradius squared.
y=S.symbols('y', real=True)
m=(1+x)/2;d=(1-x)/2
P=(m*m+2*m*d*h*y+d*d*(y*y-(1-h*h)))*(m-d*y)
P2=S.factor(S.diff(P,y,2))
assert S.simplify(P2-(2*m*d*d*(1-2*h)-6*d**3*y))==0
assert 2*float(h)>1

# Circumcircle / edge-pair enumeration independently reconstructs five-point MEC.
def mec(points):
    ans=float('inf'); support=None
    for i,j in combinations(range(5),2):
        c=((points[i][0]+points[j][0])/2,(points[i][1]+points[j][1])/2)
        r=math.dist(points[i],c)
        if r<ans and all(math.dist(a,c)<r+1e-9 for a in points):ans=r;support=(i,j)
    for i,j,k in combinations(range(5),3):
        a,b,c=points[i],points[j],points[k]
        ux,uy=2*(b[0]-a[0]),2*(b[1]-a[1]);vx,vy=2*(c[0]-a[0]),2*(c[1]-a[1])
        D=ux*vy-uy*vx
        if abs(D)<1e-10: continue
        w=(b[0]**2+b[1]**2-a[0]**2-a[1]**2)
        z=(c[0]**2+c[1]**2-a[0]**2-a[1]**2)
        center=((w*vy-z*uy)/D,(ux*z-vx*w)/D)
        r=math.dist(points[i],center)
        if r<ans and all(math.dist(a,center)<r+1e-9 for a in points):ans=r;support=(i,j,k)
    assert support is not None
    return ans

def points(x,phi):
    t=math.sqrt(x)
    return [(t*math.cos(phi+2*math.pi*j/5), math.sin(phi+2*math.pi*j/5)) for j in range(5)]

checks=0
for xx in [0.001,0.01,0.07,0.15,0.3,0.40,1/math.sqrt(5),0.46,0.48,0.4955,0.4956,0.51,0.6,0.8,0.95,0.999,1.0]:
    rb=float(Rm.subs(x,xx))
    ra=math.sqrt(float(R0sq.subs(x,xx))) if xx>=1/math.sqrt(5) else math.sin(2*math.pi/5)
    target=min(rb,ra)
    for j in range(181):
        phi=j*math.pi/(10*180)
        r=mec(points(xx,phi))
        assert r+2e-8>=target,(xx,phi,r,target)
        checks+=1
    r0=mec(points(xx,0))
    r1=mec(points(xx,math.pi/10))
    assert abs(r0-ra)<2e-8,(xx,r0,ra)
    assert abs(r1-rb)<2e-8,(xx,r1,rb)
    assert abs(min(r0,r1)-target)<2e-8

print('EXACT_GOLDEN_RATIO_IDENTITIES_AND_CONTACTS_PASSED')
print('EXACT_STRICT_CONCAVITY_CERTIFICATE_PASSED')
print('INDEPENDENT_MINIMUM_ENCLOSING_CIRCLE_DIAGNOSTICS_PASSED',checks)
print('ALL_CHECKS_PASSED')
