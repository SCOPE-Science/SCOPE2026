#!/usr/bin/env python3
from itertools import product, combinations

def vertices(q,n):
    return [v for v in product(range(q), repeat=n) if any(v) and 0 in v]

def dot(x,y,q):
    return sum(a*b for a,b in zip(x,y)) % q

def graph(q,n):
    V=vertices(q,n)
    A=[set() for _ in V]
    for i,x in enumerate(V):
        for j in range(i+1,len(V)):
            if dot(x,V[j],q)==0:
                A[i].add(j); A[j].add(i)
    return V,A

def total_dominates(S,A):
    S=set(S)
    return all(A[v] & S for v in range(len(A)))

def perfect_matching(S,A):
    S=frozenset(S)
    if not S: return True
    if len(S)%2: return False
    v=next(iter(S))
    for u in (A[v] & S):
        if perfect_matching(S-{v,u},A):
            return True
    return False

def exact_minima(q,n):
    V,A=graph(q,n)
    gt=None
    gp=None
    for k in range(2,7):
        if gt is None:
            for S in combinations(range(len(V)),k):
                if total_dominates(S,A):
                    gt=k
                    break
        if gp is None and k%2==0:
            for S in combinations(range(len(V)),k):
                if total_dominates(S,A) and perfect_matching(S,A):
                    gp=k
                    break
        if gt is not None and gp is not None:
            break
    return len(V),gt,gp

rows=[]
for q,n in [(2,3),(2,4),(2,5),(3,3),(3,4),(5,3)]:
    N,gt,gp=exact_minima(q,n)
    m=min(n,q+1)
    assert gt==m,(q,n,gt,m)
    assert gp==2*((m+1)//2),(q,n,gp,m)
    rows.append((q,n,N,gt,gp))

def projective_reps_plane(q,u,v,n):
    # One representative for each line in span(u,v):
    # u plus a*u+v for a in F_q.
    D=[u]
    for a in range(q):
        D.append(tuple((a*u[i]+v[i])%q for i in range(n)))
    return D

def check_D(q,n,D,paired):
    V=vertices(q,n)
    assert len(D)==len(set(D))
    assert all(d in V for d in D)
    for x in V:
        assert any(x!=d and dot(x,d,q)==0 for d in D), ("not total",q,n,x)
    if paired:
        # Backtracking on the selected vectors.
        A=[[i!=j and dot(D[i],D[j],q)==0 for j in range(len(D))] for i in range(len(D))]
        def pm(S):
            if not S:return True
            i=S[0]
            return any(A[i][j] and pm([k for k in S[1:] if k!=j]) for j in S[1:])
        assert pm(list(range(len(D)))), ("no matching",q,n,D)

# Odd-field anisotropic-plane paired constructions beyond the dimension threshold.
for q,n,c,a,b in [(3,5,1,1,0),(5,7,2,1,1)]:
    u=(1,0,0)+(0,)*(n-3)
    v=(0,a,b)+(0,)*(n-3)
    D=projective_reps_plane(q,u,v,n)
    assert (-c)%q not in {(x*x)%q for x in range(q)}
    assert (a*a+b*b)%q==c%q
    check_D(q,n,D,paired=True)

# Even-characteristic explicit q=2 constructions.
# n=4 exceptional paired witness.
D4=[(0,1,0,0),(0,0,1,0),(0,0,0,1),(0,0,1,1)]
check_D(2,4,D4,paired=True)
# n=5: totally isotropic plane reps plus e5.
r1=(1,1,0,0,0); r2=(0,0,1,1,0)
D5=projective_reps_plane(2,r1,r2,5)+[(0,0,0,0,1)]
check_D(2,5,D5,paired=True)

print("VERIFY_OK")
for row in rows:
    print("q=%d n=%d vertices=%d gamma_t=%d gamma_pr=%d"%row)
print("odd_field_projective_constructions=q3n5,q5n7_passed")
print("even_characteristic_paired_constructions=q2n4,q2n5_passed")
