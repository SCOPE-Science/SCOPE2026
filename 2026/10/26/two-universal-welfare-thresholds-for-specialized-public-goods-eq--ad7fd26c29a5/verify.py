"""Exact finite checks for specialized welfare selection on path networks.

No external dependencies. The infinite family is established analytically
in the accompanying result; this is a finite counterexample search/check.
"""
from fractions import Fraction


def independent_strings(n):
    def run(i, prev, bits):
        if i == n:
            yield tuple(bits)
            return
        bits.append(0)
        yield from run(i + 1, 0, bits)
        bits.pop()
        if not prev:
            bits.append(1)
            yield from run(i + 1, 1, bits)
            bits.pop()
    yield from run(0, 0, [])


def is_maximal(bits):
    n = len(bits)
    return all(bits[i] or (i > 0 and bits[i-1]) or
               (i+1 < n and bits[i+1]) for i in range(n))


def descriptor(bits):
    m = sum(bits)
    a = sum(bits[i] and bits[i+2] for i in range(len(bits)-2))
    return (m,a)


def predicted_pairs(n, t):
    low = (n+2)//3
    upper = (n-1)//2
    final = (n+1)//2
    pairs = []
    if low <= upper:
        for m in range(low, upper+1):
            pairs.append((m, 3*m-n))
    pairs.append((final, final-1))
    scores = [t*a-m for m,a in pairs]
    mx = max(scores)
    return {pair for pair, score in zip(pairs, scores) if score == mx}


def best_actual(frontier, t):
    mx=max(t*a-m for m,a in frontier)
    return {(m,a) for m,a in frontier if t*a-m==mx}

Ts=[Fraction(1,10),Fraction(1,4),Fraction(1,3),Fraction(2,5),
    Fraction(1,2),Fraction(3,5),Fraction(3,4),Fraction(9,10)]
profile_total=0
check_total=0
for n in range(2,24):
    frontier={}
    for s in independent_strings(n):
        if not is_maximal(s):
            continue
        m,a=descriptor(s)
        frontier.setdefault(m,set()).add(a)
        profile_total+=1
    for m, avals in frontier.items():
        target=(3*m-n) if m <= (n-1)//2 else m-1
        assert max(avals)==target,(n,m,max(avals),target)
        check_total+=1
    flat={(m,a) for m,as_ in frontier.items() for a in as_}
    for t in Ts:
        expected=predicted_pairs(n,t)
        actual=best_actual(flat,t)
        assert expected==actual,(n,t,actual,expected)
        check_total+=1

# Explicit twelve-agent optimal equilibrium representatives in order of regimes.
witnesses=['010010010010','010101010010','101010101010']
for s,(m,a) in zip(witnesses,[(4,0),(5,3),(6,5)]):
    bits=tuple(int(c) for c in s)
    assert len(s)==12 and is_maximal(bits) and descriptor(bits)==(m,a)
    check_total+=1
for t, correct in [(Fraction(1,4),(4,0)),
                   (Fraction(2,5),(5,3)),
                   (Fraction(3,4),(6,5))]:
    assert best_actual({descriptor(tuple(map(int,s))) for s in witnesses},t)=={correct}
    check_total+=1
print('PASS')
print('path orders verified: 2..23 inclusive')
print('independence/maximality profiles checked:',profile_total)
print('exact rational finite assertions:',check_total)
print('t grid:',','.join(str(v) for v in Ts))
print('twelve-agent phase representatives:',witnesses)
print('not an infinite proof: arbitrary path order and benefit functions require analytical reasoning')
