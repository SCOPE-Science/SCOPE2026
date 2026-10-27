"""Independent finite checks for the three-marker circular antidictionary theorem.

The theorem is proved in RESULT.md. This program enumerates finite periodic
factor sets independently and checks their minimal absent words and bispecial
factors against the proposed formulas; it is not an infinite proof.
"""
from itertools import product

ALPHABET = '01'


def factors(s):
    """All periodic factors of lengths 0..|s|+1, from every marked start."""
    n = len(s)
    periodic = s * 3
    result = [{''}]
    for length in range(1, n+2):
        result.append({periodic[i:i+length] for i in range(n)})
    return result


def minimal_absent(f, n):
    out = {c for c in ALPHABET if c not in f[1]}
    for k in range(2, n+2):
        for prefix in f[k-1]:
            for c in ALPHABET:
                candidate = prefix + c
                if candidate not in f[k] and candidate[1:] in f[k-1]:
                    out.add(candidate)
    return out


def bispecial(f, n):
    return {w for length in range(n) for w in f[length]
            if all(ch+w in f[length+1] and w+ch in f[length+1]
                   for ch in ALPHABET)}


def predicted_bispecial(a, b, c):
    a, b, c = sorted((a, b, c))
    if c == 0:
        return set()
    out = {'0'*k for k in range(c)}
    z = lambda x: '0'*x
    if a == b == c:
        pass
    elif a == b:
        out.add(z(a)+'1'+z(a))
        out.add(z(a)+'1'+z(a)+'1'+z(a))
    elif b == c:
        out.add(z(a)+'1'+z(a))
        out.add(z(a)+'1'+z(b)+'1'+z(a))
    else:
        out.update({z(a)+'1'+z(a), z(b)+'1'+z(a), z(a)+'1'+z(b)})
    return out


def predicted_count(a, b, c):
    m = max(a, b, c)
    return m + {1:1, 2:3, 3:4}[len({a,b,c})]


def check(max_gap=9):
    checked = 0
    max_length = 0
    for a, b, c in product(range(max_gap+1), repeat=3):
        s = ''.join('1' + '0'*gap for gap in (a,b,c))
        n = len(s)
        f = factors(s)
        maw = minimal_absent(f, n)
        expected = predicted_count(a,b,c)
        if len(maw) != expected:
            raise AssertionError(('MAW', (a,b,c), len(maw), expected, sorted(maw)))
        bs = bispecial(f,n)
        predicted = predicted_bispecial(a,b,c)
        if bs != predicted:
            raise AssertionError(('bispecial',(a,b,c), sorted(bs), sorted(predicted)))
        if c or a or b:
            if len(maw) != 1+len(bs):
                raise AssertionError(('telescoping',(a,b,c)))
        checked += 1
        max_length = max(max_length,n)
    print('PASS: ordered triples:', checked, 'max gap:', max_gap, 'max word length:', max_length)
    for n in range(3, 34):
        s=n-3
        values=[(predicted_count(a,b,s-a-b), tuple(sorted((a,b,s-a-b))))
                for a in range(s+1) for b in range(s-a+1)]
        measured_min=min(x[0] for x in values)
        measured_max=max(x[0] for x in values)
        expected_min=(s//3+1) if s%3==0 else (s//3+4)
        expected_max=1 if s==0 else n
        if (measured_min,measured_max)!=(expected_min,expected_max):
            raise AssertionError(('extrema',n,measured_min,measured_max))
        maximizers={g for v,g in values if v==measured_max}
        expected_maximizers=({(0,0,0)} if s==0 else {(0,0,s)} | ({(0,1,s-1)} if s>=3 else set()))
        if maximizers != expected_maximizers:
            raise AssertionError(('maximizers',n,maximizers,expected_maximizers))
    print('PASS: extremal ranges and maximizer classification at lengths 3..33')


if __name__ == '__main__':
    check(9)
