"""Exact finite checks for inverse palindromic-duplication lists."""
from itertools import product

def parent_set(w):
    out = set()
    for i in range(len(w)-3):
        if w[i] == w[i+3] and w[i+1] == w[i+2]:
            out.add(w[:i+2] + w[i+4:])
    return out

def pal_starts(w):
    return [i for i in range(len(w)-3)
            if w[i] == w[i+3] and w[i+1] == w[i+2]]

def components(starts):
    return sum(i == 0 or starts[i] != starts[i-1]+1
               for i in range(len(starts)))

def theoretical_count(q, n):
    if n == 4:
        return q*q
    if n == 5:
        return 2*q**3-q
    if n % 2 == 0:
        return q*(q-1)
    t = (n-3)//2
    return q*(q-1)*((t+1)*(q-1)+4)

def test(q, n):
    counts = 0
    incidence = 0
    maximizers = 0
    maximum = (n-2)//2
    for w in product(range(q), repeat=n):
        starts = pal_starts(w)
        parents = parent_set(w)
        if len(parents) != components(starts):
            raise AssertionError(('component lemma', q,n,w))
        if len(parents) > maximum:
            raise AssertionError(('maximum exceeded',q,n,w))
        incidence += len(parents)
        if len(parents) == maximum:
            maximizers += 1
            if n >= 6 and n % 2 == 0:
                a, b = w[:2]
                expect = tuple((a,b,b,a)[i%4] for i in range(n))
                if a == b or w != expect:
                    raise AssertionError(('even rigidity', q,n,w))
        counts += 1
    expected_incidence = (n-3)*q**(n-2) - (n-4)*q**(n-4)
    assert incidence == expected_incidence,(q,n,incidence,expected_incidence)
    assert maximizers == theoretical_count(q,n),(q,n,maximizers,theoretical_count(q,n))
    return counts, maximizers, incidence

if __name__ == '__main__':
    grand_total = 0
    for q, stop in [(2,15), (3,11), (4,9), (5,7)]:
        for n in range(4,stop+1):
            count, winners, incidence = test(q,n)
            grand_total += count
            print(f'q={q},N={n},strings={count},extremizers={winners},incidence={incidence}')
    print(f'PASS: exhaustive checks of {grand_total} received words')
