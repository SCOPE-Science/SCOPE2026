"""Exact finite checks of the claimed complete-multipartite equilibrium classification.
Only standard Python libraries. Finite enumerations corroborate an all-orders proof.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd, prod, comb
from functools import reduce


def matrix(part_sizes):
    n=sum(part_sizes)
    parts=[i for i,q in enumerate(part_sizes) for _ in range(q)]
    W=[[F(int(parts[i]!=parts[j]),n-part_sizes[parts[i]]) for j in range(n)] for i in range(n)]
    return W,parts

def solve(A,b):
    n=len(b); z=[list(A[i])+[b[i]] for i in range(n)]
    for k in range(n):
        i=next(i for i in range(k,n) if z[i][k])
        z[i],z[k]=z[k],z[i]
        v=z[k][k];z[k]=[q/v for q in z[k]]
        for i in range(n):
            if i==k:continue
            v=z[i][k]
            if v:z[i]=[z[i][j]-v*z[k][j] for j in range(n+1)]
    return [z[i][-1] for i in range(n)]

def state(part_sizes,x,alpha,beta,lam,gamma,u,r):
    W,parts=matrix(part_sizes);n=len(x)
    t=beta*(1-gamma)/(beta+lam)
    aa=beta*gamma/(beta+lam);h=lam/(beta+lam)
    y=solve([[F(int(i==j))-t*W[i][j] for j in range(n)] for i in range(n)],
            [aa*u+h*x[i] for i in range(n)])
    neighbor=[sum(W[i][j]*y[j] for j in range(n)) for i in range(n)]
    kappa=beta*lam/(beta+lam)
    delta=[alpha*(r/F(n)-1)+kappa*((1-gamma)*mi+gamma*u-F(1,2)) for mi in neighbor]
    nash=all((x[i]==1 and delta[i]>=0) or (x[i]==0 and delta[i]<=0) for i in range(n))
    return y,neighbor,delta,nash

def predicted(part_sizes,x,alpha,beta,lam,gamma,u,r):
    n=sum(part_sizes)
    k=sum(x);p=F(k,n);m=len(part_sizes)
    if k==0 or k==n:
        pass
    else:
        s=0
        for q in part_sizes:
            if sum(x[s:s+q])!=q*p:return False
            s+=q
    R=(beta*gamma*u+lam*p)/(beta*gamma+lam)
    delta=alpha*(r/F(n)-1)+beta*lam/(beta+lam)*((1-gamma)*R+gamma*u-F(1,2))
    return delta>=0 if k==n else delta<=0 if k==0 else delta==0

def payoff_delta(W,y,alpha,beta,lam,gamma,u,r):
    n=len(y); out=[]
    for i in range(n):
        vals=[]
        for x_i in (0,1):
            m=sum(W[i][j]*y[j] for j in range(n))
            z=(beta*(1-gamma)*m+beta*gamma*u+lam*x_i)/(beta+lam)
            opinion=-beta*F(1,2)*((1-gamma)*sum(W[i][j]*(z-y[j])**2 for j in range(n))+gamma*(z-u)**2)
            consistency=-lam*F(1,2)*(x_i-z)**2
            public=alpha*x_i*(r/F(n)-1)
            vals.append(opinion+consistency+public)
        out.append(vals[1]-vals[0])
    return out

def full_exhaustive():
    params=[
      (F(1,7),F(3,7),F(3,7),F(1,2),F(1),F(2)),
      (F(1,10),F(2,5),F(1,2),F(0),F(0),F(3,2)),
      (F(1,10),F(2,5),F(1,2),F(1,3),F(3,4),F(5,2)),
      (F(1,20),F(9,20),F(1,2),F(2,3),F(1,4),F(7,4)),
    ]
    cases=0
    for sz in [(1,1),(1,2),(2,2),(1,1,1),(1,2,2),(2,2,2),(2,3),(3,3),(1,3,2),(1,1,4)]:
        n=sum(sz)
        for param in params:
            aa,bb,ll,gg,uu,rr=param
            if rr>=n:continue
            for x in product((0,1),repeat=n):
                y,m,d,got=state(sz,x,*param)
                assert d==payoff_delta(matrix(sz)[0],y,*param)
                expect=predicted(sz,x,*param)
                assert got==expect,(sz,x,param,y,d,got,expect)
                assert all(F(0)<=z<=F(1) for z in y)
                cases+=1
    return cases

def exact_example():
    sz=(2,2);pars=(F(1,7),F(3,7),F(3,7),F(1,2),F(1),F(2))
    hits=[]
    for x in product((0,1),repeat=4):
        y,m,d,ok=state(sz,x,*pars)
        if ok:hits.append((x,y,d))
    assert len(hits)==6,hits
    mixed=[z for z in hits if 0<sum(z[0])<4]
    assert len(mixed)==4
    assert all(set(z[1])=={F(5,12),F(11,12)} and all(di==0 for di in z[2]) for z in mixed)
    return hits

if __name__=='__main__':
    rows=full_exhaustive()
    h=exact_example()
    print('PASS: exact rational best-response equilibrium enumeration',rows,'profiles')
    print('PASS: K_{2,2} exactly',len(h),'equilibria, of which four balanced mixed and all indifferent')
    print('PASS: mixed opinions are 5/12 (defect) and 11/12 (cooperate)')
