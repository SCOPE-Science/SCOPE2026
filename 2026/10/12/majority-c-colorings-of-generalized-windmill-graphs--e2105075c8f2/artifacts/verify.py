from itertools import product
from math import comb, factorial

def windmill(n,m):
    N=1+n*m
    adj=[set() for _ in range(N)]
    for b in range(n):
        vs=list(range(1+b*m,1+(b+1)*m))
        for v in vs:
            adj[0].add(v); adj[v].add(0)
        for i in range(m):
            for j in range(i+1,m):
                u,v=vs[i],vs[j]
                adj[u].add(v); adj[v].add(u)
    return adj

def majority(adj,col):
    for v,Nv in enumerate(adj):
        same=sum(1 for u in Nv if col[u]==col[v])
        if 2*same < len(Nv):
            return False
    return True

def structural(n,m,col):
    center=col[0]
    center_blades=0
    for b in range(n):
        vals=col[1+b*m:1+(b+1)*m]
        if len(set(vals)) != 1:
            return False
        if vals[0] == center:
            center_blades += 1
    return 2*center_blades >= n

def stirling2(n,k):
    if n==0 and k==0:
        return 1
    if n==0 or k==0 or k>n:
        return 0
    dp=[[0]*(k+1) for _ in range(n+1)]
    dp[0][0]=1
    for i in range(1,n+1):
        for j in range(1,min(i,k)+1):
            dp[i][j]=dp[i-1][j-1]+j*dp[i-1][j]
    return dp[n][k]

def formula_count(n,q):
    r=n//2
    return factorial(q)*sum(comb(n,t)*stirling2(t,q-1)
                            for t in range(q-1,r+1))

assignments_checked=0
parameter_cases=0
for n in range(1,5):
    for m in range(2,4):
        adj=windmill(n,m)
        N=len(adj)
        r=n//2
        for q in range(1,r+2):
            parameter_cases += 1
            count=0
            for col in product(range(q), repeat=N):
                if len(set(col)) != q:
                    continue
                assignments_checked += 1
                direct=majority(adj,col)
                form=structural(n,m,col)
                if direct != form:
                    raise AssertionError(("structure",n,m,q,col,direct,form))
                if direct:
                    count += 1
            expected=formula_count(n,q)
            if count != expected:
                raise AssertionError(("count",n,m,q,count,expected))

# Explicit optimal constructions and exact color use over a wider range.
constructions_checked=0
for n in range(1,31):
    r=n//2
    for m in range(2,11):
        adj=windmill(n,m)
        for q in range(1,r+2):
            # q-1 non-center blades get distinct non-center colors;
            # all remaining blades get the center color 0.
            col=[0]
            for b in range(n):
                c=b+1 if b < q-1 else 0
                col.extend([c]*m)
            if len(set(col)) != q or not majority(adj,col):
                raise AssertionError(("construction",n,m,q,col))
            constructions_checked += 1

print(
    "ALL CHECKS PASSED; "
    f"parameter_cases={parameter_cases}; "
    f"surjective_assignments_checked={assignments_checked}; "
    f"construction_cases={constructions_checked}; "
    "exhaustive_n=1..4,m=2..3"
)
