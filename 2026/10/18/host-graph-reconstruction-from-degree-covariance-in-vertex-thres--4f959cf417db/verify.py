"""Exact, standard-library checks for degree covariance in vertex-threshold graphs."""
from fractions import Fraction as F
from itertools import combinations


def qmatrix(n,edges):
    q=[[0]*n for _ in range(n)]
    for u,v in edges:
        q[u][u]+=1
        q[v][v]+=1
        q[u][v]+=1
        q[v][u]+=1
    return q


def expected_cov_direct(n, edges):
    # P(Y_e=1)=1/2; P(Y_e=Y_f=1) = 1/2 for e=f,
    # 1/3 for distinct edges meeting at a vertex, and 1/4 otherwise.
    m=len(edges)
    c=[[F(0) for _ in range(m)] for _ in range(m)]
    for i,e in enumerate(edges):
        for j,f in enumerate(edges):
            p2= F(1,2) if i==j else (F(1,3) if set(e)&set(f) else F(1,4))
            c[i][j]=p2-F(1,4)
    s=[[F(0) for _ in range(n)] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            s[u][v]=sum((c[i][j] for i,e in enumerate(edges) if u in e
                        for j,f in enumerate(edges) if v in f),F(0))
    return s


def formula(q):
    n=len(q)
    return [[F(q[i][j]+sum(q[i][k]*q[k][j] for k in range(n)),12)
             for j in range(n)] for i in range(n)]


def rank_rat(a):
    a=[[F(x) for x in row] for row in a]
    n=len(a)
    r=0
    for j in range(n):
        k=next((k for k in range(r,n) if a[k][j]),None)
        if k is None: continue
        a[r],a[k]=a[k],a[r]
        pivot=a[r][j]
        a[r]=[t/pivot for t in a[r]]
        for k in range(r+1,n):
            c=a[k][j]
            if c:
                a[k]=[a[k][h]-c*a[r][h] for h in range(n)]
        r+=1
        if r==n: break
    return r


def bipartite_components(n,edges):
    a=[[] for _ in range(n)]
    for u,v in edges:
        a[u].append(v)
        a[v].append(u)
    colors=[None]*n
    b=0
    for v in range(n):
        if colors[v] is not None: continue
        colors[v]=0
        queue=[v]
        good=True
        for u in queue:
            for w in a[u]:
                if colors[w] is None:
                    colors[w]=1-colors[u]
                    queue.append(w)
                elif colors[w]==colors[u]:
                    good=False
        b+=good
    return b


def main():
    cases=0
    for n in range(1,6):
        all_edges=list(combinations(range(n),2))
        for mask in range(1<<len(all_edges)):
            edges=[e for i,e in enumerate(all_edges) if mask>>i & 1]
            q=qmatrix(n,edges)
            assert expected_cov_direct(n,edges)==formula(q),(n,edges)
            assert n-rank_rat(formula(q))==bipartite_components(n,edges)
            # From sigma, recover Q using the unique PSD root of I+48 sigma.
            # The target root is exactly I+2Q; direct product checks avoid
            # numerical square roots and need no external packages.
            s=formula(q)
            r=[[int(i==j)+2*q[i][j] for j in range(n)] for i in range(n)]
            assert [[sum(r[i][k]*r[k][j] for k in range(n)) for j in range(n)] for i in range(n)] == [
                [int(i==j)+48*s[i][j] for j in range(n)] for i in range(n)]
            # I+2Q is PD: x^T(I+2Q)x = |x|^2 + 2 sum_edges(x_u+x_v)^2.
            # Thus r is the principal root, yielding Q exactly.
            cases+=1
    print(f'VERIFY_OK {cases} host graphs, exact edge-pair sums, rank, square-root inverse')

if __name__=='__main__':
    main()
