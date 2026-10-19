#!/usr/bin/env python3
"""Reproducibility of the compensated decorated Ising ladder four-point theorem.
Requires mpmath and sympy; all tests derive from the Hamiltonian without imported data.
"""
import itertools
import mpmath as mp
import sympy as sp
mp.mp.dps=60

def predicted_density(K,j):
    rho=mp.tanh(K); u=mp.tanh(2*j)
    return -2 - 8*u*u*rho/(1-rho) - 3*u**4*rho**2*(3+2*rho-3*rho**2)/((1-rho)**3*(1+rho))

def exact_periodic_density(N,K,j):
    kr=-mp.log(mp.cosh(2*j))/2
    spins=list(itertools.product([-1,1],repeat=2))
    mats=[]
    for k in range(5):
        R=mp.matrix(4,4)
        for x,(a,b) in enumerate(spins):
            for y,(c,d) in enumerate(spins):
                F=mp.exp(K*(a*c+b*d)+kr*a*b)
                v=2*(mp.cosh(j*(a+b)) if k%2==0 else mp.sinh(j*(a+b)))/mp.factorial(k)
                R[x,y]=F*v
        mats.append(R)
    # Taylor coefficients of T(h)^N through h^4
    T=[mp.eye(4)]+[mp.matrix(4,4) for _ in range(4)]
    for _ in range(N):
        B=[mp.matrix(4,4) for _ in range(5)]
        for k in range(5):
            for t in range(k+1):
                B[k]+=T[t]*mats[k-t]
        T=B
    z=[sum(T[i][j,j] for j in range(4)) for i in range(5)]
    assert abs(z[1]/z[0])<mp.mpf('1e-45')
    assert abs(z[3]/z[0])<mp.mpf('1e-45')
    k4=(24*z[4]/z[0]-3*(2*z[2]/z[0])**2)/N
    return k4

# Independent base-chain enumeration of 4 distinct apex observations.
def four_distinct_exact(d1,d2,d3,K,j):
    r=mp.tanh(K);u=mp.tanh(2*j)
    p=[0,d1,d1+d2,d1+d2+d3]
    def even_moment(subset):
        if len(subset)%2: return mp.mpf('0')
        return r**sum(p[subset[t+1]]-p[subset[t]] for t in range(0,len(subset),2))
    M=mp.mpf('0')
    for bit in itertools.product([0,1],repeat=4):
        ia=[i for i,b in enumerate(bit) if b==0]
        ib=[i for i,b in enumerate(bit) if b==1]
        M+=even_moment(ia)*even_moment(ib)
    M*=u**4/16
    C=lambda i,k: u*u*r**(p[k]-p[i])/2
    return M-C(0,1)*C(2,3)-C(0,2)*C(1,3)-C(0,3)*C(1,2)

num=0
for K in [mp.mpf('0.17'),mp.mpf('0.36'),mp.mpf('0.55')]:
 for j in [mp.mpf('0.45'),mp.mpf('1.1')]:
  for N in [30,60]:
   exact=exact_periodic_density(N,K,j)
   pred=predicted_density(K,j)
   err=abs(exact-pred)
   assert err<mp.mpf('0.00002'),(K,j,N,err,exact,pred)
   num+=1
  for d1,d2,d3 in [(1,1,1),(1,2,4),(3,1,5),(2,4,7)]:
   val=four_distinct_exact(d1,d2,d3,K,j)
   r=mp.tanh(K);u=mp.tanh(2*j)
   tgt=-u**4*r**(d1+2*d2+d3)/4
   assert abs(val-tgt)<mp.mpf('1e-50'),(val,tgt)
   num+=1
# Symbolic simplification of distinct-site sum and full κ4 density.
r,u=sp.symbols('r u',positive=True)
conv=sp.simplify((r/(1-r))**2*(r**2/(1-r**2)))
assert sp.simplify(conv-r**4/((1-r)**2*(1-r**2)))==0
coef=3*r**2/(1-r**2)-12*r**2/(1-r)**2-6*r**4/((1-r)**2*(1-r**2))
assert sp.factor(coef + 3*r**2*(3+2*r-3*r**2)/((1-r)**3*(1+r)))==0
num+=2
print(f'PASS {num} symbolic and independent finite-periodic transfer comparisons')
print('Example susceptibility: ',mp.nstr(predicted_density(mp.mpf('0.36'),mp.mpf('1.1')),25))
