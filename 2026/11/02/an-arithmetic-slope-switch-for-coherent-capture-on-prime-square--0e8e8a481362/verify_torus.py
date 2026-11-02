#!/usr/bin/env python3
"""Exact finite-field Krylov and Fourier-orbit sanity checks for odd-prime toroidal absorbers."""
from collections import Counter

def orbits(p):
    todo=set(range(p*p)); result=[]
    while todo:
        q=next(iter(todo)); a,b=divmod(q,p)
        orb={(u*a%p)*p+(v*b%p) for u in (1,-1) for v in (1,-1)} | {(u*b%p)*p+(v*a%p) for u in (1,-1) for v in (1,-1)}
        todo-=orb
        result.append(orb)
    return result

def spectral_rank(p,r):
    return sum(len({(k//p+r*(k%p))%p for k in orb}) for orb in orbits(p))

def formula(p,r):
    if r%p in (0,1,p-1): return p*(p+1)//2
    if (r*r+1)%p==0: return p*p-3*(p-1)//4
    return p*p-3*(p-1)//2

def krylov_rank(p,r,prime=1000003):
    n=p*p
    adj=[]
    for i in range(p):
      for j in range(p):
        adj.append((((i+1)%p)*p+j,((i-1)%p)*p+j,i*p+(j+1)%p,i*p+(j-1)%p))
    row=[]
    for t in range(p):
        v=[0]*n; v[t*p+(r*t)%p]=1; row.append(v)
    piv={}
    for k in range(n+1):
        increase=0
        for v in row:
            w=v[:]
            while True:
                a=next((i for i,x in enumerate(w) if x),None)
                if a is None: break
                if a not in piv:
                    inv=pow(w[a],-1,prime)
                    piv[a]=[(x*inv)%prime for x in w]
                    increase+=1
                    break
                lead=w[a]; pv=piv[a]
                for i in range(a,n): w[i]=(w[i]-lead*pv[i])%prime
        if increase==0: return len(piv),k
        nxt=[]
        for v in row:
            nxt.append([sum(v[j] for j in adj[i])%prime for i in range(n)])
        row=nxt
    raise AssertionError('Krylov did not close')

if __name__=='__main__':
  for p in (3,5,7,11,13,17,19,23,29):
    for r in range(p):
      assert spectral_rank(p,r)==formula(p,r),(p,r,spectral_rank(p,r),formula(p,r))
    print('Fourier-orbit formula OK p=',p)
  for p in (5,7,11,13):
    choices=sorted(set([0,1,2,next((r for r in range(2,p-1) if (r*r+1)%p==0),2)]))
    for r in choices:
      expected=formula(p,r)
      results=[]
      for q in (1000003,1000033):
        rank,k=krylov_rank(p,r,q)
        assert rank==expected,(p,r,q,expected,rank,k)
        results.append((q,rank,k))
      print('Krylov',p,r,results,'expected',expected)
  print('ALL CHECKS PASSED')
