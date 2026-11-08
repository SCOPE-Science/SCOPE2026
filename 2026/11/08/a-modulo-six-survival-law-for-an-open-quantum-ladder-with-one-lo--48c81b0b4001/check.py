#!/usr/bin/env python3
"""Independent exact-polynomial and matrix checks for lossy open ladders.
Requires SymPy and NumPy; does not import research claims or previous outputs.
"""
import math
import numpy as np
import sympy as sp

x=sp.symbols('x')

def adjacency_ladder(n):
    a=np.zeros((2*n,2*n),dtype=float)
    for r in range(2):
        for j in range(n-1):
            u=r*n+j;v=u+1;a[u,v]=a[v,u]=1.
    for j in range(n):
        a[j,j+n]=a[j+n,j]=1.
    return a

def dark_weight(n):
    a=adjacency_ladder(n)
    eig,vec=np.linalg.eigh(a)
    ans=0.
    seen=[]
    for l in eig:
        if any(abs(l-j)<1e-8 for j in seen):continue
        seen.append(l)
        basis=vec[:,np.abs(eig-l)<1e-8]
        s=basis[0,:]
        t=basis[2*n-1,:]
        # Projection of source onto the subspace orthogonal to the sink.
        ans+=float(np.vdot(t,t)-abs(np.vdot(s,t))**2/np.vdot(s,s))
    return ans


def cheb_poly(n):
    # Monic path characteristic p_0=1, p_1=x, p_n=x p_{n-1}-p_{n-2}.
    p,q=sp.Poly(1,x),sp.Poly(x,x)
    for _ in range(2,n+1):p,q=q,sp.Poly(x,x)*q-p
    return q if n>=1 else p

num=0
for n in range(2,61):
    p=cheb_poly(n)
    g=sp.gcd(p,sp.Poly(p.as_expr().subs(x,x+2),x))
    # Common roots correspond to two path energies differing by 2.
    expected=sp.Poly(x+1,x) if (n+1)%3==0 else sp.Poly(1,x)
    assert sp.expand(sp.monic(g).as_expr()-expected.as_expr())==0,(n,g,expected)
    num+=1
for n in range(2,31):
    got=dark_weight(n)
    expected=3/(2*(n+1)) if (n+1)%6==0 else 0.
    assert abs(got-expected)<1e-9,(n,got,expected)
    num+=1

# Check long-time finite-loss dynamics independently of the eigenprojector method.
from scipy.linalg import expm
for n in (4,5,6,8,11):
    a=adjacency_ladder(n).astype(complex)
    a[0,0]-=0.7j
    initial=np.zeros(2*n,dtype=complex);initial[-1]=1.
    # For moderate size the slow modes may decay slowly; test at increasing times.
    times=[1000,2000,4000]
    probs=[float(np.linalg.norm(expm(-1j*t*a)@initial)**2) for t in times]
    target=3/(2*(n+1)) if (n+1)%6==0 else 0.
    assert probs[-1]+1e-7>=target,(n,probs,target)
    assert probs[-1]<=probs[0]+1e-6,(n,probs)
    num+=1
print('PASS',num,'independent polynomial, projection, evolution checks')
for n in (2,3,4,5,6,8,11,17,23):
    print('n',n,'projection',f'{dark_weight(n):.12g}', 'exact-prediction',f'{(3/(2*(n+1)) if (n+1)%6==0 else 0):.12g}')
