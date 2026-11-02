#!/usr/bin/env python3
"""Direct exhaustive check of maximal general-position polynomials of wheel graphs.
Only the graph-distance definition is used by the direct test; the formula is implemented separately.
"""
from collections import Counter, deque

def predicted(n):
    # Compute coefficients of -n[u^n] log D(u,z) by formal reciprocal of D.
    D = {(0,0):1, (2,1):-1, (3,2):-1, (4,2):-1, (6,3):1}
    inverse=[Counter() for _ in range(n+1)]
    inverse[0][0]=1
    for degree in range(1,n+1):
        for (p,q),coeff in D.items():
            if p and degree>=p:
                for exponent,count in inverse[degree-p].items():
                    inverse[degree][exponent+q]-=coeff*count
    answer=Counter({3:n})
    for (p,q),coeff in D.items():
        if p and degree>=p:
            for exponent,count in inverse[n-p].items():
                answer[exponent+q]-=p*coeff*count
    return +answer

def direct(n):
    N=n+1
    adj=[set() for _ in range(N)]
    for i in range(n):
        for j in ((i+1)%n,n):
            adj[i].add(j);adj[j].add(i)
    distances=[]
    for start in range(N):
        ds=[-1]*N;ds[start]=0
        Q=deque([start])
        while Q:
            v=Q.popleft()
            for w in adj[v]:
                if ds[w]<0: ds[w]=ds[v]+1;Q.append(w)
        distances.append(ds)
    forbidden=[]
    for a in range(N):
        for b in range(a+1,N):
            for c in range(b+1,N):
                if (distances[a][b]+distances[b][c]==distances[a][c]
                    or distances[a][c]+distances[c][b]==distances[a][b]
                    or distances[b][a]+distances[a][c]==distances[b][c]):
                    forbidden.append((1<<a)|(1<<b)|(1<<c))
    def valid(mask):return not any(mask&tri==tri for tri in forbidden)
    result=Counter();rim=Counter();hub=Counter()
    for mask in range(1<<N):
        if not valid(mask):continue
        if all(not valid(mask|(1<<v)) for v in range(N) if not (mask>>v)&1):
            size=mask.bit_count();result[size]+=1
            if mask>>n &1:hub[size]+=1
            else:rim[size]+=1
    return +result,+rim,+hub

def max_count(n):
    k,r=divmod(n,3)
    if r==0:return 3
    if r==1:return n*(k+2)//2
    return n

def min_rim_count(n):
    return n*((n+1)//4) if n%2 else 2+(4 if n%4==0 else 0)

if __name__=='__main__':
    for n in range(5,14):
        found,rim,hub=direct(n)
        expect=predicted(n)
        assert found==expect,(n,found,expect)
        assert hub=={3:n},(n,hub)
        assert min(rim)==(n+1)//2,(n,rim)
        assert rim[(n+1)//2]==min_rim_count(n),(n,rim)
        assert max(rim)==(2*n)//3,(n,rim)
        assert rim[(2*n)//3]==max_count(n),(n,rim)
        print('n=',n,'maximal_counts=',dict(sorted(found.items())), 'OK')
    print('VERIFY_OK')
