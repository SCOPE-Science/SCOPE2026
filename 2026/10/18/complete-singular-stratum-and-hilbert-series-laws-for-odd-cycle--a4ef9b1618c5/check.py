#!/usr/bin/env python3
"""Exact reproducibility checks for odd-cycle dumbbell edge hypersurfaces."""
from itertools import combinations, product
from math import comb
from collections import Counter


def data(a,b,ell):
    assert a>=3 and b>=3 and a%2 and b%2 and ell>=1
    names=[f'A{i}' for i in range(a)]+[f'B{i}' for i in range(b)]+[f'P{j}' for j in range(1,ell+1)]
    weights=[(-1)**i for i in range(a)]+[(-1)**(ell+1+i) for i in range(b)]+[2*(-1)**j for j in range(1,ell+1)]
    plus=[max(z,0) for z in weights]
    minus=[max(-z,0) for z in weights]
    return names,weights,plus,minus


def incidence(a,b,ell):
    edges=[]
    for i in range(a):edges.append((i,(i+1)%a))
    for i in range(b):edges.append((a+i,a+(i+1)%b))
    for j in range(ell):edges.append((a+b-1+j,a+b+j))
    # bridge endpoints should instead be a_0, new vertices, b_0
    path=[0]+list(range(a+b,a+b+ell-1))+[a]
    edges=edges[:a+b]+list(zip(path,path[1:]))
    return edges


def mon_value(exps,x):
    z=1
    for e,t in zip(exps,x):z*=t**e
    return z


def grad_mon(exps,x):
    arr=[]
    for i,e in enumerate(exps):
        if e==0:arr.append(0);continue
        v=e
        for j,p in enumerate(exps):
            v*=x[j]**(p-(j==i))
        arr.append(v)
    return arr


def hess_mon(exps,x):
    m=len(exps)
    h=[[0]*m for _ in range(m)]
    for i in range(m):
      for j in range(i,m):
        if i==j:
          coef=exps[i]*(exps[i]-1)
        else:coef=exps[i]*exps[j]
        if coef:
          for v in range(m):coef*=x[v]**(exps[v]-(i==v)-(j==v))
        h[i][j]=h[j][i]=coef
    return h


def rank_matrix(a):
    from fractions import Fraction
    b=[[Fraction(v) for v in row] for row in a]
    n=len(b);m=len(b[0]);r=0
    for c in range(m):
      pivot=next((i for i in range(r,n) if b[i][c]),None)
      if pivot is None:continue
      b[pivot],b[r]=b[r],b[pivot]
      z=b[r][c];b[r]=[x/z for x in b[r]]
      for i in range(r+1,n):
        if b[i][c]:
          w=b[i][c]
          b[i]=[u-w*v for u,v in zip(b[i],b[r])]
      r+=1
      if r==n:break
    return r


def minimal_critical_sets(exps):
    sq=[i for i,e in enumerate(exps) if e==2]
    simple=[i for i,e in enumerate(exps) if e==1]
    return [frozenset([i]) for i in sq]+[frozenset(c) for c in combinations(simple,2)]


def compositions(n,m):
    # tuples of m nonnegative integers summing to n
    if m==1:
      yield (n,);return
    for k in range(n+1):
      for tail in compositions(n-k,m-1):
        yield (k,)+tail


def case(a,b,ell):
    names,w,u,v=data(a,b,ell)
    m=len(names)
    assert m==a+b+ell
    assert sum(u)==sum(v)==(a+b)//2+ell
    edges=incidence(a,b,ell)
    assert len(edges)==m
    vertex_total=[0]*(a+b+ell-1)
    for (p,q),co in zip(edges,w):
      vertex_total[p]+=co;vertex_total[q]+=co
    assert vertex_total==[0]*len(vertex_total),vertex_total
    U=minimal_critical_sets(u)
    V=minimal_critical_sets(v)
    predicted=[s|t for s in U for t in V]
    assert len(predicted)==len(set(predicted))
    # The direct vanishing of the characteristic-zero Jacobian must agree
    # for every possible zero/nonzero coordinate support.
    for mask in range(1<<m):
      x=[0 if mask>>i&1 else 1 for i in range(m)]
      direct=(mon_value(u,x)==mon_value(v,x) and
              all(t==z for t,z in zip(grad_mon(u,x),grad_mon(v,x))))
      zeros={i for i,z in enumerate(x) if not z}
      support=any(s.issubset(zeros) for s in predicted)
      assert direct==support,(a,b,ell,mask,zeros,direct,support)
    counts=Counter(len(z) for z in predicted)
    r=ell//2;c=(a+b)//2
    if ell%2==0:
      assert all(counts[z]==v for z,v in {2:r*r,3:2*r*comb(c,2),4:comb(c,2)**2}.items()),counts
      factors=[(c,r+c-1,r+c)]*2
    else:
      assert all(counts[z]==v for z,v in {2:r*(r+1),
                      3:r*comb(c-1,2)+(r+1)*comb(c+1,2),
                      4:comb(c-1,2)*comb(c+1,2)}.items()),counts
      factors=[(c+1,r+c,r+c+1),(c-1,r+c-1,r+c)]
    numerator=Counter({0:1})
    for s,d,e in factors:
      nextnum=Counter()
      for deg,coeff in numerator.items():
        for shift,fac in [(0,1),(d,-s),(e,s-1)]:
          nextnum[deg+shift]+=coeff*fac
      numerator=nextnum
    sqU=[i for i,e in enumerate(u) if e==2]
    sqV=[i for i,e in enumerate(v) if e==2]
    smU=[i for i,e in enumerate(u) if e==1]
    smV=[i for i,e in enumerate(v) if e==1]
    for degree in range(0,7):
      actual=0
      for x in compositions(degree,m):
        # The defining radical monomial ideal is (Q_U V_{s_U-1})+(Q_V V_{s_V-1}).
        insideU=(all(x[i]>0 for i in sqU) and
                 sum(x[i]>0 for i in smU)>=len(smU)-1)
        insideV=(all(x[i]>0 for i in sqV) and
                 sum(x[i]>0 for i in smV)>=len(smV)-1)
        if not (insideU or insideV): actual+=1
      expected=sum(coef*comb(degree-shift+m-1,m-1)
                   for shift,coef in numerator.items() if degree>=shift)
      assert actual==expected,(a,b,ell,degree,actual,expected)
    for zero_size in sorted(counts):
      support=next(z for z in predicted if len(z)==zero_size)
      x=[0 if i in support else 1 for i in range(m)]
      h1=hess_mon(u,x);h2=hess_mon(v,x)
      h=[[h1[i][j]-h2[i][j] for j in range(m)] for i in range(m)]
      assert rank_matrix(h)==zero_size,(a,b,ell,support)
    return f'({a},{b},{ell}): {len(predicted)} components, codimensions {dict(sorted(counts.items()))}, Hilbert degrees 0..6 checked'


if __name__=='__main__':
    for args in [(3,3,1),(3,3,2),(3,3,3),(3,3,4),(3,5,2),(5,3,3),(5,5,2)]:
      print(case(*args))
    print('VERIFY_OK')
