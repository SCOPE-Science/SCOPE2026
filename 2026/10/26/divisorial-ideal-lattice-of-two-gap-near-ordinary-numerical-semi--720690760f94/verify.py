"""Independent finite verification of a two-gap numerical-semigroup ideal census.

The test enumerates normalized ideals directly as subsets of the semigroup gaps,
computes their colon ideals, and checks the proposed binary-word parametrization.
Finite cases are corroboration, not proof of the uniform statements.
"""
from itertools import product


def setup(m):
    assert m >= 4
    gaps = tuple(range(1, m)) + (2*m-2, 2*m-1)
    missing = set(gaps)
    def in_s(x):
        return x >= 0 and x not in missing
    return gaps, in_s


def direct(m):
    gaps, in_s = setup(m)
    middle = range(m, 2*m-2)
    out = []
    for bits in product((0,1), repeat=len(gaps)):
        a = {g for g, flag in zip(gaps, bits) if flag}
        if any(not (in_s(x+s) or x+s in a)
               for x in a for s in middle):
            continue
        dual_small = [t for t in range(2*m)
                      if in_s(t) and all(in_s(t+x) for x in a)]
        closure_gaps = {g for g in gaps
                        if all(in_s(g+t) for t in dual_small)}
        out.append((a, closure_gaps, a == closure_gaps))
    return out


def formula(m):
    length = m-2
    h = {2*m-2, 2*m-1}
    result = {frozenset()}
    for word in product((0,1),repeat=length):
        if any(word[k-1] == 0 and word[k] == 1 and word[k+1] == 0
               for k in range(1,length-1)):
            continue
        u = {k+1 for k,v in enumerate(word) if v}
        a = set(h)
        for g in range(1,m):
            forbidden = {t-m+1 for t in (2*m-2-g, 2*m-1-g)
                         if m <= t <= 2*m-3}
            if forbidden <= u:
                a.add(g)
        result.add(frozenset(a))
    return result


def sequence(n):
    a = [1,2,4]
    for k in range(3,n+1):
        a.append(2*a[-1]-a[-2]+a[-3])
    return a[n]


def main():
    tested = 0
    for m in range(4,13):
        ideals = direct(m)
        actual = {frozenset(a) for a, closed, ok in ideals if ok}
        predicted = formula(m)
        assert actual == predicted, (m,actual^predicted)
        assert len(ideals) == 2**(m-1)+5, m
        assert len(actual) == 1+sequence(m-2), m
        assert all(a <= closed for a,closed,_ in ideals)
        tested += len(ideals)
        print(f'm={m} normalized={len(ideals)} reflexive={len(actual)}')
    print(f'VERIFY_OK normalized_ideals_examined={tested} multiplicities=9')


if __name__ == '__main__':
    main()
