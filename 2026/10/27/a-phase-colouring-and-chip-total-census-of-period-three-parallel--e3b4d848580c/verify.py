"""Direct state enumeration and a separate phase-formula check for parallel chip firing."""
from itertools import product
from math import factorial

def graph_edges(kind,n,m=0):
    if kind=='cycle': return n, [(i,(i+1)%n) for i in range(n)]
    if kind=='path': return n, [(i,i+1) for i in range(n-1)]
    if kind=='clique': return n, [(i,j) for i in range(n) for j in range(i+1,n)]
    if kind=='bipartite': return n+m,[(i,n+j) for i in range(n) for j in range(m)]

def count_direct(n, edges):
    nbr=[[] for _ in range(n)]
    for u,v in edges: nbr[u].append(v);nbr[v].append(u)
    degree=[len(z) for z in nbr]
    def nxt(x):
        firing=[int(x[v]>=degree[v]) for v in range(n)]
        return tuple(x[v]-degree[v]*firing[v]+sum(firing[w] for w in nbr[v]) for v in range(n))
    cnt=0
    for x in product(*(range(2*d) for d in degree)):
        y=nxt(x)
        if y!=x and nxt(nxt(y))==x:
            cnt+=1
    return cnt

def count_formula(n,edges):
    nbr=[[] for _ in range(n)]
    for u,v in edges: nbr[u].append(v);nbr[v].append(u)
    total=0
    for f in product(range(3),repeat=n):
        p=1
        for v in range(n):
            p*=sum(1 for w in nbr[v] if f[w]==(f[v]-1)%3)
            if p==0: break
        total+=p
    return 2*total

def count_bipartite(a,b):
    ans=0
    for g0 in range(1,a-1):
     for g1 in range(1,a-g0):
      g2=a-g0-g1
      g=[g0,g1,g2]
      ways_g=factorial(a)//(factorial(g0)*factorial(g1)*factorial(g2))
      for h0 in range(1,b-1):
       for h1 in range(1,b-h0):
        h2=b-h0-h1
        h=[h0,h1,h2]
        ways_h=factorial(b)//(factorial(h0)*factorial(h1)*factorial(h2))
        prod=1
        for i in range(3):
         prod*=h[(i-1)%3]**g[i] * g[(i-1)%3]**h[i]
        ans+=2*ways_g*ways_h*prod
    return ans

if __name__=='__main__':
 for kind,n,m in [('path',2,0),('path',3,0),('path',4,0),('cycle',3,0),('cycle',4,0),('cycle',5,0),('cycle',6,0),('clique',3,0),('clique',4,0),('clique',5,0),('bipartite',1,3),('bipartite',2,3),('bipartite',3,3),('bipartite',3,4)]:
    nn, ee=graph_edges(kind,n,m)
    a=count_direct(nn,ee)
    b=count_formula(nn,ee)
    print(kind,n,m,a,b)
    assert a==b
    if kind=='bipartite': assert b==count_bipartite(n,m)
 print('VERIFY_OK')

# Independent chip-total distribution check: direct enumeration versus phase intervals.
def histogram_direct(n,edges):
    nbr=[[] for _ in range(n)]
    for a,b in edges: nbr[a].append(b); nbr[b].append(a)
    deg=[len(nbr[v]) for v in range(n)]
    def step(x):
        fire=[int(x[i]>=deg[i]) for i in range(n)]
        return tuple(x[i]-deg[i]*fire[i]+sum(fire[j] for j in nbr[i]) for i in range(n))
    h={}
    for x in product(*(range(2*d) for d in deg)):
        y=step(x)
        if y!=x and step(step(y))==x:
            s=sum(x);h[s]=h.get(s,0)+1
    return h

def histogram_phase(n,edges):
    nbr=[[] for _ in range(n)]
    for a,b in edges: nbr[a].append(b); nbr[b].append(a)
    deg=[len(nbr[v]) for v in range(n)]
    h={}
    for phase in product(range(3), repeat=n):
        partial={0:1}
        for v in range(n):
            a=[sum(phase[u]==j for u in nbr[v]) for j in range(3)]
            s=phase[v]
            lower=deg[v] if s==0 else deg[v]-a[0] if s==1 else a[2]
            width=a[(s-1)%3]
            nextpoly={}
            for total,k in partial.items():
                for x in range(lower,lower+width):
                    nextpoly[total+x]=nextpoly.get(total+x,0)+k
            partial=nextpoly
            if not partial: break
        for total,k in partial.items():
            h[total]=h.get(total,0)+k
    center=4*len(edges)-n
    both=h.copy()
    for total,k in h.items():
        both[center-total]=both.get(center-total,0)+k
    return both

if __name__=='__main__':
    for kind,n,m in [('cycle',3,0),('cycle',6,0),('clique',4,0),('bipartite',3,3),('bipartite',3,4)]:
        nn,ee=graph_edges(kind,n,m)
        direct=histogram_direct(nn,ee)
        formula=histogram_phase(nn,ee)
        assert direct==formula,(kind,n,m,direct,formula)
        print('HISTOGRAM_OK',kind,n,m,sorted(direct.items()))
