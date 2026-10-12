"""Exhaustive finite check of the local pair-graph channel theorem.
No external dependencies. Run: python3 verify_pairs.py
"""
from itertools import product


def distinguishable(a, b):
    return any(a[i:i+2] != b[i:i+2]
               and a[i:i+2] != '11' and b[i:i+2] != '11'
               for i in range(len(a)-1))


def canonical(s):
    a = list(s)
    if a[1] == '1':
        a[0] = '0'
    if a[-2] == '1':
        a[-1] = '0'
    return ''.join(a)


def is_representative(s):
    return '111' not in s and s[:2] != '11' and s[-2:] != '11'


def verify(n):
    words = [''.join(t) for t in product('01', repeat=n)]
    d = [s for s in words if '111' not in s]
    reps = [s for s in words if is_representative(s)]
    if n == 2:
        assert len(reps) == 3
        assert all(distinguishable(x,y) for k,x in enumerate(reps) for y in reps[:k])
        return len(reps)
    assert set(map(canonical, d)) == set(reps)
    for k,x in enumerate(d):
        for y in d[:k]:
            assert distinguishable(x,y) == (canonical(x) != canonical(y)), (n,x,y)
    # Check that removing the middle symbol of any 111 occurrence never
    # destroys a previously existing distinguishing witness.
    if n <= 8:
        for x in words:
            p = x.find('111')
            if p < 0:
                continue
            z = x[:p+1]+'0'+x[p+2:]
            assert not distinguishable(x,z)
            for y in words:
                if distinguishable(x,y):
                    assert distinguishable(z,y), (n,x,y,z)
    return len(reps)


if __name__ == '__main__':
    for n in range(2, 12):
        print(n,verify(n))
    print('PAIR_VERIFICATION_OK')
