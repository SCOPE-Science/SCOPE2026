"""Independent exact-rational checks for edge-gradient projection on matching-deleted bicliques.

Run with Python 3 standard library: python checker.py
The finite suite is supporting evidence; the all-size proof is in RESULT.md.
"""
from fractions import Fraction as Q


def inverse(A):
    n = len(A)
    M = [[Q(A[i][j]) for j in range(n)] + [Q(int(i == j)) for j in range(n)] for i in range(n)]
    for i in range(n):
        p = next(k for k in range(i, n) if M[k][i])
        M[i], M[p] = M[p], M[i]
        v = M[i][i]
        M[i] = [x / v for x in M[i]]
        for k in range(n):
            if k != i and M[k][i]:
                c = M[k][i]
                M[k] = [a - c*b for a,b in zip(M[k],M[i])]
    return [row[n:] for row in M]


def projection(n,t):
    edges = [(i,j) for i in range(n) for j in range(n) if not(i == j and i < t)]
    B = []
    for i,j in edges:
        v = [0]*(2*n-1)
        v[i] = 1
        if j < n-1:
            v[n+j] = -1
        B.append(v)
    m=len(edges); v=2*n-1
    gram = [[sum(B[e][i]*B[e][j] for e in range(m)) for j in range(v)] for i in range(v)]
    inv = inverse(gram)
    T = [[sum(B[e][k]*inv[k][j] for k in range(v)) for j in range(v)] for e in range(m)]
    P = [[sum(T[e][k]*B[f][k] for k in range(v)) for f in range(m)] for e in range(m)]
    return edges,P


def value(n,t):
    if t == n:
        return Q(3) - Q(4,n)
    return Q(3)-Q(4,n)+Q(2*(n-2), n*(n*(n-2)+t))


def kernel(n,t,e,f):
    i,j=e;k,l=f
    D=n*(n-2)+t
    s=int(i<t)+int(j<t)
    q=int(k<t)+int(l<t)
    overlap=sum((int(i==r)+int(j==r))*(int(k==r)+int(l==r)) for r in range(t))
    common=int(i==k)+int(j==l)
    return Q(common,n)+Q(overlap,n*(n-2))-Q((n-2+s)*(n-2+q),n*(n-2)*D)


def expected_row(n,t,e):
    D=n*(n-2)+t
    s=int(e[0]<t)+int(e[1]<t)
    if s==0:return Q(3)-Q(4,n)+Q(2*(n-2),n*D)
    if s==1:return Q(3)-Q(4,n)+Q(2*(t-1)*(n-t-1),n*(n-2)*D)
    return Q(3)-Q(4,n)


def main():
    checks=0
    for n in range(3,10):
        for t in range(n+1):
            edges,P=projection(n,t)
            m=len(edges); expected=value(n,t)
            for e in range(m):
                row=P[e]
                assert sum(row) == 1
                checks+=1
                norm=sum(abs(x) for x in row)
                assert norm == expected_row(n,t,edges[e]),(n,t,edges[e],norm,expected_row(n,t,edges[e]))
                checks+=1
                for f in range(m):
                    assert row[f] == kernel(n,t,edges[e],edges[f]),(n,t,edges[e],edges[f])
                    checks+=1
            assert max(sum(abs(x) for x in row) for row in P) == expected
            checks+=1
            # A simultaneous sign witness at a norming edge attains the bound.
            norming=max(P,key=lambda row:sum(abs(x) for x in row))
            witness=[1 if x>=0 else -1 for x in norming]
            assert sum(a*b for a,b in zip(norming,witness)) == expected
            checks+=1
        vals=[value(n,t) for t in range(n+1)]
        assert all(vals[t]>vals[t+1] for t in range(n));checks+=1
        last=vals[-2]-vals[-1]
        preceding=vals[-3]-vals[-2]
        assert last/preceding==(n-2)*(n+1);checks+=1
    print('PASS: %d exact rational assertions, n=3..9, t=0..n' % checks)

if __name__=='__main__':main()
