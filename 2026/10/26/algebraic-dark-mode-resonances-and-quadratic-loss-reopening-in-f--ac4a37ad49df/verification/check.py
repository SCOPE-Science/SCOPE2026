"""Numerical cross-checks for finite SSH single-site dark-mode resonances.

Analytic theorems and proofs are in RESULT.md; finite floating-point checks are
not completeness certificates for arbitrary chain lengths.
"""
import math
import numpy as np
from scipy.linalg import eigh_tridiagonal, eigvals

checks = 0

def check(condition, context):
    global checks
    if not condition:
        raise AssertionError(context)
    checks += 1

def tridiagonal(N,r):
    return np.array([1. if i%2==0 else r for i in range(2*N-1)])

def site(A_or_B,m):
    return 2*(m-1)+(0 if A_or_B=='A' else 1)

def resonance_list(N,m):
    L=N+1-m
    ans=[]
    for j in range(1,L):
        k=math.pi*j/L
        den=math.sin((m-1)*k)
        if abs(den)<1e-10:
            continue
        r=-math.sin(m*k)/den
        if r>1e-9:
            ans.append((r,j,k))
    return ans

def clean_eigs(N,r):
    return eigh_tridiagonal(np.zeros(2*N),tridiagonal(N,r))

def numerical_dark_count(N,m,r):
    _,U=clean_eigs(N,r)
    return sum(abs(x)<2e-8 for x in U[site('A',m),:])

# Check every nonzero resonance from the explicit sine formula in a grid.
for N in range(2,24):
    for m in range(1,N+1):
        rr=resonance_list(N,m)
        for r,j,k in rr:
            E=math.sqrt(1+r*r+2*r*math.cos(k))
            a=np.array([math.sin((N-z)*k) for z in range(N)])
            b=np.array([(a[z]+r*(a[z+1] if z+1<N else 0))/E for z in range(N)])
            v=np.empty(2*N)
            v[0::2]=a;v[1::2]=b
            H=np.diag(tridiagonal(N,r),1)+np.diag(tridiagonal(N,r),-1)
            check(np.linalg.norm(H@v-E*v)<1e-7,('eigenvector',N,m,r,j))
            check(abs(a[m-1])<1e-8,('node',N,m,r,j))
            check(abs(np.dot(a,a)-np.dot(b,b))<1e-7,('balanced',N,m,r,j))
            check(np.min(abs(clean_eigs(N,r)[0]-E))<1e-8,('energy',N,m,r,j))
            check(numerical_dark_count(N,m,r)==2*sum(abs(t[0]-r)<1e-8 for t in rr),
                  ('multiplicity',N,m,r,j))
        # A generic algebraic-looking ratio checks absence away from discrete set.
        r=0.73+0.001*m/(N+1)
        if all(abs(t[0]-r)>1e-6 for t in rr):
            check(numerical_dark_count(N,m,r)==0,('generic',N,m))
        check(numerical_dark_count(N,m,1.)==math.gcd(2*m-1,2*N+1)-1,
              ('uniform gcd',N,m))
        # Spatial reflection maps B_m to A_{N+1-m}.
        r=0.73
        _,U=clean_eigs(N,r)
        _,V=clean_eigs(N,r)
        check(np.max(abs(U[site('B',m),:]**2-V[site('A',N+1-m),:]**2))<2e-8,
              ('reflection',N,m))

# Nonuniform multiplicity jump and exact no-loss modes at a finite Lindblad rate.
N=14;m=3;r0=math.sqrt(2.);s=site('A',m)
rr=resonance_list(N,m)
js=[j for r,j,k in rr if abs(r-r0)<1e-10]
check(js==[5,11],('coexistence roots',js))
E,U=clean_eigs(N,r0)
inds=[j for j in range(2*N) if abs(U[s,j])<1e-8]
check(len(inds)==4,('four dark orbitals',inds))
H=np.diag(tridiagonal(N,r0),1)+np.diag(tridiagonal(N,r0),-1)
P=np.zeros((2*N,2*N)); P[s,s]=1.
for gamma in [0.2,0.6,2.0]:
    lam=eigvals(H-0.5j*gamma*P)
    check(sum(abs(z.imag)<2e-8 for z in lam)==4,('loss independent',gamma))

# Check the exact clean-weight quadratic coefficient for each resonant branch.
for N,m in [(4,2),(7,3),(10,4),(14,3),(15,4),(18,6)]:
    L=N+1-m
    for r0,j,k0 in resonance_list(N,m):
        Fk=(N+1)*math.cos((N+1)*k0)+r0*N*math.cos(N*k0)
        if abs(Fk)<1e-10:continue
        bp=-math.sin(N*k0)/Fk
        C=L*L*bp*bp/(2*sum(math.sin(h*k0)**2 for h in range(1,N+1)))
        E0=math.sqrt(1+r0*r0+2*r0*math.cos(k0))
        check(C>0,('positive quadratic',N,m,j))
        for delta in [1e-3, 5e-4]:
            E,U=clean_eigs(N,r0+delta)
            ix=np.argmin(abs(E-E0))
            slope=U[site('A',m),ix]**2/delta**2
            check(abs(slope/C-1)<0.09,('quadratic rate',N,m,j,delta,C,slope))

print('SSH_DARK_MODE_CHECKS_PASSED',checks)
