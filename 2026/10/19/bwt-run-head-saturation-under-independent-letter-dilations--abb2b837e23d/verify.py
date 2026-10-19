"""Independent checks for the BWT letter-dilation decomposition.
Pure Python 3, no third-party dependencies.
"""
from itertools import product
from random import Random


def cyclic_bwt_direct(text):
    n = len(text)
    order = sorted(range(n), key=lambda i: text[i:] + text[:i])
    return ''.join(text[(i - 1) % n] for i in order)


def cyclic_bwt_doubling(text):
    n = len(text)
    rank = [ord(c) for c in text]
    distance = 1
    while distance < n:
        order = sorted(range(n), key=lambda i: (rank[i], rank[(i + distance) % n]))
        fresh = [0] * n
        counter = 0
        last = None
        for i in order:
            key = (rank[i], rank[(i + distance) % n])
            if last is not None and key != last:
                counter += 1
            fresh[i] = counter
            last = key
        rank = fresh
        distance *= 2
    order = sorted(range(n), key=lambda i: (rank[i], i))
    return ''.join(text[(i - 1) % n] for i in order)


def count_runs(text):
    return int(bool(text)) + sum(text[i] != text[i-1] for i in range(1, len(text)))

def run_heads(text):
    return ''.join(c for i, c in enumerate(text) if i == 0 or c != text[i-1])


def letter_dilate(word, exponents):
    return ''.join(a * exponents[a] for a in word)


def predicted_bwt(word, exponents):
    """Independent circular-run decomposition, never sorts expanded rotations."""
    n = len(word)
    if len(set(word)) == 1:
        return letter_dilate(word, exponents)
    runs = []
    for i in range(n):
        if word[i] == word[(i - 1) % n]:
            continue
        end = i
        while end < i+n and word[end % n] == word[i]:
            end += 1
        nxt = end % n
        runs.append((word[i], end-i, word[(i - 1) % n], word[nxt], word[nxt:] + word[:nxt]))
    answer = []
    for a in sorted(set(word)):
        for direction in ('lower', 'higher'):
            selected = [u for u in runs if u[0] == a and ((u[3] < a) == (direction == 'lower'))]
            if not selected:
                continue
            top = max(u[1] for u in selected)
            levels = range(1, top+1) if direction == 'lower' else range(top, 0, -1)
            for q in levels:
                active = [u for u in selected if u[1] >= q]
                block = ''.join(u[2] if u[1] == q else a for u in sorted(active, key=lambda u: u[4]))
                filler = a * ((exponents[a]-1)*len(active))
                if direction == 'lower':
                    answer.extend((filler, block))
                else:
                    answer.extend((block, filler))
    return ''.join(answer)


def verify():
    exhaustive = 0
    directions = 0
    for alphabet, largest in [('01', 9), ('012', 7), ('0123', 6)]:
        for n in range(2, largest+1):
            for letters in product(alphabet, repeat=n):
                word = ''.join(letters)
                if len(set(word)) < 2:
                    continue
                baseline = None
                variants = [
                    {a:2 for a in alphabet},
                    {a:3 for a in alphabet},
                    {a:2+(i%3) for i,a in enumerate(alphabet)},
                    {a:5+i for i,a in enumerate(alphabet)},
                ]
                for exponents in variants:
                    expanded = letter_dilate(word, exponents)
                    expected = predicted_bwt(word, exponents)
                    actual = cyclic_bwt_direct(expanded)
                    assert expected == actual, (word, exponents, expected, actual)
                    h = run_heads(actual)
                    if baseline is None:
                        baseline = h
                    else:
                        assert h == baseline, (word, exponents, h, baseline)
                    exhaustive += 1
    rng = Random(17322026)
    randomized = 0
    for _ in range(220):
        alphabet = '012345'[:rng.randrange(2, 7)]
        n = rng.randrange(15, 101)
        word = ''.join(rng.choice(alphabet) for _ in range(n))
        exponents = {a: rng.randrange(2, 9) for a in alphabet}
        expanded = letter_dilate(word, exponents)
        expected = predicted_bwt(word, exponents)
        actual = cyclic_bwt_doubling(expanded)
        assert actual == expected, (word, exponents)
        reference = cyclic_bwt_doubling(letter_dilate(word, {a: 2 for a in alphabet}))
        assert run_heads(actual) == run_heads(reference)
        randomized += 1
    assert cyclic_bwt_direct('01') == '10'
    assert cyclic_bwt_direct('0011') == '1010'
    assert count_runs(cyclic_bwt_direct('01')) == 2
    assert count_runs(cyclic_bwt_direct('0011')) == 4
    print('VERIFY_OK full_multialphabet_BWT_decomposition exhaustive_cases=%d randomized_suffix_doubling_cases=%d sharp_h1=01' % (exhaustive, randomized))


if __name__ == '__main__':
    verify()
