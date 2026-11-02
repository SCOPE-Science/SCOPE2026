#!/usr/bin/env python3
"""Finite exhaustive check of a run-limited one-marker supersequence theorem.

No third-party dependencies. Run: python3 verify_onehot_rll.py
This finite audit corroborates, but does not replace, the infinite proof.
"""

def all_no_000(length):
    """Generate all binary strings of given length avoiding three adjacent zeros."""
    def rec(prefix, zeros):
        if len(prefix) == length:
            yield prefix
        else:
            if zeros < 2:
                yield from rec(prefix + '0', zeros + 1)
            yield from rec(prefix + '1', 0)
    yield from rec('', 0)


def subsequence(needle, haystack):
    j = 0
    for symbol in haystack:
        if symbol == needle[j]:
            j += 1
            if j == len(needle):
                return True
    return False


def covers_one_marker(word, n):
    return all(subsequence('0' * i + '1' + '0' * (n - i - 1), word)
               for i in range(n))


def predicted_optimizers(n):
    if n % 2 == 0:
        return {'010' * (n // 2)}
    m = (n - 1) // 2
    words = {'001' * m + '00', '1' + '001' * m + '0',
             '01' + '001' * m}
    for j in range(m):
        lengths = [1 if q == j else 2 for q in range(m)]
        words.add('01' + ''.join('0' * d + '1' for d in lengths) + '0')
    return words


def main():
    total_words_examined = 0
    for n in range(4, 15):
        optimum = (3 * n + 1) // 2
        found = set()
        for length in range(n, optimum + 1):
            for word in all_no_000(length):
                total_words_examined += 1
                # Independent of the rank/interval criterion used in the proof.
                if covers_one_marker(word, n):
                    assert length == optimum, (n, length, word)
                    found.add(word)
        expected = predicted_optimizers(n)
        assert found == expected, (n, len(found), len(expected),
                                   found ^ expected)
        assert all('111' not in word for word in found)
        print(f'n={n}: min={optimum}, all_optimizers={len(found)}, verified')
    print(f'CHECK_OK total_candidate_hosts_examined={total_words_examined}')


if __name__ == '__main__':
    main()
