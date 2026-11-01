"""Direct finite checks of bipartite NOR orbit and path-fiber formulas."""
from collections import Counter
from itertools import product

def fib(k):
    if k<0: raise ValueError(k)
    a,b=0,1
    for _ in range(k): a,b=b,a+b
    return a

def nor(s,adj):
    o=0
    for i,nb in enumerate(adj):
        if not (s & nb): o|=1<<i
    return o

def adj_path(n):
    return [((1<<(i-1)) if i else 0)|((1<<(i+1)) if i+1<n else 0) for i in range(n)]

def one_side(y,stubs_left,stubs_right):
    """Number of input words producing a particular output word y."""
    m=len(y)
    prod=1;i=0
    while i<m:
        if y[i]:i+=1;continue
        j=i
        while j<m and y[j]==0:j+=1
        L=j-i
        t=int(i==0 and stubs_left)+int(j==m and stubs_right)
        prod*=fib(L-1+2*t)
        i=j
    return prod

def path_fiber(s,n):
    A=[(s>>i)&1 for i in range(0,n,2)]
    B=[(s>>i)&1 for i in range(1,n,2)]
    if n%2:
        return one_side(A,False,False)*one_side(B,True,True)
    return one_side(A,False,True)*one_side(B,True,False)

def path_m(n):
    if n in (0,1):return 1
    if n==2:return 2
    return path_m(n-2)+path_m(n-3)

# All simple bipartite graphs on up to 3+3 vertices, with isolates admitted.
checked=0
for a in range(1,4):
 for b in range(1,4):
  n=a+b
  for pattern in range(1<<(a*b)):
   adj=[0]*n
   for i in range(a):
    for j in range(b):
     if pattern>>(i*b+j)&1:
      adj[i]|=1<<(a+j);adj[a+j]|=1<<i
   images={nor(s,adj) for s in range(1<<n)}
   assert all(nor(nor(u,adj),adj)==u for u in images)
   fixed=sum(nor(s,adj)==s for s in range(1<<n))
   maximal=0
   for s in range(1<<n):
    if all((not (s>>i&1) or not (s&adj[i])) for i in range(n)) and all((s>>i&1) or (s&adj[i]) for i in range(n)):
     maximal+=1
   assert fixed==maximal and len(images)==fixed*fixed,(a,b,pattern, len(images),fixed)
   checked+=1

# All individual fibers for every output of paths through 15 vertices.
checked_states=0
for n in range(2,16):
 adj=adj_path(n)
 freq=Counter(nor(s,adj) for s in range(1<<n))
 m=path_m(n)
 assert len(freq)==m*m
 assert sum(nor(s,adj)==s for s in range(1<<n))==m
 for s in range(1<<n):
  assert path_fiber(s,n)==freq.get(s,0),(n,s,path_fiber(s,n),freq.get(s,0))
  checked_states+=1
 print(f"PATH n={n} fixed={m} periodic={len(freq)} two_cycles={m*(m-1)//2} checks={1<<n}")
print(f"PASS bipartite_graphs={checked} output_words_checked={checked_states}")
