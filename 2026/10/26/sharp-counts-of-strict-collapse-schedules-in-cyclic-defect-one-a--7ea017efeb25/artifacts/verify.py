#!/usr/bin/env python3
"""Independent finite tests for reachable subsets and strict-drop schedules."""
from collections import deque
from math import gcd, factorial
from itertools import permutations

def predicted(n,d,H):
    H=set(H)
    # Every directed d-orbit must meet the survivor set.
    seen=set()
    for i in range(n):
        if i in seen: continue
        orbit=[];x=i
        while x not in seen:
            seen.add(x);orbit.append(x);x=(x+d)%n
        if all(y in H for y in orbit):return 0
    chains=[];seen=set()
    for i in H:
        if (i-d)%n not in H:
            j=i;l=0
            while j in H:
                l+=1;seen.add(j);j=(j+d)%n
            chains.append(l)
    assert seen==H
    x=factorial(len(H));den=1
    for l in chains:den*=factorial(l)
    assert x%den==0
    return x//den

def brute(n,d,H):
    H=set(H)
    if not H:return 1
    ct=0
    for t in permutations(H):
        seen=set();ok=True
        for p in t:
            if (p+d)%n in seen:
                ok=False;break
            seen.add(p)
        if ok:ct+=1
    return ct

def images(n,d):
    full=(1<<n)-1
    def go_a(s):return ((s<<1)&full)|(s>>(n-1))
    def go_b(s):return (s&~1)|((1<<d) if s&1 else 0)
    q=deque([full]);nb={full:0}
    while q:
        s=q.popleft()
        for t,c in ((go_a(s),0),(go_b(s),1)):
            if t not in nb or nb[t]>nb[s]+c:
                nb[t]=nb[s]+c
                if c:q.append(t)
                else:q.appendleft(t)
    return nb

def check(max_n=8):
    cases=0
    for n in range(2,max_n+1):
        for d in range(1,n):
            dist=images(n,d)
            g=gcd(n,d)
            for mask in range(1,1<<n):
                H={i for i in range(n) if not (mask>>i&1)}
                p=predicted(n,d,H)
                b=brute(n,d,H)
                assert p==b,(n,d,H,p,b)
                attainable=all(any(mask>>i&1 for i in range(r,n,g)) for r in range(g))
                assert (mask in dist)==attainable,(n,d,mask,'reachability')
                if attainable: assert dist[mask]==len(H),(n,d,mask,dist[mask])
                cases+=1
            if g==1:
                k=n-1
                w='b'+('a'*(n-d)+'b')*(n-2)
                s=(1<<n)-1
                for c in w:
                    s=(((s<<1)&((1<<n)-1))|(s>>(n-1))) if c=='a' else (s&~1)|((1<<d) if s&1 else 0)
                assert s.bit_count()==1
                assert len(w)==1+(n-2)*(n-d+1)
                for k in range(1,n):
                    mx=max(predicted(n,d,{j for j in range(n) if not (m>>j&1)}) for m in range(1,1<<n) if m.bit_count()==n-k)
                    r=min(k,n-k);q,t=divmod(k,r)
                    bound=factorial(k)//(factorial(q)**(r-t)*factorial(q+1)**t)
                    assert mx==bound,(n,d,k,mx,bound)
            print(f'CHECK n={n} d={d} g={g}: all targets and schedules OK')
    print('VERIFY_OK',cases,'subset/automaton cases')

if __name__=='__main__':check()
