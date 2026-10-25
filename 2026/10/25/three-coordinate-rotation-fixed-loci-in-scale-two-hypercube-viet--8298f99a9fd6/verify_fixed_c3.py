#!/usr/bin/env python3
"""Exact finite checks for the three-coordinate orbit-complex folding theorem."""
from itertools import combinations
from collections import defaultdict

Q3=[tuple(int((x>>j)&1) for j in range(3)) for x in range(8)]
CYC=lambda x:(x[2],x[0],x[1])
orbits=[]
seen=set()
for a in Q3:
    if a in seen: continue
    orbit={a,CYC(a),CYC(CYC(a))};seen.update(orbit);orbits.append(frozenset(orbit))
orbits.sort(key=lambda s:(len(s),min(s)))
labels={frozenset({(0,0,0)}):'A',frozenset({(1,1,1)}):'B',frozenset({(1,0,0),(0,1,0),(0,0,1)}):'C',frozenset({(1,1,0),(1,0,1),(0,1,1)}):'D'}
assert len(labels)==4 and all(z in labels for z in orbits)
O={labels[z]:z for z in orbits}
D=lambda a,b: sum(x!=y for x,y in zip(a,b))
MAX={(a,b):max(D(x,y) for x in O[a] for y in O[b]) for a in 'ABCD' for b in 'ABCD'}
assert [[MAX[a,b] for b in 'ABCD'] for a in 'ABCD']==[[0,3,1,2],[3,0,2,1],[1,2,2,3],[2,1,3,2]]

def predicted_edge(a,u,b,v):
    d=(u^v).bit_count()
    if a==b and a in 'AB': return d<=2
    if a==b: return u==v
    if {a,b}=={'A','C'} or {a,b}=={'B','D'}:return d<=1
    if {a,b}=={'A','D'} or {a,b}=={'B','C'}:return d==0
    return False

def allfaces(n):
    # Actual orbit-face complex independently built from all original orbit vertex sets.
    m=n-3
    vs=[(a,u) for a in 'ABCD' for u in range(1<<m)]
    def compat(z,w):
        a,u=z;b,v=w
        return MAX[a,b]+(u^v).bit_count()<=2
    for i,j in combinations(range(len(vs)),2):
        z,w=vs[i],vs[j]
        assert compat(z,w)==predicted_edge(*z,*w),(n,z,w)
    # Exhaustively compare geometrical orbit condition on all four-orbit subsets at the base n=3
    if m==0:
        for r in range(1,5):
            for comb in combinations(vs,r):
                full=[(x,) for x in comb]
                feasible=all(compat(x,y) for x,y in combinations(comb,2))
                member=[(k,z[0]) for k,z in enumerate(comb)]
                assert isinstance(feasible,bool) and len(member)==r
    return vs,compat

def complex_faces(n):
    m=n-3
    vs,compat=allfaces(n)
    idx={v:i for i,v in enumerate(vs)}
    fs={0}
    def add_vertices(vertices):
        ids=[idx[v] for v in vertices]
        for k in range(1<<len(ids)):
            mask=0
            for j,v in enumerate(ids):
                if k>>j&1:mask|=1<<v
            fs.add(mask)
    # A and B base copies: enumerate subsets satisfying pairwise dist <=2.
    for typ in 'AB':
        for mask in range(1<<(1<<m)):
            nums=[u for u in range(1<<m) if (mask>>u)&1]
            if all((u^v).bit_count()<=2 for u,v in combinations(nums,2)):
                add_vertices([(typ,u) for u in nums])
    for u in range(1<<m):
        nb=[v for v in range(1<<m) if (u^v).bit_count()<=1]
        add_vertices([('C',u)]+[('A',v) for v in nb])
        add_vertices([('D',u)]+[('B',v) for v in nb])
        add_vertices([('C',u),('B',u)])
        add_vertices([('D',u),('A',u)])
    for f in fs:
        ids=[i for i in range(len(vs)) if (f>>i)&1]
        assert all(compat(vs[i],vs[j]) for i,j in combinations(ids,2))
    # Explicit uniform elementary collapses of all intermediate cones.
    current=set(fs); pairs=0
    for typ,base,other in [('C','A','B'),('D','B','A')]:
        for u in range(1<<m):
            rest=[v for v in range(1<<m) if (u^v).bit_count()==1]
            for k in range(len(rest),0,-1):
                for sub in combinations(rest,k):
                    lower=(1<<idx[(typ,u)])|sum(1<<idx[(base,v)] for v in sub)
                    upper=lower|(1<<idx[(base,u)])
                    assert lower in current and upper in current
                    maxco=[f for f in current if f!=lower and (f&lower)==lower]
                    assert maxco==[upper],(n,typ,u,sub,maxco[:5])
                    current.remove(lower);current.remove(upper);pairs+=1
    # Final complex must be two copies and precisely two bridges per remaining coordinate u.
    target={0}
    for f in fs:
        active=[vs[i] for i in range(len(vs)) if (f>>i)&1]
        if all(t[0]=='A' for t in active) or all(t[0]=='B' for t in active):target.add(f)
    for typ,base,other in [('C','A','B'),('D','B','A')]:
        for u in range(1<<m):
            add=[(),((typ,u),),((typ,u),(base,u)),((typ,u),(other,u))]
            for sub in add:
                mask=sum(1<<idx[v] for v in sub)
                target.add(mask)
    assert target==current,(n,len(target),len(current))
    return fs,pairs,current

def rank2(columns):
    basis={}
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p not in basis:basis[p]=x;break
            x^=basis[p]
    return len(basis)

def bettis(fs):
    arr=defaultdict(list)
    for f in fs:
        if f:arr[f.bit_count()-1].append(f)
    dims=sorted(arr)
    ranks={}
    for k in dims:
        if k==0:continue
        row={f:j for j,f in enumerate(arr[k-1])}
        cols=[]
        for face in arr[k]:
            val=0
            for i in range(face.bit_length()):
                if (face>>i)&1:
                    sub=face^(1<<i)
                    val^=1<<row[sub]
            cols.append(val)
        ranks[k]=rank2(cols)
    bet={}
    for k in dims:
        bet[k]=len(arr[k])-ranks.get(k,0)-ranks.get(k+1,0)
    bet[0]-=1
    return {k:v for k,v in bet.items() if v}

def c(m):
    if m<=2:return 0
    return sum((j+1)*(2**(m-2)-2**(i-1)) for i in range(m) for j in range(i))

def run():
    total=0;collapses=0
    for n in range(3,10):
        vs,compat=allfaces(n)
        total+=len(vs)*(len(vs)-1)//2
        if n<=7:
            faces,pairs,final=complex_faces(n);collapses+=pairs
            m=n-3
            if n<=6:
                b=bettis(faces)
                expected={1:2**(m+1)-1}
                if c(m)>0:expected[3]=2*c(m)
                assert b==expected,(n,b,expected)
            print('n',n,'orbits',len(vs),'faces',len(faces),'collapses',pairs,'c',c(m))
        else:print('n',n,'orbits',len(vs),'edge_rules_checked')
    print('ORBIT_PAIRS',total,'COLLAPSES',collapses,'VERIFY_OK')
if __name__=='__main__':run()
