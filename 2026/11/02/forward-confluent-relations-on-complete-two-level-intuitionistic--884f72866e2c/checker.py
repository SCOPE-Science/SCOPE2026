"""Independent finite checks for the height-two forward-confluence census.

Python 3 standard library only.  All carriers have fixed labelled levels.
"""
from itertools import product
from math import comb


def formula(a, b):
    assert a >= 1 and b >= 1
    A, B = 1 << a, 1 << b
    good = (1 << (a*a+a*b))*((B-1)**b + (B+A-1)**b - B**b)
    bad = sum(comb(b,z)*(B-1)**(b-z)*(1 << (a*(b-z)))*(2**z-1+A)**a
              for z in range(1, b+1))
    return good + bad


def forward_confluent(a, b, rows):
    """Direct quantified definition, not a test of the counting lemma."""
    n = a+b
    for x in range(a):
        for xp in range(a, n):
            for y in range(n):
                if not (rows[x] >> y) & 1:
                    continue
                found = False
                for yp in range(n):
                    if ((rows[xp] >> yp) & 1) and (y == yp or (y < a and yp >= a)):
                        found = True
                        break
                if not found:
                    return False
    return True


def structural_characterization(a, b, rows):
    upper_all = (1 << b)-1
    upper_empty = []
    for t in range(a, a+b):
        s = (rows[t] >> a) & ((1 << b)-1)
        upper_all &= s
        if s == 0:
            upper_empty.append(t)
    lower_all = (1 << a)-1
    for t in upper_empty:
        lower_all &= rows[t] & ((1 << a)-1)
    for m in range(a):
        if ((rows[m] >> a) & ~upper_all) != 0:
            return False
        if (rows[m] & ((1 << a)-1) & ~lower_all) != 0:
            return False
    return True


def brute(a, b):
    n = a+b
    count = 0
    for bits in range(1 << (n*n)):
        rows = [((bits >> (i*n)) & ((1 << n)-1)) for i in range(n)]
        fc = forward_confluent(a,b,rows)
        if fc != structural_characterization(a,b,rows):
            raise AssertionError((a,b,'structure',rows))
        count += fc
    return count


def row_sum(a, b):
    """Independent finite sum over ALL upper-source rows, no binomial simplification."""
    n = a+b
    result = 0
    for upper_rows in product(range(1 << n), repeat=b):
        top_intersection = (1 << b)-1
        bottom_intersection = (1 << a)-1
        for row in upper_rows:
            s = (row >> a) & ((1 << b)-1)
            top_intersection &= s
            if s == 0:
                bottom_intersection &= row & ((1 << a)-1)
        result += 1 << (a * (top_intersection.bit_count() + bottom_intersection.bit_count()))
    return result


def main():
    for a,b in ((1,1),(1,2),(2,1),(1,3),(2,2),(3,1)):
        actual = brute(a,b)
        expected = formula(a,b)
        assert actual == expected,(a,b,actual,expected)
        print('BRUTE', a,b, actual)
    for a,b in ((1,4),(2,3),(3,2),(3,3),(4,3)):
        actual = row_sum(a,b)
        expected = formula(a,b)
        assert actual == expected,(a,b,actual,expected)
        print('ROW_SUM',a,b,actual)
    for a in range(1,9):
        for b in range(1,9):
            N = formula(a,b)
            L = (1 << (a*a+a*b))*((1 << b)+(1 << a)-1)**b
            assert 0 <= L-N, (a,b,'upper bound')
            # Multiplying avoids any floating-point error.
            assert (L-N)*((1 << b)+(1 << a)-1)**b <= L*b*(1 << (b-1))**b, (a,b,'error bound')
    print('ALL_CHECKS_OK')


if __name__ == '__main__':
    main()
