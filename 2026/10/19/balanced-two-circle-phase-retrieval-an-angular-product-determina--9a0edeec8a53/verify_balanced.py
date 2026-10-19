#!/usr/bin/env python3
"""Direct numerical and symbolic checks of the stated two-circle sampling identities."""
import math
import numpy as np
import sympy as sp

rng=np.random.default_rng(97131)

def Mmatrix(d, theta, phi, r):
    rows=[]
    for t in theta:
        rows.append([1.0]+[v for k in range(1,d) for v in (math.cos(k*t),math.sin(k*t))]+[0.0]*(2*d-1)+[math.cos(d*t),math.sin(d*t)])
    for t in phi:
        rows.append([0.0]*(2*d-1)+[1.0]+[v for k in range(1,d) for v in (math.cos(k*t),math.sin(k*t))]+[r**d*math.cos(d*t),r**d*math.sin(d*t)])
    return np.array(rows,dtype=float)

def predicted_det(d,theta,phi,r):
    z=np.exp(1j*theta);w=np.exp(1j*phi)
    vd1=np.prod([abs(z[j]-z[i]) for i in range(2*d) for j in range(i+1,2*d)])
    vd2=np.prod([abs(w[j]-w[i]) for i in range(2*d) for j in range(i+1,2*d)])
    return r**d*2.0**(1-2*d)*vd1*vd2*abs(np.prod(z)-np.prod(w))

def hermitian_basis(n):
    basis=[]
    for i in range(n):
        h=np.zeros((n,n),dtype=complex);h[i,i]=1;basis.append(h)
    for i in range(n):
        for j in range(i+1,n):
            h=np.zeros((n,n),dtype=complex);h[i,j]=h[j,i]=1;basis.append(h)
            h=np.zeros((n,n),dtype=complex);h[i,j]=1j;h[j,i]=-1j;basis.append(h)
    return basis

def lifting(d,theta,phi,r):
    z=np.r_[np.exp(1j*theta),r*np.exp(1j*phi)]
    V=np.stack([zi**np.arange(d+1) for zi in z])
    return np.stack([np.real(np.einsum('ki,ij,kj->k',V,h,np.conj(V))) for h in hermitian_basis(d+1)],axis=1)

checks=0;worst_rel=0.0
for d in range(1,6):
    for j in range(16):
        angles=(np.arange(2*d)+0.06*rng.normal(size=2*d))*2*math.pi/(2*d)
        other=(np.arange(2*d)+0.055*rng.normal(size=2*d))*2*math.pi/(2*d)+(.1+.2*rng.random())/(2*d)
        r=.22+.6*rng.random()
        M=Mmatrix(d,angles,other,r)
        lhs=abs(np.linalg.det(M));rhs=predicted_det(d,angles,other,r)
        assert rhs>1.e-15,(d,rhs)
        error=abs(lhs-rhs)/rhs
        assert error<4.e-8,(d,j,error)
        worst_rel=max(worst_rel,error);checks+=1

for d in range(1,6):
    theta=np.arange(2*d)*2*math.pi/(2*d)
    for resonant in (False,True):
        phi=theta+(math.pi/(2*d) if not resonant else 2*math.pi/(2*d))
        M=Mmatrix(d,theta,phi,.6)
        L=lifting(d,theta,phi,.6)
        rankM=np.linalg.matrix_rank(M,tol=1.e-8)
        rankL=np.linalg.matrix_rank(L,tol=1.e-8)
        expected=4*d-int(resonant)
        assert rankM==expected and rankL==expected,(d,resonant,rankM,rankL,expected)
        checks+=2

# Resonance does not require identical or regularly spaced angular sets.
for d in range(2,6):
    t=np.arange(2*d)*math.pi/d
    small=np.linspace(-0.12,0.12,2*d)*math.pi/d
    phi=t+small  # the offsets sum to zero; products of all nodes agree
    mm=Mmatrix(d,t,phi,.65)
    LL=lifting(d,t,phi,.65)
    assert np.linalg.matrix_rank(mm,tol=1.e-8)==4*d-1
    assert np.linalg.matrix_rank(LL,tol=1.e-8)==4*d-1
    checks+=2

# Exact rational resonance of a square design and diagonal full-data kernel.
r=sp.Rational(1,2)
z1=[sp.Integer(1),sp.I,sp.Integer(-1),-sp.I]
# Encodes the Hermitian matrix via 9 real coordinates, including i offdiagonal basis.
def s_matrix(points):
    rows=[]
    for z in points:
        a=sp.Matrix([1,z,z*z]);
        basis=[]
        for i in range(3):
            H=sp.zeros(3);H[i,i]=1;basis.append(H)
        for i in range(3):
            for j in range(i+1,3):
                H=sp.zeros(3);H[i,j]=H[j,i]=1;basis.append(H)
                H=sp.zeros(3);H[i,j]=sp.I;H[j,i]=-sp.I;basis.append(H)
        rows.append([sp.simplify((a.T*H*a.conjugate())[0]) for H in basis])
    return sp.Matrix(rows)
Lsame=s_matrix(z1+[r*z for z in z1]);assert Lsame.rank()==7
# Unequal angular products: rotate the second square by 45 degrees.
rot=(1+sp.I)/sp.sqrt(2)
Lshift=s_matrix(z1+[r*rot*z for z in z1]);assert Lshift.rank()==8
# Exact determinants for the optimal and resonant two-square designs.
def msym(outer,inner,rad):
    d=2
    rows=[]
    def basis(u):
        return [sp.Integer(1)]+[v for k in range(1,d) for v in ((u**k+u**(-k))/2,(u**k-u**(-k))/(2*sp.I))]
    for u in outer:
        rows.append(basis(u)+[sp.Integer(0)]*(2*d-1)+[(u**d+u**(-d))/2,(u**d-u**(-d))/(2*sp.I)])
    for v in inner:
        rows.append([sp.Integer(0)]*(2*d-1)+basis(v)+[rad**d*(v**d+v**(-d))/2,rad**d*(v**d-v**(-d))/(2*sp.I)])
    return sp.Matrix(rows)
assert sp.simplify(msym(z1,[rot*z for z in z1],r).det()**2-256)==0
assert msym(z1,z1,r).det()==0
checks+=2

# Explicit non-phase-equivalent ambiguity under the matched-angle resonance.
for z in z1+[r*z for z in z1]:
    P=1+sp.I*z*z;Q=1-sp.I*z*z
    assert sp.simplify(P*sp.conjugate(P)-Q*sp.conjugate(Q))==0
checks+=3

print('PASS')
print('determinant_checks=80, rank_checks=28, exact_symbolic_checks=5')
print('total_checks=',checks)
print('max_relative_determinant_error=',format(worst_rel,'.4e'))
print('tested_degrees=1..5, radii randomized in (0.22,0.82)')
print('resonant_d2_rank=7, nonresonant_d2_rank=8')
