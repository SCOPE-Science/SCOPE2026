"""Direct finite checks for the locally-optimal prism-colouring formulas.

Only finite tests are claimed; the unrestricted statements require the proof.
Run: python gridlock_prism_verify.py
"""
from itertools import product
from math import comb


def predicted(n, k):
    value = k * k
    for r in range(2, n // 2 + 1):
        boundary_sets_times_r = n * comb(n - r - 1, r - 1)
        if boundary_sets_times_r % r:
            raise AssertionError('cyclic gap count is not integral')
        boundary_sets = boundary_sets_times_r // r
        chromatic_cycle = (k - 1) ** r + (-1) ** r * (k - 1)
        value += boundary_sets * chromatic_cycle
    return value


def direct(n, k):
    total = 0
    invalid_classification = 0
    for a in product(range(k), repeat=2*n):
        good = True
        for layer in range(2):
            for i in range(n):
                color = a[layer*n+i]
                matches = (a[layer*n+(i-1)%n] == color)
                matches += (a[layer*n+(i+1)%n] == color)
                matches += (a[(1-layer)*n+i] == color)
                if matches < 2:
                    good = False
                    break
            if not good:
                break
        if not good:
            continue
        total += 1
        top = a[:n]; bottom = a[n:]
        is_vertical_separation = len(set(top))==1 and len(set(bottom))==1 and top[0]!=bottom[0]
        is_rung_constant = top == bottom and all(top[i]==top[(i-1)%n] or top[i]==top[(i+1)%n] for i in range(n))
        if not (is_vertical_separation or is_rung_constant):
            invalid_classification += 1
    assert invalid_classification == 0, (n,k,invalid_classification)
    return total


def closed_form_checks():
    # Second route: Lucas recurrence and independent rational-series convolution.
    sixth_root_trace = (2, 1, -1, -2, -1, 1)
    cases = 0
    for k in range(1, 8):
        lucas = [2, 1]
        for n in range(2, 24):
            lucas.append(lucas[-1] + (k - 1) * lucas[-2])
        for n in range(3, 24):
            actual = lucas[n] + (k - 1)*sixth_root_trace[n % 6] + k*(k - 1)
            assert actual == predicted(n, k), (n,k,actual)
            cases += 1
    print(f'Lucas/periodic closed formula: {cases} integer evaluations PASS')

    def multiply(a, b):
        out = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                out[i+j] += x*y
        return out

    for k in range(0, 9):
        a = [1, -1]
        b = [1, -1, 1-k]
        c = [1, -1, 1]
        den = multiply(multiply(a,b),c)
        num = [0]*10
        for i, coef in enumerate(multiply(b,c)):
            num[i+3] += k*k*coef
        num[4] += 2*k*(k-1)
        num[5] -= k*(k-1)
        coeffs=[]
        for n in range(0, 31):
            rhs=num[n] if n<len(num) else 0
            v=rhs-sum(den[j]*coeffs[n-j] for j in range(1,min(n,len(den)-1)+1))
            coeffs.append(v)
            if n>=3:
                assert v==predicted(n,k),(n,k,v,predicted(n,k))
            else:
                assert v==0
    print('Rational generating function: 9 palette evaluations through n=30 PASS')


def run():
    closed_form_checks()
    total_tested = 0
    cases = [(n,k) for k,maximum_n in ((2,9),(3,6),(4,5)) for n in range(3,maximum_n+1)]
    for n,k in cases:
        actual = direct(n,k)
        expected = predicted(n,k)
        assert actual == expected, (n,k,actual,expected)
        examined = k**(2*n)
        total_tested += examined
        print(f'n={n:2} k={k}: {actual} locally-optimal of {examined} labelled colourings; PASS')
    print(f'ALL PASS; {len(cases)} independent finite cases; {total_tested} labelled assignments checked')

if __name__ == '__main__':
    run()
