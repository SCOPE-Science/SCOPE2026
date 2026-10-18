"""Independent exact character tests for multipartite path-free complexes.
All set permutations within selected parts are enumerated; no external libraries.
"""
from itertools import permutations, product
from math import comb


def mm(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j] += x*y
    return c


def polynomial(cycles):
    f = [1]
    for cycle in cycles:
        f = mm(f, [1]+[0]*(len(cycle)-1)+[-1])
    return f


def cycle_decomposition(perm):
    used = set()
    res = []
    for v in range(len(perm)):
        if v not in used:
            cy = []
            j = v
            while j not in used:
                used.add(j)
                cy.append(j)
                j = perm[j]
            res.append(tuple(cy))
    return res


def char_formula(parts, t, perm):
    k = t//2 - 1
    starts = [0]
    for a in parts:
        starts.append(starts[-1]+a)
    P = []
    for i in range(len(parts)):
        cs = cycle_decomposition(perm)
        cs = [cy for cy in cs if starts[i] <= cy[0] < starts[i+1]]
        P.append(polynomial(cs))
    total = [1]
    for p in P:
        total = mm(total,p)
    val = sum(total[:t])
    for i in range(len(parts)):
        other = [1]
        for j in range(len(parts)):
            if i != j:
                other = mm(other, P[j])
        for q in range(min(k, len(other)-1)+1):
            val += other[q] * sum(P[i][max(0, t-q):])
    return (-1)**(t-1)*val


def char_direct(parts, t, perm):
    n = sum(parts)
    groups = []
    for i, a in enumerate(parts):
        groups += [i]*a
    cycles = cycle_decomposition(perm)
    out = 0
    for selected in range(1 << len(cycles)):
        mask = 0
        for j, cy in enumerate(cycles):
            if selected & (1 << j):
                for v in cy:
                    mask |= 1 << v
        size = mask.bit_count()
        if size >= t and min(sum(1 for v in range(n) if (mask & (1 << v)) and groups[v]!=i) for i in range(len(parts))) > t//2-1:
            continue
        out += (-1)**selected.bit_count()
    return (-1)**(t-1)*out


def check(parts):
    local = [list(permutations(range(a))) for a in parts]
    n = sum(parts)
    count = 0
    for pieces in product(*local):
        perm = []
        offset = 0
        for piece in pieces:
            perm.extend([offset + x for x in piece])
            offset += len(piece)
        for t in range(5, min(n, 7)+1):
            c0 = char_direct(parts, t, perm)
            c1 = char_formula(parts, t, perm)
            assert c0 == c1, (parts,t,perm,c0,c1)
            count += 1
    return count

if __name__ == '__main__':
    cases=[(3,2,1),(4,2,2),(4,3,1),(3,3,2),(2,2,2,2)]
    total=0
    for parts in cases:
        q=check(parts)
        total+=q
        print(f'PASS {parts}: {q} complete class-preserving permutation/threshold comparisons')
    print(f'PASS {total} comparisons of direct signed-fixed-face Lefschetz sums versus closed cycle-polynomial character')
