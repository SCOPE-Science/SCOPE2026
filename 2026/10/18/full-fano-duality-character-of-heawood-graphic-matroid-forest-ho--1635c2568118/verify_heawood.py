"""Finite exact orbit-enumeration verification for Heawood forest homology."""
from itertools import product
from collections import Counter,defaultdict
points=range(1,8)
def dot(a,b): return (a&b).bit_count()%2
lines=sorted({frozenset((a,b,a^b)) for a in points for b in points if a!=b},key=lambda s:tuple(sorted(s)))
assert len(lines)==7
line_index={line:i for i,line in enumerate(lines)}
normal={i:next(a for a in points if all(dot(a,b)==0 for b in line)) for i,line in enumerate(lines)}
by_normal={v:i for i,v in normal.items()}
edges=[(v,8+i) for v in points for i,line in enumerate(lines) if v in line]
assert len(edges)==21
edge_index={e:j for j,e in enumerate(edges)}
gl=[]
for a,b,c in product(points,repeat=3):
    if len({a,b,c,a^b,a^c,b^c,a^b^c})!=7: continue
    f=lambda x:(a if x&1 else 0)^(b if x&2 else 0)^(c if x&4 else 0)
    gl.append(({v:f(v) for v in points},{i:line_index[frozenset(map(f,line))] for i,line in enumerate(lines)}))
assert len(gl)==168
perms={}
for duality in (0,1):
    for pp,pl in gl:
        if duality==0:
            p={v:pp[v] for v in points}
            p.update({8+i:8+pl[i] for i in range(7)})
        else:
            p={v:8+by_normal[pp[v]] for v in points}
            p.update({8+i:normal[pl[i]] for i in range(7)})
        edge_perm=tuple(edge_index[tuple(sorted((p[u],p[v]),key=lambda z:z>7))] for u,v in edges)
        assert set(edge_perm)==set(range(21))
        perms[edge_perm]=duality
assert len(perms)==336
class DSU:
    def __init__(self): self.parent=list(range(15));self.size=[1]*15;self.stack=[]
    def root(self,x):
        while x!=self.parent[x]:x=self.parent[x]
        return x
    def add(self,a,b):
        a=self.root(a);b=self.root(b)
        if a==b:return False
        if self.size[a]<self.size[b]:a,b=b,a
        self.stack.append((a,b,self.size[a]));self.parent[b]=a;self.size[a]+=self.size[b]
        return True
    def undo(self,mark):
        while len(self.stack)>mark:
            a,b,old=self.stack.pop();self.parent[b]=b;self.size[a]=old
def orbits(p):
    used=set();result=[]
    for i in range(21):
        if i in used:continue
        orbit=[];j=i
        while j not in used:
            used.add(j);orbit.append(j);j=p[j]
        result.append(orbit)
    return result
def signed_trace(p):
    oo=orbits(p);dsu=DSU()
    def recur(j):
        if j==len(oo):return 1
        val=recur(j+1);mark=len(dsu.stack)
        good=True
        for k in oo[j]:
            if not dsu.add(*edges[k]):good=False;break
        if good:val-=recur(j+1)
        dsu.undo(mark)
        return val
    return -recur(0)
def main():
    table=defaultdict(lambda:[0,None])
    for p,d in perms.items():
        cycle_lengths=tuple(sorted(map(len,orbits(p)),reverse=True))
        record=table[(d,cycle_lengths)]
        val=signed_trace(p)
        record[0]+=1
        if record[1] is None:record[1]=val
        assert record[1]==val
    actual=sorted((d,cl,n,v) for (d,cl),(n,v) in table.items())
    expected=sorted([
        (0,(1,)*21,1,3152),(0,(2,)*8+(1,)*5,21,0),
        (0,(3,)*7,56,-4),(0,(4,)*4+(2,)*2+(1,),42,0),
        (0,(7,)*3,48,2),(1,(2,)*9+(1,)*3,28,60),
        (1,(6,)*3+(3,),56,0),(1,(8,)*2+(4,)+(1,),84,0),
    ])
    assert actual==expected,(actual,expected)
    total=sum(n*v for d,cl,n,v in actual)
    preserving=sum(n*v for d,cl,n,v in actual if d==0)
    assert (total,preserving)==(4704,3024)
    print('PASS: 336 exact automorphisms, eight edge-cycle types, character',[(d,cl,n,v) for d,cl,n,v in actual])
    print('PASS: full invariants',total//336,'incidence-preserving invariants',preserving//168,'duality-odd',preserving//168-total//336)
if __name__=='__main__':main()
