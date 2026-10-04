from itertools import combinations
from collections import deque

def partitions(n,r,lo=1):
    if r==0:
        if n==0: yield ()
        return
    for x in range(lo,n+1):
        if n-x < x*(r-1): break
        for q in partitions(n-x,r-1,x): yield (x,)+q

def labels(parts):
    out=[]
    for i,a in enumerate(parts): out += [i]*a
    return out

def graph(parts):
    L=labels(parts); n=len(L)
    adj=[[v for v in range(n) if v!=u and L[v]!=L[u]] for u in range(n)]
    edges=[(u,v) for u in range(n) for v in adj[u] if u<v]
    D=[[99]*n for _ in range(n)]
    for s in range(n):
        D[s][s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if D[s][v]==99:
                    D[s][v]=D[s][u]+1; q.append(v)
    return L,edges,D

def resolving(mask,edges,D,n):
    S=[s for s in range(n) if mask>>s&1]
    codes=set()
    for u,v in edges:
        c=tuple(min(D[s][u],D[s][v]) for s in S)
        if c in codes: return False
        codes.add(c)
    return True

def predicted(mask,parts,L):
    n=len(L); T=[v for v in range(n) if not(mask>>v&1)]
    r=len(parts)
    if r>=3: return len(T)<=1
    if len(T)<=1: return True
    return len(T)==2 and L[T[0]]!=L[T[1]]

types=subsets=edges_seen=0
for n in range(3,11):
    for r in range(2,n+1):
        for parts in partitions(n,r):
            L,E,D=graph(parts)
            actual=[]
            for mask in range(1<<n):
                subsets+=1
                a=resolving(mask,E,D,n)
                p=predicted(mask,parts,L)
                assert a==p,(parts,mask,a,p)
                if a: actual.append(mask)
            mn=min(m.bit_count() for m in actual)
            target=n-2 if r==2 else n-1
            assert mn==target,(parts,mn,target)
            count=sum(m.bit_count()==mn for m in actual)
            ctarget=parts[0]*parts[1] if r==2 else n
            assert count==ctarget,(parts,count,ctarget)
            coeff=[0]*(n+1)
            for m in actual: coeff[m.bit_count()]+=1
            expected=[0]*(n+1)
            expected[n]=1; expected[n-1]=n
            if r==2: expected[n-2]=parts[0]*parts[1]
            assert coeff==expected,(parts,coeff,expected)
            types+=1; edges_seen+=len(E)

# explicit refutation K_{2,3,5}: published dimension n-r=7, true minimum 9
parts=(2,3,5); L,E,D=graph(parts); n=sum(parts)
# Published-style complement one vertex from each part.
off=[]; base=0
for a in parts:
    off.append(base); base += a
S=set(range(n))-set(off)
mask=sum(1<<v for v in S)
assert not resolving(mask,E,D,n)
# omitted-edge collision: first omitted in each part, edges between first and second and first and third
u,v,w=off
Slist=sorted(S)
def code(e): return tuple(min(D[s][e[0]],D[s][e[1]]) for s in Slist)
assert code((u,v))==code((u,w))==code((v,w))
assert sum(1 for m in range(1<<n) if resolving(m,E,D,n) and m.bit_count()==9)==10

print('VERIFY_OK')
print('multipartite_types_checked =',types)
print('vertex_subsets_checked =',subsets)
print('edge_instances_checked =',edges_seen)
print('orders = 3..10')
print('all edge codes computed from BFS distances')
print('all resolving-set classifications matched')
print('all edge-metric dimensions and minimum-basis counts matched')
print('K_{2,3,5}: published-size 7 construction fails; true dimension = 9')
