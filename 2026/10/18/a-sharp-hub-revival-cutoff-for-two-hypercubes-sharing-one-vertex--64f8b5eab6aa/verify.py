"""Independent finite-graph and exact-polynomial checks for a junction quantum walk."""
from math import comb, sqrt, pi
import numpy as np
import sympy as sp

x,y=sp.symbols('x y')


def radial(n):
    B=np.zeros((n+1,n+1),float)
    for j in range(n):
        z=sqrt(2*n) if j==0 else sqrt((j+1)*(n-j))
        B[j,j+1]=B[j+1,j]=z
    return B

def exact_poly(n):
    pm,p=sp.Integer(1),x
    for j in range(n):
        b2=2*n if j==0 else (j+1)*(n-j)
        pm,p=p,sp.expand(x*p-b2*pm)
    expr=sp.Poly(p,x)
    coeff=[sp.expand(expr.coeff_monomial(x**(2*k+(n+1)%2))) for k in range((n+1)//2+1)]
    return sp.Poly(sum(z*y**k for k,z in enumerate(coeff)),y),p

def graph(n):
    verts=[('H',0)]+[(a,z) for a in (0,1) for z in range(1,2**n)]
    lookup={v:i for i,v in enumerate(verts)}
    H=np.zeros((len(verts),len(verts)))
    for a in (0,1):
        for z in range(2**n):
            v=('H',0) if z==0 else (a,z)
            for j in range(n):
                w=z^(1<<j)
                wv=('H',0) if w==0 else (a,w)
                H[lookup[v],lookup[wv]]=1.
    U=np.zeros((len(verts),n+1))
    U[0,0]=1.
    for a in (0,1):
        for z in range(1,2**n):
            j=z.bit_count()
            U[lookup[a,z],j]=1/sqrt(2*comb(n,j))
    return H,U

allcheck=0
for n in range(1,16):
    P,poly=exact_poly(n)
    j=radial(n)
    eig=np.linalg.eigvalsh(j)
    pos=eig[eig>1e-8]
    fs=P.all_coeffs()
    if n%2==0:
        assert all(int(c)%2==0 for c in fs[1:]), (n,fs)
        if n>=4:
            assert 4 <pos[0]**2 <6, (n,pos[0]**2)
    elif n>=3:
        assert 1<pos[0]**2<2, (n,pos[0]**2)
    assert max(abs(complex(P.eval(float(z*z)))) for z in pos)<1e-3*(1+abs(float(fs[-1])))
    allcheck+=1

for n in range(1,7):
    H,U=graph(n)
    J=radial(n)
    assert np.max(np.abs(U.T@U-np.eye(n+1)))<1e-12
    assert np.max(np.abs(H@U-U@J))<1e-12
    assert np.max(np.abs(np.linalg.matrix_power(H,n)@U - U@np.linalg.matrix_power(J,n)))<1e-8
    allcheck+=1
for n,t in [(1,pi/sqrt(2)),(2,2*pi/sqrt(6))]:
    J=radial(n); vals,vecs=np.linalg.eigh(J)
    amp=(vecs[0,:]**2*np.exp(-1j*t*vals)).sum()
    assert abs(abs(amp)-1)<1e-12,(n,amp)
    allcheck+=1
print(f'PASS: {allcheck} checks (15 exact recurrences/parity/interval tests, 6 independently constructed full graph reductions, 2 exact return times).')
for n in range(1,10):
    P,pol=exact_poly(n)
    pos=np.linalg.eigvalsh(radial(n))
    pos=pos[pos>1e-8]
    print(n,'poly',str(P.as_expr()),'min-square',float(pos[0]**2))
