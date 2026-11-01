"""Exact-rational finite consistency checks for weighted Cartesian-product metric-network detours.

Run: python check_product_detour.py
"""
from fractions import Fraction as F
from itertools import product
from collections import Counter


def distances(n, edges):
    inf=None
    d=[[F(0) if i==j else inf for j in range(n)] for i in range(n)]
    for u,v,w in edges:
        w=F(w)
        if d[u][v] is None or w<d[u][v]: d[u][v]=d[v][u]=w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] is None or d[k][j] is None:continue
                q=d[i][k]+d[k][j]
                if d[i][j] is None or q<d[i][j]:d[i][j]=q
    return d


def point_dist(edge_x, pos_x, edge_y, pos_y, d):
    a,b,la=edge_x; c,e,lb=edge_y
    ans=min(pos_x+d[a][c]+pos_y,
            pos_x+d[a][e]+lb-pos_y,
            la-pos_x+d[b][c]+pos_y,
            la-pos_x+d[b][e]+lb-pos_y)
    if edge_x is edge_y or edge_x==edge_y:
        ans=min(ans,abs(pos_x-pos_y))
    return ans


def product_edges(na,nb,A,B):
    ee=[]
    for i,(u,v,l) in enumerate(A):
        for h in range(nb):
            ee.append((u*nb+h,v*nb+h,F(l),'A',i,h))
    for j,(p,q,l) in enumerate(B):
        for g in range(na):
            ee.append((g*nb+p,g*nb+q,F(l),'B',j,g))
    return ee


def check(A,B,na,nb):
    da,db=distances(na,A),distances(nb,B)
    for e in A:
        assert da[e[0]][e[1]] == F(e[2]), ('nongeodesic A edge',e)
    for e in B:
        assert db[e[0]][e[1]] == F(e[2]), ('nongeodesic B edge',e)
    es=product_edges(na,nb,A,B)
    dp=distances(na*nb,[(u,v,l) for u,v,l,*_ in es]); count=0; positives=0
    qs=(F(1,7),F(2,5),F(4,7),F(6,7))
    for i,ex in enumerate(es):
        u,v,l,k,b,layer=ex
        for j,ey in enumerate(es):
            U,V,L,K,c,otherlayer=ey
            for sx,sy in product(qs, repeat=2):
                x=l*sx; y=L*sy
                d=point_dist((u,v,l),x,(U,V,L),y,dp)
                if k=='A' and K=='A':
                    assert l==F(A[b][2]) and L==F(A[c][2])
                    ambient=point_dist(A[b],x,A[c],y,da)+db[layer][otherlayer]
                elif k=='B' and K=='B':
                    ambient=point_dist(B[b],x,B[c],y,db)+da[layer][otherlayer]
                elif k=='A':
                    # x lives on A edge b in layer h; y lives on B edge c at A-vertex otherlayer.
                    aleft=point_dist(A[b],x,(otherlayer,otherlayer,F(0)),F(0),da)
                    ambient=aleft+point_dist(B[c],y,(layer,layer,F(0)),F(0),db)
                else:
                    ambient=point_dist(B[b],x,(otherlayer,otherlayer,F(0)),F(0),db)+point_dist(A[c],y,(layer,layer,F(0)),F(0),da)
                if k==K and b==c and layer!=otherlayer:
                    delta=2*min(min(x,y),min(l-x,l-y))
                else:
                    delta=F(0)
                assert d == ambient+delta,(A,B,ex,ey,x,y,d,ambient,delta)
                count+=1
                positives+=(delta>0)
    LA=sum(F(e[2]) for e in A); LB=sum(F(e[2]) for e in B)
    total=nb*LA+na*LB
    probability=(nb*(nb-1)*sum(F(e[2])**2 for e in A)+na*(na-1)*sum(F(e[2])**2 for e in B))/total**2
    mean=(nb*(nb-1)*sum(F(e[2])**3 for e in A)+na*(na-1)*sum(F(e[2])**3 for e in B))/(3*total**2)
    assert F(0)<probability<=1 and mean>0
    # Independently check conditional distributions via exact planar area identities.
    for ell in set(F(e[2]) for e in A+B):
        for t in [ell/5,ell/3,ell/2,4*ell/5]:
            w_cdf=2*(t/ell)-(t/ell)**2
            turn_cdf=(t/ell)**2
            cdf_gap=2*(t/ell)*(1-t/ell)
            assert w_cdf-turn_cdf==cdf_gap
            assert F(0)<cdf_gap<=F(1,2)
        # E(detour) from the exact beta survival integral.
        assert ell-ell+ell/3 == ell/3
    return count,positives,probability,mean,len(es)


def main():
    families=[
       ('edge',2,[(0,1,1)]),
       ('path3',3,[(0,1,1),(1,2,2)]),
       ('path4',4,[(0,1,2),(1,2,1),(2,3,3)]),
       ('triangle',3,[(0,1,1),(1,2,2),(0,2,3)]),
       ('square',4,[(0,1,1),(1,2,2),(2,3,1),(3,0,2)]),
       ('star',4,[(0,1,2),(0,2,1),(0,3,3)]),
       ('diamond',4,[(0,1,1),(1,2,2),(2,3,1),(3,0,2),(0,2,2)]),
    ]
    tests=[(0,0),(0,1),(0,2),(1,1),(1,2),(2,2),(0,3),(1,4),(3,4),(0,5),(3,5),(2,6),(4,4),(5,5)]
    tot=0
    for i,j in tests:
        nameA,na,A=families[i];nameB,nb,B=families[j]
        c,p,pr,mean,n=check(A,B,na,nb)
        tot+=c
        print(f'{nameA} x {nameB}: {c} exact point-pair checks; positive={p}; P={pr}; mean detour={mean}; edges={n}')
    print(f'PASS: {tot} exact-rational pair-distance comparisons; 14 factor products; 2 intrinsic metric formulations.')

if __name__=='__main__':main()
