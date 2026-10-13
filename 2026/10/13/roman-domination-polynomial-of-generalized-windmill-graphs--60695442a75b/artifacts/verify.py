from itertools import product

def conv(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def power(p,n):
    r=[1]
    for _ in range(n): r=conv(r,p)
    return r

def add(a,b,scale=1):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=scale*x
    while len(c)>1 and c[-1]==0:c.pop()
    return c

def shift(p,k): return [0]*k+p

def formula(n,m):
    A=[1,1,1]
    Am=power(A,m)
    Bm=power([1,1],m)
    xm=[0]*m+[1]
    Q=add(add(Am,Bm,-1),xm)
    term_center2=shift(power(A,n*m),2)
    term_center01=conv([1,1],power(Q,n))
    xnm=[0]*(n*m)+[1]
    return add(add(term_center2,term_center01),xnm,-1)

def graph(n,m):
    N=1+n*m
    adj=[set() for _ in range(N)]
    for v in range(1,N): adj[0].add(v); adj[v].add(0)
    for b in range(n):
        vs=list(range(1+b*m,1+(b+1)*m))
        for i in range(m):
            for j in range(i+1,m):
                u,v=vs[i],vs[j]; adj[u].add(v); adj[v].add(u)
    return adj

def is_rdf(lab,adj):
    return all(a!=0 or any(lab[u]==2 for u in adj[v]) for v,a in enumerate(lab))

def brute(n,m):
    adj=graph(n,m); N=len(adj); c=[0]*(2*N+1)
    for lab in product(range(3), repeat=N):
        if is_rdf(lab,adj): c[sum(lab)]+=1
    while len(c)>1 and c[-1]==0:c.pop()
    return c
pairs=[]; assignments=0
for n,m in [(2,1),(3,1),(4,1),(2,2),(3,2),(2,3)]:
    b=brute(n,m); f=formula(n,m); pairs.append((n,m)); assignments+=3**(1+n*m)
    assert b==f,(n,m,b,f)
    assert next(i for i,x in enumerate(f) if x)==2
    assert f[2]==1
    total=sum(f)
    Qtotal=3**m-2**m+1
    expected=3**(n*m)+2*(Qtotal**n)-1
    assert total==expected,(n,m,total,expected)
print('VERIFY_OK pairs=%s assignments=%d min_weight=2 min_count=1 total_formula_checked max_order=%d' % (pairs,assignments,max(1+n*m for n,m in pairs)))
