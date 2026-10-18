"""Exact finite cross-checks for simultaneous base-b / base-(b**3) palindromes.

The independent proof establishes the all-length result; this program tests finite cases.
Python 3 standard library only.
"""
from itertools import product


def digits(n, base):
    a = []
    while n:
        a.append(n % base)
        n //= base
    return tuple(reversed(a))


def from_digits(ds, base):
    n = 0
    for d in ds:
        n = n * base + d
    return n


def expected(b, L):
    q, r = divmod(L, 3)
    if r == 0:
        return (b-1)*b**(2*((q+1)//2)-1)
    return (b-1)*b**(q//2)


def structural(b, L):
    q, r = divmod(L, 3)
    ans = set()
    if r == 0:
        orbit_count = (q+1)//2
        # One three-digit palindromic block for each orbit of block reversal.
        for a0 in range(1, b):
            for rest in product(range(b), repeat=2*orbit_count-1):
                vals = (a0, *rest)
                blocks = [tuple(vals[2*i:2*i+2][:1]) + tuple(vals[2*i+1:2*i+2]) + tuple(vals[2*i:2*i+1]) for i in range(orbit_count)]
                full = (blocks + list(reversed(blocks))) if q % 2 == 0 else (blocks + list(reversed(blocks[:-1])))
                w = sum((list(t) for t in full), [])
                ans.add(from_digits(w, b))
    else:
        orbit_count = q//2+1
        for a0 in range(1, b):
            for rest in product(range(b), repeat=orbit_count-1):
                half = [a0, *rest]
                letters = half + (list(reversed(half)) if (q+1)%2==0 else list(reversed(half[:-1])))
                if r == 1:
                    w = [letters[0]]
                    for digit in letters[1:]:
                        w += [0, 0, digit]
                else:
                    w = [letters[0], letters[0]]
                    for digit in letters[1:]:
                        w += [0, digit, digit]
                ans.add(from_digits(w, b))
    return ans


def exhaustive(b, L):
    # Enumerate all b-palindromes of length L, then independently convert
    # each integer to base b**3 without using a pre-derived block formula.
    found = set()
    h = (L+1)//2
    for leading in range(1, b):
        for rest in product(range(b), repeat=h-1):
            left = (leading, *rest)
            w = left + (left[::-1] if L%2==0 else left[-2::-1])
            n = from_digits(w, b)
            d = digits(n, b**3)
            if d == d[::-1]:
                found.add(n)
    return found


def main():
    case_count = 0
    max_lengths = {2:20, 3:14, 4:11, 5:9}
    for b, maximum in max_lengths.items():
        for L in range(1,maximum+1):
            actual = exhaustive(b,L)
            theory = structural(b,L)
            assert actual == theory, (b,L, sorted(actual ^ theory)[:12])
            assert len(actual) == expected(b,L), (b,L,len(actual),expected(b,L))
            case_count += 1
    print(f'VERIFY_OK; {case_count} base-length profiles; two independent descriptions agree')


if __name__ == '__main__':
    main()
