from itertools import product, combinations
from math import comb
from collections import Counter

def compositions(n,k):
    if k==1:
        yield (n,); return
    for first in range(1,n-k+2):
        for rest in compositions(n-first,k-1):
            yield (first,)+rest

def graph(alpha,beta):
    A=[]; B=[]; clsA=[]; clsB=[]
    idx=0
    for i,a in enumerate(alpha,1):
        arr=list(range(idx,idx+a)); idx+=a; A+=arr; clsA.append(arr)
    for j,b in enumerate(beta,1):
        arr=list(range(idx,idx+b)); idx+=b; B+=arr; clsB.append(arr)
    n=idx
    adj=[set() for _ in range(n)]
    for i,arrA in enumerate(clsA,1):
        for j,arrB in enumerate(clsB,1):
            if j<=i:
                for u in arrA:
                    for v in arrB:
                        adj[u].add(v); adj[v].add(u)
    return adj,clsA,clsB

def has_perfect_matching_induced(adj,S):
    S=set(S)
    # bipartite by ids impossible to know, use recursion generic matching
    if len(S)%2: return False
    if not S: return True
    u=min(S)
    for v in sorted(adj[u]&S):
        T=S-{u,v}
        if has_perfect_matching_induced(adj,T): return True
    return False

def dominating(adj,S):
    S=set(S)
    return all(v in S or (adj[v]&S) for v in range(len(adj)))

def pd_brute(adj,S):
    return dominating(adj,S) and has_perfect_matching_induced(adj,S)

def char(alpha,beta,clsA,clsB,S):
    S=set(S); p=len(alpha)
    a=[sum(v in S for v in clsA[i]) for i in range(p)]
    b=[sum(v in S for v in clsB[i]) for i in range(p)]
    if sum(a)!=sum(b) or sum(a)==0: return False
    if a[-1]==0 or b[0]==0: return False
    A=B=0
    for i in range(p):
        A+=a[i]; B+=b[i]
        if A>B: return False
    return True

def dp_poly(alpha,beta):
    p=len(alpha)
    F={0:Counter({0:1})}  # deficit d -> coeff by total selected
    for i,(aa,bb) in enumerate(zip(alpha,beta)):
        G={}
        for d,poly in F.items():
            for a in range(aa+1):
                if i==p-1 and a==0: continue
                ca=comb(aa,a)
                for b in range(bb+1):
                    if i==0 and b==0: continue
                    nd=d+b-a
                    if nd<0: continue
                    cb=comb(bb,b)
                    gp=G.setdefault(nd,Counter())
                    for deg,c in poly.items():
                        gp[deg+a+b]+=c*ca*cb
        F=G
    return F.get(0,Counter())

graph_types=subset_checks=poly_checks=0
for n in range(2,11):
  for p in range(1,min(4,n//2)+1):
    for na in range(p,n-p+1):
      nb=n-na
      if nb<p: continue
      for alpha in compositions(na,p):
       for beta in compositions(nb,p):
        adj,clsA,clsB=graph(alpha,beta)
        graph_types+=1
        brute=Counter()
        for mask in range(1<<n):
            S=[v for v in range(n) if mask>>v&1]
            x=pd_brute(adj,S); y=char(alpha,beta,clsA,clsB,S)
            subset_checks+=1
            if x!=y:
                print('MISMATCH',alpha,beta,S,x,y); raise SystemExit(1)
            if x: brute[len(S)]+=1
        dp=dp_poly(alpha,beta)
        poly_checks += max(len(brute),len(dp),1)
        if brute!=dp:
            print('POLY MISMATCH',alpha,beta,brute,dp); raise SystemExit(1)
print('VERIFY_OK graph_types=%d subset_checks=%d polynomial_profiles=%d max_order=10'%(graph_types,subset_checks,poly_checks))
