from itertools import product, combinations
from collections import deque, Counter

def mat_vec(A, v, p):
    return tuple(sum(A[i][j]*v[j] for j in range(len(v))) % p for i in range(len(A)))

def mat_mul(A, B, p):
    n=len(A)
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(n)) % p for j in range(n)) for i in range(n))

def mat_id(n):
    return tuple(tuple(1 if i==j else 0 for j in range(n)) for i in range(n))

def mat_pow(A, k, p):
    R=mat_id(len(A))
    while k:
        if k&1:
            R=mat_mul(R,A,p)
        A=mat_mul(A,A,p)
        k//=2
    return R

def add(u,v,p):
    return tuple((a+b)%p for a,b in zip(u,v))

def neg(u,p):
    return tuple((-a)%p for a in u)

def group_data(p,A,m):
    n=len(A)
    I=mat_id(n)
    assert mat_pow(A,m,p)==I
    assert all(mat_pow(A,k,p)!=I for k in range(1,m))
    powers=[mat_pow(A,k,p) for k in range(m)]
    vecs=list(product(range(p), repeat=n))
    elems=[(v,k) for v in vecs for k in range(m)]
    e=((0,)*n,0)
    def mul(x,y):
        v,i=x
        w,j=y
        return (add(v,mat_vec(powers[i],w,p),p),(i+j)%m)
    def inv(x):
        v,i=x
        mi=(-i)%m
        return (mat_vec(powers[mi],neg(v,p),p),mi)
    return elems,e,mul,inv

def generated(S, e, mul, inv):
    gens=list(S)+[inv(x) for x in S]
    seen={e}
    q=deque([e])
    while q:
        x=q.popleft()
        for g in gens:
            y=mul(x,g)
            if y not in seen:
                seen.add(y)
                q.append(y)
    return seen

def conjugacy_classes(elems,mul,inv):
    unseen=set(elems)
    classes=[]
    while unseen:
        x=next(iter(unseen))
        C=frozenset(mul(mul(g,x),inv(g)) for g in elems)
        classes.append(C)
        unseen-=C
    return classes

def graph_for(p,A,m):
    elems,e,mul,inv=group_data(p,A,m)
    classes=conjugacy_classes(elems,mul,inv)
    trivial=next(C for C in classes if C==frozenset({e}))
    verts=[C for C in classes if C!=trivial]
    adj=set()
    for i,j in combinations(range(len(verts)),2):
        ok=True
        for x in verts[i]:
            for y in verts[j]:
                if len(generated([x,y],e,mul,inv))!=len(elems):
                    ok=False
                    break
            if not ok:
                break
        if ok:
            adj.add((i,j))
    deg=[0]*len(verts)
    for i,j in adj:
        deg[i]+=1
        deg[j]+=1
    active=[i for i,d in enumerate(deg) if d]
    return len(elems), verts, adj, deg, active

cases=[
    ("S3",3,((2,),),2,(1,1)),
    ("AGL15",5,((2,),),4,(1,2)),
    ("F2^3:C7",2,((0,0,1),(1,0,1),(0,1,0)),7,(1,6)),
    ("F7^2:C3-multfree",7,((2,0),(0,4)),3,(12,2)),
    ("F7^2:C3-repeated",7,((2,0),(0,2)),3,(0,0)),
]

for name,p,A,m,parts in cases:
    order,verts,adj,deg,active=graph_for(p,A,m)
    if parts==(0,0):
        assert not adj and not active
    else:
        a,b=parts
        assert len(active)==a+b
        assert len(adj)==a*b
        if a==b==1:
            u,v=next(iter(adj))
            left={u}
            right={v}
        else:
            left={i for i in active if deg[i]==b}
            right=set(active)-left
        assert len(left)==a and len(right)==b
        for i,j in combinations(active,2):
            should=(i in left and j in right) or (i in right and j in left)
            assert (((min(i,j),max(i,j)) in adj) == should)
    print(name, order, len(verts), len(adj), len(active))

print("VERIFY_OK")
