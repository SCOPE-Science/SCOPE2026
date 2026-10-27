"""Self-contained exact-arithmetic reproducibility checks for a two-machine EF1 approximation theorem.
Only finite test sets are checked; the universal guarantee is proved analytically.
"""
from fractions import Fraction as Q
from itertools import product, combinations
import random

def overlaps(a,b):
    return a[0]<b[1] and b[0]<a[1]

def feasible_two(items):
    # Interval Helly: a set is two-machine schedulable iff max active count <=2.
    t=sorted({v for a,b,w in items for v in (a,b)})
    return all(sum(a<=x<b for a,b,w in items)<=2 for x in t)

def path_components(items):
    n=len(items)
    adj=[set() for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if overlaps(items[i],items[j]):
                adj[i].add(j);adj[j].add(i)
    assert all(len(neighbors)<=2 for neighbors in adj)
    seen=set(); comps=[]
    for i in range(n):
        if i in seen:continue
        comp=set();todo=[i]
        while todo:
            v=todo.pop()
            if v in comp:continue
            comp.add(v);todo.extend(adj[v]-comp)
        seen.update(comp)
        assert len(comp)==1 or sum(len(adj[v]) for v in comp)==2*(len(comp)-1)
        st=next((v for v in comp if len(adj[v])<=1),None)
        assert st is not None
        arr=[]; prev=-1;cur=st
        while cur is not None:
            arr.append(cur)
            nxt=list(adj[cur]-{prev})
            assert len(nxt)<=1
            prev,cur=cur,(nxt[0] if nxt else None)
        assert len(arr)==len(comp)
        comps.append(arr)
    return comps,adj

def fair(w,a,b):
    wa=sum((w[i] for i in a),Q(0)); wb=sum((w[i] for i in b),Q(0))
    return wa<=wb+max([w[i] for i in a],default=Q(0)) and wb<=wa+max([w[i] for i in b],default=Q(0))

def construct(items):
    assert all(b-a==1 for a,b,w in items)
    assert feasible_two(items)
    comps,adj=path_components(items)
    deletion=set()
    for p in comps:
        classes=[[v for k,v in enumerate(p) if k%3==r] for r in range(3)]
        r=min(range(3),key=lambda r:sum((items[i][2] for i in classes[r]),Q(0)))
        deletion.update(classes[r])
    rem=set(range(len(items)))-deletion
    assert all(len(adj[i]&rem)<=1 for i in rem)
    chunks=[]; seen=set()
    for i in sorted(rem):
        if i in seen:continue
        c={i}|(adj[i]&rem)
        assert len(c)<=2
        chunks.append(sorted(c));seen|=c
    # Greedy orient each edge or singleton to reduce absolute total-weight difference.
    A=[];B=[];D=Q(0)
    for c in chunks:
        if len(c)==1:
            i=c[0]
            if D>=0:B.append(i);D-=items[i][2]
            else:A.append(i);D+=items[i][2]
        else:
            i,j=c
            x=items[i][2];y=items[j][2]
            if abs(D+x-y)<=abs(D-x+y):
                A.append(i);B.append(j);D+=x-y
            else:
                A.append(j);B.append(i);D+=y-x
    w=[x[2] for x in items]
    assert all(not overlaps(items[i],items[j]) for U in (A,B) for i,j in combinations(U,2))
    assert fair(w,A,B)
    assert sum((w[i] for i in A+B),Q(0))*3>=sum(w,Q(0))*2
    return A,B,deletion

def brute_opt(items):
    n=len(items); best=Q(0);best_s=[]
    for code in product((0,1,2),repeat=n):
        A=[i for i,c in enumerate(code) if c==1]
        B=[i for i,c in enumerate(code) if c==2]
        if any(overlaps(items[i],items[j]) for U in (A,B) for i,j in combinations(U,2)):continue
        w=sum((items[i][2] for i in A+B),Q(0))
        if w>best:best=w;best_s=[A,B]
    return best,best_s

def brute_fair_opt(items):
    n=len(items); best=Q(0)
    for code in product((0,1,2),repeat=n):
        A=[i for i,c in enumerate(code) if c==1]
        B=[i for i,c in enumerate(code) if c==2]
        if any(overlaps(items[i],items[j]) for U in (A,B) for i,j in combinations(U,2)):continue
        if not fair([x[2] for x in items],A,B):continue
        best=max(best,sum((items[i][2] for i in A+B),Q(0)))
    return best

def tests():
    assertions=0
    # Exhaust all small weighted paths: construction from optimal feasible set itself.
    for length in range(1,9):
        # Unit intervals [i/2,i/2+1): consecutive edges, no triangles.
        for weights in product((Q(1),Q(2),Q(3)),repeat=length):
            items=[(Q(i,2),Q(i,2)+1,weights[i]) for i in range(length)]
            assert feasible_two(items)
            construct(items); assertions+=1
    rng=random.Random(20261023)
    for n in range(1,9):
        for run in range(65):
            start=[Q(rng.randrange(0,11),2) for _ in range(n)]
            weights=[Q(rng.randrange(1,13),rng.randrange(1,5)) for _ in range(n)]
            items=[(a,a+1,w) for a,w in zip(start,weights)]
            opt,ab=brute_opt(items)
            chosen=[items[i] for i in ab[0]+ab[1]]
            construct(chosen)
            actual=brute_fair_opt(items)
            assert actual*3>=opt*2
            assertions+=1
    # Three equal-duration jobs give the sharp limiting obstruction.
    for denominator in (3,5,10,100,10000):
        eps=Q(1,denominator)
        t=[(Q(0),Q(1),Q(1)),(Q(1,2),Q(3,2),Q(1)-eps),(Q(1),Q(2),Q(1))]
        opt,_=brute_opt(t);fo=brute_fair_opt(t)
        assert opt==3-eps and fo==2
        assertions+=1
    return assertions

if __name__=='__main__':
    print('PASS',tests(),'finite assertions (not an exhaustive proof)')
