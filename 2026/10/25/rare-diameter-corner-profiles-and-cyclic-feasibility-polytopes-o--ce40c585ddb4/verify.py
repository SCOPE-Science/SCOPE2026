"""Reproducibility checks for rare-distance laws on odd regular polygons.

Requires Python >=3.10, standard library only. Theorems are analytical;
these finite tests do not certify limiting assertions.
"""
import math
import random
from itertools import combinations


def geometry(k):
    assert k >= 5 and k % 2 == 1
    m = (k - 1) // 2
    small = math.sin(math.pi / (2 * k))
    large = math.sin(3 * math.pi / (2 * k))
    rate = 1 / math.sin(math.pi / k)
    edges = []
    for i in range(k):
        j = (i + m) % k
        # 2*i and 2*i+1 are the outgoing and incoming rays at vertex i.
        for type_a, type_b in [('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')]:
            u = 2 * i + (type_a == 'B')
            v = 2 * j + (type_b == 'B')
            c = small if (type_a, type_b) == ('B', 'A') else large
            edges.append((min(u, v), max(u, v), c))
    return small, large, rate, edges


def test_incidence(k):
    small, large, rate, edges = geometry(k)
    assert len(edges) == 4 * k
    pairs = [(a, b) for a, b, _ in edges]
    assert len(set(pairs)) == len(pairs)
    assert sum(c == small for a, b, c in edges) == k
    degree = [0] * (2 * k)
    small_degree = [0] * (2 * k)
    adjacency = [set() for _ in degree]
    for u, v, c in edges:
        degree[u] += 1
        degree[v] += 1
        adjacency[u].add(v)
        adjacency[v].add(u)
        if c == small:
            small_degree[u] += 1
            small_degree[v] += 1
    assert all(d == 4 for d in degree)
    assert all(d == 1 for d in small_degree)
    triangles = sum((v in adjacency[u] and w in adjacency[u] and w in adjacency[v])
                    for u, v, w in combinations(range(2 * k), 3))
    assert triangles == 0
    return small, large, rate, edges


def small_tail_coefficients(k):
    g, b, lam, _ = geometry(k)
    return (k * lam * lam / 8 * (1 / g**2 + 3 / b**2),
            k * lam**3 / 24 * (1 / g**3 + 6 / b**3 + 9 / (g*b*b)))


def in_cyclic_polytope(v, r):
    k = len(v)
    for i in range(k):
        s = v[i] + v[(i + 1) % k]
        if not r <= s <= 2-r:
            return False
        if v[(i - 1) % k] - v[(i + 1) % k] > 1-r:
            return False
    return True


def conditional_b_compatible(U, S, k, q, g, b):
    # B_i = U_i * S_i, A_(i+m) = (1-U_i)*S_i.
    m = (k-1)//2
    A = [0.0]*k
    B = [0.0]*k
    for i in range(k):
        B[i] = U[i]*S[i]
        A[(i+m)%k] = (1-U[i])*S[i]
    for i in range(k):
        j = (i+m)%k
        for e in (A[i]+A[j], A[i]+B[j], B[i]+B[j]):
            if b*e <= g*q:
                return False
    return True


def test_cyclic_constraint_identity(k, repetitions=2500):
    """Check the exact large-threshold angular polytope at zero excess."""
    rng = random.Random(6011+k)
    g, b, _, _ = geometry(k)
    m=(k-1)//2
    for _ in range(repetitions):
        U=[rng.random() for _ in range(k)]
        V=[U[(j*m)%k] for j in range(k)]
        assert in_cyclic_polytope(V, g/b) == conditional_b_compatible(U,[1.0]*k,k,1.0,g,b)


def simulate(k=5, trials=60000):
    rng = random.Random(31173+k)
    g, b, lam, edges = test_incidence(k)
    r = g/b
    q = 80.0 / lam
    count_poly = 0
    count_cond = 0
    small_count = 0
    small_t = 0.025 if k == 5 else 0.010
    for _ in range(trials):
        U = [rng.random() for _ in range(k)]
        # Permuting coordinates by multiplication by m preserves uniformity.
        count_poly += in_cyclic_polytope(U, r)
        S = []
        for i in range(k):
            if rng.random() < lam*q / (1 + lam*q):
                W = rng.expovariate(lam)
            else:
                W = rng.expovariate(lam)+rng.expovariate(lam)
            S.append(q+W)
        count_cond += conditional_b_compatible(U, S, k, q, g, b)
        X = [rng.expovariate(lam) for _ in range(2*k)]
        Z = 2*min(c*(X[i]+X[j]) for i, j, c in edges)
        small_count += Z <= small_t
    p = count_poly/trials
    cond = count_cond/trials
    alpha, beta = small_tail_coefficients(k)
    approx = alpha*small_t**2 - beta*small_t**3
    observed = small_count/trials
    print(f'k={k} g={g:.9f} b={b:.9f} rate={lam:.9f}')
    print(f'  small-tail observed={observed:.6f} two-term={approx:.6f}')
    print(f'  cyclic-volume estimate={p:.6f} conditional estimate={cond:.6f}')
    assert abs(cond-p) < 0.030, 'conditional localization diagnostic failed'
    assert abs(observed-approx) < 0.015, 'small-tail diagnostic failed'


if __name__ == '__main__':
    for k in [5, 7, 9, 11, 13, 17, 21]:
        test_incidence(k)
        test_cyclic_constraint_identity(k)
    for k in [5, 7]:
        simulate(k)
    print('All finite checks passed; asymptotic validity follows from the proof, not these tests.')
