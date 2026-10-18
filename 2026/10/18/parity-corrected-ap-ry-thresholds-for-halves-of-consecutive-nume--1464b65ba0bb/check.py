"""Independent integer-interval checks for the stated quotient-semigroup formulas.
Run with Python 3: python check.py
No third-party packages required.
"""

def member_direct(n, a, k):
    """Integer n is a sum of generators from [a,a+k]."""
    if n < 0:
        return False
    return (n + a + k - 1) // (a + k) <= n // a


def predicted(a, k):
    t = (a - 2) // k + 1  # ceil((a-1)/k)
    q = a - 1 - (t - 1) * k
    assert 1 <= q <= k
    if t % 2:
        frob = (a * t - 1) // 2
    elif q >= 2:
        frob = a * t // 2 - 1
    else:
        frob = (a * (t - 1) - 1) // 2
    genus_num = (k * t * (t - 1) + 2 * t * q
                 - (t - 1) * (k % 2) - q % 2)
    assert genus_num % 4 == 0
    genus = genus_num // 4
    ws = []
    for j in range(a):
        e = (j + k - 1) // k
        L = e + (e - j) % 2
        assert (j + a * L) % 2 == 0
        w = (j + a * L) // 2
        ws.append(w)
    return frob, genus, ws


def main():
    instances = 0
    membership_checks = 0
    apery_checks = 0
    for a in range(5, 121, 2):
        for k in range(3, a - 1):
            F, genus, ws = predicted(a, k)
            residues = {w % a: w for w in ws}
            assert len(residues) == a
            assert sum(ws) // a - (a-1)//2 == genus
            gaps = []
            for x in range(F + a + 1):
                direct = member_direct(2*x, a, k)
                inferred = x >= residues[x % a]
                assert direct == inferred, (a,k,x,direct,inferred)
                if not direct:
                    gaps.append(x)
                membership_checks += 1
            assert max(gaps) == F, (a,k,F,max(gaps))
            assert len(gaps) == genus, (a,k,genus,len(gaps))
            for w in ws:
                assert member_direct(2*w,a,k)
                assert w < a or not member_direct(2*(w-a),a,k)
                apery_checks += 1
            instances += 1
    print('PASS:',instances,'parameter pairs;',membership_checks,
          'membership comparisons;',apery_checks,'Apéry-minimality comparisons')


if __name__ == '__main__':
    main()
