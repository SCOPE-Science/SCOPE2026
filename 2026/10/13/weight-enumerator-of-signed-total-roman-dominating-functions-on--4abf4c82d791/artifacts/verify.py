from itertools import product
from collections import defaultdict
from math import factorial

def profiles(total):
    out=[]
    def rec(rem,last,cur):
        if rem==0:
            if len(cur)>=2:
                out.append(tuple(cur))
            return
        for x in range(last,rem+1):
            cur.append(x)
            rec(rem-x,x,cur)
            cur.pop()
    rec(total,1,[])
    return out

def graph(profile):
    part=[]
    for i,n in enumerate(profile):
        part += [i]*n
    N=len(part)
    adj=[set() for _ in range(N)]
    for u in range(N):
        for v in range(N):
            if u!=v and part[u]!=part[v]:
                adj[u].add(v)
    return part,adj

def direct(profile,labels):
    part,adj=graph(profile)
    N=len(part)
    for v in range(N):
        if sum(labels[u] for u in adj[v]) < 1:
            return False
        if labels[v]==-1 and not any(labels[u]==2 for u in adj[v]):
            return False
    return True

def structural(profile,labels):
    r=len(profile)
    start=0
    sums=[]
    neg=[]
    twos=[]
    for n in profile:
        chunk=labels[start:start+n]
        sums.append(sum(chunk))
        neg.append(sum(1 for x in chunk if x==-1))
        twos.append(sum(1 for x in chunk if x==2))
        start+=n
    W=sum(sums)
    C=sum(twos)
    if any(W-s < 1 for s in sums):
        return False
    if any(neg[i]>0 and C-twos[i] < 1 for i in range(r)):
        return False
    return True

def multinomial_count(profile):
    # enumerate partwise count triples and aggregate by total weight
    coeff=defaultdict(int)
    triples_per=[]
    for n in profile:
        ts=[]
        for a in range(n+1):
            for b in range(n-a+1):
                c=n-a-b
                ways=factorial(n)//(factorial(a)*factorial(b)*factorial(c))
                s=-a+b+2*c
                ts.append((a,b,c,s,ways))
        triples_per.append(ts)
    for arr in product(*triples_per):
        W=sum(t[3] for t in arr)
        C=sum(t[2] for t in arr)
        if any(W-t[3] < 1 for t in arr):
            continue
        if any(t[0]>0 and C-t[2] < 1 for t in arr):
            continue
        ways=1
        for t in arr:
            ways*=t[4]
        coeff[W]+=ways
    return dict(coeff)

profiles_checked=0
labelings_checked=0
for N in range(2,9):
    for profile in profiles(N):
        profiles_checked += 1
        direct_coeff=defaultdict(int)
        for labels in product((-1,1,2), repeat=N):
            labelings_checked += 1
            a=direct(profile,labels)
            b=structural(profile,labels)
            if a!=b:
                raise AssertionError(("criterion",profile,labels,a,b))
            if a:
                direct_coeff[sum(labels)] += 1
        formula=multinomial_count(profile)
        if dict(direct_coeff)!=formula:
            raise AssertionError(("enumerator",profile,dict(direct_coeff),formula))
        if any(w<2 for w in formula):
            raise AssertionError(("unexpected low weight",profile,formula))

print(
    "ALL CHECKS PASSED; "
    f"profiles={profiles_checked}; "
    f"labelings_checked={labelings_checked}; "
    "orders=2..8"
)
