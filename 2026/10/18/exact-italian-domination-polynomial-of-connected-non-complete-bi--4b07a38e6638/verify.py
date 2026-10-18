"""Independent finite checks for the Italian-domination polynomial of chain graphs.

Run with Python 3.10+; no third-party packages. The exhaustive checker builds
edges and evaluates the local defense rule, independently of the formula.
"""
from itertools import product


def multiply(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, u in enumerate(p):
        if u:
            for j, v in enumerate(q):
                out[i + j] += u * v
    return out


def power(base, n):
    result = [1]
    for _ in range(n):
        result = multiply(result, base)
    return result


def class_poly(size, mode):
    arbitrary = power([1, 1, 1], size)
    positive = power([0, 1, 1], size)
    if mode == 'U':
        return arbitrary
    if mode == 'V':
        return positive
    assert mode == 'W'
    return [u-v for u, v in zip(arbitrary, positive)]


def product_polys(polys):
    ans = [1]
    for p in polys:
        ans = multiply(ans, p)
    return ans


def tail_ge_two(p):
    q = p[:]
    for i in range(min(2, len(q))):
        q[i] = 0
    return q


def formula_cell(a, b, alpha, beta):
    p = len(a)
    assert p == len(b) and 1 <= alpha <= p+1 and 0 <= beta <= p
    aa = []
    bb = []
    for i, size in enumerate(a, 1):
        mode = 'V' if i < alpha else ('W' if i == alpha else 'U')
        aa.append(class_poly(size, mode))
    for j, size in enumerate(b, 1):
        mode = 'U' if j < beta else ('W' if j == beta else 'V')
        bb.append(class_poly(size, mode))
    if beta:
        a_poly = multiply(product_polys(aa[:beta-1]),
                          tail_ge_two(product_polys(aa[beta-1:])))
    else:
        a_poly = product_polys(aa)
    if alpha <= p:
        b_poly = multiply(tail_ge_two(product_polys(bb[:alpha])),
                          product_polys(bb[alpha:]))
    else:
        b_poly = product_polys(bb)
    return multiply(a_poly, b_poly)


def formula(a, b):
    n = sum(a) + sum(b)
    ans = [0] * (2*n + 1)
    for alpha in range(1, len(a) + 2):
        for beta in range(len(a) + 1):
            cell = formula_cell(a, b, alpha, beta)
            for d, count in enumerate(cell):
                ans[d] += count
    return ans


def brute_cells(a, b):
    p = len(a)
    A = []
    B = []
    offset = 0
    for m in a:
        A.append(list(range(offset, offset+m)))
        offset += m
    for m in b:
        B.append(list(range(offset, offset+m)))
        offset += m
    n = offset
    neighborhood = [[] for _ in range(n)]
    for i in range(p):
        for j in range(i+1):
            for u in A[i]:
                for v in B[j]:
                    neighborhood[u].append(v)
                    neighborhood[v].append(u)
    result = {(alpha, beta): [0] * (2*n+1)
              for alpha in range(1, p+2) for beta in range(p+1)}
    for labeling in product(range(3), repeat=n):
        if not all(labeling[v] != 0 or
                   sum(labeling[u] for u in neighborhood[v]) >= 2
                   for v in range(n)):
            continue
        alpha = next((i for i in range(1, p+1)
                      if any(labeling[u] == 0 for u in A[i-1])), p+1)
        beta = next((j for j in range(p, 0, -1)
                     if any(labeling[u] == 0 for u in B[j-1])), 0)
        result[(alpha, beta)][sum(labeling)] += 1
    return result


def main():
    cases = []
    for p in range(1, 5):
        for a in product(range(1, 3), repeat=p):
            for b in product(range(1, 3), repeat=p):
                if sum(a)+sum(b) <= 9:
                    cases.append((a, b))
    cases.extend([((1,)*5, (1,)*5),
                  ((1,2,1), (2,1,2)),
                  ((2,1,2), (1,2,1)),
                  ((3,1), (1,2)),
                  ((1,3), (2,1))])
    total_labelings = 0
    total_cells = 0
    for a,b in cases:
        brute = brute_cells(a,b)
        n = sum(a)+sum(b)
        total_labelings += 3**n
        p = len(a)
        computed = [0] * (2*n+1)
        for alpha in range(1,p+2):
            for beta in range(p+1):
                pred = formula_cell(a,b,alpha,beta)
                obs = brute[(alpha,beta)]
                assert pred == obs,(a,b,alpha,beta,pred,obs)
                total_cells += 1
                for degree,value in enumerate(pred):
                    computed[degree] += value
        assert computed == formula(a,b)
    print('PASS: graph profiles', len(cases))
    print('PASS: individual zero-frontier cells', total_cells)
    print('PASS: brute-force labeled assignments checked', total_labelings)
    for a,b in [((2,1),(1,2)),((1,1,1),(1,1,1))]:
        print('PROFILE',a,b,'coefficients degrees 2..6:',formula(a,b)[2:7])


if __name__ == '__main__':
    main()
