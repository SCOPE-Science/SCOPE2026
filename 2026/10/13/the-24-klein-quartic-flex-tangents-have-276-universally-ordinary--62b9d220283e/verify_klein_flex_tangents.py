"""Exact arithmetic certificate for the 24 inflection-tangent arrangement of Klein's quartic.
Requires only Python 3 standard library. Integers represent Z[zeta_7] in basis 1,z,...,z^5.
"""
from collections import Counter
from itertools import combinations

ZERO=(0,)*6
ONE=(1,0,0,0,0,0)

def plus(a,b):return tuple(a[i]+b[i] for i in range(6))
def minus(a,b):return tuple(a[i]-b[i] for i in range(6))
def times(a,b):
    c=[0]*7
    for i in range(6):
        for j in range(6):
            c[(i+j)%7]+=a[i]*b[j]
    return tuple(c[i]-c[6] for i in range(6))
def scalar(a,n):return tuple(n*x for x in a)
def power(a,n):
    q=ONE
    while n:
        if n&1:q=times(q,a)
        a=times(a,a);n//=2
    return q

def sum3(a,b,c):return plus(plus(a,b),c)
def dot(a,b):
    v=ZERO
    for x,y in zip(a,b):v=plus(v,times(x,y))
    return v

def cross(a,b):
    return (minus(times(a[1],b[2]),times(a[2],b[1])),
            minus(times(a[2],b[0]),times(a[0],b[2])),
            minus(times(a[0],b[1]),times(a[1],b[0])))

def det3(a,b,c):return dot(a,cross(b,c))

def bareiss(A):
    A=[row[:] for row in A]
    n=len(A);sgn=1;prev=1
    for k in range(n-1):
        if A[k][k]==0:
            for r in range(k+1,n):
                if A[r][k]:
                    A[k],A[r]=A[r],A[k];sgn*=-1;break
            else:return 0
        v=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=A[i][j]*v-A[i][k]*A[k][j]
                assert numerator%prev==0
                A[i][j]=numerator//prev
        for i in range(k+1,n):A[i][k]=0
        prev=v
    return sgn*A[-1][-1]

def norm(a):
    basis=[tuple(int(i==j) for i in range(6)) for j in range(6)]
    columns=[times(a,e) for e in basis]
    matrix=[[columns[j][i] for j in range(6)] for i in range(6)]
    return bareiss(matrix)

zeta=(0,1,0,0,0,0)
Z=[power(zeta,k) for k in range(7)]
points=[(ONE,ZERO,ZERO),(ZERO,ONE,ZERO),(ZERO,ZERO,ONE)]
for j in range(7):
    P=(times(Z[(3*j)%7],minus(Z[1],Z[6])),
       times(Z[j],minus(Z[2],Z[5])),minus(Z[4],Z[3]))
    points.extend([P,(P[1],P[2],P[0]),(P[2],P[0],P[1])])
assert len(points)==24

def F(p):
    x,y,z=p
    return sum3(times(power(x,3),y),times(power(y,3),z),times(power(z,3),x))

def H0(p):
    x,y,z=p
    return sum3(plus(times(power(x,5),z),times(x,power(y,5))),
                minus(ZERO,scalar(times(times(power(x,2),power(y,2)),power(z,2)),5)),
                times(y,power(z,5)))

def tangent(p):
    x,y,z=p
    return (plus(scalar(times(power(x,2),y),3),power(z,3)),
            plus(power(x,3),scalar(times(power(y,2),z),3)),
            plus(power(y,3),scalar(times(power(z,2),x),3)))
assert all(F(p)==ZERO and H0(p)==ZERO for p in points)
lines=[]
for i,p in enumerate(points):
    L=tangent(p)
    assert dot(L,p)==ZERO
    if i>=3:
        assert all(c%7==0 for e in L for c in e)
        L=tuple(tuple(c//7 for c in e) for e in L)
    lines.append(L)
assert all(cross(a,b)!=(ZERO,ZERO,ZERO) for a,b in combinations(lines,2))

# A complete census of the 2024 unordered triples of the 24 lines.
norm_counts=Counter()
for ids in combinations(range(24),3):
    v=det3(*[lines[i] for i in ids]);assert v!=ZERO,ids
    n=abs(norm(v));assert n>0
    norm_counts[n]+=1
expected={1:1,7:63,343:441,2401:63,2744:126,
          117649:735,823543:378,941192:210,40353607:7}
assert norm_counts==Counter(expected),(norm_counts,expected)
assert sum(norm_counts.values())==2024
for n in norm_counts:
    v=n
    for p in (2,7):
        while v%p==0:v//=p
    assert v==1

# Apply Gal(Q(zeta_7)/Q), zeta -> zeta**a, to each projective tangent.
def conjugate(e,a):
    value=ZERO
    for k,c in enumerate(e):
        value=plus(value,scalar(Z[(a*k)%7],c))
    return value

def collinear(a,b):return cross(a,b)==(ZERO,ZERO,ZERO)

fixed_line_counts={};fixed_pair_counts={};cycles_by_a={};pair_cycles_by_a={}
for a in range(1,7):
    sigma=[]
    for L in lines:
        gL=tuple(conjugate(c,a) for c in L)
        matches=[j for j,R in enumerate(lines) if collinear(gL,R)]
        assert len(matches)==1,(a,matches)
        sigma.append(matches[0])
    assert sorted(sigma)==list(range(24))
    fixed_line_counts[a]=sum(i==sigma[i] for i in range(24))
    fixed_pair_counts[a]=sum({i,j}=={sigma[i],sigma[j]}
                              for i,j in combinations(range(24),2))
    unvisited=set(range(24));cycle_sizes=[]
    while unvisited:
        v=next(iter(unvisited));orb=set()
        while v not in orb:
            orb.add(v);v=sigma[v]
        assert v==next(iter(orb)) or v in orb
        assert orb.issubset(unvisited)
        unvisited-=orb;cycle_sizes.append(len(orb))
    cycles_by_a[a]=sorted(cycle_sizes)
    unvisited_pairs=set(combinations(range(24),2));pair_cycle_sizes=[]
    while unvisited_pairs:
        pair=next(iter(unvisited_pairs));p=pair;orbit=set()
        while p not in orbit:
            orbit.add(p)
            p=tuple(sorted((sigma[p[0]],sigma[p[1]])))
        assert orbit.issubset(unvisited_pairs)
        unvisited_pairs-=orbit
        pair_cycle_sizes.append(len(orbit))
    pair_cycles_by_a[a]=Counter(pair_cycle_sizes)
assert fixed_line_counts=={1:24,2:3,3:3,4:3,5:3,6:6},fixed_line_counts
assert fixed_pair_counts=={1:276,2:3,3:3,4:3,5:3,6:24},fixed_pair_counts

print('VERIFY_OK')
print('triple_determinant_norm_distribution:', sorted(norm_counts.items()))
print('Galois_fixed_lines:',fixed_line_counts)
print('Galois_fixed_intersections:',fixed_pair_counts)
assert pair_cycles_by_a[3]==Counter({1:3,3:7,6:42}),pair_cycles_by_a[3]
print('Galois_cycles:',cycles_by_a)
print('Intersection_orbits_over_Q:',dict(sorted(pair_cycles_by_a[3].items())))
