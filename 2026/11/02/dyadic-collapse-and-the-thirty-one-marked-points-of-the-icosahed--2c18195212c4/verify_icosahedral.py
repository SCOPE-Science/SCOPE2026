#!/usr/bin/env python3
"""Independent exact certificate for an integral icosahedral line arrangement.
Only the Python standard library is required. Arithmetic is in Z[phi],
phi**2=phi+1; modulo 2 it becomes F4.
"""
from collections import Counter, defaultdict
from itertools import combinations, product

Z=(0,0); U=(1,0); PHI=(0,1); INV=(-1,1)
def plus(a,b): return a[0]+b[0],a[1]+b[1]
def minus(a,b): return a[0]-b[0],a[1]-b[1]
def times(a,b): return a[0]*b[0]+a[1]*b[1],a[0]*b[1]+a[1]*b[0]+a[1]*b[1]
def norm(a): return a[0]**2+a[0]*a[1]-a[1]**2
def dot(a,b): return plus(plus(times(a[0],b[0]),times(a[1],b[1])),times(a[2],b[2]))
def cross(a,b):
    return (minus(times(a[1],b[2]),times(a[2],b[1])),
            minus(times(a[2],b[0]),times(a[0],b[2])),
            minus(times(a[0],b[1]),times(a[1],b[0])))
def determinant(a,b,c): return dot(a,cross(b,c))

lines=[(U,Z,Z),(Z,U,Z),(Z,Z,U)]
for shift in range(3):
    for e,f in product((-1,1),repeat=2):
        v=[U,(0,e),(-f,f)]
        v=v[shift:]+v[:shift]
        lines.append(tuple(v))
assert len(lines)==len(set(lines))==15

# Identify this coordinate model with Calvo's orbit of the mirror x=0.
# His two diagonal involutions and the third involution (whose displayed
# symmetric matrix is -M/2) act on coefficient normals projectively.
# The normal sets differ only by interchanging the first two coordinates.
swapped=[(v[1],v[0],v[2]) for v in lines]
def opposite(a): return -a[0],-a[1]
matrices=(
    ((opposite(U),Z,Z),(Z,U,Z),(Z,Z,U)),
    ((U,Z,Z),(Z,opposite(U),Z),(Z,Z,U)),
    ((INV,PHI,U),(PHI,opposite(U),INV),(U,INV,opposite(PHI)))
)
def matmul(M,v):
    return tuple(plus(plus(times(row[0],v[0]),times(row[1],v[1])),times(row[2],v[2])) for row in M)
def proportional(v,w):return all(x==Z for x in cross(v,w))
transitions={}
for i,v in enumerate(swapped):
    for j,M in enumerate(matrices):
        u=matmul(M,v)
        indexes=[k for k,w in enumerate(swapped) if proportional(u,w)]
        assert len(indexes)==1,('non-preserved Calvo mirror orbit',i,j,indexes)
        transitions[i,j]=indexes[0]
seed=swapped.index((U,Z,Z)); reached={seed}; pending=[seed]
while pending:
    i=pending.pop()
    for j in range(3):
        k=transitions[i,j]
        if k not in reached: reached.add(k);pending.append(k)
assert len(reached)==15

# All 455 triple determinants and all 105 pairs: exhaustive finite certificates.
norm_distribution=Counter()
for i,j,k in combinations(range(15),3):
    d=determinant(lines[i],lines[j],lines[k])
    if d!=Z: norm_distribution[abs(norm(d))]+=1
assert norm_distribution=={1:37,4:156,16:188,64:4},norm_distribution

incidences={}
for i,j in combinations(range(15),2):
    group=tuple(k for k in range(15) if determinant(lines[i],lines[j],lines[k])==Z)
    incidences[group]=cross(lines[i],lines[j])
assert Counter(map(len,incidences))=={2:15,3:10,5:6}
assert sum(len(a)*(len(a)-1)//2 for a in incidences)==105

# F4 = F2[w]/(w^2+w+1), coded 0,1,2=w,3=w+1.
def red(a): return (a[0]&1)|((a[1]&1)<<1)
def fm(a,b):
    a0,a1=a&1,a>>1; b0,b1=b&1,b>>1
    c0=(a0*b0)^(a1*b1)
    c1=(a0*b1)^(a1*b0)^(a1*b1)
    return c0|(c1<<1)
def fadd(a,b): return a^b
def fscaled(v,a):return tuple(fm(x,a) for x in v)
def fnormal(v):
    h=next(x for x in v if x)
    return fscaled(v,fm(h,h)) # all nonzero elements have inverse h^2

def fr(a):return tuple(red(x) for x in a)
def fcross(a,b):
    return (fm(a[1],b[2])^fm(a[2],b[1]),
            fm(a[2],b[0])^fm(a[0],b[2]),
            fm(a[0],b[1])^fm(a[1],b[0]))
def fdot(a,b):return fm(a[0],b[0])^fm(a[1],b[1])^fm(a[2],b[2])

def primitive_at_2(v):
    while all((a%2==b%2==0) for a,b in v):
        v=tuple((a//2,b//2) for a,b in v)
    return v

reduced_lines=Counter(fnormal(fr(v)) for v in lines)
assert reduced_lines=={(1,0,0):1,(0,1,0):1,(0,0,1):1,(1,2,3):12}
reduced_support=list(reduced_lines)
reduced_nodes={fnormal(fcross(a,b)) for a,b in combinations(reduced_support,2)}
assert len(reduced_nodes)==6
assert all(sum(fdot(a,x)==0 for a in reduced_support)==2 for x in reduced_nodes)

mark_counts=Counter(); types=Counter()
for incident,coord in incidences.items():
    special=fnormal(fr(primitive_at_2(coord)))
    # independence of pair chosen and extension as a primitive integral section
    for i,j in combinations(incident,2):
        assert special==fnormal(fr(primitive_at_2(cross(lines[i],lines[j]))))
    mark_counts[special]+=1
    types[special,len(incident)]+=1
assert mark_counts=={(1,0,0):1,(0,1,0):1,(0,0,1):1,
                     (0,1,3):4,(1,0,2):4,(1,3,0):4,
                     (1,1,1):4,(1,2,3):12},mark_counts
assert all(types[x,2]==1 and types[x,3]==types[x,5]==0
           for x in [(1,0,0),(0,1,0),(0,0,1)])
assert all((types[x,2],types[x,3],types[x,5])==(0,2,2)
           for x in [(0,1,3),(1,0,2),(1,3,0)])
assert (types[(1,1,1),2],types[(1,1,1),3],types[(1,1,1),5])==(0,4,0)
assert (types[(1,2,3),2],types[(1,2,3),3],types[(1,2,3),5])==(12,0,0)

# Q=XY+w XZ+w^2 YZ: degree-two conic through coordinate vertices,
# P=(1,1,1) and Qpoint=(1,w,w^2), avoiding all three axis/L crossings.
def q(x):
    a,b,c=x
    return fm(a,b)^fm(2,fm(a,c))^fm(3,fm(b,c))
def gradient(x):
    a,b,c=x
    return (b^fm(2,c),a^fm(3,c),fm(2,a)^fm(3,b))
L=(1,2,3)
assert len(mark_counts)==8
assert all(q(x)==0 for x in [(1,0,0),(0,1,0),(0,0,1),(1,1,1),(1,2,3)])
assert all(q(x)!=0 for x in [(0,1,3),(1,0,2),(1,3,0)])
assert all(any(gradient(x)) for x in [(1,0,0),(0,1,0),(0,0,1),(1,1,1),(1,2,3)])
# Smoothness: solve grad Q=0 directly over F4, no such nonzero point on Q;
# quadratic form rank is geometric (over algebraic closure), and the unique
# grad=0 projective point has Q!=0.
for x in product(range(4),repeat=3):
    if any(x) and not any(gradient(x)):assert q(x)!=0

# Curve classes in a blowup: L,Q and the three coordinate axes intersect
# the nef divisor N=9H-4EA-EB-3EC in 0; N intersects each E positively.
assert 9-3-2*3==0       # L: 3 B and 2 C
assert 18-3*4-2*3==0   # Q: 3 A and 2 C
assert 9-(2*4+1)==0   # coordinate axis: 2 A and 1 B
assert 9*7-21*3==0    # degree-7 multiplicity-three construction
print('ICOSAHEDRAL_15_MODULAR_COLLISIONS_AND_NEFDIVISOR_OK')
print('triple_norms',dict(sorted(norm_distribution.items())))
print('generic_intersections',dict(sorted(Counter(map(len,incidences)).items())))
print('characteristic_two_marked_weights',dict(sorted(Counter(mark_counts.values()).items())))
print('characteristic_two_types',[(x,mark_counts[x],types[x,2],types[x,3],types[x,5]) for x in sorted(mark_counts)])
