#!/usr/bin/env python3
from math import comb


def conv(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    while len(c)>1 and c[-1]==0:
        c.pop()
    return c


def component_polys(m):
    E=[0]*(m+1)
    for k in range(2,m+1,2):
        E[k]=comb(m,k)
    B=[0]*(2*m+1)
    for k in range(1,m+1):
        B[2*k]=comb(m,k)**2
    return E,B


def parameters(q):
    m=q-1
    if q==2:
        return m,None,None
    if q%2==0:
        f=1
    elif q%4==1:
        f=2
    else:
        f=0
    c=(m-f)//2
    return m,f,c


def formula(q):
    m,f,c=parameters(q)
    if q==2:
        return [0]
    E,B=component_polys(m)
    P=[1]
    for _ in range(f): P=conv(P,E)
    for _ in range(c): P=conv(P,B)
    return P


def add(a,b,q):
    if q==4:
        return a^b
    return (a+b)%q


def mul(a,b,q):
    if q==4:
        # GF(4)=F_2[t]/(t^2+t+1), bits encode c0+c1*t.
        a0,a1=a&1,(a>>1)&1
        b0,b1=b&1,(b>>1)&1
        c0=(a0*b0)^(a1*b1)
        c1=(a0*b1)^(a1*b0)^(a1*b1)
        return c0|(c1<<1)
    return (a*b)%q


def actual_graph(q):
    V=[(a,b) for a in range(1,q) for b in range(1,q)]
    adj=[set() for _ in V]
    for i,x in enumerate(V):
        for j in range(i+1,len(V)):
            y=V[j]
            dot=add(mul(x[0],y[0],q),mul(x[1],y[1],q),q)
            if dot==0:
                adj[i].add(j); adj[j].add(i)
    return V,adj


def has_pm(S,adj):
    S=frozenset(S); memo={}
    def rec(T):
        if not T: return True
        if T in memo: return memo[T]
        v=next(iter(T))
        for u in adj[v].intersection(T):
            if rec(T-{v,u}):
                memo[T]=True; return True
        memo[T]=False; return False
    return rec(S)


def brute_poly(q):
    V,adj=actual_graph(q)
    n=len(V); out=[0]*(n+1)
    for mask in range(1<<n):
        k=mask.bit_count()
        if k==0 or k%2: continue
        S={i for i in range(n) if (mask>>i)&1}
        if all(v in S or bool(adj[v]&S) for v in range(n)) and has_pm(S,adj):
            out[k]+=1
    while len(out)>1 and out[-1]==0: out.pop()
    return out


def comps(q):
    V,adj=actual_graph(q)
    unseen=set(range(len(V))); sizes=[]
    while unseen:
        root=next(iter(unseen)); unseen.remove(root); stack=[root]; C={root}
        while stack:
            v=stack.pop()
            for u in adj[v]:
                if u in unseen:
                    unseen.remove(u); C.add(u); stack.append(u)
        sizes.append(len(C))
    return sorted(sizes)

for q in (3,4,5):
    assert brute_poly(q)==formula(q), q

# Direct graph component profiles for prime fields and GF(4).
assert comps(3)==[4]
assert comps(4)==[3,6]
assert comps(5)==[4,4,8]

# Algebraic polynomial/reconstruction checks for further prime powers.
for q in (7,8,9,11,13,16):
    P=formula(q)
    m,f,c=parameters(q)
    nz=[i for i,a in enumerate(P) if a]
    assert min(nz)==m+f
    # Total number of paired dominating sets.
    expected=(2**(m-1)-1)**f * (comb(2*m,m)-1)**c
    assert sum(P)==expected
    # Recover q from the polynomial alone.
    deg=max(nz); lead=P[deg]
    if lead>1:
        mr=lead
        assert deg==mr*mr-1
    else:
        mr=int(deg**0.5)
        assert mr*mr==deg
    assert mr+1==q

print('VERIFY_OK')
print('brute_actual_fields=q3,q4,q5')
print('largest_global_subset_enumeration=2^16')
print('component_profiles=q3:K2,2;q4:K3+K3,3;q5:2K4+K4,4')
print('formula_and_reconstruction_checks=q7,q8,q9,q11,q13,q16')
