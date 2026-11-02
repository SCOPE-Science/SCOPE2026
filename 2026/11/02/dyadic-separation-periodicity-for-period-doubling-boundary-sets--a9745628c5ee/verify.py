#!/usr/bin/env python3
"""Finite consistency checks for period-doubling paired-window spectra.

The infinite assertions rest on the proof in RESULT.md; this program
checks examples and the recurrence without claiming exhaustive infinity.
"""


def period_doubling_by_substitution(size):
    seq = "0"
    while len(seq) < size:
        seq = "".join("01" if c == "0" else "00" for c in seq)
    return seq[:size]


def period_doubling_by_valuation(size):
    def symbol(index):
        k = index + 1
        return "1" if (k & -k).bit_length() % 2 == 0 else "0"  # parity of v_2(k)
    return "".join(symbol(i) for i in range(size))


def spectrum(sequence, a, b, d):
    if not 0 <= a <= d or b < 0:
        raise ValueError("invalid window lengths or separation")
    return {(sequence[i:i+a], sequence[i+d:i+d+b])
            for i in range(len(sequence)-d-b+1)}


def interleave_even(word, length):
    return "".join("0" if j % 2 == 0 else str(1-int(word[j//2]))
                   for j in range(length))


def interleave_odd(word, length):
    return "".join(str(1-int(word[j//2])) if j % 2 == 0 else "0"
                   for j in range(length))


def main():
    N = 32768
    seq = period_doubling_by_substitution(N)
    assert seq == period_doubling_by_valuation(N)
    checks = N
    # Both the separated-window periodicity and the defining recursion
    # are checked from actual independently generated finite words.
    for a in range(1, 7):
        for b in range(1, 7):
            upper = max(a, b)
            period = 2 * (1 << ((upper-1).bit_length()))
            for d in range(a, a+2*period):
                assert spectrum(seq, a, b, d) == spectrum(seq, a, b, d+period), (a,b,d)
                checks += 1
    # Verify the recursive even-start/odd-start decimations at selected gaps.
    for a in range(1, 6):
        for b in range(1, 6):
            ea,oa = a//2,(a+1)//2
            eb,ob = b//2,(b+1)//2
            for d in range(a, a+13):
                if d % 2 == 0:
                    m=d//2
                    pairs1=spectrum(seq,ea,eb,m)
                    pairs2=spectrum(seq,oa,ob,m)
                    exp={(interleave_even(x,a),interleave_even(y,b)) for x,y in pairs1}
                    exp|={(interleave_odd(x,a),interleave_odd(y,b)) for x,y in pairs2}
                else:
                    m=d//2
                    pairs1=spectrum(seq,ea,ob,m)
                    pairs2=spectrum(seq,oa,eb,m+1)
                    exp={(interleave_even(x,a),interleave_odd(y,b)) for x,y in pairs1}
                    exp|={(interleave_odd(x,a),interleave_even(y,b)) for x,y in pairs2}
                assert spectrum(seq,a,b,d)==exp,(a,b,d)
                checks += 1
    types={
        2:{("00","01"),("00","10"),("01","00"),("01","01"),("10","00"),("10","10")},
        3:{("00","00"),("00","01"),("00","10"),("01","00"),("01","10"),("10","00"),("10","01")},
        0:{("00","00"),("00","01"),("00","10"),("01","00"),("01","01"),("10","00"),("10","10")},
    }
    types[1] = types[3]
    for d in range(2, 80):
        assert spectrum(seq,2,2,d)==types[d%4]
        checks+=1
    assert len({frozenset(spectrum(seq,2,2,d)) for d in range(2,6)})==3
    print("VERIFY_OK",checks,"finite checks; infinite validity from RESULT.md")


if __name__ == "__main__":
    main()
