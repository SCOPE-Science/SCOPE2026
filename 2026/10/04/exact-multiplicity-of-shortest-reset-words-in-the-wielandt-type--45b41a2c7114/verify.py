#!/usr/bin/env python3
from collections import deque, defaultdict
from math import gcd

def automaton(q,p):
    s=q-p+1
    a=[None]*q; b=[None]*q
    for i in range(q):
        b[i]=(i+1)%q
        a[i]=(i+1)%q if i!=0 else s
    return a,b,s

def image(mask,t,q):
    out=0
    for i in range(q):
        if (mask>>i)&1:
            out |= 1<<t[i]
    return out

def bfs(q,p):
    a,b,s=automaton(q,p)
    start=(1<<q)-1
    dist={start:0}; count={start:1}
    dq=deque([start]); best=None; target_counts=defaultdict(int)
    while dq:
        S=dq.popleft(); d=dist[S]
        if best is not None and d>best:
            break
        if S & (S-1)==0:
            if best is None: best=d
            target_counts[S.bit_length()-1]+=count[S]
            continue
        for t in (a,b):
            T=image(S,t,q)
            if T not in dist:
                dist[T]=d+1; count[T]=count[S]; dq.append(T)
            elif dist[T]==d+1:
                count[T]+=count[S]
    return best,dict(target_counts)

def symbolic(q,p):
    d=q-p; s=q-p+1; L=p*q-2*p+1
    R={s}
    free=forced_a=forced_b=0
    first_times=[]
    for step in range(1,L+1):
        j=step%q
        succ=(j+d)%q
        x=(j in R); y=(succ in R)
        if (not x) and y:
            R.add(j); forced_a+=1; first_times.append(step)
        elif x and (not y):
            forced_b+=1
        else:
            free+=1
    assert len(R)==q
    assert first_times==[1+m*p for m in range(q-1)]
    assert forced_a==q-1
    assert forced_b==p-1
    assert free==(p-1)*(q-3)
    return L,free

def main():
    cases=0
    for q in range(3,14):
        for p in range(2,q):
            if gcd(p,q)!=1: continue
            L,F=symbolic(q,p)
            best,targets=bfs(q,p)
            s=q-p+1
            expected=1<<F
            assert best==L,(q,p,best,L)
            assert targets=={s:expected},(q,p,targets,s,expected)
            cases+=1
    for q in range(3,101):
        for p in range(2,q):
            if gcd(p,q)==1:
                symbolic(q,p)
    print(f"VERIFY_OK exhaustive_power_cases={cases} symbolic_q_max=100")
if __name__=='__main__': main()
