#!/usr/bin/env python3
"""Exact certificate for a tangent-filling smooth plane cubic over F_7.

Only Python's standard library is used. All projective points and lines are
canonicalized; the polynomial-identity test proves geometric smoothness
without passing to a finite collection of field extensions.
"""
from collections import Counter

Q = 7

def F(x, y, z):
    return (x**3 + x*y*z + y**3 + y*z*z - z**3) % Q

def grad(x, y, z):
    return ((3*x*x+y*z) % Q,
            (x*z+3*y*y+z*z) % Q,
            (x*y+2*y*z-3*z*z) % Q)

def canon(a):
    assert any(v % Q for v in a)
    t = next(v % Q for v in a if v % Q)
    s = pow(t, -1, Q)
    return tuple((v*s) % Q for v in a)

def dot(a, b):
    return sum(x*y for x, y in zip(a, b)) % Q

def mul(A, B):
    C = [0]*(len(A)+len(B)-1)
    for i,a in enumerate(A):
        for j,b in enumerate(B):
            C[i+j] = (C[i+j] + a*b) % Q
    return C

def verify_smoothness_identity():
    # The all-characteristic-zero case X=0 is excluded directly by
    # F_X=YZ and F=Y^3+YZ^2-Z^3 on X=0.
    # On X=1, F_X=0 implies YZ=4, so Y!=0 and Z=4/Y.
    # F_Y and F_Z then imply A(Y)=B(Y)=0, respectively.
    A = [2,4,0,0,3]     # 3Y^4+4Y+2
    B = [1,0,1,1]       # Y^3+Y^2+1
    S = [3,1,-2]        # -2Y^2+Y+3
    T = [2,0,-2,-1]     # -Y^3-2Y^2+2
    U = mul(S,A)
    V = mul(T,B)
    E = [(u+v)%Q for u,v in zip(U,V)]
    assert E == [1,0,0,0,0,0,0], E
    return E

def verify():
    identity = verify_smoothness_identity()
    P = [(1,y,z) for y in range(Q) for z in range(Q)]
    P += [(0,1,z) for z in range(Q)] + [(0,0,1)]
    assert len(P) == Q*Q+Q+1 == 57 and len(set(P)) == len(P)
    assert all(canon(p)==p for p in P)
    roots = [p for p in P if F(*p)==0]
    expected_roots = [
       (1,0,1),(1,0,2),(1,0,4),(1,1,2),
       (1,1,4),(1,2,5),(1,3,0),(1,3,5),
       (1,5,0),(1,6,0),(1,6,2),(1,6,4)]
    assert roots == expected_roots, roots
    T = [canon(grad(*r)) for r in roots]
    expected_T = [
      (1,3,6),(1,2,3),(1,2,5),(1,6,0),
      (0,1,5),(1,0,4),(1,2,1),(1,2,0),
      (1,4,4),(1,1,2),(1,2,4),(1,5,1)]
    assert T == expected_T, T
    assert len(set(T)) == 12 and all(dot(t,r)==0 for t,r in zip(T,roots))
    line_size = [sum(dot(t,p)==0 for p in P) for t in T]
    assert line_size == [8]*12
    incidences = [sum(dot(t,p)==0 for t in T) for p in P]
    hist = Counter(incidences)
    assert hist == {1:36, 2:9, 3:9, 5:3}, hist
    assert sum(k*v for k,v in hist.items()) == 12*8
    assert min(incidences) == 1 and max(incidences)==5
    centers = [p for p,n in zip(P,incidences) if n==5]
    assert centers == [(1,1,4),(1,3,0),(1,3,5)]
    det = lambda a,b,c: (a[0]*(b[1]*c[2]-b[2]*c[1]) - a[1]*(b[0]*c[2]-b[2]*c[0]) + a[2]*(b[0]*c[1]-b[1]*c[0]))%Q
    assert det(*centers)==3
    pencils = [set(i for i,t in enumerate(T) if dot(t,c)==0) for c in centers]
    assert all(len(a)==5 for a in pencils)
    assert len(set.union(*pencils)) == 12
    assert len(pencils[0]&pencils[1]) == len(pencils[0]&pencils[2]) == len(pencils[1]&pencils[2]) == 1
    print('SMOOTHNESS_IDENTITY_OK',identity)
    print('RATIONAL_CUBIC_POINTS',len(roots))
    print('TANGENTS',len(T), 'POINTS_IN_PLANE',len(P))
    print('INCIDENCE_HISTOGRAM',dict(sorted(hist.items())))
    print('FIVE_FOLD_PENCIL_CENTERS',centers)
    print('DUAL_BLOCKING_SHARP',len(T),'NONTRIVIAL_MAX_COLLINEAR',max(incidences))
    print('VERIFY_OK')

if __name__ == '__main__':
    verify()
