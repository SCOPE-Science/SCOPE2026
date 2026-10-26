#!/usr/bin/env python3
"""Check exact reduced/full generator agreement and large-star asymptotics."""
import numpy as np

def reduced(m, J, gamma, eta):
    a = gamma * (1 - eta)
    r = np.sqrt(m)
    G = gamma * (m + 1) / 2
    # Real-coordinate state [hub, bright leaf, dark-leaf weight, Re z, Im z].
    M = np.array([
        [-gamma*m, a, a*(m-1), 0, -2*J*r],
        [a, -gamma, 0, 0, 2*J*r],
        [a, 0, -gamma, 0, 0],
        [0, 0, 0, -G, 0],
        [J*r, -J*r, 0, 0, -G],
    ], dtype=float)
    vals, vecs = np.linalg.eig(M)
    k = np.argmax(vals.real)
    assert abs(vals[k].imag) < 1e-8
    v = vecs[:, k].real
    if v[0] < 0:
        v = -v
    v /= v[0]+v[1]+(m-1)*v[2]
    h,s,d,x,y = v
    return vals[k].real, h, 2*abs(x+1j*y)/np.sqrt(m), 2*abs(s-d)/m

def full(m, J, gamma, eta):
    n=m+1
    H=np.zeros((n,n),dtype=complex)
    Qs=[]
    for j in range(1,n):
        H[0,j]=H[j,0]=J
        Q=np.zeros((n,n),dtype=complex);Q[0,j]=1;Qs.append(Q)
        Q=np.zeros((n,n),dtype=complex);Q[j,0]=1;Qs.append(Q)
    def lin(rho):
        z=-1j*(H@rho-rho@H)
        for Q in Qs:
            K=Q.conj().T@Q
            z+=gamma*((1-eta)*Q@rho@Q.conj().T-(K@rho+rho@K)/2)
        return z
    columns=[]
    for j in range(n):
        for k in range(n):
            E=np.zeros((n,n),dtype=complex);E[j,k]=1
            columns.append(lin(E).reshape(-1))
    vals,vecs=np.linalg.eig(np.stack(columns,axis=1))
    k=np.argmax(vals.real)
    assert abs(vals[k].imag)<1e-8
    mat=vecs[:,k].reshape(n,n)
    mat=(mat+mat.conj().T)/2
    if np.trace(mat).real<0:mat=-mat
    mat/=np.trace(mat)
    assert np.linalg.eigvalsh(mat).min()>0
    return vals[k].real, mat[0,0].real, 2*abs(mat[0,1]), 2*abs(mat[1,2])

for m in (2,3,5):
    z1=reduced(m,.7,1.3,.4)
    z2=full(m,.7,1.3,.4)
    assert np.allclose(z1,z2,rtol=1e-7,atol=1e-8), (m,z1,z2)

for J,gamma,eta in ((1,1,.5),(.2,1,.5),(1,2,.8)):
    a=4*J*J/(gamma*gamma*(1-eta)**2)
    goal=np.array((-gamma*eta*(2-eta),1-eta,4*J*eta/(gamma*(1+a)),2*a*eta/(1+a)))
    m=1000
    lam,h,ch,cl=reduced(m,J,gamma,eta)
    got=np.array((lam,m*h,m*m*ch,m*m*cl))
    assert np.all(np.abs(got-goal)<.07), (got,goal)
print('Full-versus-reduced checks (m=2,3,5) and three m=1000 asymptotic checks passed.')
