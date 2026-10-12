#!/usr/bin/env python3
from math import comb


def fan_adj(m):
    adj=[set() for _ in range(m+1)]
    for i in range(1,m+1):
        adj[0].add(i); adj[i].add(0)
    for i in range(1,m):
        adj[i].add(i+1); adj[i+1].add(i)
    return adj


def zero_forces(adj, mask):
    n=len(adj)
    blue={i for i in range(n) if (mask>>i)&1}
    while True:
        move=None
        for v in tuple(blue):
            white=[u for u in adj[v] if u not in blue]
            if len(white)==1:
                move=white[0]
                break
        if move is None:
            return len(blue)==n
        blue.add(move)


def criterion(m, mask):
    hub=(mask&1)!=0
    sel=lambda i: ((mask>>i)&1)!=0
    if hub:
        return sel(1) or sel(m) or any(sel(i) and sel(i+1) for i in range(1,m))
    return ((sel(1) and sel(2)) or
            (sel(m-1) and sel(m)) or
            any(sel(i) and sel(i+1) and sel(i+2) for i in range(1,m-1)))


def add(a,b):
    n=max(len(a),len(b)); out=[0]*n
    for i,v in enumerate(a): out[i]+=v
    for i,v in enumerate(b): out[i]+=v
    return out


def mul_x(a):
    return [0]+a


def transition_A(m):
    # states are suffixes 00,01,10,11; entries are coefficient lists in x.
    # first two bits may not be 11; final suffix may not be 11; 111 is forbidden.
    states=[[1],[0,1],[0,1],[0]]
    if m==2:
        out=[0]
        for j in (0,1,2): out=add(out,states[j])
        return out
    for _ in range(2,m):
        nxt=[[0] for _ in range(4)]
        # append 0
        nxt[0]=add(nxt[0],states[0])
        nxt[2]=add(nxt[2],states[1])
        nxt[0]=add(nxt[0],states[2])
        nxt[2]=add(nxt[2],states[3])
        # append 1; 11 -> 11 forbidden because it would create 111
        nxt[1]=add(nxt[1],mul_x(states[0]))
        nxt[3]=add(nxt[3],mul_x(states[1]))
        nxt[1]=add(nxt[1],mul_x(states[2]))
        states=nxt
    out=[0]
    for j in (0,1,2): out=add(out,states[j])
    return out


def formula_coeffs(m):
    # (1+x)^(m+1) - x Q_m(x) - A_m(x),
    # Q_m=sum_j C(m-j-1,j)x^j.
    out=[comb(m+1,k) for k in range(m+2)]
    for j in range(0,m+1):
        n=m-j-1
        q=comb(n,j) if n>=j>=0 else 0
        if q: out[j+1]-=q
    A=transition_A(m)
    for j,v in enumerate(A): out[j]-=v
    return out

subset_checks=criterion_checks=coefficient_checks=minimum_checks=0
for m in range(3,11):
    adj=fan_adj(m)
    actual=[0]*(m+2)
    for mask in range(1<<(m+1)):
        z=zero_forces(adj,mask)
        c=criterion(m,mask)
        subset_checks+=1; criterion_checks+=1
        if z!=c:
            raise AssertionError((m,mask,z,c))
        if z: actual[mask.bit_count()]+=1
    formula=formula_coeffs(m)
    if formula!=actual:
        raise AssertionError((m,actual,formula))
    coefficient_checks+=len(actual)
    nz=[i for i,a in enumerate(actual) if a]
    if min(nz)!=2 or actual[2]!=4:
        raise AssertionError((m,min(nz),actual[2]))
    minimum_checks+=2
print(f"VERIFY_OK m_range=3..10 subset_checks={subset_checks} criterion_checks={criterion_checks} coefficient_checks={coefficient_checks} minimum_checks={minimum_checks} max_order=11")
