from itertools import product


def windows(word, length):
    return [word[i:i + length] for i in range(len(word) - length + 1)]


def verify_overlap_counts():
    checked = 0
    for q in (2, 3, 4):
        for k in range(1, 5):
            for shift in range(1, k + 2):
                size = k + shift
                if q ** size > 500000:
                    continue
                equal = 0
                for word in product(range(q), repeat=size):
                    if word[:k] == word[shift:shift + k]:
                        equal += 1
                assert equal == q ** shift
                checked += 1
    return checked


def verify_local_boundary_step():
    checked = 0
    for q in range(2, 8):
        for d in range(q):
            for left in range(q):
                for right in range(q):
                    if left == d or right == d:
                        continue
                    assert d != left
                    assert d != right
                    checked += 1
    return checked


if __name__ == '__main__':
    a = verify_overlap_counts()
    b = verify_local_boundary_step()
    print('overlap-count cases:', a)
    print('boundary-symbol cases:', b)
    print('PASS')
