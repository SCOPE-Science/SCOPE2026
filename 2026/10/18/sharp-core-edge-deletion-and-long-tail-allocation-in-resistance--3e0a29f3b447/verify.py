"""Finite checks for a priced lollipop resistance design theorem.
The universal statements are proved analytically, not by these tests.
Python 3 with numpy and sympy. Run: python verify.py
"""
import math
import numpy as np
import sympy as sp

checks=0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks+=1

def policy(m,l,t,B=1.0):
    assert m>=3 and l>=1 and t>0 and B>0
    n=m+l
    k=m-1
    A=l+1
    C=n*(m-2)
    beta=t*(m-2)/2
    alpha=k-beta
    threshold=2*n*k/(A+C)
    c=np.array([j*(n-j) for j in range(1,l+1)], dtype=float)
    S=np.sqrt(c).sum()
    if t<threshold:
        check(alpha>0,'alpha positive in mixed phase')
        h=math.sqrt(A*alpha)+math.sqrt(C*beta)
        x=B*math.sqrt(A/alpha)/(h+S)
        v=B*math.sqrt(C/beta)/(h+S)
        y=(v-x)/k
    else:
        h=math.sqrt(k*(A+C))
        x=B*math.sqrt((A+C)/k)/(h+S)
        y=0.
    z=B*np.sqrt(c)/(h+S)
    return x,y,z,(h+S)**2/B,threshold

def resistance(m,l,x,y,z):
    n=m+l
    L=np.zeros((n,n))
    def edge(i,j,w):
        L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
    for i in range(1,m): edge(0,i,x)
    for i in range(1,m):
        for j in range(i+1,m):edge(i,j,y)
    # z[j-1] indexed from tip toward root, so the root edge has z[l-1]
    for i in range(l):edge(m-1+i if i>0 else 0,m+i,z[l-1-i])
    ev=np.linalg.eigvalsh(L)
    assert ev[1]>1e-12
    return n*sum(1/e for e in ev[1:])

# Symbolic, rational and asymptotic consistency checks.
m,l,t=sp.symbols('m l t',positive=True)
n=m+l;k=m-1;A=l+1;C=n*(m-2);b=t*(m-2)/2;a=k-b
th=2*n*k/(A+C)
check(sp.simplify(th-(2+2*(m-1)/(A+C)))==0,'threshold rearrangement')
check(sp.simplify((C*a-A*b).subs(t,th))==0,'active constraint')
check(sp.simplify((A*(A*k/(A+C)) + C*(C*k/(A+C)) + 2*A*C*k/(A+C)) - (A+C)*k)==0,'boundary matching')
for mm in range(3,9):
 for ll in range(1,8):
  N=mm+ll
  tt=2*N*(mm-1)/(ll+1+N*(mm-2))
  for factor in (0.03,0.45,0.99,1.,1.01,3.,20.):
   T=tt*factor
   for B in (0.3,1.,5.):
    x,y,z,Kopt,_=policy(mm,ll,T,B)
    check(x>0 and y>=-1e-11 and min(z)>0,'nonnegative allocation')
    budget=(mm-1)*x+T*(mm-1)*(mm-2)*y/2+sum(z)
    check(abs(budget-B)<1e-9*B,'budget')
    if factor<1:
     check(y>0,'positive inner-clique conductance')
    else:
     check(abs(y)<1e-12,'deleted inner-clique conductance')
    Kformula=(ll+1)/x+N*(mm-2)/(x+(mm-1)*y)+sum(j*(N-j)/z[j-1] for j in range(1,ll+1))
    check(abs(Kformula/Kopt-1)<1e-10,'decomposed objective')
    Kmatrix=resistance(mm,ll,x,y,z)
    check(abs(Kmatrix/Kopt-1)<2e-9,'Laplacian pseudoinverse objective')
    # Asymmetric feasible perturbations of full edge allocations must not improve.
    rng=np.random.default_rng(mm*100+ll*10+int(factor*100))
    for h in range(3):
     E=[]
     for j in range(1,mm):E.append((0,j,x,1.))
     for i in range(1,mm):
      for j in range(i+1,mm):E.append((i,j,y,T))
     for i in range(ll):E.append((mm-1+i if i>0 else 0,mm+i,z[ll-1-i],1.))
     # A mixture with any strictly-positive full-graph random assignment.
     weights=rng.uniform(0.1,2.,size=len(E));weights*=B/sum(e[3]*w for w,e in zip(weights,E))
     rho=0.08+0.19*h
     W=[(1-rho)*e[2]+rho*w for w,e in zip(weights,E)]
     LL=np.zeros((N,N))
     for w,(u,v,_,price) in zip(W,E):
      LL[u,u]+=w;LL[v,v]+=w;LL[u,v]-=w;LL[v,u]-=w
     ev=np.linalg.eigvalsh(LL)
     Kother=N*sum(1/e for e in ev[1:])
     check(Kother>=Kopt-1e-7,'independently perturbed allocation')
print('PASS',checks,'checks')
