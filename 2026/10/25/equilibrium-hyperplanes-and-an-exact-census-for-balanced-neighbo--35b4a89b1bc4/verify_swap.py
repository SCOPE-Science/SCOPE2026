"""Standalone exhaustive checker for two-color balanced-neighbor swap games.

Run: python verify_tripartite_swap.py
"""
from itertools import combinations, product
from math import comb


def formula_swap(counts, i, j, m):
    # Red leaves part i, blue leaves part j.
    h = len(counts)
    red = sum(counts)
    return (counts[i] >= 1 and counts[j] < m and
            counts[i] - counts[j] >= 2 and
            counts[i] + counts[j] == 2 * red - (h - 1) * m)


def direct_profit(bits, h, m, u, v):
    if bits[u] != 1 or bits[v] != 0:
        return False
    n = h * m
    def utility(x, state):
        own = state[x]
        neighbors = [y for y in range(n) if y // m != x // m]
        opposite = sum(state[y] != own for y in neighbors)
        return -abs(2 * opposite - len(neighbors))
    prior_u = utility(u, bits)
    prior_v = utility(v, bits)
    new = list(bits)
    new[u], new[v] = new[v], new[u]
    return utility(v, new) > prior_u and utility(u, new) > prior_v


def census(m):
    from itertools import product
    total = 0
    for counts in product(range(m + 1), repeat=3):
        stable = all(not formula_swap(counts,i,j,m)
                     for i,j in product(range(3),repeat=2) if i!=j)
        if stable:
            w=1
            for x in counts:w *= comb(m,x)
            total += w
    A = sum(comb(m,t) * comb(2*m,2*t) for t in range(m+1))
    B = sum(comb(m,t)**3 for t in range(m+1))
    J = sum(comb(m,2*m-3*t)*comb(m,t)**2 for t in range(m+1)
            if 0 <= 2*m-3*t <= m and 2*t != m)
    predicted = 2**(3*m) - 3*(A-B-J)
    assert total == predicted
    return total, predicted


def main():
    nprofiles = 0
    norders = 0
    for h,m in ((3,2),(3,3),(3,4),(3,5),(4,2),(4,3),(5,2)):
        n = h*m
        for bits in product((0,1), repeat=n):
            nprofiles += 1
            counts = [sum(bits[g*m:(g+1)*m]) for g in range(h)]
            for i in range(h):
                for j in range(h):
                    if i==j:continue
                    target = formula_swap(counts,i,j,m)
                    if target:
                        assert any(direct_profit(bits,h,m,u,v)
                                   for u in range(i*m,(i+1)*m)
                                   for v in range(j*m,(j+1)*m))
                    for u in range(i*m,(i+1)*m):
                        for v in range(j*m,(j+1)*m):
                            if bits[u] and not bits[v]:
                                norders+=1
                                observed=direct_profit(bits,h,m,u,v)
                                assert observed == target, (h,m,bits,u,v,observed,target)
            for i in range(h):
                for u,v in combinations(range(i*m,(i+1)*m),2):
                    if bits[u]!=bits[v]:
                        r,b=(u,v) if bits[u]==1 else (v,u)
                        assert not direct_profit(bits,h,m,r,b)
        if h==3:
            print(f'K_{{{m},{m},{m}}}: stable colorings={census(m)[0]}, total={2**(3*m)}')
    print('PASS',nprofiles,'configurations;',norders,'ordered red-to-blue cross-part cases')

if __name__ == '__main__':
    main()
