"""Exact checks for binary public-goods equilibria on triangular cyclic strips.

Requirements: Python >=3.10 and sympy >=1.12.
Run: python verify.py
"""
import math
from collections import defaultdict, deque
import sympy as sp


def bit(c, j):
    return (c >> j) & 1


def local_admissible(previous, current, following):
    for j in range(3):
        neighbor_count = (bit(previous, j) + bit(following, j)
                          + bit(current, (j + 1) % 3)
                          + bit(current, (j + 2) % 3))
        if bit(current, j) != int(neighbor_count in (0, 2)):
            return False
    return True


def transfer():
    matrix = sp.zeros(64)
    for p in range(8):
        for c in range(8):
            for q in range(8):
                if local_admissible(p, c, q):
                    matrix[8 * p + c, 8 * c + q] = 1
    return matrix


def brute(n):
    count = 0
    for mask in range(1 << (3 * n)):
        def get(i, j):
            return (mask >> (3 * (i % n) + (j % 3))) & 1
        valid = True
        for i in range(n):
            for j in range(3):
                neighbors = (get(i - 1, j) + get(i + 1, j)
                             + get(i, j - 1) + get(i, j + 1))
                if get(i, j) != int(neighbors in (0, 2)):
                    valid = False
                    break
            if not valid:
                break
        if valid:
            count += 1
    return count


def main():
    z = sp.symbols('z')
    matrix = transfer()
    p3p = z**3 - z**2 - 1
    p3m = z**3 - z**2 + 1
    p5 = z**5 + z**3 - z**2 + z - 1
    claimed_charpoly = (z**25 * (z-1)**10 * (z+1)**5
                        * (z**2+z+1)**4 * p3p * p3m * p5**2)
    assert matrix.charpoly(z).as_expr() == sp.expand(claimed_charpoly)
    print('EXACT characteristic polynomial: PASS')
    print('Nonzero transitions:', sum(int(v) for v in matrix))

    # Exact characteristic information is derived directly from an integer matrix.
    power = sp.eye(64)
    values = {}
    for n in range(1, 13):
        power = power * matrix
        values[n] = int(sp.trace(power))
    assert {n: values[n] for n in range(3, 13)} == {
        3:21, 4:9, 5:3, 6:45, 7:3, 8:33, 9:75,
        10:39, 11:69, 12:153}
    print('Exact traces n=3..12:', [values[n] for n in range(3, 13)])

    # Separate direct enumeration checks the payoff semantics independently
    # of the transfer encoding.
    for n in range(3, 7):
        got = brute(n)
        assert got == values[n], (n, got, values[n])
        print(f'Direct exhaustive enumeration n={n}: {got}, PASS')

    # Determine the nontrivial irreducible component by elementary graph search.
    adj = {u:[v for v in range(64) if matrix[u,v]] for u in range(64)}
    radj = {v:[] for v in range(64)}
    for u in range(64):
        for v in adj[u]: radj[v].append(u)
    def reaches(seed, edges):
        visited={seed}; stack=[seed]
        while stack:
            for v in edges[stack.pop()]:
                if v not in visited: visited.add(v); stack.append(v)
        return visited
    classes = []
    remaining = set(range(64))
    while remaining:
        v = min(remaining)
        comp = reaches(v, adj) & reaches(v, radj)
        classes.append(comp)
        remaining.difference_update(comp)
    sizes = sorted((len(c) for c in classes), reverse=True)
    assert sizes[0] == 18
    large = max(classes, key=len)
    assert all(reaches(v, adj) & large == large for v in large)
    assert all(reaches(v, radj) & large == large for v in large)
    vertices = sorted(large)
    block = matrix.extract(vertices, vertices)
    expected_block = (z+1)**2 * p3p * p3m * p5**2
    assert block.charpoly(z).as_expr() == sp.expand(expected_block)
    print('Strongly connected 18-state block and its factorization: PASS')

    # A simple cycle is a closed directed walk with no repeated vertex.
    # Exhibit 3- and 8-cycles in the same strongly connected block.
    def first_cycle(length):
        for start in vertices:
            def visit(path):
                u = path[-1]
                if len(path)==length:
                    if start in adj[u]: return path
                    return None
                for v in adj[u]:
                    if v in large and v not in path and v>=start:
                        found = visit(path+[v])
                        if found is not None: return found
                return None
            found=visit([start])
            if found is not None:return found
        return None
    cycles = [first_cycle(3),first_cycle(8)]
    assert all(c is not None for c in cycles) and math.gcd(3,8)==1
    print('Period one of dominant component, cycle lengths 3 and 8: PASS')
    print('Cycle witnesses:', cycles)

    # For fixed point growth, Perron-Frobenius on the primitive block
    # and positivity/root location establish the unique dominant root.
    positive_roots = [float(sp.re(root)) for root in sp.nroots(p3p)
                      if abs(float(sp.im(root))) < 1e-12 and float(sp.re(root)) > 0]
    assert len(positive_roots) == 1
    lam = positive_roots[0]
    assert abs(float(p3p.subs(z,lam))) < 1e-12
    assert p3p.subs(z,1) < 0 and p3p.subs(z,2)>0
    assert p3m.subs(z,sp.Rational(2,3))>0
    assert p5.subs(z,0)<0 and p5.subs(z,1)>0
    print('Dominant root λ ≈ 1.465571231876768, PASS')

if __name__ == '__main__':
    main()
