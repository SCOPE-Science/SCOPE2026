"""Independent direct-neighborhood finite checks of majority on clique coronas.

Usage: python3 verify_clique_corona.py
No external packages. Numerical tests corroborate, but do not prove, universal formulas.
"""
from collections import Counter
from math import comb


def direct_step(m, state, neighborhoods):
    out = 0
    for v, adj in enumerate(neighborhoods):
        tally = sum((state >> w) & 1 for w in adj)
        degree = len(adj)
        bit = int(2 * tally > degree) if 2 * tally != degree else (state >> v) & 1
        out |= bit << v
    return out


def graph(m):
    neighbors = []
    for i in range(m):
        neighbors.append(tuple(j for j in range(m) if j != i) + (m+i,))
    for i in range(m):
        neighbors.append((i,))
    return neighbors


def formula(m):
    total = 1 << (2*m)
    if m % 2 == 0:
        k = m//2
        c = comb(m,k)
        n0 = 2 + c*c
        n1 = 2*((1 << m)-1)
        n3 = c*((1 << m)-c-2)
        fixed = 2+c
    else:
        k = (m-1)//2
        c = comb(m,k)
        n0 = 2+2*c*(k+2)
        n1 = 2*((1 << m)-1)+2*c*(k+2)*((1 << k)-1)
        n3 = 2*c*(1 << k)*((1 << (k+1))-k-3)
        fixed = 2
    return (n0,n1,total-n0-n1-n3,n3),fixed


def test():
    for m in range(3,10):
        adj = graph(m)
        table = [direct_step(m,s,adj) for s in range(1 << (2*m))]
        cnt = Counter(); fixed = 0; primitive_states = 0
        for s in range(len(table)):
            seq = [s]
            for t in range(5):
                seq.append(table[seq[-1]])
            tau = next((t for t in range(4) if seq[t] == seq[t+2]), None)
            assert tau is not None, (m,s,seq)
            cnt[tau] += 1
            if tau == 0:
                if seq[1] == seq[0]: fixed +=1
                else: primitive_states +=1
        expected,fixed_exp = formula(m)
        result=tuple(cnt[t] for t in range(4))
        assert result == expected, (m,result,expected)
        assert fixed == fixed_exp, (m,fixed,fixed_exp)
        assert primitive_states == expected[0]-fixed
        print(f'm={m} total={len(table)} depth_counts={result} fixed={fixed} primitive_two_cycle_states={primitive_states}')
    print('CLIQUE_CORONA_MAJORITY_VERIFY_OK')

if __name__=='__main__': test()
