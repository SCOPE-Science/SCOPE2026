"""Exact rational checks of the canonical cut/cycle projections of K_m square C_n."""
from fractions import Fraction as F


def solve(A, b):
    size = len(b)
    rows = [[F(z) for z in a] + [F(x)] for a, x in zip(A, b)]
    for j in range(size):
        p = next((k for k in range(j, size) if rows[k][j]), None)
        assert p is not None
        rows[j], rows[p] = rows[p], rows[j]
        factor = rows[j][j]
        for k in range(j, size + 1):
            rows[j][k] /= factor
        for i in range(j + 1, size):
            factor = rows[i][j]
            if factor:
                for k in range(j, size + 1):
                    rows[i][k] -= factor * rows[j][k]
    answer = [F(0)] * size
    for j in range(size - 1, -1, -1):
        answer[j] = rows[j][size] - sum(rows[j][k] * answer[k] for k in range(j + 1, size))
    return answer


def make_graph(m, n):
    vertices = m*n
    def vertex(a,j): return j*m+a
    edges = []
    for j in range(n):
        for a in range(m):
            for b in range(a+1,m):
                edges.append((vertex(a,j),vertex(b,j),'clique'))
    for j in range(n):
        for a in range(m):
            edges.append((vertex(a,j),vertex(a,(j+1)%n),'rim'))
    L = [[0]*vertices for _ in range(vertices)]
    for x,y,_ in edges:
        L[x][x] += 1
        L[y][y] += 1
        L[x][y] -= 1
        L[y][x] -= 1
    return edges,L


def formulas(m,n):
    A = [[(m+2 if i==j else 0) - (int(j==(i+1)%n)+int(j==(i-1)%n)) for j in range(n)] for i in range(n)]
    R = solve(A, [1]+[0]*(n-1))
    assert sum(R)==F(1,m)
    assert R[0]>F(1,m*n), R[n//2]<=F(1,m*n)
    assert all(R[j]>=R[j+1] for j in range(n//2))
    lo=R[n//2]
    TV=R[0]-lo
    W=sum(abs(z-F(1,m*n)) for z in R)
    return {
       'clique': (2*F(m-1,m)+4*TV, F(3)-F(2,m)-4*lo),
       'rim': (2-F(2,m*n)+(m-1)*(W-2*lo), 1+(m-1)*(W+2*TV)),
       'R':R
    }


def check(m,n):
    edges,L=make_graph(m,n)
    total=m*n
    val=formulas(m,n)
    Lr=[row[:-1] for row in L[:-1]]
    for idx,(x,y,kind) in enumerate(edges):
        source=[0]*(total-1)
        if x<total-1: source[x]+=1
        if y<total-1: source[y]-=1
        u=solve(Lr,source)+[F(0)]
        Q=[u[v]-u[w] for v,w,_ in edges]
        C=[F(int(i==idx))-z for i,z in enumerate(Q)]
        actual=(sum(abs(z) for z in Q),sum(abs(z) for z in C))
        assert actual==val[kind],(m,n,kind,actual,val[kind])
    assert val['rim'][0]>val['clique'][0] and val['rim'][1]>val['clique'][1]
    if m>=4 or (m==3 and n==5):
        assert val['rim'][1]>val['rim'][0]
    elif m==3 and n>=6:
        assert val['rim'][1]<val['rim'][0]
    print('PASS',m,n,'columns',len(edges),'cut',val['rim'][0], 'cycle',val['rim'][1])


if __name__=='__main__':
    for m,n in [(3,5),(3,6),(3,7),(4,5),(4,6),(5,5),(6,5)]:
        check(m,n)
