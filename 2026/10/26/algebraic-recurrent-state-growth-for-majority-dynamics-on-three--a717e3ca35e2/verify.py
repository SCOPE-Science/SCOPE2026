#!/usr/bin/env python3
"""Exact majority recurrence census on cylindrical three-row strips.
Standalone: CPython standard library only. Computational certificate for stated finite matrices.
"""
from collections import Counter, deque
from math import gcd


def majority_column(left, middle, right):
    ans = 0
    for row in range(3):
        votes = ((left >> row) & 1) + ((right >> row) & 1)
        d = 2
        if row > 0:
            votes += (middle >> (row - 1)) & 1
            d += 1
        if row < 2:
            votes += (middle >> (row + 1)) & 1
            d += 1
        old = (middle >> row) & 1
        bit = 1 if 2 * votes > d else (0 if 2 * votes < d else old)
        ans |= bit << row
    return ans


def transition_graph(two_time):
    width = 64 if two_time else 8
    adj = [[] for _ in range(width * width)]
    for a in range(width):
        for b in range(width):
            ab = width * a + b
            for c in range(width):
                if two_time:
                    xa, ya = a & 7, a >> 3
                    xb, yb = b & 7, b >> 3
                    xc, yc = c & 7, c >> 3
                    admissible = (majority_column(xa, xb, xc) == yb
                                  and majority_column(ya, yb, yc) == xb)
                else:
                    admissible = majority_column(a, b, c) == b
                if admissible:
                    adj[ab].append(width * b + c)
    return adj


def cyclic_components(adj):
    N = len(adj)
    rev = [[] for _ in range(N)]
    for u, targets in enumerate(adj):
        for v in targets:
            rev[v].append(u)
    seen = bytearray(N)
    order = []
    for seed in range(N):
        if seen[seed]:
            continue
        seen[seed] = 1
        stack = [(seed, iter(adj[seed]))]
        while stack:
            v, it = stack[-1]
            w = next(it, None)
            if w is None:
                order.append(v)
                stack.pop()
            elif not seen[w]:
                seen[w] = 1
                stack.append((w, iter(adj[w])))
    seen = bytearray(N)
    components = []
    for seed in reversed(order):
        if seen[seed]:
            continue
        seen[seed] = 1
        component = [seed]
        stack = [seed]
        while stack:
            for v in rev[stack.pop()]:
                if not seen[v]:
                    seen[v] = 1
                    component.append(v)
                    stack.append(v)
        if len(component) > 1 or seed in adj[seed]:
            components.append(sorted(component))
    return sorted(components, key=lambda c: (-len(c), c))


def induced(adj, vertices):
    loc = {v:i for i, v in enumerate(vertices)}
    return [[loc[v] for v in adj[u] if v in loc] for u in vertices]


def period_of_strong_component(adj):
    dist = [-1] * len(adj)
    dist[0] = 0
    todo = deque([0])
    while todo:
        u = todo.popleft()
        for v in adj[u]:
            if dist[v] < 0:
                dist[v] = dist[u] + 1
                todo.append(v)
    assert -1 not in dist
    period = 0
    for u, targets in enumerate(adj):
        for v in targets:
            period = gcd(period, abs(dist[u] + 1 - dist[v]))
    return period


def trace_powers(adj, nmax):
    N = len(adj)
    counts = [0] * (nmax + 1)
    for root in range(N):
        vector = [0] * N
        vector[root] = 1
        for power in range(1, nmax + 1):
            nxt = [0] * N
            for u, destinations in enumerate(adj):
                z = vector[u]
                if z:
                    for v in destinations:
                        nxt[v] += z
            vector = nxt
            counts[power] += vector[root]
    return counts


def characteristic_det_coeffs(trace, N):
    # Newton identities: det(I-z A)=sum c[k] z**k.
    c = [1]
    for k in range(1, N+1):
        s = sum(c[k-j] * trace[j] for j in range(1, k+1))
        assert s % k == 0, (k, s)
        c.append(-s // k)
    return c


def multiply_factors(factors):
    result = [1]
    for coeff, power in factors:
        for _ in range(power):
            c = [0] * (len(result)+len(coeff)-1)
            for i,a in enumerate(result):
                for j,b in enumerate(coeff):
                    c[i+j] += a*b
            result = c
    return result


def pf_bounds(adj, lower_num, upper_num, denom, niterate=60):
    v = [1] * len(adj)
    for _ in range(niterate):
        v = [sum(v[j] for j in edges) for edges in adj]
    av = [sum(v[j] for j in edges) for edges in adj]
    assert min(v)>0
    assert all(lower_num*q < denom*p < upper_num*q for p,q in zip(av, v))


def independent_direct_counts(n):
    neighbours = []
    for col in range(n):
        for row in range(3):
            inds = [(3*((col-1)%n)+row), (3*((col+1)%n)+row)]
            if row>0: inds.append(3*col+row-1)
            if row<2: inds.append(3*col+row+1)
            neighbours.append(tuple(inds))
    def F(x):
        y=0
        for k,inds in enumerate(neighbours):
            votes=sum((x>>j)&1 for j in inds)
            old=(x>>k)&1
            b = (1 if 2*votes>len(inds) else 0 if 2*votes<len(inds) else old)
            y |= b<<k
        return y
    q=p=0
    for x in range(1 << (3*n)):
        y=F(x)
        if y==x:q+=1
        if F(y)==x:p+=1
    return q,p


def main():
    A = transition_graph(False)
    B = transition_graph(True)
    ca = cyclic_components(A)
    cb = cyclic_components(B)
    assert Counter(map(len, ca)) == Counter({20:1, 1:2})
    assert Counter(map(len, cb)) == Counter({200:1, 2:10, 1:2})
    AA = induced(A, ca[0])
    BB = induced(B, cb[0])
    assert period_of_strong_component(AA) == period_of_strong_component(BB) == 1
    qcore = trace_powers(AA, 200)
    pcore = trace_powers(BB, 200)
    dqa = characteristic_det_coeffs(qcore,20)
    dpb = characteristic_det_coeffs(pcore,200)
    # Factored polynomials are checked independently from trace-derived exact determinants.
    # Coefficients are listed from low powers to high powers of z.
    factors_q = [([ -1,1 ],3),([1,1],2),([-1,2,0,1],1),([1,-1,1,1],1),([-1,2,-3,3,0,1],1)]
    factors_p = [([-1,1],3),([1,1],1),([1,0,1],1),([-1,1,1,1],1),
                 ([1,2,3,1,-5,-1,1],1),([1,-2,3,-1,-5,1,1],1),
                 ([1,2,1,-5,-7,-3,9],1),([1,3,1,-4,-8,-4,0,1],1),
                 ([-1,3,-1,-4,8,-4,0,1],1),
                 ([-1,-3,-4,-2,7,3,7,-10,9],1),
                 ([-1,3,-9,13,-1,11,10,-5,40,-6,5],1),
                 ([-1,5,-3,-10,12,-30,41,-26,97,-28,-104,28,2,5],1)]
    # Products may have constant -1: match determinant after normalizing to constant 1.
    for actual, factors, dim in [(dqa,factors_q,20),(dpb,factors_p,200)]:
        prod = multiply_factors(factors)
        assert prod[0] in (-1,1)
        prod = [prod[0]*v for v in prod]
        assert actual == prod + [0]*(dim+1-len(prod)), (dim,[(i,x,y) for i,(x,y) in enumerate(zip(actual, prod)) if x!=y][:5])
    pf_bounds(AA,22055,22057,10000)
    pf_bounds(BB,34578,34580,10000)
    expected = [(3,8,62),(4,36,402),(5,78,768),(6,146,2678),(7,260,4348),(8,572,21906)]
    for n,q,p in expected:
        assert 2 + qcore[n]==q
        assert 2 + (20 if n%2==0 else 0) + pcore[n] ==p
    for n,q,p in expected[:4]:
        assert independent_direct_counts(n)==(q,p), (n,independent_direct_counts(n),(q,p))
    print('VERIFY_OK')
    print('SCC_COUNTS Q={20:1,1:2}, P={200:1,2:10,1:2}; both large cores primitive')
    print('DET_DEGREES_Q_16_P_72; exact factor products verified by Newton identities')
    print('PF_INTERVALS_Q=(2.2055,2.2057), P=(3.4578,3.4580)')
    print('COUNTS n,Q_n,P_n:',expected)
    print('BRUTE_FORCE n=3..6 agrees; all integer assertions passed')

if __name__ == '__main__':
    main()
