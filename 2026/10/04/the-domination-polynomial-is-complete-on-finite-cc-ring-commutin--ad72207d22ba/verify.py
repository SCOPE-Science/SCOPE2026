#!/usr/bin/env python3
from math import comb
from itertools import combinations, product

def pmul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    while len(c)>1 and c[-1]==0:
        c.pop()
    return c

def pdiv_exact(a,b):
    a=a[:]
    q=[0]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b):
        if a[-1] % b[-1]:
            raise ValueError
        coeff=a[-1]//b[-1]
        deg=len(a)-len(b)
        q[deg]=coeff
        for j in range(len(b)):
            a[deg+j]-=coeff*b[j]
        while len(a)>1 and a[-1]==0:
            a.pop()
    if any(a):
        raise ValueError
    while len(q)>1 and q[-1]==0:
        q.pop()
    return q

def cyclotomics(N):
    phi={}
    for n in range(1,N+1):
        f=[-1]+[0]*(n-1)+[1]
        for d in range(1,n):
            if n%d==0:
                f=pdiv_exact(f,phi[d])
        phi[n]=f
    return phi

def cluster_domination_polynomial(profile):
    p=[1]
    for m in profile:
        p=pmul(p,[0]+[comb(m,k) for k in range(1,m+1)])
    return p

def shift_x_to_y_minus_1(p):
    q=[0]*len(p)
    for k,pk in enumerate(p):
        for j in range(k+1):
            q[j]+=pk*comb(k,j)*((-1)**(k-j))
    while len(q)>1 and q[-1]==0:
        q.pop()
    return q

def recover_profile(p):
    q=shift_x_to_y_minus_1(p)
    N=len(q)-1
    phis=cyclotomics(N)
    E={}
    rem=q[:]
    for d in range(1,N+1):
        count=0
        while True:
            try:
                rem2=pdiv_exact(rem,phis[d])
            except ValueError:
                break
            rem=rem2
            count+=1
        if count:
            E[d]=count
    assert rem in ([1],[-1])
    A={}
    for m in range(N,0,-1):
        exact=E.get(m,0)-sum(A.get(k*m,0) for k in range(2,N//m+1))
        if exact:
            assert exact>0
            A[m]=exact
    out=[]
    for m,a in A.items():
        out.extend([m]*a)
    return sorted(out),E

def integer_partitions(n, lo=1):
    if n==0:
        yield []
        return
    for x in range(lo,n+1):
        for rest in integer_partitions(n-x,x):
            yield [x]+rest

# Exhaustive collision check among cluster graphs of total order <= 12.
seen={}
count=0
for N in range(1,13):
    for profile in integer_partitions(N):
        profile=tuple(profile)
        P=tuple(cluster_domination_polynomial(profile))
        if P in seen:
            assert seen[P]==profile, (seen[P],profile)
        seen[P]=profile
        recovered,_=recover_profile(list(P))
        assert recovered==list(profile)
        count+=1

# Direct finite-ring example: upper triangular 2x2 matrices over F_p.
def mul(x,y,p):
    a,b,c=x; d,e,f=y
    return ((a*d)%p,(a*e+b*f)%p,(c*f)%p)

def commuting_graph_ut2(p):
    V=list(product(range(p),repeat=3))
    Z={(a,0,a) for a in range(p)}
    W=[x for x in V if x not in Z]
    adj=[set() for _ in W]
    for i,x in enumerate(W):
        for j in range(i+1,len(W)):
            y=W[j]
            if mul(x,y,p)==mul(y,x,p):
                adj[i].add(j); adj[j].add(i)
    return W,adj,Z

def component_sizes(adj):
    unseen=set(range(len(adj)))
    sizes=[]
    while unseen:
        root=next(iter(unseen))
        stack=[root]; comp={root}; unseen.remove(root)
        while stack:
            v=stack.pop()
            for u in adj[v]:
                if u in unseen:
                    unseen.remove(u); comp.add(u); stack.append(u)
        sizes.append(len(comp))
    return sorted(sizes)

def brute_dom_poly(adj):
    n=len(adj); out=[0]*(n+1)
    for mask in range(1<<n):
        S={i for i in range(n) if (mask>>i)&1}
        if all(v in S or bool(adj[v]&S) for v in range(n)):
            out[len(S)]+=1
    return out

ut_profiles={}
for p in (2,3):
    W,adj,Z=commuting_graph_ut2(p)
    prof=component_sizes(adj)
    expected=[p*(p-1)]*(p+1)
    assert prof==expected, (p,prof,expected)
    P=cluster_domination_polynomial(prof)
    rec,_=recover_profile(P)
    assert rec==prof
    ut_profiles[p]=(len(W),len(Z),prof)
    if p==2:
        assert brute_dom_poly(adj)==P

# Additional deterministic profile checks.
profiles=[
    [1],[2],[1,2],[2,3],[3,3,5],[1,2,4],[2,2,2],
    [4,6,9],[6,6,6,6],[2,5,5,8]
]
for prof in profiles:
    P=cluster_domination_polynomial(prof)
    rec,_=recover_profile(P)
    assert rec==sorted(prof)

print("VERIFY_OK")
print(f"cluster_profiles_exhaustive_total_order_le_12={count}")
print("UT2_F2_noncentral=6 center=2 components=3xK2 brute_polynomial=matched")
print("UT2_F3_noncentral=24 center=3 components=4xK6")
print("cyclotomic_profile_reconstruction=passed")
