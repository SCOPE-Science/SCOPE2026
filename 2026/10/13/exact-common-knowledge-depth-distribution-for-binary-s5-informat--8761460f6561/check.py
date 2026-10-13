"""Finite sanity checks for exact common-knowledge convergence depth."""
from fractions import Fraction
from math import factorial
from collections import deque

def involutions(n):
    p = list(range(n))
    def rec(unused):
        if not unused:
            yield tuple(p); return
        i = min(unused)
        p[i] = i
        yield from rec(unused-{i})
        for j in sorted(unused-{i}):
            p[i]=j; p[j]=i
            yield from rec(unused-{i,j})
            p[j]=j
        p[i]=i
    yield from rec(set(range(n)))

def diameter(r,s):
    n=len(r)
    adj=[set((r[i],s[i]))-{i} for i in range(n)]
    result=0
    for a in range(n):
        dist={a:0};q=deque([a])
        while q:
            v=q.popleft()
            for t in adj[v]:
                if t not in dist:dist[t]=dist[v]+1;q.append(t)
        result=max(result,max(dist.values()))
    return result

def predicted(n,d):
    # exact EGF coefficient of exp(P_d), recurrence f_k = 1/k sum_{j=1}^k j p_j f_{k-j}
    p=[Fraction(0)]*(n+1)
    for j in range(1,min(n,d+1)+1):p[j]+=1
    for j in range(1,min(d,n//2)+1):p[2*j]+=Fraction(1,2*j)
    f=[Fraction(1)]+[Fraction(0)]*n
    for k in range(1,n+1):f[k]=sum(j*p[j]*f[k-j] for j in range(1,k+1))/k
    return int(f[n]*factorial(n))

def verify():
    print('n   total_pairs    counts_by_exact_depth')
    for n in range(1,8):
        inv=list(involutions(n)); counts=[0]*n
        for r in inv:
            for s in inv:
                d=diameter(r,s)
                counts[d]+=1
        assert sum(counts)==len(inv)**2
        for d in range(n):
            assert sum(counts[:d+1])==predicted(n,d),(n,d,counts)
        if n>=3: assert counts[n-1]==factorial(n),(n,counts)
        print(n, len(inv)**2,counts)
    # direct semantics of everyone knows and common knowledge for every assignment
    for n in range(1,5):
        for r in involutions(n):
            for s in involutions(n):
                D=diameter(r,s)
                for bits in range(1<<n):
                    S={i for i in range(n) if bits&(1<<i)}
                    cur=set(S)
                    for k in range(n):
                        if k==D:
                            C={w for w in range(n) if all(u in S for u in component(w,r,s))}
                            assert cur==C,(n,r,s,bits,k)
                        cur={w for w in range(n) if all(u in cur for u in {w,r[w],s[w]})}
    print('Semantics checks passed.')

def component(w,r,s):
    q=[w];seen={w}
    for t in q:
        for x in (r[t],s[t]):
            if x not in seen:seen.add(x);q.append(x)
    return seen

if __name__=='__main__': verify()
