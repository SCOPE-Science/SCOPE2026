"""Independent finite-field commutation-graph checks for three-block unipotent groups.

Run with: python3 verify_graph.py
Only the Python standard library is used.
"""
from collections import deque
from itertools import product


def field_mul(a, b, q):
    if q != 4:
        return (a * b) % q
    r = 0
    if b & 1:
        r ^= a
    if b & 2:
        r ^= a << 1
    if r & 8:
        r ^= (0b1011 << 0)  # x^3 = x+1 (intermediate overflow)
    if r & 4:
        r ^= 0b111  # x^2 + x + 1 = 0
    return r


def add(a,b,q):
    return a ^ b if q == 4 else (a + b) % q


def sub(a,b,q):
    return a ^ b if q == 4 else (a - b) % q


def commutes(x, y, a, b, c, q):
    A, B = x
    D, E = y
    for i in range(a):
        for j in range(c):
            left = right = 0
            for k in range(b):
                left = add(left, field_mul(A[i*b+k], E[k*c+j], q), q)
                right = add(right, field_mul(D[i*b+k], B[k*c+j], q), q)
            if left != right:
                return False
    return True


def graph_stats(a,b,c,q):
    elements = [(A,B) for A in product(range(q), repeat=a*b)
                for B in product(range(q), repeat=b*c) if any(A) or any(B)]
    n = len(elements)
    neighbors = [set() for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if commutes(elements[i], elements[j], a,b,c,q):
                neighbors[i].add(j)
                neighbors[j].add(i)
    seen = set()
    components = []
    distances = []
    for start in range(n):
        if start in seen:
            continue
        frontier = [start]
        component = set(frontier)
        while frontier:
            frontier = [v for u in frontier for v in neighbors[u] if v not in component]
            component.update(frontier)
        components.append(component)
        seen.update(component)
    for component in components:
        if len(component) > 1 and all(len(neighbors[i] & component) == len(component)-1 for i in component):
            distances.append(1)
        else:
            for start in component:
                dd = {start: 0}
                todo = deque([start])
                while todo:
                    u = todo.popleft()
                    for v in neighbors[u]:
                        if v not in dd:
                            dd[v] = dd[u]+1
                            todo.append(v)
                assert len(dd) == len(component)
                distances.append(max(dd.values()))
    return [len(comp) for comp in components], max(distances), n


def test_case(a,b,c,q):
    comps, diam, n = graph_stats(a,b,c,q)
    assert n == q ** (b*(a+c))-1
    if b == 1:
        center = q ** (a*c)
        pattern = sorted([q**a-1,q**c-1] + [q-1]*((q**a-1)*(q**c-1)//(q-1)))
        assert sorted(comps) == pattern, (a,b,c,q,comps,pattern)
        assert all(length > 0 for length in comps)
        print('DISCONNECTED', (a,b,c,q), 'component quotient sizes', sorted(comps))
    else:
        assert len(comps) == 1 and diam <= 3
        if min(a,c) == 1:
            assert diam == 2
        if min(a,c) >= b:
            assert diam == 3
        print('CONNECTED', (a,b,c,q), 'diameter', diam)


def test_mul():
    if 1:
        for x in range(4):
            for y in range(4):
                assert 0 <= field_mul(x,y,4) < 4
        assert field_mul(2,2,4) == 3
        assert field_mul(3,3,4) == 2
        assert field_mul(2,3,4) == 1


if __name__ == '__main__':
    test_mul()
    tests = [(1,1,1,2), (2,1,2,2), (1,1,1,3), (2,1,1,3),
             (1,2,1,2), (1,2,1,3), (1,2,1,4), (1,2,1,5),
             (1,2,2,2), (2,2,1,2), (2,2,2,2), (1,3,2,2),
             (1,2,2,3)]
    for p in tests:
        test_case(*p)
    print('ALL_GRAPH_CHECKS_PASSED', len(tests))
