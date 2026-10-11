#!/usr/bin/env python3
"""Direct PL-chain computation for separated unordered pairs on metric stars.

Triangulates the actual polygonal configuration space and compares its mod-two
homology with the proposed incidence-graph model. Python 3 standard library only.
"""
from fractions import Fraction as F
from itertools import combinations
from random import Random


def hull(pts):
    pts=sorted(set(pts))
    if len(pts)<=1:return pts
    def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lo=[]
    for p in pts:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    hi=[]
    for p in pts[::-1]:
        while len(hi)>=2 and cross(hi[-2],hi[-1],p)<=0:hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]


def poly(Li,Lj,r):
    q=[]
    for x in [F(0),Li]:
        for y in [F(0),Lj]:
            if x+y>=r:q.append((x,y))
        y=r-x
        if 0<=y<=Lj:q.append((x,y))
    for y in [F(0),Lj]:
        x=r-y
        if 0<=x<=Li:q.append((x,y))
    return hull(q)


def simplices(L,r):
    L=list(map(F,L));r=F(r)
    vertices=set();edges=set();faces=set()
    def vid(i,j,p):
        x,y=p
        if y==0 and x>=r: return ('a',i,x)
        if x==0 and y>=r: return ('a',j,y)
        return ('q',i,j,x,y)
    def add(s):
        s=tuple(sorted(set(s)))
        if len(s)==1:vertices.add(s[0])
        if len(s)>=2:
            for a in s:vertices.add(a)
            for a,b in combinations(s,2):edges.add((a,b))
        if len(s)==3:faces.add(s)
    k=len(L)
    for i,j in combinations(range(k),2):
        pp=poly(L[i],L[j],r)
        if not pp:continue
        q=[vid(i,j,p) for p in pp]
        if len(q)==1:add(q)
        elif len(q)==2:add(q)
        else:
            for t in range(1,len(q)-1):add((q[0],q[t],q[t+1]))
    for i in range(k):
        if L[i]<r:continue
        # Sorted particle radii on the same arm.
        a= ('a',i,r)
        b= ('a',i,L[i])
        c= ('t',i,L[i]-r,L[i])
        add((a,b,c))
    return vertices,edges,faces


def rank_mod2(rows):
    basis={}
    for v in rows:
        while v:
            p=v.bit_length()-1
            if p in basis:v^=basis[p]
            else:
                basis[p]=v
                break
    return len(basis)


def homology_simplices(L,r):
    verts,edges,faces=simplices(L,r)
    if not verts:return (0,0,0,len(verts),len(edges),len(faces))
    e=sorted(edges);e_idx={x:i for i,x in enumerate(e)}
    tri=[]
    for f in faces:
        mask=0
        for x in combinations(f,2):mask^=1<<e_idx[tuple(sorted(x))]
        tri.append(mask)
    rank_d2=rank_mod2(tri)
    # Union-find for rank of the graph boundary map.
    par={v:v for v in verts}
    def find(v):
        while par[v]!=v:
            par[v]=par[par[v]]
            v=par[v]
        return v
    for a,b in e:par[find(a)]=find(b)
    c=len({find(v) for v in verts})
    return (c,len(e)-len(verts)+c-rank_d2,len(faces)-rank_d2,len(verts),len(e),len(faces))


def model(L,r):
    L=list(map(F,L));r=F(r);k=len(L)
    long=[i for i,x in enumerate(L) if x>=r]
    short=[i for i,x in enumerate(L) if x<r]
    feasible=[(i,j) for i,j in combinations(range(k),2) if L[i]+L[j]>=r]
    c=(1 if long else 0)+sum(1 for i,j in feasible if i in short and j in short)
    b1=(len(long)-1)*(len(long)-2)//2 if len(long)>=2 else 0
    return c,b1,0


def check(L,r):
    b=homology_simplices(L,r)
    expected=model(L,r)
    assert b[:3]==expected,(L,r,b,expected)
    return b


def run():
    import sys
    rng=Random(912103)
    counter=0
    selected=[]
    for k in range(3,9):
        cases=[]
        for t in range(30):
            if t<10:
                L=[F(rng.randint(1,6)) for _ in range(k)]
            else:
                L=[F(rng.randint(2,13),rng.choice([1,2,3])) for _ in range(k)]
            crit={F(0)}|set(L)|{L[i]+L[j] for i,j in combinations(range(k),2)}
            rs=sorted({x for x in crit if x>0}|{x+F(1,1000) for x in crit}|{(a+b)/2 for a,b in zip(sorted(crit),sorted(crit)[1:])})
            cases.append((L,rs))
        for L,rs in cases:
            for r in rs:
                b=check(L,r)
                counter+=1
                if k==4 and len(selected)<10:selected.append((list(map(str,L)),str(r),b[:3]))
    print('VERIFY_OK',counter,'polygonal-mod-two-chain comparisons, k=3..8')
    for r in selected[:6]:print('SAMPLE',r)

if __name__=='__main__':run()
