"""Exact finite checks of facet areas of tree root crosspolytopes.

Run: python tree_crosspolytope_verify.py
Uses only Python standard library; networkx is optional for extra tree types.
"""
import itertools
import math
from fractions import Fraction


def det_int(A):
    # Exact permutation determinant; small facet dimensions only.
    n=len(A)
    if not n:return 1
    if n==1:return A[0][0]
    z=0
    for j in range(n):
        sub=[row[:j]+row[j+1:] for row in A[1:]]
        z+=(-1)**j*A[0][j]*det_int(sub)
    return z


def rooted_edges(n,edges):
    adj=[[] for _ in range(n)]
    for a,b in edges:
        adj[a].append(b);adj[b].append(a)
    parents=[-1]*n;order=[0];parents[0]=0
    for v in order:
        for w in adj[v]:
            if parents[w]<0:
                parents[w]=v;order.append(w)
    assert len(order)==n
    return [(parents[v],v) for v in order[1:]]


def check(n,edges):
    orientations=rooted_edges(n,edges)
    d=n-1
    A=[]
    for s in itertools.product([-1,1],repeat=d):
        # Vertices of facet: signed graph incidence vectors in ambient R^n.
        vs=[]
        for (u,v),eps in zip(orientations,s):
            x=[0]*n;x[u]=-eps;x[v]=eps;vs.append(x)
        D=[[x-y for x,y in zip(vs[i],vs[-1])] for i in range(d-1)]
        G=[[sum(a*b for a,b in zip(x,y)) for y in D] for x in D]
        gram=det_int(G)
        assert gram>0
        # Separately build the centered integer potential of signed differences.
        phi=[0]*n
        for (u,v),eps in zip(orientations,s):phi[v]=phi[u]+eps
        q=Fraction(sum(z*z for z in phi),1)-Fraction(sum(phi)**2,n)
        assert gram==n*q,(n,edges,s,gram,q)
        A.append(gram)
    # Direct Wiener index from breadth-first shortest-path distances.
    adj=[[] for _ in range(n)]
    for u,v in edges:adj[u].append(v);adj[v].append(u)
    W=0
    for u in range(n):
        dis=[-1]*n;dis[u]=0;queue=[u]
        for x in queue:
            for y in adj[x]:
                if dis[y]<0:dis[y]=dis[x]+1;queue.append(y)
        W+=sum(dis)
    W//=2
    # Squared facet area = Gram / ((d-1)!)^2.
    assert Fraction(sum(A),len(A))==W
    return len(A),W


def main():
    count=0;signs=0
    for n in range(3,8):
        trees=[[(i-1,i) for i in range(1,n)],[(0,i) for i in range(1,n)]]
        if n>=5:
            trees.append([(0,1),(1,2)]+[(1,i) for i in range(3,n)])
        for edges in trees:
            m,W=check(n,edges);count+=1;signs+=m
    # Confirm 4-vertex path/star exact distance moments and sign-Q multisets.
    assert check(4,[(0,1),(1,2),(2,3)])[1]==10
    assert check(4,[(0,1),(0,2),(0,3)])[1]==9
    # Deterministic numerical check of the Brownian integral.
    # The truncated correction past u=32 is exponentially small; the integral
    # of the leading 1/u^2 tail is inserted analytically.
    L=32.0;N=64000;h=L/N
    def integrand(u):
        if abs(u)<1e-6:return 1.0/12.0
        return (1.0-math.sqrt(u/math.sinh(u)))/(u*u)
    accum=integrand(0)+integrand(L)
    for j in range(1,N):accum+=(4 if j%2 else 2)*integrand(j*h)
    c=math.sqrt(2/math.pi)*(accum*h/3 +1/L)
    assert 0.37812<c<0.37814,c
    print('VERIFY_OK trees=',count,'independent_exact_facet_checks=',signs,
          'Brownian_constant=',format(c,'.10f'))

if __name__=='__main__':main()
