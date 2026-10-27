"""Exact-rational independent finite certificates for squared-cycle cut/cycle norms.
No external dependencies. Run: python3 squared_cycle_checker.py
"""
from fractions import Fraction as F


def solve(a, b):
    n = len(b)
    a = [[F(x) for x in row] for row in a]
    b = [F(x) for x in b]
    for j in range(n):
        pivot = next(i for i in range(j, n) if a[i][j])
        a[j], a[pivot] = a[pivot], a[j]
        b[j], b[pivot] = b[pivot], b[j]
        z = a[j][j]
        for i in range(j + 1, n):
            if a[i][j]:
                t = a[i][j] / z
                for k in range(j + 1, n):
                    a[i][k] -= t * a[j][k]
                a[i][j] = 0
                b[i] -= t * b[j]
    x = [F(0)] * n
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - sum(a[i][j] * x[j] for j in range(i+1, n))) / a[i][i]
    return x


def get_k(n):
    a = [[F(3 if i == j else 0) + F((j == (i+1)%n) + (j == (i-1)%n))
          for j in range(n)] for i in range(n)]
    b = [F(i == 0) for i in range(n)]
    k = solve(a, b)
    assert all(3*k[i] + k[(i-1)%n] + k[(i+1)%n] == b[i] for i in range(n))
    return k


def orbit_columns(k):
    n = len(k)
    e1 = [k[i] - F(1, 5*n) for i in range(n)]
    f1 = [k[i] + k[(i+1)%n] - F(2, 5*n) for i in range(n)]
    e2 = [k[i] + k[(i-1)%n] - F(2, 5*n) for i in range(n)]
    f2 = [F(i == 0) - k[i] - F(4, 5*n) for i in range(n)]
    A1 = sum(map(abs,e1)) + sum(map(abs,f1))
    A2 = sum(map(abs,e2)) + sum(map(abs,f2))
    R1 = k[0] - F(1, 5*n)
    R2 = 2*(k[0]+k[1]) - F(4, 5*n)
    P1 = A1 + 1 - 2*R1
    P2 = A2 + 1 - 2*R2
    return A1,A2,P1,P2,R1,R2,(e1,f1,e2,f2)


def direct_column(n, step):
    # Independently solve the graph Laplacian rather than using its factorization.
    a = [[F(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        for h in (1,2):
            j=(i+h)%n
            a[i][i]+=1; a[j][j]+=1
            a[i][j]-=1; a[j][i]-=1
    b = [F(int(i==0)-int(i==step)) for i in range(n)]
    x = solve([row[:-1] for row in a[:-1]], b[:-1]) + [F(0)]
    return [[x[i]-x[(i+h)%n] for i in range(n)] for h in (1,2)]


def main():
    finite = 0
    direct = 0
    margins = []
    for n in range(7, 36):
        k = get_k(n)
        a1,a2,p1,p2,r1,r2,(e1,f1,e2,f2) = orbit_columns(k)
        assert a2>a1 and p2>p1, (n,a1,a2,p1,p2)
        assert F(0)<r1<1 and F(0)<r2<1
        margins.append((n,a2-a1,p2-p1))
        finite += 1
        if n <= 12:
            assert direct_column(n,1) == [e1,f1]
            assert direct_column(n,2) == [e2,f2]
            direct += 2
    print('EXACT_SQUARED_CYCLE_OK finite_sizes=%d direct_graph_columns=%d' % (finite,direct))
    print('smallest_Q_gap:', min(margins,key=lambda z:z[1]))
    print('smallest_P_gap:', min(margins,key=lambda z:z[2]))
    for n in (7,8,10,16,35):
        a1,a2,p1,p2,*_=orbit_columns(get_k(n))
        print(n,'Q',a2,'P',p2,'Q_short',a1,'P_short',p1)

if __name__=='__main__': main()
