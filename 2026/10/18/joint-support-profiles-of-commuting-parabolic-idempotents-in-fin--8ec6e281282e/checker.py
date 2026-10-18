#!/usr/bin/env python3
"""Exact independent tests for the joint support-size 0-Hecke idempotent commutation theorem."""
from itertools import permutations
from collections import Counter

def projection(word, mask):
    # Repeated passes of adjacent antisorting realize the parabolic longest
    # 0-Hecke element. The loop terminates once no permitted swap remains.
    arr=list(word)
    for _ in range(len(word)*len(word)+1):
        moved=False
        for i in range(len(word)-1):
            if mask>>i&1 and arr[i]<arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                moved=True
        if not moved:
            return tuple(arr)
    raise AssertionError('antisorting did not stabilize')

def commute_by_full_action(n, I, J):
    for p in permutations(range(n)):
        if projection(projection(p,I),J)!=projection(projection(p,J),I):
            return False
    return True

def commute_by_regular_action(n,I,J):
    p=tuple(range(n))
    return projection(projection(p,I),J)==projection(projection(p,J),I)

def component_condition(m,I,J):
    U=I|J
    i=0
    while i<m:
        if not (U>>i&1):i+=1;continue
        start=i
        while i<m and U>>i&1:i+=1
        C=((1<<(i-start))-1)<<start
        if I&C!=C and J&C!=C:return False
    return True

def recurrence_coefficients(m):
    # State 0: since last 00, no I-only or J-only letter;
    # 1: I-only has occurred; 2: J-only has occurred.
    state={ (0,0,0,0):1 }
    for _ in range(m):
        nxt=Counter()
        for (s,a,b,c),v in state.items():
            for u,vv in ((0,0),(1,0),(0,1),(1,1)):
                if not u and not vv:ns=0
                elif u and vv:ns=s
                elif u:
                    if s==2:continue
                    ns=1
                else:
                    if s==1:continue
                    ns=2
                nxt[ns,a+u,b+vv,c+(u or vv)]+=v
        state=nxt
    res=Counter()
    for (_,a,b,c),v in state.items():res[a,b,c]+=v
    return res

for n in range(2,10):
    m=n-1
    counts=Counter()
    for I in range(1<<m):
        for J in range(1<<m):
            pred=component_condition(m,I,J)
            real=commute_by_regular_action(n,I,J)
            assert pred==real,(n,I,J)
            if real: counts[I.bit_count(),J.bit_count(),(I|J).bit_count()]+=1
    assert counts==recurrence_coefficients(m),(n,counts,recurrence_coefficients(m))
    a=sum(counts.values())
    seq=[1,4]
    for _ in range(2,m+1):seq.append(4*seq[-1]-2*seq[-2])
    assert a==seq[m],(n,a,seq[m])
    print('joint_support_profile_pass',n,'total',a,'terms',len(counts))

# This separately tests equality as transformations, not just on the identity.
for n in range(2,7):
    m=n-1
    for I in range(1<<m):
        for J in range(1<<m):
            assert commute_by_full_action(n,I,J)==component_condition(m,I,J),(n,I,J)
            if component_condition(m,I,J):
                for p in permutations(range(n)):
                    assert projection(projection(p,I),J)==projection(p,I|J),(n,I,J,p)
    print('full_action_pass',n)
print('CHECKER_OK')

# Independent signed-permutation (type B3) faithful 0-Hecke action.
from itertools import product as cartprod

def length_B(p):
    return (sum(x<0 for x in p)
            +sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
            +sum(-p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p))))

def mul_B_gen(p,i):
    q=list(p)
    if i==0:q[0]=-q[0]
    else:q[i-1],q[i]=q[i],q[i-1]
    q=tuple(q)
    return q if length_B(q)>length_B(p) else p

def projection_B(p,mask):
    for _ in range(30):
        old=p
        for i in range(len(p)):
            if mask>>i&1:p=mul_B_gen(p,i)
        if old==p:return p
    raise AssertionError('B projection failed')

for n in (2,3,4):
    points=[tuple(e*x for e,x in zip(sign,p))
            for p in permutations(range(1,n+1))
            for sign in cartprod((-1,1),repeat=n)]
    for I in range(1<<n):
        for J in range(1<<n):
            expected=component_condition(n,I,J)
            same=True
            for p in points:
                a=projection_B(projection_B(p,I),J)
                b=projection_B(projection_B(p,J),I)
                if a!=b:same=False
                if expected:assert a==projection_B(p,I|J),(n,I,J,p)
            assert same==expected,(n,I,J)
    print('B_type_full_action_pass',n)
print('ALL_EXACT_CHECKS_PASSED')

# The closed connected-component sum is computed in a different order from
# the run automaton: sum over occupied subsets, then over component choices.
from math import comb

def graph_joint_profile(n,edges):
    ans=Counter()
    edge_set={frozenset(edge) for edge in edges}
    for U in range(1<<n):
        remaining={i for i in range(n) if U>>i&1}
        cs=[]
        while remaining:
            start=next(iter(remaining));remaining.remove(start)
            comp={start};front=[start]
            while front:
                x=front.pop()
                for y in tuple(remaining):
                    if frozenset((x,y)) in edge_set:
                        remaining.remove(y);comp.add(y);front.append(y)
            cs.append(len(comp))
        pol=Counter({(0,0,0):1})
        for t in cs:
            ct=Counter()
            for j in range(t+1):
                ct[t,j,t]+=comb(t,j)
                ct[j,t,t]+=comb(t,j)
            ct[t,t,t]-=1
            new=Counter()
            for (a,b,c),v in pol.items():
                for (i,j,k),w in ct.items():
                    new[a+i,b+j,c+k]+=v*w
            pol=new
        ans.update(pol)
    return +ans

for m in range(0,8):
    p=graph_joint_profile(m,[(i,i+1) for i in range(m-1)])
    assert p==recurrence_coefficients(m),(m,p,recurrence_coefficients(m))
    print('path_component_polynomial_pass',m)
for m in range(2,8):
    star_edges=[(0,i) for i in range(1,m)]
    p=graph_joint_profile(m,star_edges)
    # Directly enumerate vertex-color pairs independently of the component sum.
    direct=Counter()
    for I in range(1<<m):
        for J in range(1<<m):
            U=I|J
            components=[]; rem={i for i in range(m) if U>>i&1}
            while rem:
                start=rem.pop();comp={start};queue=[start]
                while queue:
                    x=queue.pop()
                    for y in list(rem):
                        if (x,y) in star_edges or (y,x) in star_edges:
                            rem.remove(y);comp.add(y);queue.append(y)
                components.append(comp)
            if all(all((I>>i)&1 for i in C) or all((J>>i)&1 for i in C) for C in components):
                direct[I.bit_count(),J.bit_count(),U.bit_count()]+=1
    assert p==direct,(m,p,direct)
    print('star_component_polynomial_pass',m)
print('FINAL_ALL_CHECKS_PASSED')
