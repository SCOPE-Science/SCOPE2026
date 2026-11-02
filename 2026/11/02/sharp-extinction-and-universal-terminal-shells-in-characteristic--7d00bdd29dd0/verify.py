"""Independent finite checks for the branch-divisibility extinction theorem.
Run: python3 verify.py (standard Python only).
"""
from itertools import product

def rooted_tree(branches):
    # branches[v] gives child count for vertex v as vertices are processed.
    adj = [set()]
    parents = [-1]
    depths = [0]
    i = 0
    while i < len(adj):
        c = branches(i, depths[i])
        for _ in range(c):
            j = len(adj)
            adj.append({i}); adj[i].add(j)
            parents.append(i); depths.append(depths[i]+1)
        i += 1
    return [sorted(x) for x in adj], parents, depths

def mult(A, B, p):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n))%p for j in range(n)] for i in range(n)]

def rank(A,p):
    rows=[r[:] for r in A]
    n=len(rows); m=len(rows[0]); r=0
    for j in range(m):
        pivot=next((i for i in range(r,n) if rows[i][j]%p),None)
        if pivot is None:continue
        rows[r],rows[pivot]=rows[pivot],rows[r]
        inv=pow(rows[r][j],-1,p)
        rows[r]=[v*inv%p for v in rows[r]]
        for i in range(r+1,n):
            q=rows[i][j]%p
            if q:rows[i]=[(a-q*b)%p for a,b in zip(rows[i],rows[r])]
        r+=1
    return r

def exercise(label,adj,depth,p,bruteforce=False):
    n=len(adj);h=max(depth)
    A=[[int(j in adj[i]) for j in range(n)] for i in range(n)]
    X=[[int(i==j) for j in range(n)] for i in range(n)]
    ranks={0:n}
    for t in range(1,2*h+2):
        X=mult(A,X,p)
        ranks[t]=rank(X,p)
    assert ranks[2*h-1]==2,(label,ranks)
    assert ranks[2*h]==1,(label,ranks)
    assert ranks[2*h+1]==0,(label,ranks)
    if bruteforce:
        cnt=[0]*(2*h+2)
        for bits in product(range(p), repeat=n):
            v=bits
            for t in range(2*h+2):
                if all(x==0 for x in v):
                    cnt[t]+=1;break
                v=tuple(sum(v[j] for j in adj[i])%p for i in range(n))
            else:raise AssertionError((label,'failed extinction'))
        assert sum(cnt)==p**n
        assert cnt[2*h]==(p-1)*p**(n-2),(label,cnt)
        assert cnt[2*h+1]==(p-1)*p**(n-1),(label,cnt)
        assert sum(cnt[:2*h])==p**(n-2),(label,cnt)
        print('OK',label,'n',n,'p',p,'h',h,'ranks-tail',(2,1,0),'counts',cnt)
    else:
        print('OK',label,'n',n,'p',p,'h',h,'ranks-tail',(2,1,0))

cases=[]
for d,h,p,b in [(2,1,2,True),(2,2,2,True),(2,3,2,True),(2,4,2,False),
                 (4,1,2,True),(4,2,2,False),(3,1,3,True),(3,2,3,False),
                 (6,1,3,True)]:
    adj,parents,depth=rooted_tree(lambda i,l,d=d,h=h: d if l<h else 0)
    cases.append(('uniform_'+str(d)+'_'+str(h),adj,depth,p,b))
# Unequal-depth trees; each nonterminal vertex has p or 2p children.
for p in (2,3):
    adj,parents,depth=rooted_tree(lambda i,l,p=p: p if i==0 else (p if i==1 else 0))
    cases.append(('irregular_'+str(p)+'_2',adj,depth,p,True))
adj,parents,depth=rooted_tree(lambda i,l: 2 if i in (0,1,3) else 0)
cases.append(('irregular_2_3',adj,depth,2,True))
for label,adj,depth,p,b in cases:
    exercise(label,adj,depth,p,b)
# Nondivisible homogeneous branching keeps a nonzero state indefinitely.
for p,d,h in [(2,3,1),(2,3,2),(2,3,3),(3,2,1),(3,2,2)]:
    adj,parents,depth=rooted_tree(lambda i,l: d if l<h else 0)
    n=len(adj)
    # At p-adic characteristic not dividing d, nonnilpotency test by powers.
    A=[[int(j in adj[i]) for j in range(n)] for i in range(n)]
    X=[[int(i==j) for j in range(n)] for i in range(n)]
    for t in range(1,n+1):X=mult(A,X,p)
    assert any(any(v for v in row) for row in X),(p,d,h)
    print('OK_nonextinction',p,d,h,n)
print('BRANCH_DIVISIBILITY_VERIFY_OK',len(cases),'extinguishing cases, 5 nonextinguishing cases')
