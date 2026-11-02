#!/usr/bin/env python3
"""Independent finite-state checks of pendant-target reset hitting laws.
Standard-library only. Run: python checker.py
"""
from fractions import Fraction as F
from math import sqrt

checks=0

def chk(cond, name):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(name)

def trap_edges(m,d,variant=0):
    if not (0<=d<m and (m*d)%2==0):
        raise ValueError('infeasible regularity')
    edges=set()
    for j in range(1,d//2+1):
        for i in range(m):
            a,b=sorted((i,(i+j)%m))
            edges.add((a,b))
    if d%2:
        for i in range(m//2):
            edges.add((i,i+m//2))
    if variant and m==6 and d==2:
        edges={(0,1),(0,2),(1,2),(3,4),(3,5),(4,5)}
    if variant and m==6 and d==3:
        edges={(i,j) for i in range(3) for j in range(3,6)}
    if variant and m==8 and d==2:
        edges={(i,(i+1)%4) for i in range(4)}|{(4+i,4+(i+1)%4) for i in range(4)}
    degrees=[0]*m
    for a,b in edges:
        degrees[a]+=1;degrees[b]+=1
    chk(len(edges)==m*d//2 and all(x==d for x in degrees),'regular graph')
    return edges

def graph(m,d,L,variant=0):
    # vertices: 0 source; 1..m trap; m+1 target; other leaves
    N=m+L+1
    nbr=[set() for i in range(N)]
    def edge(i,j): nbr[i].add(j);nbr[j].add(i)
    for j in range(1,N): edge(0,j)
    for a,b in trap_edges(m,d,variant):edge(a+1,b+1)
    return nbr,m+1

def gaussian(A,b):
    A=[list(row)+[rhs] for row,rhs in zip(A,b)]
    n=len(b)
    for j in range(n):
        pivot=next(i for i in range(j,n) if A[i][j])
        A[j],A[pivot]=A[pivot],A[j]
        fac=A[j][j]
        A[j]=[x/fac for x in A[j]]
        for i in range(n):
            if i!=j and A[i][j]:
                fac=A[i][j]
                A[i]=[a-fac*c for a,c in zip(A[i],A[j])]
    return [A[i][-1] for i in range(n)]

def full_mean(nbr,target,r):
    states=[i for i in range(len(nbr)) if i!=target]
    A=[]
    for i in states:
        row=[]
        for j in states:
            p= r*(j==0)+(1-r)*F(j in nbr[i],len(nbr[i]))
            row.append(F(i==j)-p)
        A.append(row)
    return gaussian(A,[F(1) for i in states])[0]

def exact_mean(m,d,L,r):
    return F(m+L,1)/(1-r)+F(m*(d+1),1)/(1+d*r)+L-1

def finite_law(nbr,target,r,steps):
    state={0:F(1)}; probs=[]
    for k in range(steps):
        after={};hit=F(0)
        for i,prob in state.items():
            for j,p in [(0,r)]+[(j,(1-r)*F(1,len(nbr[i]))) for j in nbr[i]]:
                if j==target:hit+=prob*p
                else:after[j]=after.get(j,F(0))+prob*p
        state=after;probs.append(hit)
    return probs

def lump_law(m,d,L,r,steps):
    p=(1-r)*F(1,m+L);v=(1-r)*F(m,m+L)
    w=(1-r)*F(L-1,m+L);q=r+(1-r)*F(1,d+1)
    S,H,D=F(1),F(0),F(0);out=[]
    for k in range(steps):
        out.append(S*p)
        S,H,D=S*r+H*q+D, S*v+H*(1-q), S*w
    return out


def full_pgf(nbr,target,r,z):
    states=[i for i in range(len(nbr)) if i!=target]
    A=[]; rhs=[]
    for i in states:
        row=[]
        for j in states:
            p=r*(j==0)+(1-r)*F(j in nbr[i],len(nbr[i]))
            row.append(F(i==j)-z*p)
        A.append(row)
        rhs.append(z*(1-r)*F(target in nbr[i],len(nbr[i])))
    return gaussian(A,rhs)[0]

def closed_pgf(m,d,L,r,z):
    p=(1-r)*F(1,m+L);v=(1-r)*F(m,m+L)
    w=(1-r)*F(L-1,m+L);q=r+(1-r)*F(1,d+1)
    return z*p*(1-z*(1-q))/((1-z*r-z*z*w)*(1-z*(1-q))-z*z*v*q)

def optimum(m,d,L):
    if d==0 or m*d*(d+1)<=m+L:return 0.0
    kap=sqrt(m*d*(d+1)/(m+L))
    return (kap-1)/(kap+d)

for m in range(2,10):
 for d in range(m):
  if m*d%2:continue
  for L in (1,2,3,6):
   for r in (F(0),F(1,5),F(1,2),F(4,5)):
    for variant in ((0,1) if (m,d) in ((6,2),(6,3),(8,2)) else (0,)):
     nbr,t=graph(m,d,L,variant)
     chk(full_mean(nbr,t,r)==exact_mean(m,d,L,r),'full Markov mean')
     chk(finite_law(nbr,t,r,10)==lump_law(m,d,L,r,10),'full law vs 3-class model')
     for z in (F(1,3),F(2,3)):
      chk(full_pgf(nbr,t,r,z)==closed_pgf(m,d,L,r,z),'full-resolvent pgf')
  for L in (1,2,3,6,m,max(1,m*(d*(d+1)-1)),max(1,m*(d*(d+1)-1)+1)):
   if L<1:continue
   r0=optimum(m,d,L)
   f0=float(exact_mean(m,d,L,F(0)))
   fm=lambda x:(m+L)/(1-x)+m*(d+1)/(1+d*x)+L-1
   chk(fm(r0)<=f0+1e-9,'minimum dominates no reset')
   for x in (0.0,0.01,0.1,0.35,0.6,0.85,0.99):
    chk(fm(r0)<=fm(x)+1e-8,'global optimum')
   if r0>0:
    closed=(sqrt((m+L)*d/(d+1))+sqrt(m))**2+L-1
    chk(abs(fm(r0)-closed)<1e-8,'closed minimum')
   chk((r0>0)==(m*d*(d+1)>m+L),'sharp phase boundary')

# Analytic limiting constants verified by direct exact-mean evaluation.
for lam in (0,0.25,1,3):
 C=(sqrt(1+lam)+1)**2+lam
 rlim=1/(1+sqrt(1+lam))
 for m in (200,1000,5000):
  d=m-1;L=max(1,round(lam*m))
  rr=optimum(m,d,L)
  f=(m+L)/(1-rr)+m*(d+1)/(1+d*rr)+L-1
  chk(abs(rr-rlim)<4/m,'reset limit')
  chk(abs(f/m-C)<10/m,'mean limit')
print('PASS',checks,'exact comparison and analytic-limit assertions')
