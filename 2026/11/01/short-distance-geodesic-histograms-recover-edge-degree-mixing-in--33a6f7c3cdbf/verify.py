#!/usr/bin/env python3
"""Independent exact-rational finite regression for a local metric-graph CDF theorem."""
import itertools
from fractions import Fraction as Q

def connected(edges,n):
    seen={0};todo=[0]
    while todo:
        u=todo.pop()
        for a,b in edges:
            if a==u and b not in seen:seen.add(b);todo.append(b)
            if b==u and a not in seen:seen.add(a);todo.append(a)
    return len(seen)==n

def distances(edges,n):
    ans=[]
    for src in range(n):
        d=[10000]*n;d[src]=0;todo=[src]
        for u in todo:
            for a,b in edges:
                v=b if a==u else (a if b==u else None)
                if v is not None and d[v]>d[u]+1:d[v]=d[u]+1;todo.append(v)
        ans.append(d)
    return ans

def clip(poly,A,B,C):
    if not poly:return []
    out=[]
    def value(p):return A*p[0]+B*p[1]-C
    for i,p in enumerate(poly):
        q=poly[(i+1)%len(poly)];vp,vq=value(p),value(q)
        if vp<=0:out.append(p)
        if (vp<0<vq) or (vp>0>vq):
            t=vp/(vp-vq);out.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
        elif vp>0 and vq==0:out.append(q)
    return list(dict.fromkeys(out))

def area(poly):
    if len(poly)<3:return Q(0)
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1]-poly[i][1]*poly[(i+1)%len(poly)][0] for i in range(len(poly)))/2)

def pair_area(e,f,dist,r):
    if e==f:return 2*r-r*r if r<1 else Q(1)
    forms=[]
    for i,u in enumerate(e):
        for j,v in enumerate(f):
            forms.append((Q(1 if i==0 else -1),Q(1 if j==0 else -1),r-Q(i+j+dist[u][v])))
    out=Q(0)
    for k in range(1,5):
        for idx in itertools.combinations(range(4),k):
            poly=[(Q(0),Q(0)),(Q(1),Q(0)),(Q(1),Q(1)),(Q(0),Q(1))]
            for j in idx:poly=clip(poly,*forms[j])
            out+=(-1)**(k+1)*area(poly)
    return out

def check(edges,n):
    m=len(edges);d=[0]*n
    for a,b in edges:d[a]+=1;d[b]+=1
    s=sum(x*(x-1) for x in d);h=sum(d[a]*d[b] for a,b in edges);R=h-2*s
    dist=distances(edges,n)
    for r in (Q(1,3),Q(1),Q(6,5),Q(3,2)):
        lhs=sum(pair_area(e,f,dist,r) for e in edges for f in edges)/m**2
        rhs=(2*m*r+(Q(s,2)-m)*r*r+(R*(r-1)**2 if r>1 else 0))/m**2
        assert lhs==rhs,(edges,r,lhs,rhs)
    return m,s,h

def main():
    tested=0
    for n in range(2,6):
        poss=list(itertools.combinations(range(n),2))
        for mask in range(1,1<<len(poss)):
            if n==5 and mask%11!=0:continue
            edges=[e for j,e in enumerate(poss) if mask>>j&1]
            if connected(edges,n):check(edges,n);tested+=1
    A=[(0,4),(1,2),(1,3),(2,3),(3,4)]
    B=[(0,1),(1,3),(1,4),(2,3),(2,4)]
    assert check(A,5)==(5,12,24)
    assert check(B,5)==(5,12,23)
    print('VERIFY_OK graphs',tested+2,'radii_per_graph',4,'exact_area_comparisons',(tested+2)*4)
if __name__=='__main__':main()
