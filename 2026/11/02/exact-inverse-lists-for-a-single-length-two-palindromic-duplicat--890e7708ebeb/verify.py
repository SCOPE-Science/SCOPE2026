"""Exhaustive independent checker for one reverse-palindromic duplication of span two.
Scientific data only; no external dependencies.
"""
from itertools import product


def parents(y):
    result = set()
    for i in range(len(y) - 3):
        a, b, c, d = y[i:i+4]
        if a == d and b == c:
            result.add(y[:i+2] + y[i+4:])
    return result


def marked_runs(y):
    runs = []
    for x in y:
        if runs and runs[-1][0] == x:
            runs[-1] = (x, runs[-1][1] + 1)
        else:
            runs.append((x, 1))
    count = 0
    for j, (letter, length) in enumerate(runs):
        if length >= 4:
            count += 1
        elif (length == 2 and 0 < j < len(runs)-1
              and runs[j-1][0] == runs[j+1][0]):
            count += 1
    return count


def total_formula(q, m):
    return q**(m-4) * ((m-3)*q*(q-1) + q + (m-4)*(q-1))


def run():
    count_words = 0
    cases = 0
    for q, upper in ((2, 12), (3, 9), (4, 7)):
        for m in range(4, upper+1):
            cases += 1
            tally = 0
            peak = 0
            for t in product(range(q), repeat=m):
                word = ''.join(map(str, t))
                p = parents(word)
                predicted = marked_runs(word)
                assert len(p) == predicted, (q, m, word, p, predicted)
                tally += len(p)
                peak = max(peak, len(p))
                count_words += 1
            assert peak == (m-2)//2, (q, m, peak)
            assert tally == total_formula(q, m), (q, m, tally, total_formula(q,m))
    print(f'VERIFY_OK cases={cases} received_words={count_words} all_parent_sets=checked exact_peak=checked exact_incidence=checked')


if __name__ == '__main__':
    run()
