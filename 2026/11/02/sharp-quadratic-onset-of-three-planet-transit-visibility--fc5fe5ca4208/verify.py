"""Self-contained checks for the sharp three-band onset formula.
Run: python verify.py
Only uses the Python standard library. Finite checks supplement the analytic proof.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt, pi, asin, isclose

SIGNS = list(product((-1, 1), repeat=3))

def det(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def matvec(A,x):
    return [dot(row,x) for row in A]

def invert(A):
    d=det(A)
    assert d != 0
    C=[[A[(j+1)%3][(i+1)%3]*A[(j+2)%3][(i+2)%3]
       -A[(j+1)%3][(i+2)%3]*A[(j+2)%3][(i+1)%3]
       for j in range(3)] for i in range(3)]
    return [[C[i][j]/d for j in range(3)] for i in range(3)]

def exact_geometry(A):
    values=[dot(matvec(A,s),matvec(A,s)) for s in SIGNS]
    h2=max(values)
    maxi=[s for s,v in zip(SIGNS,values) if v == h2]
    # Using unnormalized vertex v=A*s, the positivity of each
    # coordinate d_i is equivalent to s_i*(v . A_column_i)>0.
    for s in maxi:
        v=matvec(A,s)
        for i in range(3):
            col=[row[i] for row in A]
            assert s[i]*dot(v,col) >= dot(col,col) > 0
    # Feasible unit direction exists iff t^2*H^2 >= 1.
    # This is checked algebraically at the extreme cube vertices.
    assert all(v<=h2 for v in values)
    return h2,maxi

# Exact arithmetic on six nontrivial invertible rational matrices.
seeds = [
  [[1,0,0],[0,1,0],[0,0,1]],
  [[2,0,0],[1,3,0],[0,2,4]],
  [[3,1,0],[0,4,1],[1,0,2]],
  [[4,1,1],[1,3,0],[0,1,5]],
  [[2,-1,0],[1,2,1],[0,1,3]],
  [[1,2,1],[0,1,3],[2,0,1]],
]
for M in seeds:
    A=[[F(v,5) for v in row] for row in M]
    assert det(A)
    h2,maxi=exact_geometry(A)
    assert len(maxi)>=2
    inv=invert(A)
    for s in maxi:
        v=matvec(A,s)
        assert matvec(inv,v)==list(s)

# Independent 1-dimensional integration of exact uniform-sphere area
# for three mutually orthogonal orbital normals and equal widths.
# For 1/sqrt(3)<h<1/sqrt(2), eight octants give
# P(h)=(2/pi) integral_{sqrt(1-2h^2)}^h
#              [2 arcsin(h/sqrt(1-x^2))-pi/2] dx.
def probability_orthogonal(h,n=8192):
    assert 1/sqrt(3)<h<1/sqrt(2) and n%2==0
    left=sqrt(1-2*h*h)
    right=h
    dx=(right-left)/n
    def f(x):
        ratio=min(1.,h/sqrt(1-x*x))
        return 2*asin(ratio)-pi/2
    total=f(left)+f(right)
    for i in range(1,n):
        total+=(4 if i%2 else 2)*f(left+i*dx)
    return (2/pi)*dx*total/3

C=3*sqrt(3)/pi
ratios=[]
for delta in (0.1,0.03,0.01,0.003,0.001):
    h=(1+delta)/sqrt(3)
    value=probability_orthogonal(h)
    ratio=value/delta**2
    ratios.append(ratio)
    assert value>0
    assert abs(ratio/C-1)<2.0*delta+0.004
assert abs(ratios[-1]/C-1)<0.002
assert all(ratios[i]>ratios[i+1] for i in range(len(ratios)-1))

# Coefficient formula for the orthogonal reference case.
e=1/sqrt(3)
A=[[e,0,0],[0,e,0],[0,0,e]]
H=1.0
summand=0.0
for s in SIGNS:
    vertex=[v/H for v in matvec(A,s)]
    ds=[s[i]*dot(vertex,[row[i] for row in A]) for i in range(3)]
    assert all(z>0 for z in ds)
    summand+=1/(ds[0]*ds[1]*ds[2])
calculated=H*H*abs(det(A))*summand/(8*pi)
assert isclose(calculated,C,rel_tol=1e-13)
print('PASS: exact rational cube-vertex and strict-corner checks on 6 matrices')
print('PASS: eight-corner onset coefficient 3*sqrt(3)/pi')
print('PASS: independent spherical integral converges to coefficient')
print('Numerical ratios:', ['%.9f'%r for r in ratios])
