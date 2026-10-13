from itertools import combinations
from collections import Counter
N=6; T=2

def word(x): return tuple((x>>(N-1-i))&1 for i in range(N))
def enc(b):
    z=0
    for u in b: z=(z<<1)|u
    return z

def patterns_a():
    P=[]
    for r in range(T+1):
        for E in combinations(range(1,N),r):
            if all(E[i+1]>E[i]+1 for i in range(len(E)-1)):
                P.append(E)
    return P

def patterns_b():
    P=[]
    for m in range(1<<(N-1)):
        idx=[i+1 for i in range(N-1) if (m>>i)&1]
        if len(idx)<=T and all(idx[i+1]>idx[i]+1 for i in range(len(idx)-1)):
            P.append(tuple(idx))
    return sorted(P)
PA=sorted(patterns_a()); PB=patterns_b(); assert PA==PB

def ball_a(x):
    b=word(x); out=set()
    for E in PA:
        y=list(b)
        for i in E: y[i]=b[i-1]
        out.add(enc(y))
    return frozenset(out)

def ball_b(x):
    b=word(x); out={x}
    # enumerate all allowed subsets directly as masks, recomputing output from original b
    for m in range(1<<(N-1)):
        if m.bit_count()>T or (m & (m<<1)): continue
        y=list(b)
        for j in range(N-1):
            if (m>>j)&1: y[j+1]=b[j]
        out.add(enc(y))
    return frozenset(out)
B=[]
for x in range(1<<N):
    a=ball_a(x); b=ball_b(x); assert a==b
    B.append(a)

adj=[set() for _ in range(1<<N)]
for i in range(1<<N):
    for j in range(i+1,1<<N):
        if B[i].isdisjoint(B[j]):
            adj[i].add(j); adj[j].add(i)
edges=sum(map(len,adj))//2

max_size=0; maxima=[]; hist=Counter(); nodes=0
def bk(R,P,X):
    global max_size,nodes,maxima
    nodes+=1
    if not P and not X:
        hist[len(R)]+=1
        if len(R)>max_size:
            max_size=len(R); maxima=[tuple(sorted(R))]
        elif len(R)==max_size:
            maxima.append(tuple(sorted(R)))
        return
    if len(R)+len(P)<max_size: return
    u=max(P|X,key=lambda z:len(P&adj[z])) if (P or X) else None
    for v in sorted(P-(adj[u] if u is not None else set())):
        bk(R+[v],P&adj[v],X&adj[v]); P.remove(v); X.add(v)
bk([],set(range(1<<N)),set())
maxima=sorted(set(maxima))
assert max_size==10 and len(maxima)==16
# independent size-11 impossibility by maximum-clique branch and independent count of size-10 cliques in increasing order
best=0
def expand(R,cands):
    global best
    if len(R)+len(cands)<=best: return
    if not cands:
        best=max(best,len(R)); return
    while cands:
        if len(R)+len(cands)<=best: return
        v=cands.pop()
        expand(R+[v],[u for u in cands if u in adj[v]])
        best=max(best,len(R)+1)
expand([],list(range(64)))
assert best==10
count10=0
def enumk(prefix,cands,k):
    global count10
    if len(prefix)==k:
        count10+=1; return
    need=k-len(prefix)
    for ii,v in enumerate(cands):
        if len(cands)-ii<need: break
        enumk(prefix+[v],[u for u in cands[ii+1:] if u in adj[v]],k)
enumk([],list(range(64)),10)
assert count10==16
core=set(maxima[0])
for C in maxima[1:]: core.intersection_update(C)
core=sorted(core)
assert core==[12,25,38,51]
union=sorted(set().union(*map(set,maxima)))
assert len(union)==16
print('VERIFY_OK',f'patterns={len(PA)}',f'vertices=64',f'edges={edges}',f'bk_nodes={nodes}',
      'maximal_hist='+','.join(f'{k}:{hist[k]}' for k in sorted(hist)),f'maximum={max_size}',
      f'labeled_maxima={len(maxima)}',f'independent_10cliques={count10}',
      'core='+','.join(f'{x:06b}' for x in core),f'union_size={len(union)}')
print('MAXIMA')
for C in maxima: print(' '.join(f'{x:06b}' for x in C))
