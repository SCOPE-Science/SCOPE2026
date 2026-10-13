from fractions import Fraction
from itertools import product, combinations
from math import isclose, sqrt

pts=list(product((-1,1), repeat=3))
# coefficient order: 12,13,14,23,24,34
A=[]
for u,v,w in pts:
    A.append((u,v,w,u*v,u*w,v*w))

for col in range(6):
    for parity in (-1,1):
        s=sum(A[r][col] for r,(u,v,w) in enumerate(pts) if u*v*w==parity)
        assert s==0

def eval_coeff(a):
    return [sum(ai*x for ai,x in zip(a,row)) for row in A]

def ratio(a):
    y=eval_coeff(a)
    l1=Fraction(sum(abs(z) for z in y),8)
    l2sq=Fraction(sum(z*z for z in y),8)
    return float(sqrt(float(l2sq))/float(l1))

order=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
partitions=(((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2)))
patterns=[]
for (i,j),(k,l) in partitions:
    for s in (-1,1):
        for t in (-1,1):
            d={}
            for a,ca in ((i,1),(j,s)):
                for b,cb in ((k,1),(l,t)):
                    key=tuple(sorted((a,b)))
                    d[key]=d.get(key,0)+ca*cb
            coeff=tuple(d.get(q,0) for q in order)
            y=eval_coeff(coeff)
            supp=tuple(r for r,z in enumerate(y) if z)
            assert len(supp)==2
            assert pts[supp[0]][0]*pts[supp[0]][1]*pts[supp[0]][2] == pts[supp[1]][0]*pts[supp[1]][1]*pts[supp[1]][2]
            assert isclose(ratio(coeff),2.0,rel_tol=0,abs_tol=1e-12)
            patterns.append(frozenset(supp))

same_parity_pairs=[]
for i,j in combinations(range(8),2):
    pi=pts[i][0]*pts[i][1]*pts[i][2]
    pj=pts[j][0]*pts[j][1]*pts[j][2]
    if pi==pj:
        same_parity_pairs.append(frozenset((i,j)))
assert len(patterns)==12
assert len(set(patterns))==12
assert set(patterns)==set(same_parity_pairs)

# n=3 sharp witness: h=e1(e2+e3) has four reduced values +/-2,0,0.
y3=[u+v for u,v in product((-1,1), repeat=2)]
l1=sum(abs(z) for z in y3)/4
l2=sqrt(sum(z*z for z in y3)/4)
assert isclose(l2/l1,sqrt(2),rel_tol=0,abs_tol=1e-12)
print('VERIFY_OK parity_sums=12 equality_orbits=12 n3_witness=sqrt2')
