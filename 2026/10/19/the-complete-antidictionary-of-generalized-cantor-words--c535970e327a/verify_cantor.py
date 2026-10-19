"""Independent finite tests for the generalized-Cantor minimal absent factor classification.

Runs on Python 3 standard library. No external data or packages are needed.
All tests are finite and do not replace the general mathematical proof.
"""
from itertools import product


def substitution(q, generations):
    word = '1'
    for _ in range(generations):
        word = ''.join(('1' + '0'*(q-2) + '1') if c == '1' else ('0'*q) for c in word)
    return word


def valuation(n):
    assert n > 0
    return (n & -n).bit_length()-1


def digit_cantor(q, n):
    # A position is marked precisely when every base-q digit is 0 or q-1.
    while n:
        n, digit = divmod(n, q)
        if digit not in (0, q-1):
            return '0'
    return '1'


def allowed_gap(q, width):
    scale = q-2
    exponent = 0
    while scale < width:
        scale *= q
        exponent += 1
    if scale == width:
        return exponent
    return None


def threshold(q, width):
    exponent = 0
    scale = q-2
    while scale < width:
        scale *= q
        exponent += 1
    return exponent


def is_factor_by_congruences(q, word):
    """Exact (infinite-word) factor membership, independent of any alleged MAW list."""
    if '1' not in word:
        return True
    pieces = word.split('1')
    count = len(pieces)-1
    constraints = [(0, 1 << threshold(q, len(pieces[0]))),
                   (0, 1 << threshold(q, len(pieces[-1])))]
    # Record each congruence x+j ≡ c (mod m), represented for x.
    constraints[1] = ((-count) % constraints[1][1], constraints[1][1])
    for j, gap in enumerate(pieces[1:-1], start=1):
        e = allowed_gap(q, len(gap))
        if e is None:
            return False
        m = 1 << (e+1)
        constraints.append(((1 << e)-j % m, m))
    # The moduli are powers of 2; pairwise agreement proves compatibility.
    for r1, m1 in constraints:
        for r2, m2 in constraints:
            m = min(m1, m2)
            if (r1-r2) % m:
                return False
    return True


def predicted(q, length):
    result = set()
    if length >= 2 and allowed_gap(q, length-2) is None:
        result.add('1'+'0'*(length-2)+'1')
    w = '1'
    j = 0
    while (2*q-3)*q**j+2 <= length:
        L = (q-2)*q**j
        a = '0'*(L+1)+w+'0'*(L+1)
        b = '1'+'0'*L+w+'0'*L+'1'
        if len(a) == length:
            result.update((a,b))
        w = substitution_step(q,w)
        j += 1
    return result


def substitution_step(q, w):
    return ''.join(('1' + '0'*(q-2) + '1') if c=='1' else '0'*q for c in w)


def check():
    distinct_exhaustive=0
    for q in range(3,9):
        # Exhaustively enumerates ALL 2^n words for bounded n.
        factors_prev = {''}
        for n in range(1,15):
            factors = {''.join(bits) for bits in product('01',repeat=n)
                       if is_factor_by_congruences(q,''.join(bits))}
            actual = {v+c for v in factors_prev for c in '01'
                      if v+c not in factors and (v+c)[1:] in factors_prev}
            assert actual == predicted(q,n), (q,n,sorted(actual^predicted(q,n)))
            factors_prev = factors
            distinct_exhaustive += len(actual)

    direct_checks=0
    for q,gen,limit in [(3,10,110),(4,9,100),(5,8,85),(6,7,70)]:
        s = substitution(q,gen)
        assert all(s[p] == digit_cantor(q,p) for p in range(len(s)))
        # Factor sets extracted directly from a long finite substitution iterate.
        prev={''}
        for n in range(1,limit+1):
            fs={s[p:p+n] for p in range(len(s)-n+1)}
            assert all(is_factor_by_congruences(q,u) for u in fs)
            maw={v+c for v in prev for c in '01'
                 if v+c not in fs and (v+c)[1:] in prev}
            assert maw == predicted(q,n), (q,n,sorted(maw^predicted(q,n)))
            prev=fs
            direct_checks+=1

    # Independently test sparse high-scale candidates with the exact 2-adic
    # occurrence criterion, beyond the lengths of the finite-prefix checks.
    highscale=0
    for q in range(3,14):
        w='1'
        for j in range(5):
            L=(q-2)*q**j
            for u in ('0'*(L+1)+w+'0'*(L+1),
                      '1'+'0'*L+w+'0'*L+'1'):
                assert not is_factor_by_congruences(q,u)
                assert is_factor_by_congruences(q,u[:-1])
                assert is_factor_by_congruences(q,u[1:])
                highscale += 1
            w=substitution_step(q,w)
    print('VERIFY_OK exhaustive_q=3..8_lengths=1..14 direct_prefix_cases=%d highscale_candidates=%d distinct_absences=%d' % (direct_checks,highscale,distinct_exhaustive))


if __name__ == '__main__':
    check()
