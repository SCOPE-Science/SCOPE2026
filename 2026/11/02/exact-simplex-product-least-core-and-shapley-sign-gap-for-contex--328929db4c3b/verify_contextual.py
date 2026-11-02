#!/usr/bin/env python3
"""Exact checks for the additive-base contextual coalition model.
All arithmetic in the combinatorial and excess checks uses fractions.
The LP checks use scipy HiGHS independently of the closed form.
"""
from fractions import Fraction as F
from math import factorial, comb
from itertools import product
import numpy as np
from scipy.optimize import linprog, minimize


def data(u,d,a,b,m):
    n=u+d
    def v(s):
        return sum(m[i] for i in range(u) if s >> i & 1) + a*sum(bool(s >> i & 1) for i in range(u,n)) + (b if s == (1<<u)-1 else F(0))
    return n,v

def sh_exact(n, v):
    f=factorial
    vals=[]
    for i in range(n):
        val=F(0)
        for s in range(1<<n):
            if s >> i & 1: continue
            k=s.bit_count()
            val += F(f(k)*f(n-k-1),f(n)) * (v(s | 1<<i)-v(s))
        vals.append(val)
    return vals


def exhaustive(u,d,a,b,m):
    n,v=data(u,d,a,b,m)
    U=(1<<u)-1
    T=b/2
    base=m+[a]*d
    ys=[T/F(u)]*u+[-T/F(d)]*d
    xs=[base[i]+ys[i] for i in range(n)]
    assert sum(xs)==v((1<<n)-1)
    excess=lambda S: v(S)-sum(xs[i] for i in range(n) if S>>i&1)
    exc=[excess(s) for s in range(1,(1<<n)-1)]
    assert max(exc)==T, (u,d,a,b,max(exc),T)
    assert excess(U)==T and excess(((1<<n)-1)^U)==T

    # Independently solve full exponential-constraint least-core LP.
    eq=[[1.]*n+[0.]]
    eqval=[float(v((1<<n)-1))]
    A=[]; B=[]
    for s in range(1,(1<<n)-1):
        A.append([(-1. if (s>>i)&1 else 0.) for i in range(n)]+[-1.])
        B.append(-float(v(s)))
    lp=linprog([0.]*n+[1.], A_ub=A,b_ub=B,A_eq=eq,b_eq=eqval,
               bounds=[(None,None)]*(n+1),method='highs')
    assert lp.success,lp.message
    assert abs(lp.fun-float(T))<1e-7,(u,d,a,b,lp.fun,T)

    sh=sh_exact(n,v)
    cf=F(comb(n,u))
    shp=[m[i]+b/F(u)/cf for i in range(u)]+[a-b/F(d)/cf]*d
    assert sh==shp,(u,d,sh,shp)

    # Check every predicted simplex-product vertex is an optimal payoff.
    for i in range(u):
      for j in range(d):
        y=[F(0)]*n
        y[i]=T; y[u+j]=-T
        xv=[base[k]+y[k] for k in range(n)]
        assert sum(xv)==v((1<<n)-1)
        assert max(v(s)-sum(xv[k] for k in range(n) if s>>k&1) for s in range(1,(1<<n)-1))==T
    return len(exc),u*d


def check_min_norm():
    for u,d in [(2,2),(3,2),(4,2),(4,3)]:
      n=u+d
      m=[F(2*i+1) for i in range(u)]
      a=F(3); b=F(2*u*d+3)
      T=float(b/2)
      base=list(map(float,m))+[float(a)]*d
      lo=min(base[:u]);hi=max(base[:u])+T+1
      for z in range(90):
          md=(lo+hi)/2
          if sum(max(0,md-base[i]) for i in range(u))<T: lo=md
          else: hi=md
      theta=(lo+hi)/2
      ystar=[max(0,theta-base[i]) for i in range(u)]+[-T/d]*d
      xstar=np.array(base)+np.array(ystar)
      def cons1(z):return sum(z[:u])-T
      def cons2(z):return sum(z[u:])+T
      opt=minimize(lambda y:sum((np.array(base)+y)**2), ystar,
                method='SLSQP', constraints=[{'type':'eq','fun':cons1},{'type':'eq','fun':cons2}],
                bounds=[(0,None)]*u+[(None,0)]*d, options={'ftol':1e-12,'maxiter':500})
      assert opt.success or np.linalg.norm(opt.x-ystar)<1e-5
      assert np.linalg.norm(opt.x-ystar)<1e-5,(u,d,opt.x,ystar)
    return True

if __name__=='__main__':
    cases=0;coals=0;vertices=0
    for u in range(1,5):
      for d in range(1,4):
        if u+d>7:continue
        for a,b in product([F(1),F(5,2)],[F(3),F(11,2),F(17)]):
          m=[F(i+2,2) for i in range(u)]
          c,v=exhaustive(u,d,a,b,m)
          cases+=1;coals+=c;vertices+=v
    check_min_norm()
    print('VERIFY_OK cases=%d coalitional_constraints=%d simplex_vertices=%d min_norm_cases=4' %(cases,coals,vertices))
