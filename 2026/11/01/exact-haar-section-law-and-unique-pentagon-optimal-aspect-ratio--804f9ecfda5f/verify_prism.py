"""Exact chamber certificate for Haar central sections of a right regular triangular prism.

Python 3, standard library only. The combinatorial enumeration uses Fraction;
no floating-point predicate affects the exact chamber classification.
"""
from fractions import Fraction as F
from itertools import combinations, product
from collections import Counter
from math import acos, atan, pi, sqrt, cos, sin, log
from random import Random

# w=(x, y/sqrt(3), z) so actual Euclidean vertex is (w0,sqrt(3)*w1,h*w2).
base=[(F(1),F(0)),(F(-1,2),F(1,2)),(F(-1,2),F(-1,2))]
w=[(a,b,F(z)) for z in (1,-1) for a,b in base]
edges=((0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(0,3),(1,4),(2,5))

def det(a,b,c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))

def kind(i,j):
    if i%3==j%3: return 'V'
    if i//3==j//3: return 'S'
    return 'O'

# Check no three defining great circles concur, for ALL h>0:
# the determinant of the physical normals is h*sqrt(3)*det(w_i,w_j,w_k).
triples={idx:det(*(w[i] for i in idx)) for idx in combinations(range(6),3)}
assert len(triples)==20 and all(d!=0 for d in triples.values())
assert set(abs(x) for x in triples.values())=={F(1,2),F(1),F(3,2)}

# An entry is (coefficient of pi, of theta_S, theta_O, theta_V).
rows=Counter()
patterns=[]
for signs in product((-1,1),repeat=6):
    active=[]
    for i,j in combinations(range(6),2):
        for eps in (-1,1):
            if all(signs[k]*eps*det(w[i],w[j],w[k])>0
                   for k in range(6) if k not in (i,j)):
                active.append((i,j))
    if not active:
        continue
    assert len(active)>=3, (signs,active)
    N=sum(signs[i]!=signs[j] for i,j in edges)
    k=len(active)
    coeff={'pi':-(k-2),'S':0,'O':0,'V':0}
    for i,j in active:
        t=kind(i,j)
        if signs[i]==signs[j]:
            coeff['pi']+=1;coeff[t]-=1
        else:
            coeff[t]+=1
    row=(N,k,coeff['pi'],coeff['S'],coeff['O'],coeff['V'])
    rows[row]+=1
    patterns.append((signs,row,active))

expected={
  (3,6,-4,0,6,0):2,
  (4,3,2,-1,-2,0):12,
  (4,4,2,-2,0,-2):6,
  (5,4,-2,2,1,1):12,
}
assert rows==Counter(expected), (rows,expected)
assert len(patterns)==32
# The sum of all spherical chamber areas is the full sphere, identically in h.
total=[sum(m*r[i] for r,m in rows.items()) for i in range(2,6)]
assert total==[4,0,0,0],total

def angles(h):
    q=h*h
    return dict(S=acos((q-.5)/(1+q)),O=acos((-q-.5)/(1+q)),
                V=2*atan(h))

def probs(h):
    a=angles(h);S,O,V=a['S'],a['O'],a['V']
    return (3*O/pi-2,
            9-6*(O+S)/pi-3*V/pi,
            3*(O+2*S+V-2*pi)/pi)

def derivative_factor(h):
    return 1+h/sqrt(4*h*h+3)-2*sqrt(3)*h/sqrt(4*h*h+1)

lo,hi=0.0,2.0
for _ in range(100):
    mid=(lo+hi)/2
    if derivative_factor(mid)>0: lo=mid
    else:hi=mid
hmax=(lo+hi)/2
assert abs(derivative_factor(hmax))<1e-14
assert 0.53146 < hmax < 0.53148
assert 0.38515 < probs(hmax)[2] < 0.38516

# Independent edge-crossing check from Gaussian normals.
for h in (0.1,0.5,1,2,5):
    a=angles(h)
    P=probs(h)
    assert all(0<p<1 for p in P) and abs(sum(P)-1)<2e-13
    # Each of 6 horizontal and 3 vertical edges crosses a random central plane
    # with probability of its endpoints' angular separation divided by pi.
    expected_n=(6*a['S']+3*a['V'])/pi
    assert abs(sum((3+i)*P[i] for i in range(3))-expected_n)<1e-12
    rng=Random(73221)
    counts=[0,0,0]
    for _ in range(80000):
        x,y,z=rng.gauss(0,1),rng.gauss(0,1),rng.gauss(0,1)
        scores=(x+h*z, -x/2+sqrt(3)*y/2+h*z, -x/2-sqrt(3)*y/2+h*z,
                x-h*z, -x/2+sqrt(3)*y/2-h*z, -x/2-sqrt(3)*y/2-h*z)
        sides=sum((scores[i]>0)!=(scores[j]>0) for i,j in edges)
        assert sides in (3,4,5)
        counts[sides-3]+=1
    assert max(abs(c/80000-P[i]) for i,c in enumerate(counts))<.015,(h,counts,P)
print('VERIFY_OK: 20 exact nonzero triple determinants, 64 exact sign patterns, '
      '32 spherical chambers; four area orbits and 400000 Gaussian trials')
print('h_star=',repr(hmax),'P5_max=',repr(probs(hmax)[2]))
for h in (0.1,0.5,1,2,5):print('h',h,'p3,p4,p5',tuple(round(x,12) for x in probs(h)))
