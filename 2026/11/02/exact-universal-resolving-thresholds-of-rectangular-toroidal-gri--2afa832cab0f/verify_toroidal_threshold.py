#!/usr/bin/env python3
"""Independent checks for the metric-dimension threshold of rectangular tori.
Does not require nonstandard dependencies.
"""
from collections import Counter, deque

def circle_dist(n,i):
    i %= n
    return min(i,n-i)

def hist(n,s):
    return Counter(circle_dist(n,x)-circle_dist(n,x-s) for x in range(n))

def claimed_E(m,n):
    if m%2==0 and n%2==0:
        return m*n//2
    if m%2 and n%2:
        return (m-1)*(n-1)//2 + 1
    if m%2==0:
        return 2*n if m==4 else m*(n-1)//2
    return 2*m if n==4 else n*(m-1)//2

def compare_exact(m,n):
    h1=[hist(m,a) for a in range(m)]
    h2=[hist(n,b) for b in range(n)]
    best=-1; args=[]
    for a in range(m):
        for b in range(n):
            if not (a or b): continue
            cur=sum(v*h2[b].get(-k,0) for k,v in h1[a].items())
            if cur>best:best=cur;args=[(a,b)]
            elif cur==best:args.append((a,b))
    want=claimed_E(m,n)
    if best!=want:raise AssertionError((m,n,best,want,args[:10]))
    return best

def brute_shortest_paths(m,n):
    N=m*n
    adj=[[] for _ in range(N)]
    for x in range(m):
      for y in range(n):
        v=x*n+y
        adj[v]=[((x+1)%m)*n+y,((x-1)%m)*n+y,x*n+(y+1)%n,x*n+(y-1)%n]
    distances=[]
    for s in range(N):
      d=[-1]*N;d[s]=0;Q=deque([s])
      while Q:
        z=Q.popleft()
        for w in adj[z]:
          if d[w]<0:d[w]=d[z]+1;Q.append(w)
      distances.append(d)
    assert all(distances[x*n+y][u*n+v]==circle_dist(m,x-u)+circle_dist(n,y-v) for x in range(m) for y in range(n) for u in range(m) for v in range(n))
    upper=0
    for u in range(N):
       for v in range(u+1,N):
          count=sum(distances[u][w]==distances[v][w] for w in range(N))
          upper=max(upper,count)
    assert upper==claimed_E(m,n),(m,n,upper,claimed_E(m,n))

if __name__=='__main__':
    c=0
    for m in range(3,41):
      for n in range(3,41):
        compare_exact(m,n);c+=1
    b=0
    for m in range(3,11):
      for n in range(3,11):
        brute_shortest_paths(m,n);b+=1
    print('VERIFY_OK',c,'full offset-pair histogram cases;',b,'independent BFS all-vertex-pair cases')
