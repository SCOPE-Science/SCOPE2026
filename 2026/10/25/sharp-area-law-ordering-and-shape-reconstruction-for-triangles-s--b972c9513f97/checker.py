"""Reproduce exact moment identities and numerical geometric crosschecks.

This finite checker supplements, but does not replace, the analytic proof.
"""
from fractions import Fraction as F
from math import comb, sqrt
import random


def same_moment(k):
    return F(2, (k + 1) ** 2 * (k + 2))


def different_moment(k):
    return sum((F(1, comb(k, j) ** 2) for j in range(k + 1)), F(0)) / (k + 1) ** 3


def moments(p, k):
    e2 = p[0]*p[1]+p[1]*p[2]+p[2]*p[0]
    e3 = p[0]*p[1]*p[2]
    if k == 0:
        return F(1)
    return 3*(e2 - 3*e3)*same_moment(k)+6*e3*different_moment(k)


assert [different_moment(k) for k in range(1, 5)] == [F(1, 4),F(1,12),F(5,144),F(31,1800)]
for p in [(F(1,3),)*3, (F(3,10),F(4,10),F(3,10)), (F(1,2),F(1,2),F(0))]:
    e2=p[0]*p[1]+p[0]*p[2]+p[1]*p[2]
    e3=p[0]*p[1]*p[2]
    assert moments(p,1) == e2/2
    assert moments(p,2) == e2/6
    assert moments(p,3) == 3*e2/40 - e3/60
    assert 9*moments(p,1) - 60*moments(p,3) == e3
    assert 2*moments(p,1) == e2
    assert sum(x**3 for x in p) == 1-3*e2+3*e3

rng = random.Random(403911)

def trial(sides):
    a,b,c=sides
    # A=(0,0), B=(c,0), C determined by opposite side lengths a=BC,b=CA.
    x=(b*b+c*c-a*a)/(2*c)
    y=sqrt(b*b-x*x)
    vertices=((0.,0.),(c,0.),(x,y))
    lengths=(c,a,b)
    P=sum(lengths)
    p=tuple(F(z,P) for z in lengths)
    n=140000
    sums=[0.,0.,0.]
    zero=0
    cdf=[0]*8
    thresholds=[.01,.05,.1,.2,.3,.5,.7,.9]
    for _ in range(n):
        points=[]
        choices=[]
        for __ in range(3):
            t=rng.random()*P
            if t<lengths[0]:j=0; q=t/lengths[0]
            elif t<lengths[0]+lengths[1]:j=1; q=(t-lengths[0])/lengths[1]
            else:j=2;q=(t-lengths[0]-lengths[1])/lengths[2]
            A=vertices[j];B=vertices[(j+1)%3]
            points.append((A[0]*(1-q)+B[0]*q,A[1]*(1-q)+B[1]*q))
            choices.append(j)
        u,v,w=points
        z=abs((v[0]-u[0])*(w[1]-u[1])-(v[1]-u[1])*(w[0]-u[0]))/(c*y)
        for k in range(3):sums[k]+=z**(k+1)
        zero+=len(set(choices))==1
        for j,t in enumerate(thresholds): cdf[j]+=z>t
    m1,m2,m3=[s/n for s in sums]
    exact=[float(moments(p,k)) for k in (1,2,3)]
    qzero=float(sum(z**3 for z in p))
    assert abs(m1-exact[0])<.0025,(sides,'m1',m1,exact[0])
    assert abs(m2-exact[1])<.0025,(sides,'m2',m2,exact[1])
    assert abs(m3-exact[2])<.0025,(sides,'m3',m3,exact[2])
    assert abs(zero/n-qzero)<.004,(sides,'atom',zero/n,qzero)
    return sides, [round(x,7) for x in (m1,m2,m3)], [round(x,7) for x in exact], round(zero/n,6),round(qzero,6)

for sides in [(3,4,5),(5,5,6),(2,3,4)]:
    print('GEOMETRIC_CHECK',trial(sides))

# Exact pointwise conditional coupling on a sample of cube points; analytic proof handles all.
for _ in range(100000):
    u,v,w=rng.random(),rng.random(),rng.random()
    A=(1-u)*v; B=u*(1-v)
    same=abs(u-v)*w
    distinct=min(A,B)+abs(A-B)*w
    assert distinct>=same-1e-14
print('EXACT_MOMENTS_AND_COUPLING_CHECKS_PASS')
