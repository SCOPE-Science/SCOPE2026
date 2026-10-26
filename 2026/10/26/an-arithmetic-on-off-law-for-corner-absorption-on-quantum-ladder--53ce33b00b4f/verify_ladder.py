"""Independent checks for the corner-trap quantum ladder statement.
Run: python verify_ladder.py (requires numpy and sympy).
"""
from math import pi, sin, sqrt
import numpy as np
import sympy as sp

z=sp.Symbol('z')
checks=0

def test(ok, context):
    global checks
    if not ok: raise AssertionError(context)
    checks+=1

# Exact characteristic-polynomial test, independent of Ramanujan trace proof.
P0,P1=sp.Poly(1,z),sp.Poly(z,z)
for n in range(1,51):
    Pn=P1
    Pplus=sp.Poly(Pn.as_expr().subs(z,z+1),z)
    Pminus=sp.Poly(Pn.as_expr().subs(z,z-1),z)
    g=sp.gcd(Pplus,Pminus).monic()
    target=sp.Poly(z,z) if (n+1)%3==0 else sp.Poly(1,z)
    test(g.as_expr()==target.as_expr(),f'charpoly n={n} gcd {g.as_expr()}')
    P0,P1=P1,sp.Poly(z*P1.as_expr()-P0.as_expr(),z)

# Direct adjacency and its eigenspaces, independent of polynomial gcd.
for n in range(2,22):
    p=n+1
    A=np.zeros((2*n,2*n))
    for x in range(n):
        a,b=2*x,2*x+1
        A[a,b]=A[b,a]=1
        if x+1<n:
            A[a,a+2]=A[a+2,a]=1
            A[b,b+2]=A[b+2,b]=1
    ev, U=np.linalg.eigh(A)
    groups=[]
    for k,e in enumerate(ev):
        if not groups or abs(e-ev[groups[-1][-1]])>1e-8:
            groups.append([k])
        else:
            groups[-1].append(k)
    test(len(groups)==2*n-int(p%3==0),f'eigenlevels n={n}')
    test(max(len(g) for g in groups)==(2 if p%3==0 else 1),f'largest eigenspace n={n}')
    bright=0
    dark=np.zeros((2*n,2*n))
    for g in groups:
        block=U[:,g]
        v=block[0,:]
        test(np.linalg.norm(v)>1e-9,f'vanishing eigenspace corner n={n}, group={g}')
        bright+=1
        dark+=block@block.T-(block@v[:,None]@v[None,:]@block.T)/(v@v)
    test(np.linalg.norm(dark@dark-dark)<3e-8,f'dark projector n={n}')
    test(abs(np.trace(dark)-int(p%3==0))<2e-8,f'dark dimension n={n}')
    for x in range(1,p):
        for y in (1,2):
            idx=2*(x-1)+y-1
            residue=x%6
            target=(3/(2*p) if ((y==1 and residue in (2,4)) or (y==2 and residue in (1,5))) and p%3==0 else 0)
            test(abs(dark[idx,idx]-target)<1e-8,f'dark local n={n} x={x} y={y}')
    if p%3==0:
        phi=np.zeros(2*n)
        for x in range(1,p):
            v1=(sin(pi*x/3)-sin(2*pi*x/3))/sqrt(2*p)
            v2=(-sin(pi*x/3)-sin(2*pi*x/3))/sqrt(2*p)
            phi[2*(x-1):2*x]=[v1,v2]
        test(abs(phi@phi-1)<1e-11,f'normalization n={n}')
        test(np.linalg.norm(A@phi)<1e-10,f'zero dark mode n={n}')
        test(np.linalg.norm(dark-np.outer(phi,phi))<1e-8,f'projector n={n}')
        for gamma in (0.18,1.0,3.7):
            H=A.astype(complex)
            H[0,0]-=0.5j*gamma
            eig=np.linalg.eigvals(H)
            test(sum(abs(e.imag)<1e-8 for e in eig)==1,f'absorption dark n={n}, gamma={gamma}')
    else:
        for gamma in (0.18,1.0,3.7):
            H=A.astype(complex)
            H[0,0]-=0.5j*gamma
            eig=np.linalg.eigvals(H)
            test(max(e.imag for e in eig)<-1e-11,f'absorption all n={n}, gamma={gamma}')
print('ALL_CHECKS_PASSED',checks)
