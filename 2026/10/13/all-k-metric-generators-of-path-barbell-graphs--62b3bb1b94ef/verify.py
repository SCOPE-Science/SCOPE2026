from collections import deque, Counter
from math import comb

# Path-barbell B(p,q,l): K_p with distinguished a, K_q with distinguished b,
# plus an a-b path of length l whose internal vertices are new.
def graph(p,q,l):
    # X = p-1 left non-cut clique vertices, Y=q-1 right non-cut clique vertices.
    # path positions C[0]=a, C[l]=b.
    X=list(range(p-1))
    a=p-1
    internal=list(range(p,p+l-1)) if l>=2 else []
    b=p+l-1
    Y=list(range(p+l,p+q+l-1))
    n=p+q+l-1
    C=[a]+internal+[b]
    adj=[set() for _ in range(n)]
    L=X+[a]; R=[b]+Y
    for K in (L,R):
        for i,u in enumerate(K):
            for v in K[i+1:]:
                adj[u].add(v); adj[v].add(u)
    for u,v in zip(C,C[1:]):
        adj[u].add(v); adj[v].add(u)
    return adj,X,Y,C

def dists(adj):
    n=len(adj); D=[]
    for s in range(n):
        d=[-1]*n; d[s]=0; Q=deque([s])
        while Q:
            u=Q.popleft()
            for v in adj[u]:
                if d[v]<0:
                    d[v]=d[u]+1; Q.append(v)
        D.append(d)
    return D

def is_kgen(mask,D,k):
    n=len(D)
    for u in range(n):
        for v in range(u+1,n):
            c=0
            for w in range(n):
                if (mask>>w)&1 and D[u][w]!=D[v][w]:
                    c+=1
                    if c>=k: break
            if c<k: return False
    return True

def predicted(mask,X,Y,k):
    if k==1:
        ox=sum(((mask>>v)&1)==0 for v in X)
        oy=sum(((mask>>v)&1)==0 for v in Y)
        return ox<=1 and oy<=1
    if k==2:
        return all((mask>>v)&1 for v in X+Y)
    return False

def mul(A,B):
    C=Counter()
    for i,a in A.items():
        for j,b in B.items(): C[i+j]+=a*b
    return C

def formula(p,q,l,k):
    if k==1:
        A=Counter({p-2:p-1,p-1:1})
        B=Counter({q-2:q-1,q-1:1})
        P=Counter({j:comb(l+1,j) for j in range(l+2)})
        return mul(mul(A,B),P)
    if k==2:
        return Counter({p+q-2+j:comb(l+1,j) for j in range(l+2)})
    return Counter()

subset_checks=0
param=0
for p in range(3,6):
    for q in range(3,6):
        for l in range(1,4):
            adj,X,Y,C=graph(p,q,l); D=dists(adj); n=len(adj); param+=1
            for k in (1,2,3):
                got=Counter()
                for mask in range(1<<n):
                    truth=is_kgen(mask,D,k)
                    pred=predicted(mask,X,Y,k)
                    assert truth==pred,(p,q,l,k,mask,truth,pred)
                    if truth: got[mask.bit_count()]+=1
                    subset_checks+=1
                exp=formula(p,q,l,k)
                assert got==exp,(p,q,l,k,got,exp)
                if k==1:
                    assert min(got)==p+q-4
                    assert got[p+q-4]==(p-1)*(q-1)
                elif k==2:
                    assert min(got)==p+q-2
                    assert got[p+q-2]==1
                else:
                    assert not got
print(f'VERIFY_OK parameter_triples={param} k_values=3 subset_checks={subset_checks} max_order={5+5+3-1}')
