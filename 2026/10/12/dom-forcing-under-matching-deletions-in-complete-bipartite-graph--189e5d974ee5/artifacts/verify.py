from itertools import combinations

def adj_graph(m,n,t):
    N=m+n; A=[set() for _ in range(N)]
    for i in range(m):
        for j in range(n):
            if i<t and j==i: continue
            A[i].add(m+j); A[m+j].add(i)
    return A

def connected(A):
    seen={0}; stack=[0]
    while stack:
        u=stack.pop()
        for v in A[u]:
            if v not in seen: seen.add(v); stack.append(v)
    return len(seen)==len(A)

def dom(A,S):
    S=set(S)
    return all(v in S or bool(A[v]&S) for v in range(len(A)))

def zf(A,S):
    B=set(S)
    while True:
        x=None
        for u in tuple(B):
            W=A[u]-B
            if len(W)==1:
                x=next(iter(W)); break
        if x is None: break
        B.add(x)
    return len(B)==len(A)

def expected(m,n,t):
    N=m+n
    z=N-2-min(t,2)
    exc=(m,n,t)==(2,2,1) or (m==2 and t==2 and n>=3) or (m==3 and n==3 and t in (2,3))
    return z,z+int(exc)

def exact(m,n,t):
    A=adj_graph(m,n,t); N=m+n
    z=fd=None; zcnt=fdcnt=0
    for k in range(N+1):
        for S in combinations(range(N),k):
            q=zf(A,S)
            if q:
                if z is None: z=k
                if z==k: zcnt+=1
                if dom(A,S):
                    if fd is None: fd=k
                    if fd==k: fdcnt+=1
        if z is not None and fd is not None and k>=max(z,fd): break
    return z,fd,zcnt,fdcnt

profiles=0
for m in range(2,6):
    for n in range(m,8):
        for t in range(m+1):
            A=adj_graph(m,n,t)
            if not connected(A):
                assert (m,n,t)==(2,2,2)
                continue
            if m+n<=10:
                got=exact(m,n,t)[:2]
                exp=expected(m,n,t)
                assert got==exp,(m,n,t,got,exp)
                profiles+=1

# Validate explicit witnesses used in the proof over a larger range.
def witness(m,n,t):
    N=m+n
    if t==0:
        W={0,m+0}
        return set(range(N))-W
    if t==1:
        if m==2 and n>=3:
            W={0,m+0,m+1}
        else:
            W={0,1,m+1}
        return set(range(N))-W
    # t >= 2
    if m==2:
        # one-above-minimum dom-forcing witness; minimum ZF witnesses cannot dominate
        return {0} | {m+j for j in range(n) if j not in (1,2 if n>=3 else 1)}
    if m==3 and n==3:
        return {0,1,m+0}
    if t==2:
        W={0,1,m+1,m+3}
    else:
        W={1,2,m+2,m+3}
    return set(range(N))-W

wchecks=0
for m in range(2,13):
    for n in range(m,16):
        for t in range(m+1):
            A=adj_graph(m,n,t)
            if not connected(A): continue
            z,fd=expected(m,n,t)
            S=witness(m,n,t)
            # exception (2,2,1): witness formula above is not intended
            if (m,n,t)==(2,2,1):
                S={0, 1}
            assert len(S)==fd,(m,n,t,len(S),fd,S)
            assert zf(A,S),(m,n,t,'not zf',S)
            assert dom(A,S),(m,n,t,'not dom',S)
            wchecks+=1
print(f'ALL CHECKS PASSED; exhaustive_connected_profiles={profiles}; witness_profiles={wchecks}')
