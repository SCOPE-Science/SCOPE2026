"""Exact rational-polygon certificate for six-direction lattice arrangements.

Standard library only. Each primitive direction has all integral offsets -n..n.
The certificate calculates Ehrhart coefficients for every subset of directions
and recovers all finite intersection multiplicities via binomial inversion.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from math import atan2, comb, gcd

DIRECTIONS = [(1,0),(0,1),(1,1),(1,-1),(1,2),(2,1)]

def det(u,v):
    return u[0]*v[1]-u[1]*v[0]

def poly(S):
    vertices=set()
    for (a,b),(c,d) in combinations(S,2):
        dd=a*d-b*c
        assert dd
        for s,t in product((-1,1),repeat=2):
            x,y=Q(s*d-b*t,dd),Q(a*t-s*c,dd)
            if all(abs(e*x+f*y)<=1 for e,f in S):
                vertices.add((x,y))
    v=list(vertices)
    assert len(v)>=3
    center=(sum((x for x,y in v),Q(0))/len(v),
            sum((y for x,y in v),Q(0))/len(v))
    v.sort(key=lambda p: atan2(float(p[1]-center[1]),float(p[0]-center[0])))
    for i in range(len(v)):
        a,b,c=v[i-1],v[i],v[(i+1)%len(v)]
        assert det((b[0]-a[0],b[1]-a[1]),(c[0]-b[0],c[1]-b[1]))>0
        assert all((6*q).denominator==1 for q in b)
    return v

def ehrhart(S):
    v=poly(S)
    area=abs(sum(x*v2-y*u for (x,y),(u,v2) in zip(v,v[1:]+v[:1])))/2
    index=0
    for p,q in combinations(S,2):
        index=gcd(index,abs(det(p,q)))
    edge_steps=0
    for p,q in zip(v,v[1:]+v[:1]):
        delta=(6*(q[0]-p[0]),6*(q[1]-p[1]))
        dots=[a*delta[0]+b*delta[1] for a,b in S]
        assert all(z.denominator==1 for z in dots)
        steps=0
        for z in dots: steps=gcd(steps,abs(int(z)))
        edge_steps+=steps
    return (index*area,Q(edge_steps,12),Q(1))

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(c,a): return tuple(c*x for x in a)

M={j:(Q(0),Q(0),Q(0)) for j in range(2,7)}
for j in range(2,7):
    for choice in combinations(DIRECTIONS,j):
        M[j]=add(M[j],ehrhart(choice))
assert M=={2:(60,60,15),3:(39,39,20),4:(21,21,15),5:(7,7,6),6:(1,1,1)}
T={}
for j in range(6,1,-1):
    T[j]=M[j]
    for k in range(j+1,7):
        T[j]=sub(T[j],mul(comb(k,j),T[k]))
assert T=={2:(14,14,0),3:(5,5,0),4:(1,1,0),5:(1,1,0),6:(1,1,1)}

def value(poly,n):return poly[0]*n*n+poly[1]*n+poly[2]
for n in (6,12,18,24):
    finite={m:int(value(t,n)) for m,t in T.items()}
    d=12*n+6
    total=dict(finite)
    total[2*n+1]=6
    assert sum(comb(m,2)*c for m,c in total.items())==comb(d,2)
    c1=9-5*d+sum((3*m-4)*c for m,c in total.items())
    c2=3-2*d+sum((m-1)*c for m,c in total.items())
    assert (c1,c2)==(86*n*n+62*n-13,36*n*n+24*n-4)
print('EXACT_EHRHART_CERTIFICATE_OK')
print('Subset-count coefficients:',M)
print('Finite multiplicity coefficients:',T)
print('Log Chern coefficients: (86,62,-13); (36,24,-4)')
