#!/usr/bin/env python3
"""Exact finite certificate for binary digit-reversal false-positive onset."""
def reverse_bits(n, length):
    result = 0
    for _ in range(length):
        result = 2 * result + (n & 1)
        n >>= 1
    return result

def acorr(n, length):
    return tuple((n & (n >> d)).bit_count() for d in range(length))

def census(limit=21):
    exceptional = []
    for length in range(2, limit+1):
        fibers = {}
        bad = []
        for interior in range(1 << (length-2)):
            value = 1 + (interior << 1) + (1 << (length-1))
            reverse = reverse_bits(value,length)
            if value > reverse:
                continue
            key = value * reverse
            profile = acorr(value,length)
            alternatives = fibers.setdefault(key,{})
            if profile not in alternatives:
                for other_profile, other in alternatives.items():
                    bad.append((other,value,key))
                alternatives[profile] = value
        expected = [] if length < 21 else [(1100125,1269125,1681449752125)]
        bad = [(*sorted((a,b)),v) for a,b,v in bad]
        assert sorted(bad) == expected, (length,bad)
        print(length,len(fibers),len(bad))
        exceptional.extend((length,a,b,key) for a,b,key in bad)
    assert exceptional == [(21,1100125,1269125,1681449752125)]
    # At the exceptional product there are precisely two canonical words,
    # not merely two distinct autocorrelation vectors.
    length = 21
    key = 1681449752125
    members = []
    for interior in range(1 << (length-2)):
        value = 1 + (interior << 1) + (1 << (length-1))
        reverse = reverse_bits(value, length)
        if value <= reverse and value*reverse == key:
            members.append(value)
    assert members == [1100125,1269125], members
    a,b = 1100125,1269125
    assert a * reverse_bits(a,21) == b * reverse_bits(b,21) == 1681449752125
    assert acorr(a,21)[0] == 10 and acorr(b,21)[0] == 11
    print('CERTIFIED: unique false-positive fiber at length 21')
if __name__ == '__main__':
    census()
