"""Independent finite checks of exact book-graph Lipschitz-body inertia identities."""
from fractions import Fraction as F
from itertools import combinations
import numpy as np
from scipy.spatial import ConvexHull
from scipy.integrate import quad

def D(k):
    return F(2**(k+1)-1,k+1)

def exact(m):
    T=(4*D(m)-4*D(m+1)+D(m+2))/D(m)
    B=D(m+2)/(12*D(m))
    return T,B

def verts(m):
    d=m+1
    rows=[]; rhs=[]
    for side in (-1,1):
        x=np.zeros(d);x[0]=side;rows.append(x);rhs.append(1.)
    for j in range(m):
        for side in (-1,1):
            x=np.zeros(d);x[j+1]=side;rows.append(x);rhs.append(1.)
            x=np.zeros(d);x[j+1]=side;x[0]=-side;rows.append(x);rhs.append(1.)
    A=np.array(rows); b=np.array(rhs); out={}
    for ix in combinations(range(len(b)),d):
        mat=A[list(ix)];bb=b[list(ix)]
        if abs(np.linalg.det(mat))<1e-9:continue
        xx=np.linalg.solve(mat,bb)
        if np.max(A@xx-b)<1e-8:out[tuple(np.round(xx,9))]=xx
    return np.array(list(out.values()))

for m in range(2,9):
    T,B=exact(m)
    t2=quad(lambda t:t*t*(2-t)**m,0,1,epsabs=1e-12)[0] / quad(lambda t:(2-t)**m,0,1,epsabs=1e-12)[0]
    b2=quad(lambda t:((2-t)**2/12)*(2-t)**m,0,1,epsabs=1e-12)[0]/quad(lambda t:(2-t)**m,0,1,epsabs=1e-12)[0]
    assert abs(t2-float(T))<1e-10 and abs(b2-float(B))<1e-10
    hub=T/2; leaf=B; block=2*B/(m+2)
    assert leaf>block
    if m==2: assert hub>block and hub<leaf
    elif m==3: assert hub==block
    else: assert hub<block
for m in (2,3):
    v=verts(m)
    volume=ConvexHull(v).volume
    assert abs(volume-2*float(D(m)))<1e-9, (m,volume, 2*float(D(m)))
# Algebraic sign identity for m=2..100, accompanied by an all-integer proof in RESULT.md.
for m in range(2,101):
    T,B=exact(m)
    left=(m+2)*(4*D(m)-4*D(m+1)+D(m+2))-D(m+2)/3
    right=F(-(2**(m+1)*(4*m-20)+3*m*m+20*m+41),3*(m+1)*(m+3))
    assert left==right
print('VERIFY_OK quadrature=14 volume_hulls=2 exact_sign_identities=99 mode_crossing=2,3,4+')
