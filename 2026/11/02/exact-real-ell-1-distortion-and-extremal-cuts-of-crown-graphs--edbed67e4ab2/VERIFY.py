"""Exact supplementary checks for finite crown-graph distortion theorem.
Run: python3 VERIFY.py (Python 3 standard library only).
The theorem for all n is established by the accompanying symbolic proof.
"""
from collections import deque
from fractions import Fraction
from itertools import combinations


def dist_crown(n):
    graph = [[] for _ in range(2*n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                graph[i].append(n+j)
                graph[n+j].append(i)
    result = []
    for a in range(2*n):
        d = [-1]*(2*n)
        d[a] = 0
        q = deque([a])
        while q:
            v = q.popleft()
            for w in graph[v]:
                if d[w] == -1:
                    d[w] = d[v]+1
                    q.append(w)
        result.append(d)
    return result


def sep_sums(n, cut):
    x = [(cut >> i) & 1 for i in range(n)]
    y = [(cut >> (n+i)) & 1 for i in range(n)]
    k, l = sum(x), sum(y)
    t = sum(x[i]*y[i] for i in range(n))
    S_numer = k*(n-k)+l*(n-l)
    U_numer = (n-1)*(k+l)-2*k*l+2*t
    return k,l,t,S_numer,U_numer


def zero_type(n,k,l,t):
    # Classify nontrivial equality cuts up to complementation.
    if (k,l) in ((0,0),(n,n)):
        return True
    if k+l > n:
        k,l,t = n-k,n-l,n-k-l+t
    v,z = k+l,k-l
    if n%2 == 0:
        return v == n and z == 0 and t == 0
    return t == 0 and ((v == n and abs(z)==1) or (v == n-1 and z == 0))


checks = 0
for n in range(3,13):
    D = dist_crown(n)
    for a in range(2*n):
        for b in range(2*n):
            if a == b:
                expected = 0
            elif (a < n) == (b < n):
                expected = 2
            else:
                expected = 3 if a % n == b % n else 1
            assert D[a][b] == expected, ('distance',n,a,b,D[a][b],expected)
            checks += 1

for n in range(3,9):
    h = (n+1)//2
    for bits in range(1 << (2*n)):
        k,l,t,S_num,U_num = sep_sums(n,bits)
        gap_num = h*U_num-(h-1)*S_num
        assert gap_num >= 0, ('cut inequality',n,bits,gap_num)
        assert (gap_num == 0) == zero_type(n,k,l,t), ('equality type',n,bits,gap_num)
        checks += 2

for n in range(3,14):
    h = (n+1)//2
    k = n//2
    total = 0
    sep = [[0]*(2*n) for _ in range(2*n)]
    for tup in combinations(range(n),k):
        I = set(tup)
        x = [int(i in I) for i in range(n)]
        label = x+[1-v for v in x]
        total += 1
        for a in range(2*n):
            for b in range(a+1,2*n):
                sep[a][b] += int(label[a]!=label[b])
    W = Fraction(2*(2*h-1),h)
    distortion = Fraction(2*(h-1),h)
    for a in range(2*n):
        for b in range(a+1,2*n):
            embed = W*Fraction(sep[a][b],total)
            source = 2 if (a<n)==(b<n) else (3 if a%n==b%n else 1)
            if (a<n)==(b<n):
                assert embed == 2
            elif a%n==b%n:
                assert embed == W
            else:
                assert embed == distortion
            assert source <= embed <= source*distortion,('embedding',n,a,b,embed,source,distortion)
            checks += 2

print('CHECK_OK',checks,'exact integer/rational assertions for distances, cuts, equality cases, and embeddings, n<=13')
