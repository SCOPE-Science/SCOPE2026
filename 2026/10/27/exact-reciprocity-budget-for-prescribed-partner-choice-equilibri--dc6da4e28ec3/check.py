"""Exact and independent checks for reciprocal-payoff partner-choice theorem.
Usage: python check.py
Requires standard Python; SciPy used only for optional independent LP checks.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb, factorial


def cycles(f):
    n=len(f); done=set(); ans=[]
    for start in range(n):
        if start in done: continue
        path=[]; pos={}; u=start
        while u not in done and u not in pos:
            pos[u]=len(path); path.append(u); u=f[u]
        if u in pos: ans.append(path[pos[u]:])
        done.update(path)
    return ans


def cycle_mean(f, margins):
    means=[sum((margins[i] for i in c), Q(0))/len(c)
           for c in cycles(f) if len(c)>=3]
    return max(means,default=Q(0))


def payoff_witness(f, margins):
    """A positive rational payoff matrix realizing f at minimum reciprocity error."""
    n=len(f); margins=[Q(x) for x in margins]; D=max(margins)
    L=(n+2)*D+1; B=(n+3)*L
    U=[[Q(1) for _ in range(n)] for _ in range(n)]
    cs=cycles(f)
    cyc={i for c in cs for i in c}
    for c in cs:
        if len(c)==1: U[c[0]][c[0]]=B
        elif len(c)==2:
            i,j=c; U[i][j]=U[j][i]=B
        else:
            mean=sum((margins[i] for i in c),Q(0))/len(c)
            a=[Q(0)]*len(c)
            for t in range(1,len(c)):
                a[t]=a[t-1]+margins[c[t]]-mean
            for t,i in enumerate(c):
                j=c[(t+1)%len(c)]
                U[i][j]=B+a[t]
                U[j][i]=B+a[t]-mean
    def depth(i):
        d=0
        while i not in cyc:
            d+=1; i=f[i]
        return d
    for i in range(n):
        if i not in cyc:
            j=f[i]; w=B-depth(i)*L
            U[i][j]=U[j][i]=w
    assert min(min(row) for row in U)>0
    for i in range(n):
        for j in range(n):
            if j!=f[i]: assert U[i][f[i]]-U[i][j]>=margins[i]
    dmax=max(abs(U[i][j]-U[j][i]) for i in range(n) for j in range(n))
    assert dmax==cycle_mean(f,margins), (f,margins,dmax,cycle_mean(f,margins))
    return U


def involutions(n):
    return sum(factorial(n)//(2**j*factorial(j)*factorial(n-2*j))
               for j in range(n//2+1))


def count_formula(n):
    return sum(comb(n,k)*involutions(k)*k*n**(n-k-1) if k<n else involutions(n)
               for k in range(1,n+1))


def run():
    total=0
    for n in range(1,7):
        count=0
        for f in product(range(n),repeat=n):
            margin=tuple(Q(i+1) for i in range(n))
            payoff_witness(f,margin)
            count+=cycle_mean(f,[Q(1)]*n)==0
            total+=1
        predicted=count_formula(n)
        assert count==predicted,(n,count,predicted)
        print(f'ORDER {n}: maps={n**n}, restricted={count}, unrestricted={n**n}')
    print('EXACT_WITNESS_AND_CENSUS_PASS',total)
    try:
        import numpy as np
        from scipy.optimize import linprog
    except ImportError:
        print('LP_CHECK_SKIPPED: scipy unavailable')
        return
    lp_count=0
    for n in (3,4):
      for f in product(range(n),repeat=n):
        margins=[i+1 for i in range(n)]
        num=n*n+1; rows=[]; rhs=[]
        for i in range(n):
          for j in range(n):
            if j==f[i]: continue
            row=np.zeros(num)
            row[i*n+f[i]]=-1; row[i*n+j]=1
            rows.append(row);rhs.append(-margins[i])
        for i in range(n):
          for j in range(i+1,n):
            for s in (-1,1):
              row=np.zeros(num)
              row[i*n+j]=s;row[j*n+i]=-s;row[-1]=-1
              rows.append(row);rhs.append(0)
        obj=np.zeros(num);obj[-1]=1
        sol=linprog(obj,A_ub=np.array(rows),b_ub=np.array(rhs),bounds=[(0,None)]*num,method='highs')
        assert sol.success,(n,f,sol.message)
        predicted=float(cycle_mean(f,margins))
        assert abs(sol.fun-predicted)<1e-7, (n,f,sol.fun,predicted)
        lp_count+=1
    print('INDEPENDENT_LP_OPTIMUM_PASS',lp_count)

if __name__=='__main__':run()
