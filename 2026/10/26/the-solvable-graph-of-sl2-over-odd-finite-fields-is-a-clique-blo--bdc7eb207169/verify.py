#!/usr/bin/env python3
"""Exact finite-field/graph check for the stated Lie solvable-graph theorem.
Only the Python standard library is needed. Tested prime fields: 3 and 5.
"""
from itertools import product, combinations
from math import comb
from collections import Counter, deque

def rank3(rows, p):
    a = [[z % p for z in row] for row in rows]
    r = 0
    for col in range(3):
        k = next((k for k in range(r, len(a)) if a[k][col]), None)
        if k is None:
            continue
        a[k], a[r] = a[r], a[k]
        inv = pow(a[r][col], -1, p)
        a[r] = [(v * inv) % p for v in a[r]]
        for j in range(len(a)):
            if j != r:
                z = a[j][col]
                a[j] = [(a[j][i] - z * a[r][i]) % p for i in range(3)]
        r += 1
    return r

def bracket(x, y, p):
    a,b,c = x
    d,e,f = y
    return ((b*f-c*e)%p, (2*(a*e-b*d))%p, (2*(c*d-a*f))%p)

def proj(x,p):
    z = next(t for t in x if t)
    w = pow(z,-1,p)
    return tuple(t*w %p for t in x)

def invariant_lines(x,p):
    a,b,c=x
    vals = [t for t in range(p) if (c-2*a*t-b*t*t)%p==0]
    if b==0: vals.append(p)  # p names the projective point at infinity
    return frozenset(vals)

def actual_graph(p):
    vs = [t for t in product(range(p), repeat=3) if any(t)]
    N=len(vs)
    nbr = [set() for _ in vs]
    for i in range(N):
        for j in range(i+1,N):
            if rank3((vs[i],vs[j],bracket(vs[i],vs[j],p)),p)<3:
                nbr[i].add(j)
                nbr[j].add(i)
    return vs,nbr

def components(nbr):
    remain=set(range(len(nbr)))
    sizes=[]
    while remain:
        root=remain.pop()
        seen={root}
        queue=[root]
        for v in queue:
            for w in nbr[v]:
                if w not in seen:
                    seen.add(w)
                    remain.remove(w)
                    queue.append(w)
        sizes.append(len(seen))
    return sorted(sizes,reverse=True)

def middle_laplacian(n):
    vs=[(i,) for i in range(n)]+list(combinations(range(n),2))
    vcount=len(vs)
    adj=[[0]*vcount for _ in range(vcount)]
    for i,x in enumerate(vs):
        for j in range(i+1,vcount):
            y=vs[j]
            if set(x)&set(y):adj[i][j]=adj[j][i]=1
    return [[(sum(adj[i]) if i==j else -adj[i][j]) for j in range(vcount)] for i in range(vcount)]

def matmul(a,b):
    n=len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def characteristic_polynomial(a):
    # Fraction-free Faddeev-LeVerrier: coefficients in descending powers.
    n=len(a)
    B=[[int(i==j) for j in range(n)] for i in range(n)]
    ans=[1]
    for k in range(1,n+1):
        B=matmul(a,B)
        tr=sum(B[i][i] for i in range(n))
        assert tr%k==0
        c=-tr//k
        ans.append(c)
        for i in range(n):B[i][i]+=c
    return ans

def polymul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):c[i+j]+=u*v
    return c

def predicted_polynomial(n):
    ans=[1,0]
    ans=polymul(ans,[1,-(n+1)])
    for _ in range(n-1):ans=polymul(ans,[1,-(2*n+1),n*n])
    for _ in range(n*(n-3)//2):ans=polymul(ans,[1,-2*n])
    return ans

def check(p):
    q=p; n=q+1;m=q-1;c=q*(q-1)//2
    vs,adj=actual_graph(q)
    assert len(vs)==q**3-1
    lines=[proj(x,q) for x in vs]
    borels=[invariant_lines(x,q) for x in vs]
    assert Counter(map(len,borels))=={0:c*m,1:n*m,2:comb(n,2)*m}
    assert len(set(lines))==(q*q+q+1)
    for i in range(len(vs)):
        for j in range(i+1,len(vs)):
            model=(lines[i]==lines[j] or bool(borels[i]&borels[j]))
            assert ((j in adj[i])==model),(q,i,j)
    assert components(adj)==[(n+comb(n,2))*m]+[m]*c
    deg=Counter(map(len,adj))
    assert deg=={m*n-1:n*m, m*(2*n-1)-1:comb(n,2)*m, m-1:c*m}
    L=middle_laplacian(n)
    assert characteristic_polynomial(L)==predicted_polynomial(n)
    print(f'EXACT_CHECK_OK q={q} vertices={len(vs)} components={c+1} middle_order={len(L)}')

if __name__=='__main__':
    for p in (3,5):check(p)
    print('VERIFY_OK')
