"""Exact-rational independent checks of endpoint projection identities on Cartesian graph cylinders.
Run with Python 3.10+: python verify.py
"""
from fractions import Fraction as F
from itertools import combinations


def inverse(a):
    n=len(a)
    A=[[F(z) for z in row]+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for col in range(n):
        k=next((i for i in range(col,n) if A[i][col]),None)
        assert k is not None, 'singular matrix'
        A[col],A[k]=A[k],A[col]
        v=A[col][col]
        A[col]=[t/v for t in A[col]]
        for i in range(n):
            if i!=col and A[i][col]:
                v=A[i][col]
                A[i]=[x-v*y for x,y in zip(A[i],A[col])]
    return [row[n:] for row in A]


def solve_matrix(a,b):
    return [sum(x*y for x,y in zip(row,b)) for row in inverse(a)]


def laplacian(n,edges):
    L=[[F(0) for _ in range(n)] for _ in range(n)]
    for i,j in edges:
        L[i][i]+=1; L[j][j]+=1; L[i][j]-=1;L[j][i]-=1
    return L


def cproj(n,edges):
    # Independent exact full graph calculation from the grounded Kirchhoff system.
    L=laplacian(n,edges)
    inverse_grounded=inverse([row[:-1] for row in L[:-1]])
    E=len(edges)
    Q=[[F(0) for _ in range(E)] for _ in range(E)]
    for j,(u,v) in enumerate(edges):
        b=[F(i==u)-F(i==v) for i in range(n-1)]
        p=[sum(inverse_grounded[i][t]*b[t] for t in range(n-1)) for i in range(n-1)]+[F(0)]
        for i,(x,y) in enumerate(edges):Q[i][j]=p[x]-p[y]
    return Q


def product(n,edges,m):
    ee=[]
    for a,b in edges:
        for c in range(m):ee.append((a*m+c,b*m+c))
    for v in range(n):
        for a,b in combinations(range(m),2):ee.append((v*m+a,v*m+b))
    return n*m,ee


def norms(Q):
    N=len(Q)
    q=max(sum(abs(Q[i][j]) for i in range(N)) for j in range(N))
    c=max(F(1)+sum(abs(Q[i][j]) for i in range(N))-2*Q[j][j] for j in range(N))
    return q,c


def compressed(n,edges,m):
    # A completely different small-matrix derivation of the graph-product columns.
    L=laplacian(n,edges)
    S=inverse([[L[i][j]+(m if i==j else 0) for j in range(n)] for i in range(n)])
    q=cproj(n,edges)
    E=len(edges)
    qnorm=F(0);cnorm=F(0);Dmax=F(0)
    def dot(e,vec):return vec[e[0]]-vec[e[1]]
    for e0,(u,v) in enumerate(edges):
        p=[S[x][u]-S[x][v] for x in range(n)]
        horizontal=F(m-1)*sum(map(abs,p))
        for f0,f in enumerate(edges):
            h=dot(f,p)
            horizontal+=abs(h+(q[f0][e0]-h)/m)
            horizontal+=F(m-1,m)*abs(q[f0][e0]-h)
        d=q[e0][e0]/m+F(m-1,m)*dot((u,v),p)
        qnorm=max(qnorm,horizontal);cnorm=max(cnorm,1+horizontal-2*d)
        Dmax=max(Dmax,d)
    for x in range(n):
        vertical=F(2*(m-1),m)+2*sum(abs(S[u][x]-S[v][x]) for u,v in edges)
        d=2*S[x][x]
        qnorm=max(qnorm,vertical);cnorm=max(cnorm,1+vertical-2*d)
        Dmax=max(Dmax,d)
    return qnorm,cnorm,Dmax


def isconnected(n,ee):
    reached={0}
    for _ in range(n):
        reached|={v for u,v in ee if u in reached}
        reached|={u for u,v in ee if v in reached}
    return len(reached)==n


def main():
    # Unrestricted labeled connected graphs on 2, 3, 4 vertices (not just symmetric examples).
    count=0
    for n in [2,3,4]:
        pairs=list(combinations(range(n),2))
        for mask in range(1,1<<len(pairs)):
            ee=[e for j,e in enumerate(pairs) if mask>>j&1]
            if not isconnected(n,ee):continue
            for m in [4,5,6]:
                q,c,D=compressed(n,ee,m)
                assert D<=F(3,m+2),(n,ee,m,D)
                assert c-q>=F(m-4,m+2),(n,ee,m,q,c)
                if n>2:assert c-q>F(m-4,m+2)
                count+=1
    print('Compressed exact-rational all connected labeled graphs n<=4:',count,'PASS')
    # Both derivations checked for a diverse set; fully numerical-free.
    families={
        'edge':(2,[(0,1)]),
        'three-path':(3,[(0,1),(1,2)]),
        'triangle':(3,[(0,1),(1,2),(0,2)]),
        'square':(4,[(0,1),(1,2),(2,3),(0,3)]),
        'star':(4,[(0,1),(0,2),(0,3)]),
        'diamond':(4,[(0,1),(0,2),(0,3),(1,2),(2,3)]),
    }
    full=0
    for name,(n,ee) in families.items():
        for m in [3,4,5]:
            N, prod=product(n,ee,m)
            q1,c1=norms(cproj(N,prod))
            q2,c2,D=compressed(n,ee,m)
            assert (q1,c1)==(q2,c2),(name,m,(q1,c1),(q2,c2))
            full+=1
    print('Direct full-graph Kirchhoff vs compressed resolvent:',full,'PASS')
    # Sharp saturation at K2 for all m>=4 and m=3 obstruction.
    for m in range(4,65):
        q,c,_=compressed(2,[(0,1)],m)
        assert q==F(3*m,m+2)
        assert c==F(4*(m-1),m+2)
    q,c,_=compressed(2,[(0,1)],3)
    assert (q,c)==(F(9,5),F(5,3)),(q,c)
    print('Sharp K2 identities m=4..64, and failure at m=3: PASS')
    # The exact transfer-current columns imply the claimed asymptotics;
    # the rational checks below only corroborate them, not serve as proof.
    for name,(n,ee) in families.items():
        qh,_=norms(cproj(n,ee))
        q,c,_=compressed(n,ee,1024)
        assert abs(q-(qh+2))<F(1,20)
        assert abs(c-(qh+3))<F(1,20)
    print('All fixed-graph large-clique checks: PASS')

if __name__=='__main__':main()
