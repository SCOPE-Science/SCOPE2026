"""Direct finite checks for marked-boundary lifting. Python 3, no dependencies."""

def mu(w):
    return ''.join('01' if c == '0' else '10' for c in w)


def factors_with_occurrences(w):
    found = {}
    for i in range(len(w)):
        for j in range(i + 1, len(w) + 1):
            found.setdefault(w[i:j], []).append((i + 1, j))
    return found


def check_seed(w, cuts):
    assert {w[b - 1:b + 1] for b in cuts} == {'00', '01', '10', '11'}
    positions = factors_with_occurrences(w)
    for x, occurrences in positions.items():
        if len(x) >= 2:
            assert any(a <= b and b + 1 <= z for a, z in occurrences for b in cuts), (w, x)
    return [sum(len(x) == length for x in positions) for length in range(2, len(w) + 1)]


def check_attractor(w, marks):
    for x, occurrences in factors_with_occurrences(w).items():
        assert any(a <= p <= z for a, z in occurrences for p in marks), (len(w), x, marks)


def check_scaled(w, cuts, kmax):
    check_seed(w, cuts)
    for k in range(kmax + 1):
        check_attractor(w, [b * (1 << k) for b in cuts])
        print('verified', repr(w), 'scale', k, 'length', len(w))
        w = mu(w)


if __name__ == '__main__':
    seed = '01101001100101'
    counts = check_seed(seed, (3, 6, 8, 11))
    assert counts == [4, 6, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    check_scaled(seed, (3, 6, 8, 11), 4)
    check_scaled('00110', (1, 2, 3, 4), 3)
    print('All finite consistency checks passed.')
