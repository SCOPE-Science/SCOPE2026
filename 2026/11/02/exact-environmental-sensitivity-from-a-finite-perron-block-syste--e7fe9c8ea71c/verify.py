#!/usr/bin/env python3
"""Exact finite-dimensional checks for common-reproductive-value matrix products.

Requires only Python 3 standard library. Run: python verify.py
This script checks finite identities and examples; the mathematical theorem
for arbitrary dimensions and times is proved separately.
"""
from fractions import Fraction as F
from itertools import product
import random
import math

R = random.Random(20261028)

def Q(a,b=1): return F(a,b)
def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))), F(0)) for j in range(len(B[0]))] for i in range(len(A))]
def mv(A,v): return [sum((z*w for z,w in zip(row,v)), F(0)) for row in A]
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def vsum(a,b): return [x+y for x,y in zip(a,b)]
def scale(v,c): return [c*x for x in v]
def solve(A,b):
    A=[list(row)+[v] for row,v in zip(A,b)]; n=len(A)
    for j in range(n):
        i=next((i for i in range(j,n) if A[i][j]),None)
        assert i is not None,'singular system'
        A[i],A[j]=A[j],A[i]
        p=A[j][j]; A[j]=[x/p for x in A[j]]
        for i in range(n):
            if i!=j:
                q=A[i][j]
                A[i]=[x-q*y for x,y in zip(A[i],A[j])]
    return [row[-1] for row in A]

def invariant(M,weight):
    n=len(M)
    eq=[[M[i][j]-(1 if i==j else 0) for j in range(n)] for i in range(n)]
    eq[-1]=weight[:]
    ans=solve(eq,[F(0)]*(n-1)+[F(1)])
    assert mv(M,ans)==ans and dot(weight,ans)==1
    assert all(x>0 for x in ans)
    return ans

def make_model(d,m):
    ell=list(map(F, range(1,d+1)))
    Bs=[]
    for _ in range(m):
        raw=[[F(R.randint(1,11)) for _ in range(d)] for _ in range(d)]
        B=[[raw[i][j]*ell[j]/dot(ell,[raw[z][j] for z in range(d)]) for j in range(d)] for i in range(d)]
        assert [dot(ell,[B[i][j] for i in range(d)]) for j in range(d)]==ell
        Bs.append(B)
    raw=[[F(R.randint(1,9)) for _ in range(m)] for _ in range(m)]
    P=[[raw[j][k]/sum((raw[i][k] for i in range(m)),F(0)) for k in range(m)] for j in range(m)]
    rhos=[F(R.randint(1,9),R.randint(1,7)) for _ in range(m)]
    return ell,Bs,P,rhos

def block(Bs,P):
    m=len(Bs);d=len(Bs[0]);return [[P[j][k]*Bs[k][i][q] for k in range(m) for q in range(d)] for j in range(m) for i in range(d)]

def model_stationary(ell,Bs,P):
    d=len(ell);m=len(Bs)
    pi=invariant(P,[F(1)]*m)
    M=block(Bs,P)
    mu=invariant(M,ell*m)
    assert [dot(ell,mu[k*d:(k+1)*d]) for k in range(m)]==pi
    return pi,M,mu

def test_exact_example():
    ell=[F(1),F(1)]
    Bs=[[[Q(9,10),Q(2,5)],[Q(1,10),Q(3,5)]],[[Q(1,5),Q(4,5)],[Q(4,5),Q(1,5)]]]
    P=[[Q(3,4),Q(1,3)],[Q(1,4),Q(2,3)]]
    rho=[F(2),F(4)]
    pi,M,mu=model_stationary(ell,Bs,P)
    assert pi==[Q(4,7),Q(3,7)]
    assert mu==[Q(8,21),Q(4,21),Q(5,21),Q(4,21)]
    b1=mu[0]/rho[0];b2=mu[2]/rho[1]
    assert (b1,b2,b1+b2)==(Q(4,21),Q(5,84),Q(1,4))
    assert b1!=pi[0]*(b1+b2)
    assert mm(Bs[0],Bs[1])!=mm(Bs[1],Bs[0])
    # iid with the SAME environmental frequencies, still noncommuting matrices
    Pi=[[pi[j] for _ in range(2)] for j in range(2)]
    _,_,mu_iid=model_stationary(ell,Bs,Pi)
    r=[sum((mu_iid[k*2+i] for k in range(2)),F(0)) for i in range(2)]
    assert r==[Q(10,17),Q(7,17)]
    assert (pi[0]*r[0]/rho[0],pi[1]*r[0]/rho[1])==(Q(20,119),Q(15,238))
    assert pi[0]*r[0]/rho[0]!=pi[0]*r[0]*(pi[0]/rho[0]+pi[1]/rho[1])
    return ell,Bs,P,rho,mu

def test_finite_derivatives(ell,Bs,P,rho):
    d=len(ell);m=len(Bs)
    As=[[[rho[k]*v for v in row] for row in Bs[k]] for k in range(m)]
    count=0
    for T in range(1,10):
        words=list(product(range(m),repeat=T)) if T<=7 else [tuple(R.randrange(m) for _ in range(T)) for __ in range(70)]
        for word in words:
            z=[F(R.randint(1,8)) for _ in range(d)];x=scale(z,F(1)/dot(ell,z))
            dx=[F(0)]*d; direct=x[:]; gradient=F(0)
            k_target=R.randrange(m); ii=R.randrange(d); jj=R.randrange(d)
            for k in word:
                if k==k_target:
                    gradient+=ell[ii]*x[jj]/rho[k]
                    Hx=[F(0)]*d;Hx[ii]=direct[jj]
                else: Hx=[F(0)]*d
                dx=vsum(mv(As[k],dx),Hx)
                direct=mv(As[k],direct)
                x=mv(Bs[k],x)
            assert gradient==dot(ell,dx)/dot(ell,direct),(word,gradient,dx,direct)
            count+=1
    return count

def test_markov_closure():
    cases=0; enum=0; derivatives=0
    for it in range(70):
        d=2+(it%2);m=2+(it%3==0)
        ell,Bs,P,rho=make_model(d,m)
        pi,M,mu=model_stationary(ell,Bs,P)
        # All entries of B and P strictly positive; invariant vector unique.
        for k in range(m):
            assert sum((pi[j]*P[k][j] for j in range(m)),F(0))==pi[k]
        for i in range(d):
            for j in range(d):
                b=sum((ell[i]*mu[k*d+j]/rho[k] for k in range(m)),F(0))
                assert b>0; derivatives+=1
        cases+=1
        if it<15:
            x0=[F(R.randint(1,7)) for _ in range(d)];x0=scale(x0,F(1)/dot(ell,x0))
            mu0=[pi[k]*x0[i] for k in range(m) for i in range(d)]
            cur=[(k,x0,pi[k]) for k in range(m)]
            for T in range(1,5):
                nxt=[]
                for k,x,p in cur:
                    nx=mv(Bs[k],x)
                    for j in range(m):nxt.append((j,nx,p*P[j][k]))
                cur=nxt
                observed=[sum((p*x[i] for k,x,p in cur if k==j),F(0)) for j in range(m) for i in range(d)]
                mu0=mv(M,mu0)
                assert observed==mu0
                enum+=len(cur)
    return cases,enum,derivatives

def test_markov_gradient_monte_carlo(ell,Bs,P,rho,mu):
    seed=56789
    for target in range(2):
        rng=random.Random(seed+target)
        h=1e-4
        # Grow two perturbed populations using the *same* environment chain.
        vecplus=[.5,.5];vecminus=[.5,.5]
        totals=[0.0,0.0]
        k=0
        for t in range(220000):
            for idx, (delta, x) in enumerate(((h,vecplus),(-h,vecminus))):
                A=[[float(rho[k]*Bs[k][i][j]) for j in range(2)] for i in range(2)]
                if k==target: A[0][0]+=delta
                y=[sum(A[i][j]*x[j] for j in range(2)) for i in range(2)]
                mass=y[0]+y[1]
                totals[idx]+=math.log(mass)
                x[:]=[v/mass for v in y]
            k=0 if rng.random()<float(P[0][k]) else 1
        approx=(totals[0]-totals[1])/(2*h*220000)
        expected=float(mu[target*2]/rho[target])
        assert abs(approx-expected)<0.004,(approx,expected)
        print('finite_difference_state',target+1,'observed',format(approx,'.7f'),'exact',format(expected,'.7f'))

if __name__=='__main__':
    ell,Bs,P,rho,mu=test_exact_example()
    n=test_finite_derivatives(ell,Bs,P,rho)
    cases,enum,derivatives=test_markov_closure()
    test_markov_gradient_monte_carlo(ell,Bs,P,rho,mu)
    print('PASS', 'exact_finite_horizon_identities',n,'exact_random_models',cases,
          'linear_stationarity_derivatives',derivatives,'enumerated_markov_paths',enum)
