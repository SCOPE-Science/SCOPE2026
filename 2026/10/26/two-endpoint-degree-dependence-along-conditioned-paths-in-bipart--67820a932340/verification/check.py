"""Exact exhaustive checker for marked distances and endpoint degrees in biclique USTs."""
from itertools import combinations
from collections import Counter,defaultdict,deque
from fractions import Fraction
from math import comb,prod

def fall(x,k):return prod(range(x-k+1,x+1)) if k else 1

def tree_counts(a,b):
    n=a+b; edges=[(i,a+j) for i in range(a) for j in range(b)]
    out=defaultdict(Counter);total=0
    for ids in combinations(range(a*b),n-1):
        parent=list(range(n));adj=[[] for _ in range(n)]
        def root(x):
            while parent[x]!=x:x=parent[x]
            return x
        for i in ids:
            x,y=edges[i];X,Y=root(x),root(y)
            if X==Y:break
            parent[X]=Y;adj[x].append(y);adj[y].append(x)
        else:
            total+=1;distance=[-1]*n;distance[0]=0;q=deque([0])
            while q:
                x=q.popleft()
                for y in adj[x]:
                    if distance[y]<0:distance[y]=distance[x]+1;q.append(y)
            out[distance[a]][(len(adj[0]),len(adj[a]))]+=1
    assert total==a**(b-1)*b**(a-1)
    return out,total

def verify():
    checks=0
    for a in range(2,6):
      for b in range(2,6):
        if a*b>20:continue
        out,total=tree_counts(a,b)
        for t in range(1,min(a,b)+1):
            c=t*(a+b-t); R=b-t; L=a-t; d=2*t-1
            row=out[d]; mass=sum(row.values())
            p=Fraction(fall(a-1,t-1)*fall(b-1,t-1)*c,(a*b)**t)
            assert Fraction(mass,total)==p,(a,b,t,'distance');checks+=1
            for j in range(R+1):
              for k in range(L+1):
                observed=sum(count*fall(x-1,j)*fall(y-1,k) for (x,y),count in row.items())
                observed=Fraction(observed,mass)
                proposed=Fraction(fall(R,j)*fall(L,k),a**j*b**k)*(1+Fraction(j*(a-t)+k*(b-t)-j*k,c))
                assert observed==proposed,(a,b,t,j,k,observed,proposed)
                checks+=1
            ux=sum(x*v for (x,y),v in row.items())
            vy=sum(y*v for (x,y),v in row.items())
            both=sum(x*y*v for (x,y),v in row.items())
            cov=Fraction(both,mass)-Fraction(ux*vy,mass**2)
            assert cov==-Fraction(R*L,c*c),(a,b,t,cov);checks+=1
        assert sum(Fraction(sum(v.values()),total) for v in out.values())==1;checks+=1
        for t in range(1,min(a,b)):
            left=out[2*t-1];right=out[2*(t+1)-1]
            for which in (0,1):
                maxd=b if which==0 else a
                for cutoff in range(2,maxd+1):
                    x=Fraction(sum(v for deg,v in left.items() if deg[which]>=cutoff),sum(left.values()))
                    y=Fraction(sum(v for deg,v in right.items() if deg[which]>=cutoff),sum(right.values()))
                    assert x>=y
                    checks+=1
                assert any(Fraction(sum(v for deg,v in left.items() if deg[which]>=cutoff),sum(left.values())) > Fraction(sum(v for deg,v in right.items() if deg[which]>=cutoff),sum(right.values())) for cutoff in range(2,maxd+1));checks+=1
        print('PASS K_%s,%s %s trees'%(a,b,total))
    print('PASS exact comparison count',checks)
if __name__=='__main__':verify()
