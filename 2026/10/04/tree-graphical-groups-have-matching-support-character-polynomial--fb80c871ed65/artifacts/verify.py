from itertools import product
from collections import Counter

def rank_mod(A,q):
    A=[row[:] for row in A]
    m=len(A); n=len(A[0]) if A else 0
    r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]%q),None)
        if p is None:
            continue
        A[r],A[p]=A[p],A[r]
        inv=pow(A[r][c]%q,-1,q)
        A[r]=[(inv*x)%q for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%q:
                z=A[i][c]%q
                A[i]=[(A[i][j]-z*A[r][j])%q for j in range(n)]
        r+=1
    return r

def matching_number(n,edges):
    E=list(edges)
    best=0
    def rec(i,used,count):
        nonlocal best
        if count+(len(E)-i)<=best:
            return
        if i==len(E):
            best=max(best,count); return
        rec(i+1,used,count)
        a,b=E[i]
        if a not in used and b not in used:
            rec(i+1,used|{a,b},count+1)
    rec(0,set(),0)
    return best

def support_poly(n,edges,q):
    H=Counter()
    m=len(edges)
    for mask in range(1<<m):
        S=[edges[j] for j in range(m) if (mask>>j)&1]
        mu=matching_number(n,S)
        H[mu]+=(q-1)**len(S)
    return H

def poly_add(A,B):
    C=Counter(A); C.update(B); return C

def poly_scale(A,c,shift=0):
    return Counter({k+shift:c*v for k,v in A.items() if c*v})

def poly_mul(A,B):
    C=Counter()
    for i,a in A.items():
        for j,b in B.items():
            C[i+j]+=a*b
    return C

def rooted_recursion(n,edges,q,root=0):
    adj=[[] for _ in range(n)]
    for a,b in edges:
        adj[a].append(b); adj[b].append(a)
    def dfs(v,parent):
        children=[w for w in adj[v] if w!=parent]
        if not children:
            return Counter({0:1}), Counter()
        states=[dfs(w,v) for w in children]
        P0=Counter({0:1})
        total=Counter({0:1})
        for A,B in states:
            P0=poly_mul(P0,poly_add(A,poly_scale(B,q)))
            total=poly_mul(total,poly_add(A,B))
        total=poly_scale(total,q**len(children))
        diff=Counter(total)
        for k,vv in P0.items():
            diff[k]-=vv
            if diff[k]==0:
                del diff[k]
        assert all(vv>=0 for vv in diff.values())
        P1=poly_scale(diff,1,1)
        return P0,P1
    A,B=dfs(root,None)
    return poly_add(A,B)

def direct_rank_hist(n,edges,q):
    H=Counter()
    for vals in product(range(q),repeat=len(edges)):
        M=[[0]*n for _ in range(n)]
        supp=[]
        for (a,b),x in zip(edges,vals):
            if x:
                supp.append((a,b))
            M[a][b]=x%q
            M[b][a]=(-x)%q
        rr=rank_mod(M,q)
        mu=matching_number(n,supp)
        assert rr==2*mu,(n,edges,q,vals,rr,mu)
        H[rr//2]+=1
    return H

trees={
    "path5":(5,[(0,1),(1,2),(2,3),(3,4)]),
    "star4":(5,[(0,1),(0,2),(0,3),(0,4)]),
    "branched6":(6,[(0,1),(0,2),(1,3),(1,4),(2,5)]),
    "binary7":(7,[(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)]),
}
for q in (3,5):
    for name,(n,E) in trees.items():
        H=direct_rank_hist(n,E,q)
        S=support_poly(n,E,q)
        R=rooted_recursion(n,E,q,0)
        assert H==S==R,(q,name,H,S,R)
        order=q**(n+len(E))
        chars={i:q**(n-2*i)*c for i,c in H.items()}
        assert sum(chars[i]*(q**i)**2 for i in chars)==order
        print({
            "q":q,
            "tree":name,
            "rank_support_coeffs":dict(sorted(H.items())),
            "character_counts":dict(sorted(chars.items())),
        })
print("VERIFY_OK")
