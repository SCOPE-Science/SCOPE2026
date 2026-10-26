"""Finite checks accompanying the same-slope Sturmian parity theorem.

These computations test rational rotation approximants and singular branch
identities. Irrational injectivity and measure classification are proved
analytically in RESULT.md; they are not inferred from this script.
"""
from math import gcd

def circle_code(p, q, t):
    """Period-q rational mechanical coding as one Python integer."""
    return sum((((t + n*p) % q >= q-p) << n) for n in range(q))

def check_grid(p, q):
    assert 0 < p < q
    assert gcd(p,q) == 1
    words = [circle_code(p, q, t) for t in range(q)]
    assert len(set(words)) == q
    seen = {}
    for t in range(q):
        for s in range(t, q):
            y = words[t] ^ words[s]
            old = seen.get(y)
            if old is not None:
                assert y == 0 and t == s
            else:
                seen[y] = (t,s)
    assert len(seen) == 1 + q*(q-1)//2
    assert seen[0][0] == seen[0][1]
    return q*(q-1)//2

def check_singular():
    # Each characteristic Sturmian branch pair differs only at -1,0.
    from decimal import Decimal, getcontext, ROUND_FLOOR, ROUND_CEILING
    getcontext().prec = 90
    alpha = (Decimal(5).sqrt()-Decimal(1))/Decimal(2)
    def floor(x): return int(x.to_integral_value(rounding=ROUND_FLOOR))
    def ceil(x): return int(x.to_integral_value(rounding=ROUND_CEILING))
    idx = list(range(-350,351))
    low = {n:int(floor((n+1)*alpha)-floor(n*alpha)) for n in idx}
    up = {n:int(ceil((n+1)*alpha)-ceil(n*alpha)) for n in idx}
    differences = {n for n in idx if low[n] != up[n]}
    assert differences == {-1,0}, differences
    for d in (1,2,11,57):
        shifted = {n for n in idx if n-d in low and low[n-d] != up[n-d]}
        assert shifted == {d-1,d}
        assert shifted != differences
        assert differences.symmetric_difference(shifted)
    return len(idx)

def main():
    sizes=[(89,233),(144,377)]
    pairs=[check_grid(*pq) for pq in sizes]
    width=check_singular()
    print('VERIFY_OK: rational rotation grids q=233 and q=377;',
          'unordered off-diagonal XOR images',pairs,
          '(all distinct), diagonal maps to zero;',
          'singular Sturmian branch difference is two adjacent sites;',
          f'checked on {width} indices and four nonzero shifts;',
          'the infinite irrational theorem rests on the separate proof.')
if __name__=='__main__':main()
