"""Independent finite checks for support inequalities and contact witnesses.

These calculations corroborate, but cannot certify, universal convex-geometric
statements. The accompanying analytical proof handles every permitted graph.
"""
import itertools
import math
import random

RNG = random.Random(183459)


def support(edges, v):
    return sum(math.hypot(v[a], v[b]) for a, b in edges)


def degrees(edges, n):
    d = [0] * n
    for i, j in edges:
        d[i] += 1
        d[j] += 1
    return d


def examples():
    for n in range(3, 13):
        yield (f'path{n}', n, [(i, i + 1) for i in range(n - 1)])
        yield (f'star{n}', n, [(0, j) for j in range(1, n)])
    for p, q in [(1, 2), (1, 7), (2, 3), (2, 6), (3, 4), (3, 5), (4, 4), (4, 7)]:
        yield (f'K{p}_{q}', p + q, [(i, p + j) for i in range(p) for j in range(q)])
    for k in range(3, 8):
        n = 2*k
        yield (f'cycle{n}', n, [(i, (i + 1) % n) for i in range(n)])
    # Incidence graph of K4: left vertices 0,...,3 degree 3;
    # right vertices 4,...,9 degree 2. Connected and noncomplete.
    pairs = list(itertools.combinations(range(4), 2))
    yield ('K4_incidence', 10, [(i, 4+j) for j, (a,b) in enumerate(pairs) for i in (a,b)])


def close(a,b,scale=1.0):
    if abs(a-b) > 2e-10 * max(scale,abs(a),abs(b),1.0):
        raise AssertionError((a,b))


support_tests = contact_tests = covariance_tests = 0
for name, n, edges in examples():
    d = degrees(edges, n)
    assert min(d) > 0
    m = len(edges)
    for _ in range(250):
        u = [RNG.uniform(-2.5, 2.5) for _ in range(n)]
        lo = math.sqrt(sum((d[i]*u[i])**2 for i in range(n)))
        hi = math.sqrt(m * sum(d[i]*u[i]**2 for i in range(n)))
        h = support(edges,u)
        assert lo <= h + 1e-9, (name, 'lower support')
        assert h <= hi + 1e-9, (name, 'upper support')
        support_tests += 1
    for i in range(n):
        u = [0.0]*n
        u[i] = 1.0
        close(support(edges,u), d[i])
        contact_tests += 1
    if name.startswith('K') and name != 'K4_incidence':
        # Kp_q, with p and q deduced from the name.
        p = int(name[1:].split('_')[0]); q = n-p
    elif name.startswith('cycle'):
        p = n//2; q = n//2
    elif name == 'K4_incidence':
        p = 4; q = 6
    else:
        if not name.startswith('star'):
            continue
        p = 1; q = n-1
    A = list(range(p)) if not name.startswith('cycle') else list(range(0,n,2))
    B = [v for v in range(n) if v not in A]
    assert len(A)==p and len(B)==q
    assert all((i in A) != (j in A) for i,j in edges)
    assert len({d[i] for i in A}) == len({d[j] for j in B}) == 1
    for _ in range(45):
        theta = RNG.uniform(0,math.pi/2)
        sig = [RNG.choice([-1,1]) for _ in range(n)]
        u = [sig[i]*(math.cos(theta) if i in A else math.sin(theta)) for i in range(n)]
        x = [d[i]*u[i] for i in range(n)]
        h = support(edges,u)
        close(h,m)
        close(sum(x[i]*u[i] for i in range(n)),h)
        close(sum(x[i]*x[i]/(m*d[i]) for i in range(n)),1)
        contact_tests += 1
    # A sign design at cos^2(theta)=p/n is a tight frame in
    # coordinates normalized by the enclosing ellipsoid semiaxes.
    t2 = p/n
    for i in range(n):
        component_sq = (d[i]*(t2 if i in A else 1-t2))/m
        close(component_sq,1/n)
        covariance_tests += 1

print(f'PASS support_inequalities={support_tests}; exact_axis_and_outer_contacts={contact_tests}; normalized_covariance_entries={covariance_tests}; analytic scope all finite connected graphs (John), connected biregular bipartite graphs (Lowner).')
