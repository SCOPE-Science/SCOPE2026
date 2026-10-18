#!/usr/bin/env python3
"""Exact binary arithmetic for all-smooth pencils of plane-filling quartics."""
from collections import Counter
from itertools import product

def mon(d):
    return [(i,j,d-i-j) for i in range(d,-1,-1) for j in range(d-i,-1,-1)]
M4=mon(4); M6=mon(6); M7=mon(7); M10=mon(10)
INDEX4={v:i for i,v in enumerate(M4)}
INDEX10={v:i for i,v in enumerate(M10)}

def times(a,b): return tuple(a[k]+b[k] for k in range(3))

def generate_q4(A):
    # f_A = (Ax) dot (x cross x^(2)).
    # cross components yz^2+y^2z, zx^2+z^2x, xy^2+x^2y.
    cr=[[(0,1,2),(0,2,1)],[(2,0,1),(1,0,2)],[(1,2,0),(2,1,0)]]
    mask=0
    for i in range(3):
        for j in range(3):
            if A[i][j]:
                var=[0,0,0];var[j]=1
                for term in cr[i]:mask ^= 1<<INDEX4[times(var,term)]
    return mask

def matmul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(3))%2 for j in range(3)] for i in range(3)]

def matrix_vector(A,v):return tuple(sum(A[i][j]*v[j] for j in range(3))%2 for i in range(3))
I=[[int(i==j) for j in range(3)] for i in range(3)]

def singular_eigen(A):
    for v in product((0,1),repeat=3):
        if v!=(0,0,0) and matrix_vector(A,v) in (v,(0,0,0)): return True
    return False

# Each matrix modulo scalars produces one of the 256 quartics vanishing on all 7 rational points.
representatives={}
for v in product((0,1),repeat=9):
    A=[list(v[3*i:3*i+3]) for i in range(3)]
    f=generate_q4(A)
    representatives.setdefault(f,[]).append(A)
assert len(representatives)==256
assert set(len(v) for v in representatives.values())=={2}

def mac_rank(f):
    # The degree-10 ideal piece (f,f_x,f_y,f_z)_10 has 28+3*36 columns.
    terms=[]
    for k,e in enumerate(M4):
        if not (f>>k)&1:continue
        terms.append(e)
    polys=[terms]
    for h in range(3):
        dx=[]
        for e in terms:
            if e[h]%2:
                e2=list(e);e2[h]-=1;dx.append(tuple(e2))
        polys.append(dx)
    piv={}
    for ix,poly in enumerate(polys):
        bas=M6 if ix==0 else M7
        for b in bas:
            col=0
            for e in poly:col ^=1<<INDEX10[times(e,b)]
            while col:
                k=col.bit_length()-1
                if k in piv:col^=piv[k]
                else:piv[k]=col;break
            if len(piv)==66:return 66
    return len(piv)

smooth={f for f in representatives if f and mac_rank(f)==66}
assert len(smooth)==24, len(smooth)
for f,reps in representatives.items():
    by_eigen=all(not singular_eigen(A) for A in reps)
    assert by_eigen == (f in smooth), (f,by_eigen)

# In a pencil over F2 the nonzero members are exactly f, g, f+g.
pencils=set()
for f in smooth:
    for g in smooth:
        if f<g and (f^g) in smooth:
            pencils.add(tuple(sorted((f,g,f^g))))
assert len(pencils)==8,(len(pencils),sorted(pencils))
assert set(f for W in pencils for f in W)==smooth
assert all(sum(f in W for W in pencils)==1 for f in smooth)

# Produce the projective GL3(F2) action directly on polynomials.
def pmul(P,Q):
    out={}
    for a,ca in P.items():
        for b,cb in Q.items():
            e=times(a,b);out[e]=out.get(e,0)^(ca&cb)
    return {a:b for a,b in out.items() if b}

def substitution(f,A):
    lin=[]
    for row in A:
        lin.append({tuple(1 if i==j else 0 for i in range(3)):1 for j in range(3) if row[j]})
    ans={}
    for k,e in enumerate(M4):
        if not (f>>k)&1:continue
        term={(0,0,0):1}
        for j in range(3):
            for _ in range(e[j]):term=pmul(term,lin[j])
        for exp in term:ans[exp]=ans.get(exp,0)^1
    return sum(v<<INDEX4[k] for k,v in ans.items())

def det(A):
    return (A[0][0]*(A[1][1]*A[2][2]^A[1][2]*A[2][1])^
            A[0][1]*(A[1][0]*A[2][2]^A[1][2]*A[2][0])^
            A[0][2]*(A[1][0]*A[2][1]^A[1][1]*A[2][0]))%2
G=[]
for v in product((0,1),repeat=9):
    A=[list(v[3*i:3*i+3]) for i in range(3)]
    if det(A):G.append(A)
assert len(G)==168
W0=min(pencils)
orbit={tuple(sorted(substitution(f,A) for f in W0)) for A in G}
assert orbit==pencils
stab=[A for A in G if tuple(sorted(substitution(f,A) for f in W0))==W0]
assert len(stab)==21

# Stabilizer of each of the 3 member curves is order 7, and agrees across the pencil.
curve_stabilizers=[{tuple(z for row in A for z in row) for A in G if substitution(f,A)==f} for f in W0]
assert all(len(T)==7 for T in curve_stabilizers)
assert curve_stabilizers[0]==curve_stabilizers[1]==curve_stabilizers[2]

print('PLANE_FILLING_QUARTIC_FORM_SPACE 256')
print('GEOMETRICALLY_SMOOTH_PLANE_FILLING_QUARTICS',len(smooth))
print('ALL_SMOOTH_PLANE_FILLING_PENCILS',len(pencils))
print('PROJECTIVE_GROUP_ORDER',len(G))
print('PENCIL_ORBIT_SIZE',len(orbit),'PENCIL_STABILIZER',len(stab))
print('EACH_CURVE_STABILIZER',len(curve_stabilizers[0]))
print('REPRESENTATIVE_PENCIL_MASKS',*W0)
print('REPRESENTATIVE_POLYNOMIALS')
for f in W0:
    print(' + '.join(''.join('xyz'[j]+('^'+str(e[j]) if e[j]>1 else '') for j in range(3) if e[j]) for i,e in enumerate(M4) if f>>i&1))
print('ALL_EIGHT_PENCIL_MASKS')
for W in sorted(pencils):print(*W)
print('PASS')
