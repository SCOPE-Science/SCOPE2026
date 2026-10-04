from fractions import Fraction as F
from itertools import product

# A polynomial is c0 + c1*a + c2*a^2, stored as exact Fractions.
def add(*ps):
    return tuple(sum((p[i] for p in ps), F(0)) for i in range(3))
def mul_scalar(p,s):
    return tuple(s*x for x in p)
def val(p,a):
    return p[0]+p[1]*a+p[2]*a*a

def min_quad_on_interval(p,L,R):
    pts=[L,R]
    if p[2] != 0:
        x=-p[1]/(2*p[2])
        if L <= x <= R:
            pts.append(x)
    return min(val(p,x) for x in pts)

SUPPORT = [
((0,0,0,0,4),(F(1),F(-4),F(71,16))),
((0,0,0,1,3),(F(0),F(1),F(-3,2))),
((0,0,1,0,3),(F(0),F(1),F(-27,16))),
((0,0,3,0,1),(F(0),F(0),F(1,16))),
((0,1,0,0,3),(F(0),F(1),F(-33,16))),
((0,1,1,2,0),(F(0),F(0),F(3,8))),
((0,1,2,0,1),(F(0),F(0),F(3,16))),
((0,2,0,0,2),(F(0),F(0),F(3,8))),
((1,0,0,0,3),(F(0),F(1),F(-5,2))),
((1,0,0,1,2),(F(0),F(0),F(3,4))),
((1,0,1,0,2),(F(0),F(0),F(3,4))),
((1,1,0,0,2),(F(0),F(0),F(3,4))),
((4,0,0,0,0),(F(0),F(0),F(1,16))),
]

def reject(n):
    n1,n2,n3,n4,n5=n
    return (n1>=1 or n1+n2>=2 or n1+n2+n3>=3 or n1+n2+n3+n4>=4)

def B(n):
    n1,n2,n3,n4,n5=n
    return (F(1,12)*n1*(n1-1) + F(1,2)*n2*(n2-1)
            + F(1,6)*n3*(n3-1) + F(1,6)*n4*(n4-1)
            + F(1,3)*(n1*n2+n1*n3+n1*n4+n1*n5+n2*n3)
            + F(1,6)*n3*n4)

def comps(total,k,prefix=()):
    if k==1:
        yield prefix+(total,)
        return
    for x in range(total+1):
        yield from comps(total-x,k-1,prefix+(x,))

# The dual certificate majorizes the Simes rejection indicator on all 70 cells.
all_cells=list(comps(4,5))
assert len(all_cells)==70
for n in all_cells:
    assert B(n) >= (1 if reject(n) else 0)

# Extremizer weights are probabilities throughout 0 <= a <= 2/5.
L,R=F(0),F(2,5)
for n,q in SUPPORT:
    assert min_quad_on_interval(q,L,R) >= 0
assert add(*(q for _,q in SUPPORT)) == (F(1),F(0),F(0))

# Exact first and pairwise category moments.
means=[]
for j in range(5):
    means.append(add(*(mul_scalar(q,n[j]) for n,q in SUPPORT)))
assert means[:4] == [(F(0),F(1),F(0))]*4
assert means[4] == (F(4),F(-4),F(0))

for j in range(5):
    diag=add(*(mul_scalar(q,n[j]*(n[j]-1)) for n,q in SUPPORT))
    target=(F(0),F(0),F(3,4)) if j<4 else (F(12),F(-24),F(12))
    assert diag==target
for j in range(5):
    for k in range(j+1,5):
        cross=add(*(mul_scalar(q,n[j]*n[k]) for n,q in SUPPORT))
        target=(F(0),F(0),F(3,4)) if k<4 else (F(0),F(3),F(-3))
        assert cross==target

# Every support cell lies on equality of the dual certificate.
for n,q in SUPPORT:
    assert B(n) == (1 if reject(n) else 0)

# Hence the attained rejection probability is a + 13 a^2/16.
obj=add(*(q for n,q in SUPPORT if reject(n)))
assert obj == (F(0),F(1),F(13,16))

a=F(1,20)
exact=val(obj,a)
assert exact == F(333,6400)
print('VERIFY_OK')
print('objective_polynomial = a + 13*a^2/16')
print('alpha=1/20 exact_size = 333/6400')
print('alpha=1/20 decimal =', float(exact))
