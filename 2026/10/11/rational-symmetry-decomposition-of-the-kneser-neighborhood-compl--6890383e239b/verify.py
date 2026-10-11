"""Reproducible exact topological and equivariant computation for KG(6,2)."""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations
from math import factorial,prod

N=6
V=tuple(combinations(range(N),2))
assert len(V)==15
ADJ=tuple(tuple(j for j,b in enumerate(V) if not set(a).intersection(b)) for a in V)
assert all(len(ns)==6 for ns in ADJ)
F=set()
for ns in ADJ:
    for r in range(1,len(ns)+1):
        F.update(sum(1<<j for j in t) for t in combinations(ns,r))
F=sorted(F,key=lambda m:(m.bit_count(),m))
FD={m:m.bit_count()-1 for m in F}
assert Counter(FD.values())=={0:15,1:105,2:260,3:225,4:90,5:15}
assert len(F)==710

# Staged coordinate matching, with critical simplex verification independent of Morse boundary.
remaining=set(F)
matched={}
pivot_counts=[]
for v in reversed(range(len(V))):
    bit=1<<v
    pairs=[(sigma,sigma|bit) for sigma in sorted(remaining) if not sigma&bit and sigma|bit in remaining]
    for a,b in pairs:
        assert a in remaining and b in remaining and a not in matched and b not in matched
        assert (b^a).bit_count()==1 and FD[b]==FD[a]+1
        matched[a]=b;matched[b]=a
        remaining.remove(a);remaining.remove(b)
    pivot_counts.append((v,len(pairs)))
assert len(matched)==690
assert Counter(FD[c] for c in remaining)=={0:1,2:19}

# Complete Hasse directed graph; reverse only matched upward incidences.
indegree={f:0 for f in F};out={f:[] for f in F};arrow_count=0
for top in F:
    for j in range(len(V)):
        if not top&(1<<j):continue
        bot=top^(1<<j)
        if bot==0:continue
        assert bot in FD
        if matched.get(bot)==top:
            u,w=bot,top
        else:
            u,w=top,bot
        out[u].append(w);indegree[w]+=1;arrow_count+=1
q=deque(sorted(f for f in F if not indegree[f]));processed=0
while q:
    v=q.popleft();processed+=1
    for w in out[v]:
        indegree[w]-=1
        if indegree[w]==0:q.append(w)
assert processed==len(F),f'Nonacyclic matching: visited {processed}/{len(F)}'

@lru_cache(None)
def partitions(n,upper=None):
    if n==0:return ((),)
    ans=[]
    for i in range(min(n,upper if upper is not None else n),0,-1):
        for p in partitions(n-i,i):ans.append((i,)+p)
    return tuple(ans)

P=partitions(6)
def representative(cycle_type):
    perm=list(range(6));off=0
    for n in cycle_type:
        segment=list(range(off,off+n))
        for i in range(n):perm[segment[i]]=segment[(i+1)%n]
        off+=n
    return perm

def signature(images):
    return -1 if sum(images[i]>images[j] for i in range(len(images)) for j in range(i+1,len(images)))%2 else 1

character=[];euler_chain_rows=[]
for cycle_type in P:
    p=representative(cycle_type)
    action=[V.index(tuple(sorted((p[a],p[b])))) for a,b in V]
    chain_trace=[0]*6
    for sigma in F:
        members=[i for i in range(15) if sigma>>i&1]
        moved=[action[i] for i in members]
        if sorted(moved)!=members:continue
        inverse={x:i for i,x in enumerate(members)}
        chain_trace[len(members)-1]+=signature([inverse[x] for x in moved])
    lefschetz=sum((-1)**k*val for k,val in enumerate(chain_trace))
    character.append(lefschetz-1) # H0 has character 1.
    euler_chain_rows.append(chain_trace)
assert character==[-1,-1,1,1,1,1,1,-1,-1,-5,19],character

@lru_cache(None)
def young_char(shape,cycles):
    if not cycles:return int(not shape)
    k=cycles[0]
    old={(i,j) for i,n in enumerate(shape) for j in range(n)}
    ans=0
    for sub in partitions(len(old)-k):
        if len(sub)>len(shape) or any(sub[i]>shape[i] for i in range(len(sub))):continue
        leftover=old-{(i,j) for i,n in enumerate(sub) for j in range(n)}
        assert len(leftover)==k
        reached={next(iter(leftover))};todo=list(reached)
        while todo:
            i,j=todo.pop()
            for r in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if r in leftover and r not in reached:reached.add(r);todo.append(r)
        if len(reached)!=k:continue
        if any((i+1,j) in leftover and (i,j+1) in leftover and (i+1,j+1) in leftover for i,j in leftover):continue
        ans+=(-1)**(len({i for i,j in leftover})-1)*young_char(sub,cycles[1:])
    return ans

class_sizes=[]
for c in P:
    ct=Counter(c)
    class_sizes.append(factorial(6)//prod(i**n*factorial(n) for i,n in ct.items()))
assert sum(class_sizes)==720
T=[[young_char(a,b) for b in P] for a in P]
assert all(sum(class_sizes[k]*T[i][k]*T[j][k] for k in range(len(P)))==(720 if i==j else 0) for i in range(len(P)) for j in range(len(P)))
mult=[sum(class_sizes[k]*character[k]*T[i][k] for k in range(len(P)))//720 for i in range(len(P))]
assert mult==[1 if x in ((3,1,1,1),(2,2,1,1)) else 0 for x in P]
assert all(sum(class_sizes[k]*character[k]*T[i][k] for k in range(len(P)))%720==0 for i in range(len(P)))

print('F-vector',tuple(sum(FD[f]==i for f in F) for i in range(6)))
print('Morse pivot counts',pivot_counts)
print('Morse critical dims',dict(Counter(FD[c] for c in remaining)))
print('Hasse arrows',arrow_count,'topologically sorted',processed)
print('S6 conjugacy type : trace',list(zip(P,character)))
print('S6 irreducible multiplicities',[(p,n) for p,n in zip(P,mult) if n])
print('verified')
