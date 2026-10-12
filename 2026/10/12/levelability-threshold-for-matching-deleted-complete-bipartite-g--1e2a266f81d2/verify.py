#!/usr/bin/env python3
from itertools import combinations

def graph(a,b,t):
    n=a+b
    adj=[0]*n
    for i in range(a):
        for j in range(b):
            if i<t and j==i:
                continue
            u=i; v=a+j
            adj[u]|=1<<v; adj[v]|=1<<u
    return adj

def maximal_independent_sets(adj):
    n=len(adj); out=[]
    for S in range(1,1<<n):
        ok=True
        for u in range(n):
            if (S>>u)&1 and (adj[u]&S): ok=False; break
        if not ok: continue
        maximal=True
        for v in range(n):
            if not ((S>>v)&1) and (adj[v]&S)==0:
                maximal=False; break
        if maximal: out.append(S)
    return sorted(out)

def expected(a,b,t):
    A=sum(1<<i for i in range(a)); B=sum(1<<(a+j) for j in range(b)); sets=[]
    if t==0:
        sets=[A,B]
    else:
        if a>=2: sets.append(A)
        if b>=2: sets.append(B)
        for i in range(t): sets.append((1<<i)|(1<<(a+i)))
    return sorted(sets)

def weights(a,b,t):
    # explicit positive integer witness for exactly the classified positive cases
    if t==0:
        return [b]*a+[a]*b
    if t==1:
        if a==b==1: return [1,1]
        w=[1]*(a+b)
        if a>=2 and b>=2:
            w[0]=b-1; w[a]=a-1
        elif a==1:
            w[0]=b-1; w[a]=1
        else: # b==1
            w[0]=1; w[a]=a-1
        return w
    if (a,b,t)==(2,2,2):
        return [1,2,2,1]
    return None

def levelable_pred(a,b,t):
    return t<=1 or (a,b,t)==(2,2,2)

def set_weight(S,w):
    return sum(w[i] for i in range(len(w)) if (S>>i)&1)

cases=0; mis_count=0; nonlevel_cert=0
for a in range(1,7):
  for b in range(1,7):
    for t in range(min(a,b)+1):
      cases+=1
      adj=graph(a,b,t); mis=maximal_independent_sets(adj); exp=expected(a,b,t)
      assert mis==exp,(a,b,t,mis,exp)
      mis_count += len(mis)
      W=weights(a,b,t)
      if levelable_pred(a,b,t):
          assert W and min(W)>0
          vals={set_weight(S,W) for S in mis}
          assert len(vals)==1,(a,b,t,W,vals)
      else:
          # Here t>=2, a,b>=2 and a+b>4. A,B,P1,P2 are maximal;
          # P1,P2 are disjoint and their union is a strict subset of A union B,
          # which is the explicit obstruction used in the analytic proof.
          assert t>=2 and a>=2 and b>=2 and a+b>4
          A=(1<<a)-1; B=((1<<b)-1)<<a
          P1=(1<<0)|(1<<a); P2=(1<<1)|(1<<(a+1))
          assert all(S in mis for S in [A,B,P1,P2])
          assert (P1&P2)==0 and (P1|P2)!=(A|B) and ((P1|P2)&~(A|B))==0
          nonlevel_cert+=1
print(f"ALL CHECKS PASSED; parameter_cases={cases}; maximal_sets_checked={mis_count}; nonlevel_obstructions={nonlevel_cert}; a,b_range=1..6")
