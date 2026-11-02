"""Reproduce elementary planar-lattice circular-cap and inverse identities."""
import math
from fractions import Fraction


def cap(t,d):
    if t <= d: return 0.0
    return t*t*math.acos(max(-1.0,min(1.0,d/t)))-d*math.sqrt(max(0.,t*t-d*d))

def geometry(a,b):
    assert 0 <= a <= 0.5 and a*a+b*b >= 1-1e-12
    alpha=(b*b+a*a-a)/(2*b)
    beta=(b*b-a*a+a)/(2*b)
    R=math.hypot(0.5,alpha)
    assert abs(R-math.hypot(a-0.5,beta)) < 1e-11
    vv=((1.0,0.0),(a,b),(a-1,b)) if a>0 else ((1.,0.),(0.,b))
    dd=tuple(math.hypot(x,y)/2 for x,y in vv)
    assert max(dd)<R
    return dd,R,vv

def F(t,a,b,dd,R):
    if t>=R: return 1.
    return (math.pi*t*t-2*sum(cap(t,d) for d in dd))/b

def radial_angle_integral(t,vv,n=81920):
    total=0.
    for k in range(n):
        th=2*math.pi*(k+0.5)/n
        dx,dy=math.cos(th),math.sin(th)
        rho=min((x*x+y*y)/(2*abs(dx*x+dy*y)) for x,y in vv if abs(dx*x+dy*y)>1e-14)
        total+=min(t*t,rho*rho)
    return math.pi*total/n

def heron(vals):
    a,b,c=vals
    s=(a+b+c)/2
    return math.sqrt(max(0,s*(s-a)*(s-b)*(s-c)))

for a,b in ((0,1.0),(0,1.7),(0.3,1.2),(0.5,math.sqrt(3)/2),(0.01,1.5),(0.45,0.9),(0.4,2.0)):
    d,R,v=geometry(a,b)
    assert all(abs(F(x,a,b,d,R)-radial_angle_integral(x,v)/b)<6e-5
               for x in (0.4*min(d),0.97*min(d),0.5*(max(d)+R),0.997*R))
    assert abs(math.pi*R*R-2*sum(cap(R,x) for x in d)-b)<2e-11
    if len(d)==3:
        assert abs(2*heron([2*x for x in d])-b)<2e-11
    else:
        assert abs(4*d[0]*d[1]-b)<2e-11
    print('PASS',a,b,'support',R,'half-relevant lengths',d)

# Rational exact checks of the reconstructed triangle Gram matrix.
for aa,bb in [(Fraction(1,3),Fraction(6,5)),(Fraction(1,5),Fraction(3,2)),
              (Fraction(1,2),Fraction(1,1))]:
    lengths2=[Fraction(1),aa*aa+bb*bb,(aa-1)**2+bb*bb]
    dot=(lengths2[0]+lengths2[1]-lengths2[2])/2
    assert dot==aa
    det2=lengths2[0]*lengths2[1]-dot*dot
    assert det2==bb*bb
print('EXACT_GRAM_AND_AREA_IDENTITIES_PASSED')

# Independent high precision limit for the circular segment onset.
import mpmath as mp
mp.mp.dps=65
for d in ['0.5','0.618465843842649','1.75']:
    r=mp.mpf(d)
    for eps in ['1e-8','1e-12','1e-17']:
        t=r+mp.mpf(eps)
        C=t*t*mp.acos(r/t)-r*mp.sqrt(t*t-r*r)
        asym=mp.mpf(4)/3*mp.sqrt(2*r)*mp.mpf(eps)**mp.mpf('1.5')
        assert abs(C/asym-1)<mp.mpf('1e-6')
print('SHARP_THREE_HALVES_ONSET_PASSED')
print('ALL_CHECKS_PASSED')
