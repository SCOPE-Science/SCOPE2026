"""Independent exact enumeration of the first-entry depths of t -> t*t+1 mod 2**k.
No third-party packages required. Run: python verify.py
"""

def predicted(k):
    assert k >= 3
    max_depth = (2*k + 1)//3
    odd_count = lambda h: (1 << (k-1)) if h <= 3 else (1 << (k+2-h))
    even_two_count = lambda h: (1 << (k-2)) if h <= 5 else (1 << (k+3-h))
    cumulative = [2]
    for t in range(1, max_depth+1):
        odd_gain = 3*t//2 - 1
        even_gain = 3*(t-1)//2
        val = odd_count(k-odd_gain) + even_two_count(k-even_gain)
        if t == max_depth:
            val += 1 << (k-2)
        cumulative.append(val)
    return cumulative

def observed(k):
    mod = 1 << k
    mask = mod-1
    def f(x):
        return (x*x + 1)&mask
    periodic = {x for x in range(mod) if f(f(x)) == x}
    assert len(periodic) == 2
    depth = []
    for x in range(mod):
        z = x
        t = 0
        while z not in periodic:
            z = f(z)
            t += 1
            assert t <= 2*k
        depth.append(t)
    largest = max(depth)
    assert largest == (2*k+1)//3
    assert sum(d == largest for d in depth) == mod//4
    assert all((d == largest) == (x % 4 == 0)
               for x, d in enumerate(depth))
    return [sum(d<=t for d in depth) for t in range(largest+1)]

if __name__ == '__main__':
    for k in range(3, 15):
        expected = predicted(k)
        actual = observed(k)
        assert actual == expected, (k, expected, actual)
        histogram = [actual[0]] + [actual[t]-actual[t-1]
                                    for t in range(1, len(actual))]
        print('LEVEL_OK', k, 'max_depth', len(actual)-1,
              'histogram', histogram)
    print('VERIFY_OK exact_all_residues_levels=3..14')
