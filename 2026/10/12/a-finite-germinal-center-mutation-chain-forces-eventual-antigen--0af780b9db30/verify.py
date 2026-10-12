#!/usr/bin/env python3
import sympy as sp

alpha,sigma,G,H,d,kappa = sp.symbols("alpha sigma G H d kappa", positive=True)

def verify_chain(n):
    B = sp.symbols("B0:"+str(n+1), positive=True)
    P = sp.symbols("P", nonnegative=True)

    rhs = [None]*(n+1)
    rhs[0] = -d*B[0]-sigma*B[0]*H
    if n == 1:
        rhs[1] = alpha*sigma*B[0]*H-(d+kappa)*B[1]
    else:
        rhs[1] = alpha*sigma*B[0]*H-sigma*B[1]*G-d*B[1]
        for i in range(2,n):
            rhs[i] = alpha*sigma*B[i-1]*G-sigma*B[i]*G-d*B[i]
        rhs[n] = alpha*sigma*B[n-1]*G-(d+kappa)*B[n]

    Pdot = kappa*B[n]
    Qdot = rhs[0]
    for i in range(1,n+1):
        Qdot += alpha**(-i)*rhs[i]
    Qdot += alpha**(-n)*Pdot

    target = -d*B[0]
    for i in range(1,n+1):
        target -= d*alpha**(-i)*B[i]

    assert sp.simplify(Qdot-target) == 0

for n in (1,2,3,5,8):
    verify_chain(n)

sN,dN,alphaN,V,N,dH,gamma,B0,dG,eta,sumB = sp.symbols(
    "sN dN alphaN V N dH gamma B0 dG eta sumB", positive=True
)
Np = sN-dN*N-alphaN*V*N
Hp = alphaN*V*N-dH*H-gamma*H*B0
Gp = gamma*H*B0-dG*G-eta*G*sumB
Tdot = sp.expand(Np+Hp+Gp)
target_T = sN-dN*N-dH*H-dG*G-eta*G*sumB
assert sp.simplify(Tdot-target_T) == 0

print("VERIFY_OK")
print("weighted_chain_cancellation lengths 1,2,3,5,8")
print("T_identity", sp.simplify(Tdot-target_T))
