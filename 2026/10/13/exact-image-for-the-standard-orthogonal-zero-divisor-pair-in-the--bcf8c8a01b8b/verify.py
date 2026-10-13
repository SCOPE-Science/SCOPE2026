import sympy as sp

# 2x2 matrix utilities for the Cayley-Dickson model O=M2(F) + M2(F) w, w^2=1.
def bar(A):
    return sp.trace(A)*sp.eye(2) - A

def omul(u,v):
    a,x = u
    b,y = v
    return (a*b + bar(y)*x, y*a + x*bar(b))

def oadd(u,v):
    return (u[0]+v[0], u[1]+v[1])

def osub(u,v):
    return (u[0]-v[0], u[1]-v[1])

def lmul_matrix(A, z):
    return omul((A,sp.zeros(2)), z)

E11=sp.Matrix([[1,0],[0,0]])
E12=sp.Matrix([[0,1],[0,0]])
E21=sp.Matrix([[0,0],[1,0]])
E22=sp.Matrix([[0,0],[0,1]])
p0,n0=E11,E12

# General symbolic x,y.
xs=sp.symbols('x11 x12 x21 x22 u11 u12 u21 u22')
ys=sp.symbols('y11 y12 y21 y22 v11 v12 v21 v22')
x=(sp.Matrix([[xs[0],xs[1]],[xs[2],xs[3]]]), sp.Matrix([[xs[4],xs[5]],[xs[6],xs[7]]]))
y=(sp.Matrix([[ys[0],ys[1]],[ys[2],ys[3]]]), sp.Matrix([[ys[4],ys[5]],[ys[6],ys[7]]]))
phi=osub(lmul_matrix(p0, omul(x,y)), lmul_matrix(n0, omul(y,x)))
# Global containment: quaternion part always has zero lower row.
assert sp.expand(phi[0][1,0]) == 0
assert sp.expand(phi[0][1,1]) == 0

# Fixed slice x0=E11+E21 (with zero omega part).
x0=(E11+E21, sp.zeros(2))
basis=[E11,E12,E21,E22]
obasis=[(b,sp.zeros(2)) for b in basis] + [(sp.zeros(2),b) for b in basis]

def coords(z):
    a,b=z
    return sp.Matrix([a[0,0],a[0,1],a[1,0],a[1,1],b[0,0],b[0,1],b[1,0],b[1,1]])

cols=[]
for e in obasis:
    z=osub(lmul_matrix(p0, omul(x0,e)), lmul_matrix(n0, omul(e,x0)))
    cols.append(coords(z))
M=sp.Matrix.hstack(*cols)
expected=sp.Matrix([
    [1,0,-1,-1,0,0,0,0],
    [0,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,1,1,0,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,0,1],
])
assert M == expected
minor=M.extract([0,1,4,5,6,7],[0,1,4,5,6,7])
assert sp.det(minor) == 1
assert M.rank() == 6

# Its image is exactly W = span(E11,E12,E11w,E12w,E21w,E22w).
W_indices=[0,1,4,5,6,7]
assert all(M.row(i)==sp.zeros(1,8) for i in [2,3])
assert M.extract(W_indices,W_indices).det()==1

# p0,n0 are independent zero divisors, and their polar norm is zero in this model.
def det(A): return sp.expand(A.det())
assert det(p0)==0 and det(n0)==0 and det(p0+n0)==0
# N(a+xw)=det(a)-det(x); here omega parts are zero.
polar=det(p0+n0)-det(p0)-det(n0)
assert polar==0

print('slice_matrix=')
print(M)
print('minor_det=', sp.det(minor))
print('slice_rank=', M.rank())
print('global_quaternion_lower_row=', [sp.expand(phi[0][1,0]), sp.expand(phi[0][1,1])])
print('polar_norm_p0_n0=', polar)
print('VERIFY_OK')
