#!/usr/bin/env python3
"""Independent finite checks for the 2-adic image theorem of U_n(P,1).

The infinite conclusion is established by the accompanying proof, not this code.
"""

def valuation_2(x):
    if x == 0:
        raise ValueError('The tested differences must be nonzero')
    return (abs(x) & -abs(x)).bit_length() - 1


def exact_sequence(p, n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, p * b - a
    return result


def modular_image(p, bits):
    modulus = 1 << bits
    a, b = 0, 1
    seen = set()
    steps = 0
    while True:
        seen.add(a)
        a, b = b, (p*b-a) % modulus
        steps += 1
        if (a, b) == (0, 1):
            return seen, steps
        if steps > 16*modulus:
            raise AssertionError('Unexpected period bound')


def predicted_image(h, bits):
    mod = 1 << bits
    return {
        z for z in range(mod)
        if z % (1 << min(h,bits)) == 0
        or z % (1 << min(2*h,bits)) == 1 % (1 << min(2*h,bits))
        or z % (1 << min(2*h,bits)) == (-1) % (1 << min(2*h,bits))
    }


def check():
    modular_profiles = 0
    metric_pairs = 0
    checked_states = 0
    for p in (-32,-16,-12,-8,-4,4,8,12,16,24,32,40):
        h = valuation_2(p)
        for bits in range(1,12):
            image, period = modular_image(p,bits)
            expected = predicted_image(h,bits)
            assert image == expected, (p,bits, sorted(image ^ expected))
            formula = 1 << max(0,bits-h)
            plusminus = (1 if bits == 1 else 2) * (1 << max(0,bits-2*h))
            assert len(image) == formula + plusminus, (p,bits,len(image),formula+plusminus)
            modular_profiles += 1
            checked_states += period
        series = exact_sequence(p, 210)
        for j in range(1,100):
            assert valuation_2(series[2*j]) == h + valuation_2(j)
        for i in range(38):
            for j in range(i+1,38):
                assert valuation_2(series[2*j]-series[2*i]) == h+valuation_2(j-i)
                assert valuation_2(series[4*j+1]-series[4*i+1]) == 2*h+valuation_2(j-i)
                assert valuation_2(series[4*j+3]-series[4*i+3]) == 2*h+valuation_2(j-i)
                metric_pairs += 3
    print('PASS', modular_profiles, 'complete modular images,',checked_states,'modular recurrence states,',metric_pairs,'valuation-isometry comparisons')


if __name__ == '__main__':
    check()
