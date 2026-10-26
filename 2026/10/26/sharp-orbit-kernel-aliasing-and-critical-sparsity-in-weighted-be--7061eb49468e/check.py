#!/usr/bin/env python3
"""Independent numerical checks for a weighted Bergman kernel orbit theorem.
Python 3 standard library only; finite checks supplement the analytic proof.
"""
import cmath, math

def logc(j,b): return math.lgamma(j+b)-math.lgamma(b)-math.lgamma(j+1)

def indices(N,m,t):
    lo=N%m
    # Tail begins well beyond a gamma-density's effective support. The
    # last few exponentially tiny terms do not affect reported tolerances.
    hi=max(5*N, int((80+5*b_global)*N/max(t,.3)))
    return range(lo,hi+1,m)

def mass(N,m,b,t):
    global b_global
    b_global=b
    jj=list(indices(N,m,t))
    arr=[logc(j,b)-t*j/N for j in jj]
    mx=max(arr)
    zz=[math.exp(x-mx) for x in arr]
    z=sum(zz)
    prob=math.exp(logc(N,b)-t-mx)/z
    avg=sum((j/N)*u for j,u in zip(jj,zz))/z
    return prob,avg

def optimal(N,m,b):
    if m>N:return (float('inf'),1.0)
    a,bound=1.e-5,80.0
    for _ in range(55):
        mid=(a+bound)/2
        _,av=mass(N,m,b,mid)
        # d log P / dt = average j/N -1 decreases in t.
        if av>1:a=mid
        else:bound=mid
    t=(a+bound)/2
    return t,mass(N,m,b,t)[0]

def solve(A,b):
    n=len(b);mat=[list(A[i])+[b[i]] for i in range(n)]
    for i in range(n):
        j=max(range(i,n),key=lambda k:abs(mat[k][i]))
        mat[i],mat[j]=mat[j],mat[i]
        p=mat[i][i]
        assert abs(p)>1e-14
        mat[i]=[q/p for q in mat[i]]
        for k in range(n):
            if k==i:continue
            fac=mat[k][i]
            mat[k]=[mat[k][j]-fac*mat[i][j] for j in range(n+1)]
    return [mat[i][-1] for i in range(n)]

checks=0
for beta in [1.25,2.,3.5]:
 for N in range(2,12):
  for m in range(1,min(N+2,7)):
   t=1.3+N/17; r=math.exp(-t/(2*N))
   w=[r*cmath.exp(2j*math.pi*j/m) for j in range(m)]
   G=[[(1-w[i].conjugate()*w[j])**(-beta) for j in range(m)] for i in range(m)]
   cn=math.exp(logc(N,beta));v=[cn**.5*w[j].conjugate()**N for j in range(m)]
   x=solve(G,v)
   q=sum(v[j].conjugate()*x[j] for j in range(m)).real
   p,_=mass(N,m,beta,t)
   assert abs(p-q)<2e-8,(N,m,beta,p,q)
   checks+=1

for beta in [1.25,2.,3.5]:
 for N in [40,100,200,500]:
  for m in [1,2,5,10]:
   t,p=optimal(N,m,beta)
   assert 0<p<1 and t>0
   for dt in [.002,.01,.1,.5]:
    assert p+1e-12>=mass(N,m,beta,t+dt)[0]
    assert p+1e-12>=mass(N,m,beta,max(1e-9,t-dt))[0]
    checks+=2

for beta in [1.25,2.,3.5]:
 C=beta**beta*math.exp(-beta-math.lgamma(beta))
 for N,m in [(1000,3),(2000,5),(3000,7)]:
  t,p=optimal(N,m,beta)
  assert abs(t-beta)<.035
  assert abs(p*N/m-C)<.006
  checks+=2

for beta in [1.25,2.,3.5]:
 for N,ell in [(10000,0),(10000,2),(100000,0),(100000,5)]:
  m=N-ell;t,p=optimal(N,m,beta)
  a=math.exp(logc(ell,beta)-logc(N,beta))
  bb=math.exp(logc(N+m,beta)-logc(N,beta))
  pred=2*math.sqrt(a*bb)
  if pred<.16: assert abs((1-p)/pred-1)<.15,(beta,N,ell,p,pred)
  checks+=1

for beta in [1.25,2.,3.5]:
 for N in [5,20,200]:
  for m in [N+1,N+2]:
   for t in [10,20,40]:
    assert 0<mass(N,m,beta,t)[0]<=1+1e-12
    checks+=1
print('PASS: %d independent finite numerical assertions' % checks)
