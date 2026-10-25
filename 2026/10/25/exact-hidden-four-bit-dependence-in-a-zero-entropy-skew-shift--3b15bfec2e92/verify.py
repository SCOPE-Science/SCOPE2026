"""Independent finite verification of an exact four-sign skew-shift correlation.
All polygon integrations use rational arithmetic; no symbolic theorem checker is claimed.
"""
from fractions import Fraction as F
from itertools import combinations
from math import sqrt, pi, sin


def theory(a):
    t = a % F(1, 2)
    if t <= F(1, 6):
        return F(1, 3) - 16*t*t
    if t <= F(1, 3):
        return -F(1, 3) + 32*(t-F(1, 4))**2
    return F(1, 3) - 16*(t-F(1, 2))**2


def clip(poly, A, B, C):
    """Intersect convex rational polygon with Ax+By<=C."""
    if not poly: return []
    ans=[]
    def val(pt): return A*pt[0]+B*pt[1]-C
    for p,q in zip(poly, poly[1:]+poly[:1]):
        vp,vq=val(p),val(q)
        if vp<=0: ans.append(p)
        if (vp<0<vq) or (vp>0>vq):
            r=vp/(vp-vq)
            ans.append((p[0]+r*(q[0]-p[0]),p[1]+r*(q[1]-p[1])))
    return ans


def area(poly):
    if len(poly)<3: return F(0)
    return abs(sum(p[0]*q[1]-q[0]*p[1] for p,q in zip(poly,poly[1:]+poly[:1])))/2


def exact_moment(a, times):
    """Integrates a product of dyadic signs over the full Haar square exactly."""
    sq=[(F(0),F(0)),(F(1),F(0)),(F(1),F(1)),(F(0),F(1))]
    states=[(sq,1)]
    for k in times:
        const = F(k*(k-1),2)*a
        lo= (2*const).__floor__()-1
        hi= (2*(const+k+1)).__ceil__()+1 if k>=0 else (2*(const+1)).__ceil__()+1
        if k<0:
            lo=(2*(const+k)).__floor__()-1
        nxt=[]
        for poly,sign in states:
            for j in range(lo,hi+1):
                q=clip(poly,F(k),F(1),F(j+1,2)-const)
                if not q: continue
                q=clip(q,-F(k),-F(1),const-F(j,2))
                if area(q)>0: nxt.append((q,sign if j%2==0 else -sign))
        states=nxt
    return sum(sign*area(poly) for poly,sign in states)


for a in [F(0), F(1,24), F(1,8), F(1,6), F(1,5), F(1,4), F(1,3), F(3,8), F(7,16)]:
    got=exact_moment(a,[0,1,2,3])
    exp=theory(a)
    assert got==exp,(a,got,exp)
    for h in [2,3]:
        got_h=exact_moment(a,[0,h,2*h,3*h])
        assert got_h==theory(h*h*a),(a,h,got_h,theory(h*h*a))



def joint_law_four(a):
    """Independent exact enumeration of all 16 four-bit patterns by rational clipping."""
    sq=[(F(0),F(0)),(F(1),F(0)),(F(1),F(1)),(F(0),F(1))]
    states=[(sq,())]
    for k in range(4):
        const=F(k*(k-1),2)*a
        lo=(2*const).__floor__()-1
        hi=(2*(const+k+1)).__ceil__()+1
        nxt=[]
        for poly, signs in states:
            for j in range(lo,hi+1):
                q=clip(poly,F(k),F(1),F(j+1,2)-const)
                if not q: continue
                q=clip(q,-F(k),-F(1),const-F(j,2))
                if area(q)>0: nxt.append((q,signs+((1 if j%2==0 else -1),)))
        states=nxt
    from itertools import product
    law={v:F(0) for v in product((-1,1),repeat=4)}
    for poly,v in states: law[v]+=area(poly)
    return law

for alpha in (F(0),F(1,8),F(1,5),F(1,4),F(1,3)):
    theta=theory(alpha)
    law=joint_law_four(alpha)
    assert sum(law.values())==1
    for v,p in law.items():
        expected=(1+theta*(v[0]*v[1]*v[2]*v[3]))/16
        assert p==expected,(alpha,v,p,expected)

# Every primitive integer linear relation on any three sample times has an even entry.
triple_count=0
for inds in combinations(range(-5,9),3):
    i,j,k=inds
    r=(k-j,i-k,j-i)
    assert sum(r)==0
    assert r[0]*i+r[1]*j+r[2]*k==0
    assert any(v%2==0 for v in r)
    triple_count+=1

# Check the single-frequency formula against a symmetric absolutely convergent odd sum.
for r in range(-5,6):
    if r==0: continue
    trunc=0.0
    for j in range(-12001,12002,2):
        if j%2==0: continue
        trunc+=1/((2*r-j)*(3*j-4*r)*(2*r-3*j)*j)
    trunc*=16/pi**4
    expected=6*sin(2*pi*r/3)/(pi**3*r**3)
    assert abs(trunc-expected)<1e-10,(r,trunc,expected)

# At exceptional roots of consecutive-time 4-dependence, spacing by two detects dependence.
t=1/(4*sqrt(3))
assert abs((1/3-16*t*t))<1e-14
w=(4*t)%0.5
witness=1/3-16*w*w
assert abs(witness-(-9+16/sqrt(3)))<1e-12
assert witness>0.2
print('VERIFY_OK exact Haar integrals: 27; exact 16-pattern laws: 5; triple parity relations:',triple_count,
      '; Fourier coefficients: 10; exceptional lag-two witness:',round(witness,12))
