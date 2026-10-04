#!/usr/bin/env python3
from itertools import product
from math import comb

def ball(n,t,kp,km):
    vals=range(-km,kp+1)
    return {v for v in product(vals, repeat=n) if sum(a!=0 for a in v)<=t}

def local(s,kp,km):
    K=kp+km
    if s==0:
        return {(0,0):1,(1,1):K}
    if abs(s)>K:
        return {}
    alpha=int(-km<=s<=kp)
    beta=int(-km<=-s<=kp)
    gamma=K+1-abs(s)-alpha-beta
    out={}
    if alpha: out[(1,0)]=alpha
    if beta: out[(0,1)]=beta
    if gamma: out[(1,1)]=gamma
    return out

def formula(d,t,kp,km):
    dp={(0,0):1}
    for s in d:
        nxt={}
        for (a,b),c in dp.items():
            for (u,v),w in local(s,kp,km).items():
                aa,bb=a+u,b+v
                if aa<=t and bb<=t:
                    nxt[(aa,bb)]=nxt.get((aa,bb),0)+c*w
        dp=nxt
        if not dp: break
    return sum(dp.values())

def direct(B,d):
    return sum(tuple(e[i]-d[i] for i in range(len(d))) in B for e in B)

def V(K,n,t):
    return sum(comb(n,j)*K**j for j in range(0,min(n,t)+1))

def main():
    displacements=0
    parameter_sets=0
    for n in range(1,5):
      for t in range(1,n+1):
       for kp in range(1,3):
        for km in range(0,kp+1):
         parameter_sets+=1
         K=kp+km
         B=ball(n,t,kp,km)
         best=0
         for d in product(range(-K,K+1), repeat=n):
            got=direct(B,d)
            want=formula(d,t,kp,km)
            assert got==want,(n,t,kp,km,d,got,want)
            if any(d): best=max(best,got)
            displacements+=1
         target=K*V(K,n-1,t-1)
         assert best==target,(n,t,kp,km,best,target)
    support_one=0
    for n in range(1,31):
      for t in range(1,n+1):
       for kp in range(1,6):
        for km in range(0,kp+1):
         K=kp+km
         for s in range(-K,K+1):
          if s==0: continue
          d=(s,)+(0,)*(n-1)
          got=formula(d,t,kp,km)
          want=(K+1-abs(s))*V(K,n-1,t-1)
          assert got==want,(n,t,kp,km,s,got,want)
          support_one+=1
    print(f"VERIFY_OK exhaustive_displacements={displacements} parameter_sets={parameter_sets} support_one_grid={support_one}")
if __name__=='__main__': main()
