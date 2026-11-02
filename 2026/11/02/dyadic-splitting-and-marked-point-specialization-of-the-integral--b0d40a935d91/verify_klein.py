#!/usr/bin/env python3
"""Exact arithmetic checks for the quadratic-integral model of Klein's 21-line divisor.

All algebraic-integer calculations use Z[a]/(a*a+a+2). No floating point,
randomization, black-box computer algebra, or external files are required.
"""
from itertools import combinations
from collections import Counter, defaultdict

ZERO=(0,0)
ONE=(1,0)
ALPHA=(0,1)

def plus(x,y):
    return (x[0]+y[0],x[1]+y[1])

def minus(x):
    return (-x[0],-x[1])

def times(x,y):
    # alpha^2 = -alpha-2
    return (x[0]*y[0]-2*x[1]*y[1],
            x[0]*y[1]+x[1]*y[0]-x[1]*y[1])

def determinant(a,b,c):
    out=ZERO
    for i,j,k,sign in ((0,1,2,1),(1,2,0,1),(2,0,1,1),
                       (0,2,1,-1),(1,0,2,-1),(2,1,0,-1)):
        term=times(a[i], times(b[j],c[k]))
        out=plus(out,term if sign==1 else minus(term))
    return out

def norm(x):
    # Minimal polynomial of alpha: t^2+t+2; field norm is positive definite.
    u,v=x
    return u*u-u*v+2*v*v

# The 21 line equations in Gevay--Pokora, arXiv:2211.15309, section 2.1.
# Entries (u,v) encode the coefficient u+v*alpha, alpha^2+alpha+2=0.
L=[
 (ONE,ZERO,ZERO), (ZERO,ONE,ONE), (ALPHA,ONE,minus(ONE)),
 (ALPHA,minus(ONE),ONE), (ZERO,minus(ONE),ONE),
 (ONE,ALPHA,minus(ONE)),(ALPHA,minus(ONE),minus(ONE)),
 (minus(ONE),ONE,ALPHA),(ALPHA,ONE,ONE),(minus(ONE),ALPHA,ONE),
 (minus(ONE),minus(ONE),ALPHA),(ONE,ZERO,ONE),
 (minus(ONE),ALPHA,minus(ONE)),(ONE,ALPHA,ONE),
 (minus(ONE),ZERO,ONE),(ONE,minus(ONE),ALPHA),(ONE,ONE,ALPHA),
 (ZERO,ZERO,ONE),(minus(ONE),ONE,ZERO),(ONE,ONE,ZERO),
 (ZERO,ONE,ZERO),
]
assert len(L)==21
assert all(any(a in (ONE,minus(ONE)) for a in row) for row in L)

# Every triple of lines: complete exact norm catalogue.
norm_hist=Counter()
point_to_pair={}
for i,j,k in combinations(range(21),3):
    norm_hist[norm(determinant(L[i],L[j],L[k]))]+=1
assert norm_hist=={0:112,1:169,2:228,4:271,8:320,16:156,32:70,64:4}, norm_hist
for i,j in combinations(range(21),2):
    # A unit-norm witness prevents these two lines from coalescing away from 2.
    assert any(norm(determinant(L[i],L[j],L[k])) != 0
               for k in range(21) if k not in (i,j))
    incident=tuple(k for k in range(21)
                   if determinant(L[i],L[j],L[k])==ZERO)
    point_to_pair.setdefault(incident,(i,j))
assert len(point_to_pair)==49
assert Counter(map(len,point_to_pair))=={3:28,4:21}
assert sum(len(g)*(len(g)-1)//2 for g in point_to_pair)==210

# At 2 the ring of integers has the two residue maps alpha -> 0 and 1.
def norm_projective(vec):
    nz=next((u for u in vec if u),None)
    assert nz is not None
    return tuple((u*pow(nz,-1,2))%2 for u in vec)

def at_alpha(row,a):
    return tuple((u+a*v)%2 for u,v in row)

def reduced_divisor(a):
    grouped=Counter(norm_projective(at_alpha(row,a)) for row in L)
    X=(1,0,0);Y=(0,1,0);Z=(0,0,1)
    XY=(1,1,0); XZ=(1,0,1);YZ=(0,1,1);XYZ=(1,1,1)
    if a==0:
        expected={X:1,Y:1,Z:1,XY:6,XZ:6,YZ:6}
    else:
        expected={X:1,Y:1,Z:1,XY:2,XZ:2,YZ:2,XYZ:12}
    assert grouped==expected, (a,grouped)
    assert sum(grouped.values())==21
    return grouped

for a in (0,1):
    groups=reduced_divisor(a)
    # The pairwise intersection lattice of the reduced divisor.
    distinct=list(groups)
    def d2(u,v,w):
        return (u[0]*(v[1]*w[2]-v[2]*w[1])
                -u[1]*(v[0]*w[2]-v[2]*w[0])
                +u[2]*(v[0]*w[1]-v[1]*w[0]))%2
    support={tuple(k for k in range(len(distinct))
                   if d2(distinct[i],distinct[j],distinct[k])==0)
             for i,j in combinations(range(len(distinct)),2)}
    assert len(support)==7
    assert Counter(map(len,support))==({3:4,2:3} if a==0 else {3:7})

# Specialization of a characteristic-zero projective intersection point.
# Divide its cross-product by the local uniformizer until a coordinate is a unit.
# alpha is a uniformizer at (2,alpha), and alpha+1 at (2,alpha+1).
def cross(a,b):
    return (plus(times(a[1],b[2]),minus(times(a[2],b[1]))),
            plus(times(a[2],b[0]),minus(times(a[0],b[2]))),
            plus(times(a[0],b[1]),minus(times(a[1],b[0]))))

def divide_uniformizer(x,a):
    u,v=x
    if a==0:
        assert u%2==0
        return (-(u-2*v)//2,-u//2)
    assert (u-v)%2==0
    return (v,-(u-v)//2)

def limit(i,j,a):
    coords=cross(L[i],L[j]); depth=0
    while all((u+a*v)%2==0 for u,v in coords):
        coords=tuple(divide_uniformizer(t,a) for t in coords)
        depth+=1
        assert depth<=8
    return tuple((u+a*v)%2 for u,v in coords)

# Table indexed by point over F2: (quadruple count, triple count), for each prime.
expected={
  0:{(1,0,0):(1,4),(0,1,0):(1,4),(0,0,1):(1,4),
     (1,1,0):(2,0),(1,0,1):(2,0),(0,1,1):(2,0),(1,1,1):(12,16)},
  1:{(1,0,0):(1,0),(0,1,0):(1,0),(0,0,1):(1,0),
     (1,1,0):(6,8),(1,0,1):(6,8),(0,1,1):(6,8),(1,1,1):(0,4)},
}
for a in (0,1):
    result=defaultdict(lambda:[0,0])
    for incident,pair in point_to_pair.items():
        image=limit(*pair,a)
        for alternative in combinations(incident,2):
            assert limit(*alternative,a)==image
        result[image][0 if len(incident)==4 else 1]+=1
    actual={p:tuple(c) for p,c in result.items()}
    assert actual==expected[a],(a,actual)
    assert sum(t[0] for t in actual.values())==21
    assert sum(t[1] for t in actual.values())==28
print('KLEIN_21_INTEGRAL_ARITHMETIC_REDUCTION_AND_49_SPECIALIZATIONS_PASS')
print('Triple determinant norms:',dict(sorted(norm_hist.items())))
print('Dyadic special fibers: alpha=0 -> 6 lines; alpha=1 -> 7 Fano lines.')
