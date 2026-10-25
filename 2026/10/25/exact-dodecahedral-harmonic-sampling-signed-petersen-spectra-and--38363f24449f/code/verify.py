"""Exact arithmetic checks for the dodecahedral harmonic sampling spectrum.

Standard-library-only checker. Every tested Legendre value and eigenvalue is
represented by an exact rational number; no floating-point rank decisions.
"""
from fractions import Fraction as Q
from collections import Counter

ONE = Q(1)
ZERO = Q(0)

def add(x, y):
    return (x[0] + y[0], x[1] + y[1])

def neg(x):
    return (-x[0], -x[1])

def times(x, y):
    # x=(a,b) represents a+b sqrt(5).
    return (x[0]*y[0]+5*x[1]*y[1], x[0]*y[1]+x[1]*y[0])

def scale(x, s):
    return (x[0]*s, x[1]*s)

def dot(x, y):
    z=(ZERO,ZERO)
    for a,b in zip(x,y):
        z=add(z,times(a,b))
    return scale(z,Q(1,3))

# 20 unnormalized vertices, with squared Euclidean norm exactly 3.
phis=(Q(1,2),Q(1,2))
iphis=(Q(-1,2),Q(1,2))
O=(ZERO,ZERO)
U=(ONE,ZERO)
verts=[]
for a in (-1,1):
    for b in (-1,1):
        for c in (-1,1):
            verts.append(tuple(scale(U,Q(s)) for s in (a,b,c)))
for z in range(3):
    for s in (-1,1):
        for t in (-1,1):
            w=[O,O,O]
            w[(z+1)%3]=scale(iphis,Q(s))
            w[(z+2)%3]=scale(phis,Q(t))
            verts.append(tuple(w))
assert len(verts)==20 and len(set(verts))==20
for v in verts:
    assert dot(v,v)==U

# Pick one vertex from each antipodal pair; orientation is arbitrary.
rep=[]
for v in verts:
    if v not in rep and tuple(neg(a) for a in v) not in rep:
        rep.append(v)
assert len(rep)==10
A=[[0]*10 for _ in range(10)]
B=[[0]*10 for _ in range(10)]
C=[[0]*10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        t=dot(rep[i],rep[j])
        if i==j:
            assert t==U
        elif t in ((ZERO,Q(1,3)),(ZERO,Q(-1,3))):
            B[i][j]=1 if t[1]>0 else -1
            A[i][j]=1
        elif t in ((Q(1,3),ZERO),(Q(-1,3),ZERO)):
            C[i][j]=1 if t[0]>0 else -1
        else:
            raise AssertionError(('unexpected pairwise product', i,j,t))
assert all(sum(row)==3 for row in A)
assert all(sum(abs(s) for s in row)==3 for row in B)

def square(M):
    return [[sum(M[i][k]*M[k][j] for k in range(10))
             for j in range(10)] for i in range(10)]
AA=square(A)
BB=square(B)
for i in range(10):
    for j in range(10):
        assert AA[i][j]==2*(i==j)-A[i][j]+1
        assert BB[i][j]==3*(i==j)+C[i][j]
assert all(sum(BB[i][k]*B[k][j] for k in range(10)) == 5*B[i][j]
           for i in range(10) for j in range(10))
assert sum(B[i][i] for i in range(10))==0
assert sum(BB[i][i] for i in range(10))==30

# The matrix identities give eigenvalue/multiplicity lists:
# A: +3 (1), +1 (5), -2 (4).
# B: +sqrt(5) (3), -sqrt(5) (3), 0 (4).
# C = B^2 - 3 I, giving +2 on both 3-dimensional
# B eigenspaces and -3 on the 4-dimensional kernel.

def legendre_data(max_degree):
    # P_l(sqrt(5)/3) represented by a_l+b_l sqrt(5).
    p0,p1=(ONE,ZERO),(ZERO,Q(1,3))
    q0,q1=ONE,Q(1,3) # P_l(1/3)
    yield 0,p0,q0
    if max_degree==0: return
    yield 1,p1,q1
    for n in range(1,max_degree):
        mp=(5*p1[1]/3, p1[0]/3)
        p2=tuple(((2*n+1)*mp[i]-n*p0[i])/(n+1) for i in (0,1))
        q2=((2*n+1)*q1/3-n*q0)/(n+1)
        p0,p1,q0,q1=p1,p2,q1,q2
        yield n+1,p1,q1

def sectors(n,p,q):
    if n%2==0:
        assert p[1]==0
        a=p[0]
        return {'one':(1,ONE+3*a+6*q),
                'five':(5,ONE+a-2*q),
                'four':(4,ONE-2*a+q)}
    assert p[0]==0
    r=5*p[1] # sqrt(5)*P_l(sqrt(5)/3) is rational
    return {'three+':(3,ONE+r+2*q),
            'three-':(3,ONE-r+2*q),
            'four':(4,ONE-3*q)}

expected_rank=[1,3,5,7,9,6,10,10,9,10,10,10,10,10,9]
expected_zero={0:{'five','four'},1:{'three-','four'},
               2:{'one','four'},3:{'three+'},4:{'one'},
               5:{'four'},8:{'one'},14:{'one'}}
smallest=None
positive_values=[]
full=[]
num_rational_tests=0
for n,p,q in legendre_data(186):
    e=sectors(n,p,q)
    assert sum(m for m,v in e.values())==10
    zeros={name for name,(m,v) in e.items() if v==0}
    assert zeros==expected_zero.get(n,set()),(n,zeros)
    rank=sum(m for m,v in e.values() if v>0)
    if n<15: assert rank==expected_rank[n],(n,rank)
    else: assert rank==10,(n,rank)
    for name,(multiplicity,v) in e.items():
        num_rational_tests+=1
        assert v>=0,(n,name,v)
        if v>0: positive_values.append((v,n,name,multiplicity))
        if v>0 and (smallest is None or v<smallest[0]):
            smallest=(v,n,name,multiplicity)
    if rank==10:full.append(n)
assert smallest==(Q(3094,1594323),13,'three+',3),smallest
assert [t for t in positive_values if t[0]==smallest[0]]==[smallest]

# Laplace integral bound: |P_l(t)| <= sqrt(pi/(2*l*(1-t^2))).
# Use pi<22/7, sqrt(2)>140/99, giving
# C^2 = (pi/2)*(9/2+9/sqrt(2))^2 <186.
upper=Q(11,7)*(Q(9,2)+Q(891,140))**2
assert upper<186
qmin=Q(3094,1594323)
assert (1-qmin)**2>Q(186,187)
# Hence for every l>=187 Gershgorin gives each active
# parity-sector Gram eigenvalue >=2*(1-sqrt(186/l))>2*qmin.
print('DODECAHEDRON EXACT SAMPLING CHECK: PASS')
print('Unique vertices:',len(verts),'antipodal representatives:',len(rep))
print('Signed Petersen identities: PASS')
print('Exact Legendre rational sector checks:',num_rational_tests)
print('Exceptional ranks (degrees 0..14):',expected_rank)
print('All degrees 15..186: full parity rank 10')
print('Smallest positive quotient eigenvalue:',qmin,'at degree',smallest[1],
      'in multiplicity',smallest[3],'sector',smallest[2])
print('Global sharp positive Gram eigenvalue:',2*qmin)
print('Analytic tail, degrees >=187: certified with rational bounds')
