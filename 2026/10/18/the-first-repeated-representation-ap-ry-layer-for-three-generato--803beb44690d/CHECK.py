"""Exact integral verification of the first repeated-representation thresholds.

Run with `python3 CHECK.py`. No third-party dependencies.
Finite checks corroborate, but do not replace, the symbolic proof.
"""


def proposed(b):
    m = b*b + b + 1
    thresholds = []
    for r in range(m):
        q, s = divmod(r, b+1)
        if s == b:
            k = q+b+2
        elif q == 0:
            k = s+b+2
        else:
            k = q+s+b
        thresholds.append(m*k+r)
    g = ((2*b+1)*m-2 if b <= 3 else (3*b-2)*m-3)
    genus = b*(4*b*b+b+11)//2
    assert sum((w-r)//m for r, w in enumerate(thresholds)) == genus
    assert max(thresholds)-m == g
    return m, thresholds, g, genus


def counts_by_coin_recurrence(coins, top):
    counts = [0]*(top+1)
    counts[0] = 1
    for coin in coins:
        for n in range(coin, top+1):
            counts[n] += counts[n-coin]
    return counts


def direct_count(n, a, c):
    """A distinct computation: enumerate last coefficient z, solve two-coin congruence."""
    total = 0
    for z in range(n//c+1):
        v = n-z*c
        ymin = v % a
        if (a+1)*ymin <= v:
            total += 1+(v//(a+1)-ymin)//a
    return total


def main():
    direct_instances = 0
    residue_classes = 0
    for b in range(2, 21):
        m, pred, g, genus = proposed(b)
        a, c = m+1, m+b+1
        top = max(pred)+m
        d = counts_by_coin_recurrence((m, a, c), top)
        actual = []
        for r in range(m):
            vals = [n for n in range(r, top+1, m) if d[n]>=2]
            assert vals, (b, r)
            first = vals[0]
            assert first == pred[r], (b, r, first, pred[r])
            assert all(d[n]<=1 for n in range(r, first, m))
            assert all(d[n]>=2 for n in range(first, top+1, m))
            actual.append(first)
            residue_classes += 1
        assert max(actual)-m == g, (b,'Frobenius')
        assert sum(d[n]<=1 for n in range(max(actual))) == genus, (b,'genus')
        if b <= 8:
            for n in range(top+1):
                assert d[n] == direct_count(n, m, c), (b, n, d[n], direct_count(n,m,c))
                direct_instances += 1
        print(f'b={b:2d}: multiplicity={m:3d}, g1={g:6d}, n1={genus:6d}, residues={m:3d}')
    print(f'PASS: {residue_classes} entire residue thresholds and {direct_instances} independent exact counts')


if __name__ == '__main__':
    main()
