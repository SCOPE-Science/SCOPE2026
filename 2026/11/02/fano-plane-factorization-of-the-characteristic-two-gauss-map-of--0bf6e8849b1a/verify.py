"""Exact polynomial checks for the characteristic-two Cayley duality factorization.
Run with Python 3 and SymPy (no external data or external process)."""
from itertools import combinations, product
from sympy import symbols, Poly, diff, expand, factor, prod

u,v,w,t=symbols('u v w t')
x=[t+u,t+v,t+w,t]
F=sum(prod(x[j] for j in range(4) if j!=i) for i in range(4))
T=t*t*(u+v+w)+u*v*w

def zero2(poly,*vars):
    return Poly(expand(poly),*vars,modulus=2).is_zero

assert zero2(F-T,u,v,w,t)
assert zero2(diff(F,t),u,v,w,t)
L=u+v+w
P=[v*w*(v+w),u*w*(u+w),u*v*(u+v)]
partials=[diff(T,q) for q in (u,v,w)]
for q,p in zip(partials,P):
    assert zero2(L*q-p-T,u,v,w,t)
print('CUBIC_AND_GAUSS_OK: t^2(u+v+w)+uvw; Gauss factors through projection')

# All rational points of P^2(F2), and the complete cubics passing through them.
pts=sorted({tuple(z) for z in product((0,1),repeat=3) if z!=(0,0,0)})
assert len(pts)==7
assert all(all(int(f.subs({u:a,v:b,w:c}))%2==0 for f in P) for a,b,c in pts)
monoms=[u**i*v**j*w**(3-i-j) for i in range(4) for j in range(4-i)]
M=[[int(m.subs({u:a,v:b,w:c}))%2 for m in monoms] for a,b,c in pts]
def rank2(mat):
    A=[row[:] for row in mat];nr=len(A);nc=len(A[0]);r=0
    for col in range(nc):
        pivot=next((i for i in range(r,nr) if A[i][col]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        for i in range(nr):
            if i!=r and A[i][col]: A[i]=[a^b for a,b in zip(A[i],A[r])]
        r+=1
        if r==nr:break
    return r
assert rank2(M)==7
# Smooth simple base points: at every point some pair of cubic linear parts spans cotangent.
for point in pts:
    idx=point.index(1)
    coords=(u,v,w)
    subs={coords[idx]:1}
    local=[q for j,q in enumerate(coords) if j!=idx]
    f=[expand(p.subs(subs)) for p in P]
    A=[[int(diff(z,q).subs({local[0]:point[coords.index(local[0])],local[1]:point[coords.index(local[1])]}))%2 for q in local] for z in f]
    assert rank2(A)==2,(point,A)
print('FANO_BASE_OK: exactly seven simple F2 points; full net of cubics has dimension three')

# Inseparability of degree-two planar factor (Jacobian wedge is identically zero).
a,b=symbols('a b')
pp=[expand(z.subs({u:1,v:a,w:b})) for z in P]
A,B,C=pp
N=expand((diff(B,a)*A-B*diff(A,a))*(diff(C,b)*A-C*diff(A,b))
         -(diff(B,b)*A-B*diff(A,b))*(diff(C,a)*A-C*diff(A,a)))
assert zero2(N,a,b)
print('INSEPARABILITY_OK: planar map has vanishing Jacobian wedge')

# Classical Steiner dual equation and its characteristic-two quadruple plane limit.
r,s,q,h=symbols('r s q h')
U=[r,s,q,h]
G=expand((sum(z*z for z in U)-2*sum(U[i]*U[j] for i,j in combinations(range(4),2)))**2-64*prod(U))
assert zero2(G-(r+s+q+h)**4,r,s,q,h)
assert expand(G.subs({r:u*u,s:v*v,q:w*w,h:(-u-v-w)**2}))==0
print('DUAL_SPECIALIZATION_OK: classical Steiner quartic reduces to fourth power of dual plane')
print('VERIFY_OK')
