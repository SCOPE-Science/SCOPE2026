"""Finite checks for explicit minimal absent factors of period-doubling words.

This program checks independently specified substitutions, candidate formulas,
minimal absence, the three-position occurrence lemma, and a finite census.
The all-level theorem is proved by induction in RESULT.md, not by enumeration.
"""


def mu(word):
    return ''.join('01' if c == '0' else '00' for c in word)


def psi(word):
    return mu(word)[1:]


def factors(word, size):
    return {word[i:i + size] for i in range(len(word) - size + 1)}


def absent_minimal(word, candidate):
    return (candidate not in word and candidate[:-1] in word
            and candidate[1:] in word)


def all_maw(word):
    observed = {0: {''}}
    output = set()
    for m in range(1, len(word) + 2):
        fm = factors(word, m)
        previous = observed[m - 1]
        if m >= 2:
            for prefix in previous:
                for letter in '01':
                    candidate = prefix + letter
                    if candidate not in fm and candidate[1:] in previous:
                        output.add(candidate)
        observed[m] = fm
    return output


def check():
    words = ['0']
    for _ in range(12):
        words.append(mu(words[-1]))
    for k in range(3, 12):
        w = words[k]
        v = words[k - 2]
        n = len(v)
        occurrences = [i for i in range(len(w) - n + 1) if w.startswith(v, i)]
        assert occurrences == [0, 2 * n, 3 * n], (k, occurrences)
        a = v[-1] + v + '0'
        b = words[k - 1][-1] + words[k - 1]
        candidates = {'11', a, b}
        x, y = '0000', '1001'
        for j in range(k - 2):
            candidates.add(x)
            candidates.add(y)
            x, y = psi(x), psi(y)
        assert len(candidates) == 2 * k - 1
        for candidate in candidates:
            assert absent_minimal(w, candidate), (k, candidate)
        if k <= 8:
            all_words = all_maw(w)
            assert candidates <= all_words
            print(f'k={k}, length={len(w)}, exhibited={len(candidates)}, total={len(all_words)}')
        else:
            print(f'k={k}, length={len(w)}, exhibited={len(candidates)}')
    print('PASS: witness minimal absence k=3..11; exact finite census k=3..8.')


if __name__ == '__main__':
    check()
