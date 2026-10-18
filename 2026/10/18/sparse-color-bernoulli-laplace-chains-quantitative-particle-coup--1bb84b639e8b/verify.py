#!/usr/bin/env python3
"""Exact finite-state verification of a rare-color Bernoulli--Laplace coupling bound."""
from fractions import Fraction as F
from math import comb

def hyp(N,K,s,a):
    if not (0<=a<=K and 0<=s-a<=N-K): return F(0)
    return F(comb(K,a)*comb(N-K,s-a),comb(N,s))

def bn(n,p):
    return [F(comb(n,j))*p**j*(1-p)**(n-j) for j in range(n+1)]

def conv(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b): c[i+j]+=ai*bj
    return c

def tv(a,b): return sum((abs(x-y) for x,y in zip(a,b)),F(0))/2

def exact(N,m,k,r,x,t):
    assert 1<=k<=min(m,N-m) and r<=min(m,N-m)
    P=[[sum((hyp(m,i,k,a)*hyp(N-m,r-i,k,j-i+a) for a in range(i+1)),F(0)) for j in range(r+1)] for i in range(r+1)]
    assert all(sum(row)==1 for row in P)
    v=[F(int(i==x)) for i in range(r+1)]
    for _ in range(t): v=[sum((v[i]*P[i][j] for i in range(r+1)),F(0)) for j in range(r+1)]
    h=F(m,N); rho=1-F(k,m)-F(k,N-m)
    L=h+(1-h)*rho**t; R=h-h*rho**t
    proxy=conv(bn(x,L),bn(r-x,R))
    pi=[F(comb(m,j)*comb(N-m,r-j),comb(N,r)) for j in range(r+1)]
    prod=bn(r,h)
    bound=t*F(r*(r-1),2)*(F(1,m-r+1)+F(1,N-m-r+1)) + F(r*(r-1),2*(N-r+1))
    assert tv(v,proxy)<=bound and tv(pi,prod)<=bound
    assert abs(tv(v,pi)-tv(proxy,prod))<=bound
    return float(tv(v,pi)), float(tv(proxy,prod)), float(bound)

def main():
    total=0
    examples=[]
    for N in [12,18,25,40,60]:
      for m in [N//3,N//2]:
       for k in [1,max(1,m//3),min(m,N-m)]:
        for r in [1,2,3,4]:
         if r>min(m,N-m):continue
         for x in range(r+1):
          for t in [0,1,2,3]:
           d,dproxy,bd=exact(N,m,k,r,x,t); total+=1
           if N==40 and m==20 and k==10 and r==3 and x==3 and t==3: examples.append((d,dproxy,bd))
    print('PASS exact finite-chain distributions and TV approximation: ',total,'cases')
    print('example true/proxy/bound:',examples)

if __name__=='__main__':main()
