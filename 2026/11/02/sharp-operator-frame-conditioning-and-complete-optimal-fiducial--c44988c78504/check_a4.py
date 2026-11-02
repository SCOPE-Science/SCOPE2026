"""Exact symbolic checks for the tetrahedral complex projective 2-design theorem.

Requires Python 3 and SymPy. Run: python3 check_a4.py
All group elements, moments, and reconstruction identities are computed afresh.
"""
import sympy as s
from itertools import product

checks=0

def check(c,label):
    global checks
    if not c:
        raise AssertionError(label)
    checks+=1

def zero(x):
    return s.simplify(s.expand_complex(x)) == 0

def matzero(A):
    return all(zero(x) for x in A)

R=s.Matrix([[0,0,1],[1,0,0],[0,1,0]])
Ds=[s.diag(*eps) for eps in product([1,-1],repeat=3) if s.prod(eps)==1]
Gs=[D*(R**k) for D in Ds for k in range(3)]
check(len(Gs)==12 and len({tuple(g) for g in Gs})==12,"12 distinct matrices")
check(all(g.T*g==s.eye(3) and g.det()==1 for g in Gs),"orthogonal rotations")
check(all(any(g*h == k for k in Gs) for g in Gs for h in Gs),"closure")

# In the symmetric tensor square, diagonal coordinates precede cross coordinates.
B=[]
for i in range(3):
    b=s.zeros(9,1); b[3*i+i]=1; B.append(b)
for i,j in [(0,1),(1,2),(2,0)]:
    b=s.zeros(9,1)
    b[3*i+j]=1/s.sqrt(2)
    b[3*j+i]=1/s.sqrt(2)
    B.append(b)
B=s.Matrix.hstack(*B)
check(matzero(B.conjugate().T*B-s.eye(6)),"symmetric basis orthonormal")

def symmetric_moment(v):
    w=s.kronecker_product(v,v)
    out=s.zeros(6)
    for g in Gs:
        gw=s.kronecker_product(g,g)*w
        u=B.conjugate().T*gw
        out+=u*u.conjugate().T
    return out/12

def predicted_moment(v):
    a,b,c=v
    z=s.Matrix([a*a,b*b,c*c])
    Q=s.expand(sum((s.conjugate(t)*t)**2 for t in v))
    U=s.expand(z[0]*s.conjugate(z[1])+z[1]*s.conjugate(z[2])+z[2]*s.conjugate(z[0]))
    # Mean of the cyclic conjugates of z z* (same result without relying on U orientation).
    h=s.zeros(3)
    for k in range(3):
        w=(R**k)*z
        h+=w*w.conjugate().T/3
    out=s.zeros(6)
    out[:3,:3]=h
    for i in range(3,6):
        out[i,i]=(1-Q)/3
    return out

# Independently test the universal symmetry reduction on several unrelated seeds.
for raw in [s.Matrix([1,2,3]),s.Matrix([1,2*s.I,3]),s.Matrix([1+s.I,2+s.I,1])]:
    v=raw/s.sqrt((raw.conjugate().T*raw)[0])
    check(matzero(symmetric_moment(v)-predicted_moment(v)),"exact general twirl")

v=s.Matrix([s.sqrt(s.Rational(2,3)),(s.sqrt(7)+3*s.I)/(4*s.sqrt(6)),(s.sqrt(7)+3*s.I)/(4*s.sqrt(6))])
check(zero((v.conjugate().T*v)[0]-1),"unit seed")
a,b,c=v
Q=sum((s.conjugate(t)*t)**2 for t in v)
U=a*a*s.conjugate(b*b)+b*b*s.conjugate(c*c)+c*c*s.conjugate(a*a)
check(zero(Q-s.Rational(1,2)),"amplitudes quartic")
check(zero(U),"phase quartic")
M=symmetric_moment(v)
check(matzero(M-s.eye(6)/6),"exact design moment on Sym²")

P=[(g*v)*(g*v).conjugate().T for g in Gs]
check(matzero(sum(P,s.zeros(3))-4*s.eye(3)),"first moment")
F=s.zeros(9)
for i in range(3):
    for j in range(3):
        F[3*i+j,3*j+i]=1
check(matzero(sum((s.kronecker_product(p,p) for p in P),s.zeros(9))-(s.eye(9)+F)),"second moment on full tensor")

# Nine independent Hermitian test matrices: reconstruct arbitrary Hermitian X by linearity.
Hs=[]
for i in range(3):
    x=s.zeros(3); x[i,i]=1; Hs.append(x)
for i,j in [(0,1),(0,2),(1,2)]:
    x=s.zeros(3); x[i,j]=x[j,i]=1; Hs.append(x)
    y=s.zeros(3); y[i,j]=s.I; y[j,i]=-s.I; Hs.append(y)
check(len(Hs)==9,"nine Hermitian basis elements")
for X in Hs:
    ys=[s.trace(X*p) for p in P]
    recon=sum(((ys[k]-sum(ys)/16)*P[k] for k in range(12)),s.zeros(3))
    check(matzero(recon-X),"Hermitian reconstruction")
    frame=sum((ys[k]*P[k] for k in range(12)),s.zeros(3))
    check(matzero(frame-X-s.trace(X)*s.eye(3)),"frame spectrum identity")

check(any(not zero(s.trace(P[0]*P[j])-s.Rational(1,4)) for j in range(1,12)),"not a SIC")
check(len({tuple(p) for p in P})==12,"all 12 lines distinct")
print("ALL_CHECKS_PASS",checks)
