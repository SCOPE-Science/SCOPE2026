from collections import Counter
from fractions import Fraction
from itertools import product


def face_term(nodes):
    """Return (real part, coefficient of i/(2*pi)) for one triangular face."""
    counts = Counter(nodes)
    if len(counts) == 3:
        return Fraction(0), Fraction(0)
    if len(counts) == 1:
        return Fraction(1, 2), Fraction(0)
    repeated = next(value for value, multiplicity in counts.items() if multiplicity == 2)
    singleton = next(value for value, multiplicity in counts.items() if multiplicity == 1)
    # G({r,r,s}) = -i/(2*pi*(s-r)).
    return Fraction(0), -Fraction(1, singleton - repeated)


def exact_face_sum(k):
    """The common positive facet-area factor is omitted; zeros are unchanged."""
    values = (0, *k)
    real = Fraction(0)
    imag_coefficient = Fraction(0)
    for omitted in range(4):
        nodes = tuple(values[j] for j in range(4) if j != omitted)
        r, im = face_term(nodes)
        real += r
        imag_coefficient += im
    return real, imag_coefficient


def predicted_zero(k):
    values = (0, *k)
    counts = Counter(values)
    multiplicities = sorted(counts.values(), reverse=True)
    if multiplicities in ([1, 1, 1, 1], [2, 2]):
        return True
    if multiplicities == [2, 1, 1]:
        repeated = next(value for value, multiplicity in counts.items() if multiplicity == 2)
        singletons = [value for value, multiplicity in counts.items() if multiplicity == 1]
        return sum(singletons) == 2 * repeated
    return False


def main():
    tested = 0
    zero_count = 0
    for k in product(range(-4, 5), repeat=3):
        exact = exact_face_sum(k)
        actual = exact == (Fraction(0), Fraction(0))
        predicted = predicted_zero(k)
        assert actual == predicted, (k, exact, predicted)
        tested += 1
        zero_count += int(actual)
    assert tested == 729
    assert zero_count == 396
    print(f"checked={tested}; zeros={zero_count}; mismatches=0")


if __name__ == "__main__":
    main()
