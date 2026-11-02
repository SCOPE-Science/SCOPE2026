#!/usr/bin/env python3
"""Independent exact rank-four FO type recurrence for finite height-two crowns.
No orbit reductions; all ordered triples are enumerated.
"""
import itertools, sys
cache = {r:{} for r in range(1,5)}
def label(r, sig):
    f=frozenset(sig)
    if f not in cache[r]: cache[r][f]=len(cache[r])
    return cache[r][f]
def calc(n):
    V=range(2*n)
    def lt(x,y):
        if x%2 or y%2!=1: return False
        a=x//2; b=y//2
        return b == a or b == (a-1)%n
    def atom(t):
        out=[]
        for i in range(4):
            for j in range(i+1,4):
                a,b=t[i],t[j]
                out.append(0 if a==b else 1 if lt(a,b) else 2 if lt(b,a) else 3)
        return tuple(out)
    # Globally enumerate ground atomic patterns, without assigning signatures based on numerical labels.
    t1={}
    for t in itertools.product(V,repeat=3):
        t1[t]=label(1,(atom(t+(z,)) for z in V))
    t2={}
    for t in itertools.product(V,repeat=2):
        t2[t]=label(2,(t1[t+(z,)] for z in V))
    t3={}
    for x in V:
        t3[x]=label(3,(t2[(x,z)] for z in V))
    return label(4,t3.values()), (len(cache[1]),len(cache[2]),len(cache[3]),len(cache[4]))
if __name__=='__main__':
    for n in range(2,1+(int(sys.argv[1]) if len(sys.argv)>1 else 14)):
        t,c=calc(n)
        print(n,t,' '.join(map(str,c)),flush=True)
