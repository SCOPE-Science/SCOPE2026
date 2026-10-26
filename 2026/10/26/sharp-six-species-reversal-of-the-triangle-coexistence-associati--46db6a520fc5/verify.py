"""Exact checks for the six-vertex competition/clustering theorem.

Python >= 3.9; standard library only. Run: python verify.py
Finite enumeration below is exhaustive for graphs with at most five vertices.
"""
from fractions import Fraction as F
from itertools import combinations, permutations
from collections import defaultdict

G0=[(0,2),(0,3),(0,4),(1,2),(1,3),(3,5)]
G1=[(0,3),(0,4),(0,5),(1,2),(1,3),(2,3)]
A0=[(0,1),(1,3),(1,4),(2,3),(2,4)]
A1=[(0,4),(1,2),(1,3),(2,3),(3,4)]
B0=[(0,2),(0,3),(0,4),(1,2),(1,3),(1,4)]
B1=[(0,1),(0,3),(0,4),(1,2),(2,3),(3,4)]

def adj(n,edges):
    a=[[0]*n for _ in range(n)]
    for u,v in edges:
        assert 0<=u<n and 0<=v<n and u!=v and a[u][v]==0
        a[u][v]=a[v][u]=1
    return a

def poly_mul(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):r[i+j]+=ai*bj
    return trim(r)

def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0:p.pop()
    return p

def poly_det(a,replace_col=None):
    """Exact polynomial determinant of I+t*A, optionally one column replaced by 1."""
    n=len(a);p=[0]*(n+1)
    for perm in permutations(range(n)):
        degree=0
        for i,j in enumerate(perm):
            if j==replace_col or i==j:continue
            if not a[i][j]:break
            degree+=1
        else:
            inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
            p[degree]+=(-1)**inversions
    return trim(p)

def determinant(mat):
    n=len(mat);m=[[F(x) for x in row] for row in mat]; d=F(1)
    for k in range(n):
        pivot=next((i for i in range(k,n) if m[i][k]),None)
        if pivot is None:return F(0)
        if pivot!=k:m[k],m[pivot]=m[pivot],m[k];d=-d
        z=m[k][k];d*=z
        for i in range(k+1,n):
            ratio=m[i][k]/z
            for j in range(k+1,n):m[i][j]-=ratio*m[k][j]
            m[i][k]=F(0)
    return d

def minors_at(a,t,psd=False):
    n=len(a)
    matrix=[[F(i==j)+t*a[i][j] for j in range(n)] for i in range(n)]
    if psd:
        for k in range(1,n+1):
            for ids in combinations(range(n),k):
                m=[[matrix[i][j] for j in ids] for i in ids]
                assert determinant(m)>=0, ('PSD principal minor',ids)
        return determinant(matrix)
    lead=[]
    for k in range(1,n+1):
        d=determinant([row[:k] for row in matrix[:k]])
        assert d>0, ('positive definiteness',k)
        lead.append(d)
    return lead

def tri_count(a):
    n=len(a)
    return sum(a[i][j]*a[j][k]*a[k][i] for i,j,k in combinations(range(n),3))

def mean_clustering(a):
    n=len(a); total=F(0)
    for i in range(n):
        neigh=[j for j in range(n) if a[i][j]]
        d=len(neigh)
        if d>=2:
            v=sum(a[j][k] for j,k in combinations(neigh,2))
            total+=F(v,d*(d-1)//2)
    return total/n

def mask_edges(n,mask):
    all_edges=list(combinations(range(n),2))
    return [e for j,e in enumerate(all_edges) if (mask>>j)&1]

def connected(a):
    n=len(a);seen={0};pending=[0]
    while pending:
        u=pending.pop()
        for v in range(n):
            if a[u][v] and v not in seen:seen.add(v);pending.append(v)
    return len(seen)==n

def signature(n,edges):
    """Canonical label by exhaustive relabeling: valid for n<=5."""
    all_edges=list(combinations(range(n),2))
    ix={e:k for k,e in enumerate(all_edges)}
    best=None
    for perm in permutations(range(n)):
        value=0
        for u,v in edges:
            edge=tuple(sorted((perm[u],perm[v])))
            value|=1<<ix[edge]
        if best is None or value<best:best=value
    return best

def verify_finite_minimality():
    grouped=defaultdict(lambda:defaultdict(set))
    totals={}
    for n in range(2,6):
        total=0
        for mask in range(1<<(n*(n-1)//2)):
            edges=mask_edges(n,mask); a=adj(n,edges)
            if not connected(a):continue
            total+=1
            degrees=tuple(sorted(sum(row) for row in a))
            triangle=tri_count(a)
            if n<=4:grouped[(n,degrees)][triangle].add(0)
            else:
                # Only canonicalize groups that can have distinct triangle counts;
                # store masks initially, convert those exceptional families below.
                grouped[(n,degrees)][triangle].add(mask)
        totals[n]=total
    variable={key for key,vs in grouped.items() if len(vs)>1}
    exceptional={(5,(1,2,2,2,3)),(5,(2,2,2,3,3))}
    assert variable==exceptional, variable
    for key,reprs in [((5,(1,2,2,2,3)),{0:A0,1:A1}),
                      ((5,(2,2,2,3,3)),{0:B0,1:B1})]:
        assert set(grouped[key])=={0,1}
        for tri,edges in reprs.items():
            expected=signature(5,edges)
            assert tri_count(adj(5,edges))==tri
            actual={signature(5,mask_edges(5,mask)) for mask in grouped[key][tri]}
            assert actual=={expected}, (key,tri,len(actual))
    print('EXHAUSTIVE finite graph enumeration: PASS, connected labeled counts',totals)
    print('Only degree families with varying triangle count:',sorted(variable))


def verify_polynomials():
    p=[1,-2,-1,1]     # 1-2t-t^2+t^3
    q=[1,2,-1,-1]    # 1+2t-t^2-t^3
    d=[1,1,-5,-3,4]  # 1+t-5t^2-3t^3+4t^4
    targets={
      'G0':(6,G0,poly_mul(p,q),[
          poly_mul(p,[1,-1,-1]),poly_mul(p,[1]),poly_mul(p,[1]),
          poly_mul(p,[1,-1,-1]),poly_mul(p,[1,1]),poly_mul(p,[1,1])]),
      'G1':(6,G1,poly_mul([1,-1],d),[
          poly_mul([1,-1],poly_mul([1,-1],[1,-1,-4])),
          poly_mul([1,-1],poly_mul([1,1],[1,-2])),
          poly_mul([1,-1],poly_mul([1,1],[1,-2])),
          poly_mul([1,-1],[1,-2,-1,4]),
          poly_mul([1,-1],[1,0,-3]),
          poly_mul([1,-1],[1,0,-3])])
    }
    for name,(n,edges,det,columns) in targets.items():
        a=adj(n,edges)
        assert poly_det(a)==trim(det),(name,'determinant',poly_det(a),det)
        for i,expected in enumerate(columns):
            assert poly_det(a,i)==trim(expected),(name,i,poly_det(a,i),expected)
    # Four five-vertex witnesses: polynomial determinant and the
    # Cramer's numerator for the coordinate that first vanishes.
    small=[
       ('A0',A0,[1,0,-5,0,2],1,poly_mul([-1,1],[-1,2,2])),
       ('A1',A1,poly_mul([1,0,-1],[1,0,-4,2]),3,
           poly_mul(poly_mul([1,-1],[1,1]),poly_mul([1,-1],[1,-2]))),
       ('B0',B0,[1,0,-6],0,[1,-3]),
       ('B1',B1,poly_mul([1,-2],[1,0,0]),4,[1,0,0,0,0])
    ]
    # For the B1 boundary, the determinant factor and all principal
    # minors are checked separately. Other small families are checked
    # directly at rational points against exact Cramer formulae.
    for name,edges,det,ix,num in small[:2]:
        a=adj(5,edges)
        assert poly_det(a)==trim(det),(name,poly_det(a),det)
        assert poly_det(a,ix)==trim(num),(name,'coordinate numerator',poly_det(a,ix),num)
    # B0: x_0=(1-3t)/(1-6t^2); B1: x_4=-1/Q(t).
    assert poly_det(adj(5,B0))==[1,0,-6]
    assert poly_det(adj(5,B0),0)==[1,-3]
    Q=[-1,-2,2,2]   # 2t^3+2t^2-2t-1
    assert poly_det(adj(5,B1))==poly_mul([-1,2],Q)
    assert poly_det(adj(5,B1),4)==trim([1,-2])
    print('EXACT polynomial/Cramer determinant certificates: PASS')

if __name__=='__main__':
    for edges,n in [(G0,6),(G1,6)]:
        assert tuple(sorted(sum(row) for row in adj(n,edges)))==(1,1,2,2,3,3)
    assert set(G0)-set(G1)=={(0,2),(3,5)}
    assert set(G1)-set(G0)=={(0,5),(2,3)}
    assert tri_count(adj(6,G0))==0
    assert tri_count(adj(6,G1))==1
    assert mean_clustering(adj(6,G0))==0
    assert mean_clustering(adj(6,G1))==F(7,18)
    print('SWAP, degrees, triangles and clustering: PASS')
    print('G1 positive definiteness at 2/5:',minors_at(adj(6,G1),F(2,5)))
    print('A0 at 3/8:',minors_at(adj(5,A0),F(3,8)))
    print('A1 at 1/2:',minors_at(adj(5,A1),F(1,2)))
    print('B0 at 1/3:',minors_at(adj(5,B0),F(1,3)))
    assert minors_at(adj(5,B1),F(1,2),psd=True)==0
    print('B1 PSD boundary at 1/2: PASS')
    verify_polynomials()
    verify_finite_minimality()
    print('ALL EXACT CHECKS PASSED')
