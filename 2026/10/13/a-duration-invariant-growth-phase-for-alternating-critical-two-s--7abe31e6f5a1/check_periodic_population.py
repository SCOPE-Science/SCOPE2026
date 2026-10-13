"""Exact-arithmetic spot and grid verification for a two-environment, critical Leslie model.
This program checks finite instances only; the unrestricted result follows from its proof.
"""
from fractions import Fraction as Q
from itertools import product

def matmul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def m_pow(a,m):
    out=((Q(1),Q(0)),(Q(0),Q(1)))
    for _ in range(m): out=matmul(out,a)
    return out

def det(a): return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def det_I(a):return Q(1)-a[0][0]-a[1][1]+det(a)
def L(j,f):return ((Q(1)-j*f,j),(f,Q(0)))

def verify(j,f,k,g,m,n):
    x,y=L(j,f),L(k,g)
    assert Q(0)<j*f<Q(1) and Q(0)<k*g<Q(1)
    assert det_I(x)==0 and det_I(y)==0
    am=(Q(1)-(-j*f)**m)/(Q(1)+j*f)
    bn=(Q(1)-(-k*g)**n)/(Q(1)+k*g)
    assert am>0 and bn>0
    p=matmul(m_pow(x,m),m_pow(y,n))
    assert det_I(p)==am*bn*(j-k)*(f-g)
    assert all(z>0 for r in p for z in r)
    # For a positive 2x2 matrix P with |det(P)| < 1,
    # sign(det(I-P)) is the sign of (1-rho(P)).
    assert abs(det(p))<1
    assert (det_I(p)>0)-(det_I(p)<0)==((j-k)*(f-g)>0)-((j-k)*(f-g)<0)

cases=0
params=[]
for j in (Q(1,5),Q(1,3),Q(1,2),Q(3,4)):
    for f in (Q(1,2),Q(1),Q(3,2),Q(2)):
        if j*f<1:params.append((j,f))
for (j,f),(k,g) in product(params,repeat=2):
    for m,n in product(range(1,9),repeat=2):
        verify(j,f,k,g,m,n)
        cases+=1

# A convex temporal average has the same strict phase as alternating blocks.
for (j,f),(k,g) in product(params,repeat=2):
    x,y=L(j,f),L(k,g)
    for t in (Q(1,7),Q(1,3),Q(1,2),Q(3,4),Q(6,7)):
        z=tuple(tuple((Q(1)-t)*x[i][b]+t*y[i][b] for b in range(2)) for i in range(2))
        assert det_I(z)==t*(Q(1)-t)*(j-k)*(f-g)
        assert all(z[i][b]>0 for i in range(2) for b in range(2) if not (i==1 and b==1))

# Two exact examples for the sharp signs.
x,y=L(Q(1,2),Q(1)),L(Q(1,4),Q(2))
assert det_I(matmul(x,y))==-Q(1,4)
x,y=L(Q(1,4),Q(1)),L(Q(1,2),Q(3,2))
assert det_I(matmul(x,y))==Q(1,8)

# Check the long-spell limit using exact spectral projections.
for (j,f),(k,g) in product(params,repeat=2):
    x,y=L(j,f),L(k,g)
    def projector(j,f):
        v=(Q(1),f)
        w=(Q(1),j)
        z=Q(1)+j*f
        return tuple(tuple(v[i]*w[t]/z for t in range(2)) for i in range(2))
    pa,pb=projector(j,f),projector(k,g)
    assert matmul(x,pa)==pa and matmul(y,pb)==pb
    pp=matmul(pa,pb)
    tr=pp[0][0]+pp[1][1]
    target=(Q(1)+j*g)*(Q(1)+k*f)/((Q(1)+j*f)*(Q(1)+k*g))
    assert tr==target and det(pp)==0
print('VERIFY_OK exact_pair_block_cases='+str(cases)+' parameter_pairs='+str(len(params)**2)+' mixed_signs_long_spells_and_averages=1')
