#!/usr/bin/env python3

def mu(s):
    return ''.join('10' if c == '1' else '11' for c in s)

def pd_prefix(n):
    s='1'
    while len(s)<n:
        s=mu(s)
    return s[:n]

def coverage_masks(w):
    d={}
    n=len(w)
    for i in range(n):
        f=''
        m=0
        for j in range(i,n):
            f += w[j]
            m |= 1 << j
            d[f]=d.get(f,0) | m
    return tuple(d.values())

def attracted(w,S):
    sm=0
    for i in S:
        sm |= 1 << i
    return all(m & sm for m in coverage_masks(w))

N=128
p=pd_prefix(N)
S=[]
g=[]
for n in range(1,N+1):
    if not attracted(p[:n],S):
        S.append(n-1)
        g.append(n-1)
    assert attracted(p[:n],S)
expected=[]
k=0
while (1<<k)-1 < N:
    expected.append((1<<k)-1)
    k += 1
assert g==expected

P='1'; Q='0'
levels=13
for k in range(levels):
    L=len(P)
    assert len(Q)==L
    assert P[:-1]==Q[:-1]
    assert P[-1]!=Q[-1]
    W=P+Q
    occ=[j for j in range(L+1) if W[j:j+L]==Q]
    assert occ==[L]
    if k+1<levels:
        P,Q=P+Q,P+P

print('VERIFY_OK prefixes=128 dyadic_levels=13 greedy_indices=' + ','.join(map(str,g)))
