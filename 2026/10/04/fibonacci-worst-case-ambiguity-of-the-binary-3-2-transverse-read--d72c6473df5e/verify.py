#!/usr/bin/env python3
from collections import Counter

# Fibonacci convention used in the theorem: F_0=0, F_1=1.
def fib(k):
    a,b=0,1
    for _ in range(k):
        a,b=b,a+b
    return a

def read_direct(bits):
    return tuple(bits[i] + bits[i+1] + bits[i+2] for i in range(0,len(bits)-2,2))

def read_windows(bits):
    out=[]
    j=0
    while 2*j+2 < len(bits):
        a=bits[2*j]
        c=bits[2*j+1]
        b=bits[2*j+2]
        out.append(a+c+b)
        j += 1
    return tuple(out)

def transition(pair, symbol):
    p,q=pair
    if symbol==0:
        return (p,0)
    if symbol==1:
        return (p+q,p)
    if symbol==2:
        return (q,p+q)
    if symbol==3:
        return (0,q)
    raise ValueError(symbol)

def fiber_by_dp(y):
    pair=(1,1)
    for s in y:
        pair=transition(pair,s)
    return sum(pair)

def enumerate_fibers(m):
    n=2*m+1
    counts=Counter()
    for z in range(1<<n):
        bits=tuple((z>>i)&1 for i in range(n))
        a=read_direct(bits)
        b=read_windows(bits)
        assert a==b
        counts[a]+=1
    return counts

# Exhaustive cross-check for all binary inputs through n=19.
for m in range(1,10):
    counts=enumerate_fibers(m)
    maximum=max(counts.values())
    target=fib(m+3)
    maximizers=sorted(y for y,v in counts.items() if v==maximum)
    assert maximum==target, (m,maximum,target)
    assert maximizers==[(1,)*m,(2,)*m], (m,maximizers)
    # Independent dynamic fiber computation for every realized read vector.
    for y,v in counts.items():
        assert fiber_by_dp(y)==v, (m,y,v,fiber_by_dp(y))
    print(f"m={m} n={2*m+1} outputs={len(counts)} max={maximum} maximizers=2")

# Algebraic recurrence check for the two extremal outputs through a much larger range.
pair1=(1,1)
pair2=(1,1)
for m in range(1,101):
    pair1=transition(pair1,1)
    pair2=transition(pair2,2)
    assert sum(pair1)==fib(m+3)
    assert sum(pair2)==fib(m+3)
    assert pair2==(pair1[1],pair1[0])

# Check the induction inequalities over all reachable count pairs for prefixes up to length 15.
reachable={(1,1): {()}}
for j in range(0,15):
    next_pairs={}
    for pair,prefixes in reachable.items():
        p,q=pair
        S=p+q
        M=max(p,q)
        assert S<=fib(j+3)
        assert M<=fib(j+2)
        for s in range(4):
            np=transition(pair,s)
            next_pairs.setdefault(np,set())
            # Store only a bounded witness set; the inequalities depend only on the pair.
            if len(next_pairs[np])<3:
                for pref in prefixes:
                    next_pairs[np].add(pref+(s,))
                    if len(next_pairs[np])>=3:
                        break
    reachable=next_pairs
    jj=j+1
    equality_pairs=[]
    for pair,prefixes in reachable.items():
        p,q=pair
        S=p+q
        M=max(p,q)
        assert S<=fib(jj+3)
        assert M<=fib(jj+2)
        if S==fib(jj+3):
            equality_pairs.append(pair)
    assert set(equality_pairs)=={(fib(jj+2),fib(jj+1)),(fib(jj+1),fib(jj+2))}

print("VERIFY_OK")
