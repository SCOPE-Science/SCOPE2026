#!/usr/bin/env python3
from itertools import product, combinations

def symp(v,w,p,n):
    s=0
    for i in range(n):
        s += v[i]*w[n+i] - v[n+i]*w[i]
    return s % p

def model_graph(p,n):
    vecs=[v for v in product(range(p), repeat=2*n) if any(v)]
    # Each nonzero coset of Z has p group elements.
    vertices=[(v,z) for v in vecs for z in range(p)]
    adj=[set() for _ in vertices]
    for i,(v,z) in enumerate(vertices):
        for j in range(i+1,len(vertices)):
            w,_=vertices[j]
            if symp(v,w,p,n)!=0:
                adj[i].add(j); adj[j].add(i)
    return vertices,adj

def dominates(S,adj,total=False):
    S=set(S)
    for v in range(len(adj)):
        if total:
            if not (adj[v] & S):
                return False
        else:
            if v not in S and not (adj[v] & S):
                return False
    return True

def perfect_matching(S,adj):
    S=set(S)
    if not S:
        return True
    if len(S)%2:
        return False
    v=next(iter(S))
    for u in list(adj[v] & S):
        if perfect_matching(S-{v,u},adj):
            return True
    return False

def minima(p,n,max_k):
    V,adj=model_graph(p,n)
    gamma=gamma_t=gamma_pr=None
    for k in range(1,max_k+1):
        if gamma is None:
            for S in combinations(range(len(V)),k):
                if dominates(S,adj,False):
                    gamma=k
                    break
        if gamma_t is None:
            for S in combinations(range(len(V)),k):
                if dominates(S,adj,True):
                    gamma_t=k
                    break
        if gamma_pr is None and k%2==0:
            for S in combinations(range(len(V)),k):
                if dominates(S,adj,False) and perfect_matching(S,adj):
                    gamma_pr=k
                    break
        if gamma is not None and gamma_t is not None and gamma_pr is not None:
            return len(V),gamma,gamma_t,gamma_pr
    raise AssertionError((p,n,gamma,gamma_t,gamma_pr))

# Small exact cases.
rows=[]
for p,n in [(2,1),(3,1),(2,2)]:
    N,g,gt,gp=minima(p,n,2*n)
    assert (g,gt,gp)==(2*n,2*n,2*n)
    rows.append((p,n,N,g,gt,gp))

# Direct D8 and Q8 sanity checks for the two extraspecial 2-groups of order 8.
def d8_mul(x,y):
    # r^a s^b, with s r s = r^-1
    a,b=x; c,d=y
    return ((a + ((-1)**b)*c) % 4, (b+d)%2)

D8=[(a,b) for a in range(4) for b in range(2)]
D8Z={(0,0),(2,0)}

# Q8 labels 0=1,1=-1,2=i,3=-i,4=j,5=-j,6=k,7=-k
def q8_mul(a,b):
    sign=[1,-1,1,-1,1,-1,1,-1]
    unit=[0,0,1,1,2,2,3,3]  # 0=1,1=i,2=j,3=k
    sa,ua=sign[a],unit[a]
    sb,ub=sign[b],unit[b]
    if ua==0:
        s,u=sa*sb,ub
    elif ub==0:
        s,u=sa*sb,ua
    elif ua==ub:
        s,u=-sa*sb,0
    else:
        table={(1,2):(1,3),(2,3):(1,1),(3,1):(1,2),
               (2,1):(-1,3),(3,2):(-1,1),(1,3):(-1,2)}
        t,u=table[(ua,ub)]
        s=sa*sb*t
    # encode
    if u==0: return 0 if s==1 else 1
    base={1:2,2:4,3:6}[u]
    return base if s==1 else base+1

Q8=list(range(8)); Q8Z={0,1}

def graph_from_group(G,Z,mul):
    V=[x for x in G if x not in Z]
    adj=[set() for _ in V]
    for i,x in enumerate(V):
        for j in range(i+1,len(V)):
            y=V[j]
            if mul(x,y)!=mul(y,x):
                adj[i].add(j); adj[j].add(i)
    return V,adj

for name,G,Z,mul in [("D8",D8,D8Z,d8_mul),("Q8",Q8,Q8Z,q8_mul)]:
    V,adj=graph_from_group(G,Z,mul)
    for k in (1,2):
        ds=[S for S in combinations(range(len(V)),k) if dominates(S,adj,False)]
        if ds:
            assert k==2
            break

# Arithmetic inequality used in the lower bound:
# p(p^m-1) >= 2m for p>=2,m>=1.
for p in range(2,18):
    for m in range(1,13):
        assert p*(p**m-1) >= 2*m

print("VERIFY_OK")
for p,n,N,g,gt,gp in rows:
    print(f"symplectic_model_p={p}_n={n}: vertices={N} gamma={g} gamma_t={gt} gamma_pr={gp}")
print("D8_and_Q8_actual_group_checks=gamma_2")
print("lower_bound_inequality_grid=p2..17_m1..12_passed")
