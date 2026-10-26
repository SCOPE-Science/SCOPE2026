"""Standalone finite verification for conditional leaf regression in uniform Cayley trees.
Run with: python verify_cayley_leaf_distance.py
All exact checks use Python integers and Fraction; asymptotics are not certified by this code.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
import math

checks = 0

def check(condition, msg=''):
    global checks
    assert condition, msg
    checks += 1


def formula(n, k):
    r = Fraction(n-1, n)
    return r ** (n-k-2) * (n-k+1-Fraction(2, k+1))


def p_dist(n,k):
    falling = math.factorial(n-2)//math.factorial(n-k-1)
    return Fraction((k+1)*falling,n**k)


def a_rooted_path(n,k):
    return Fraction(k,k+1) * Fraction(n-1,n)**(n-k-2)


def off_path_leaf(n,k):
    if n-k-1==0:
        return Fraction(0)
    return Fraction(n-k-1,n-2) * Fraction(n-1,n)**(n-k-2)


def tree_from_prufer(code,n):
    deg = [1]*n
    for x in code: deg[x]+=1
    edges=[]
    for x in code:
        leaf=next(i for i in range(n) if deg[i]==1)
        edges.append((leaf,x))
        deg[leaf]-=1;deg[x]-=1
    remains=[i for i in range(n) if deg[i]==1]
    edges.append(tuple(remains))
    return edges


def record_exhaustively(n):
    v=defaultdict(lambda:[0,0,0,0])
    total_leaves=0
    for seq in product(range(n),repeat=n-2):
        edges=tree_from_prufer(seq,n)
        adj=[[] for _ in range(n)]
        for a,b in edges: adj[a].append(b);adj[b].append(a)
        degree=[len(x) for x in adj]
        leaves=sum(d==1 for d in degree)
        dist=[-1]*n;dist[0]=0;queue=[0]
        for x in queue:
            for y in adj[x]:
                if dist[y]<0:dist[y]=dist[x]+1;queue.append(y)
        k=dist[1]
        v[k][0]+=1
        v[k][1]+=leaves
        v[k][2]+=int(degree[0]==1)
        v[k][3]+=int(degree[2]==1) if n>=3 else 0
        total_leaves+=leaves
    count=n**(n-2)
    check(sum(row[0] for row in v.values())==count,f'enumeration {n}')
    check(Fraction(total_leaves,count)==n*Fraction(n-1,n)**(n-2),f'leaf mean {n}')
    for k in range(1,n):
        c,suml,leaf0,leaf2=v[k]
        check(Fraction(c,count)==p_dist(n,k),f'path law {(n,k)}')
        check(Fraction(suml,c)==formula(n,k),f'leaf regression {(n,k)}')
        check(Fraction(leaf0,c)==a_rooted_path(n,k),f'endpoint {(n,k)}')
        if n>=3:
            # An interior-path vertex cannot be a leaf; only off-path cases contribute.
            check(Fraction(leaf2,c)==off_path_leaf(n,k),f'third {(n,k)}')

for n in range(2,9):
    record_exhaustively(n)

for n in range(4,151):
    mu = n*Fraction(n-1,n)**(n-2)
    check(formula(n,1)==mu,f'adjacency centering {n}')
    peak=[]
    for k in range(1,n-1):
        threshold=Fraction((k+2)*(k*k+1),2)
        lhs=formula(n,k+1)-formula(n,k)
        check((lhs>0)==(n>threshold), f'difference positive {(n,k)}')
        check((lhs==0)==(n==threshold), f'difference equality {(n,k)}')
        check((lhs<0)==(n<threshold), f'difference negative {(n,k)}')
        predicted=Fraction(2*(n-threshold), n*(k+1)*(k+2))*Fraction(n-1,n)**(n-k-3)
        check(lhs==predicted,f'finite difference {(n,k)}')
    peak_index=next(k for k in range(1,n) if (k+2)*(k*k+1)>=2*n)
    vals=[formula(n,k) for k in range(1,n)]
    maxval=max(vals)
    maximizers=[k+1 for k,v in enumerate(vals) if v==maxval]
    expected=[peak_index,peak_index+1] if (peak_index+2)*(peak_index*peak_index+1)==2*n else [peak_index]
    check(maximizers==expected,f'maximizers {n} {maximizers} != {expected}')
    check(maxval>mu,f'nontrivial uplift {n}')

for k in range(2,30):
    n=(k+2)*(k*k+1)//2
    check(2*n==(k+2)*(k*k+1),f'integral tie n={n}')
    peak_index=next(t for t in range(1,n) if (t+2)*(t*t+1)>=2*n)
    check(peak_index==k, f'tie location {(n,k)}')
    check(formula(n,k)==formula(n,k+1),f'tie value {(n,k)}')

# The limit profile is analytical; representative numerical convergence only.
for c in (0.5,1.0,math.sqrt(2),2.0,3.0):
    n=300000
    k=max(1,round(c*math.sqrt(n)))
    r=1-1/n
    y=math.exp((n-k-2)*math.log1p(-1/n))*(n-k+1-2/(k+1))
    mu=n*math.exp((n-2)*math.log1p(-1/n))
    approx=math.exp(-1)*(1-c*c/2)
    check(abs((y-mu)-approx)<0.01,f'Rayleigh scale c={c}')

print(f'PASS: {checks} deterministic checks; exhaustive Cayley trees n=2,...,8')
