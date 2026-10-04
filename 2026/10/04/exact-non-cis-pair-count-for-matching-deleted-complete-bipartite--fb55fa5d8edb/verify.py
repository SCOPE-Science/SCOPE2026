from itertools import combinations


def graph(a,b,t):
    A=list(range(a)); B=list(range(a,a+b)); n=a+b
    deleted={(i,a+i) for i in range(t)}
    E=set()
    for i in A:
        for j0 in range(b):
            j=a+j0
            if (i,j) not in deleted:
                E.add((i,j))
    adj=[set() for _ in range(n)]
    for u,v in E:
        adj[u].add(v); adj[v].add(u)
    return adj


def is_clique(S,adj):
    S=set(S)
    return all(v in adj[u] for u,v in combinations(S,2))

def is_stable(S,adj):
    S=set(S)
    return all(v not in adj[u] for u,v in combinations(S,2))

def maximal_sets(adj,pred):
    n=len(adj); out=[]
    for mask in range(1,1<<n):
        S=[i for i in range(n) if mask>>i&1]
        if not pred(S,adj): continue
        SS=set(S)
        if all(not pred(S+[v],adj) for v in range(n) if v not in SS):
            out.append(frozenset(S))
    return out

def defect(a,b,t):
    adj=graph(a,b,t)
    C=maximal_sets(adj,is_clique)
    S=maximal_sets(adj,is_stable)
    return sum(1 for c in C for s in S if c.isdisjoint(s)), C, S

def formula(a,b,t):
    return t*((a-1)*(b-1)-t+1)

def classified_cis(a,b,t):
    return t==0 or min(a,b)==1 or (a,b,t)==(2,2,2)

def classified_almost(a,b,t):
    return (a,b,t)==(2,2,1)

cases=0
subset_tests=0
for a in range(1,6):
  for b in range(1,6):
    for t in range(min(a,b)+1):
      d,C,S=defect(a,b,t)
      f=formula(a,b,t)
      assert d==f,(a,b,t,d,f,C,S)
      assert (d==0)==classified_cis(a,b,t),(a,b,t,d)
      assert (d==1)==classified_almost(a,b,t),(a,b,t,d)
      cases+=1
      subset_tests += (1<<(a+b))-1

for n in range(2,7):
    d,_,_=defect(n,n,n)
    assert d==n*(n-1)*(n-2),(n,d)

print(f"ALL CHECKS PASSED; parameter_cases={cases}; subset_candidates_per_family_sum={subset_tests}; a,b_range=1..5; crown_n_range=2..6")
