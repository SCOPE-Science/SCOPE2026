"""Exact rational checks for the sharp simplex-ridge componentwise descent margin.

This is a finite regression test, not a substitute for the algebraic proof.
"""
from fractions import Fraction as Q
from itertools import product

def dot(x,y):
    return sum(p*q for p,q in zip(x,y))

def check_pair(u,v,rho):
    a,b,c = dot(u,u),dot(v,v),dot(u,v)
    d=a+b-2*c
    if d==0: return
    w=(b-c+rho)/(d+2*rho)
    w=min(Q(1),max(Q(0),w))
    comb=tuple(w*x+(1-w)*y for x,y in zip(u,v))
    first,second=dot(u,comb),dot(v,comb)
    assert first==a*w+c*(1-w)
    assert second==c*w+b*(1-w)
    if c<0:
        assert Q(0)<w<Q(1)
        det=a*b-c*c
        assert first==(det+rho*(a+c))/(d+2*rho)
        assert second==(det+rho*(b+c))/(d+2*rho)
        if det>0:
            if a+c>=0 and b+c>=0:
                assert first>0 and second>0
            else:
                neg=(a+c) if a+c<0 else (b+c)
                threshold=det/(-neg)
                assert (first>0 and second>0)==(rho<threshold)
                assert (first>=0 and second>=0)==(rho<=threshold)
    elif a>0 and b>0:
        assert first>0 and second>0

vectors=[tuple(Q(z) for z in u) for u in product(range(-3,4),repeat=2) if u!=(0,0)]
count=0
for u in vectors:
    for v in vectors:
        for r in (Q(1,20),Q(1),Q(5),Q(30)):
            check_pair(u,v,r); count+=1

u=(Q(1),Q(0)); v=(Q(-2),Q(1)); rho=Q(2); sig=Q(1)
a,b,c=dot(u,u),dot(v,v),dot(u,v)
d=a+b-2*c
assert (a,b,c,d)==(Q(1),Q(5),Q(-2),Q(10))
assert (a*b-c*c)/(-a-c)==1
w=(b-c+rho)/(d+2*rho)
assert w==Q(9,14)
vel=tuple(w*x+(1-w)*y for x,y in zip(u,v))
assert vel==(Q(-1,14),Q(5,14))
p=tuple(-z/sig for z in vel)
assert p==(Q(1,14),Q(-5,14))
f1_increase=dot(u,p)+dot(p,p)/2
assert f1_increase==Q(27,196)
assert dot(v,p)<0
print('VERIFY_OK',count,'rational geometry instances; witness objective increase',f1_increase)

# Exact high-dimensional sharpness family: the optimizer is interior and its
# first component realizes equality in the universal bound.
for m in range(2,13):
    cap=Q(m-1,4*m)
    top=Q(m+1,2*m)
    others=Q(1,2*m)
    last=Q(m+1,4*m)
    k=Q(m+1,m-1)
    lam=(top,)+(others,)*(m-1)
    assert sum(lam)==1
    assert top-sum(w*w for w in lam)==cap
    for rho in (Q(1,2),Q(2),Q(4)):
        for s in (Q(1,4),Q(1,2),Q(1),Q(2)):
            gs=((s-rho*cap/s,Q(1)),)+((s+rho*last/s,-k),)*(m-1)
            vx=sum(lam[j]*gs[j][0] for j in range(m))
            vy=sum(lam[j]*gs[j][1] for j in range(m))
            assert (vx,vy)==(s,0)
            kkt=[dot(g,(s,0))+rho*lam[j] for j,g in enumerate(gs)]
            assert len(set(kkt))==1
            assert dot(gs[0],(s,0))==s*s-rho*cap
            assert gs[0][0]*gs[1][1]-gs[0][1]*gs[1][0]==-Q(2*m,m-1)*s

# A co-ercive biobjective quadratic exhibits actual, not merely directional, ascent.
g1=(Q(-1,2),Q(1)); g2=(Q(7,2),Q(-3)); v=(Q(1,2),Q(0)); p=(-v[0],-v[1])
assert dot(g1,p)+dot(p,p)/2 == Q(3,8)
assert dot(g2,p)+dot(p,p)/2 == Q(-13,8)
assert dot(g1,(-2,-2)) == dot(g2,(-2,-2)) == -1
print('SHARP_CERTIFICATE_OK', 'm=2..12, exact KKT, noncollinearity, quadratic ascent')
