"""Independent direct transition simulation of all one-letter insertions."""


def reset(word, n):
    states = list(range(n))
    for symbol in word:
        if symbol == 'a':
            states = [(x + 1) % n for x in states]
        else:
            states = [0 if x == n - 1 else x for x in states]
    return len(set(states)) == 1


def is_subsequence(x, y):
    iterator = iter(y)
    return all(any(c == wanted for c in iterator) for wanted in x)


def main():
    for n in range(2, 31):
        word = 'b' + ('a' * (n - 1) + 'b') * (n - 2)
        assert len(word) == (n - 1) ** 2
        assert reset(word, n)
        words = {word[:i] + symbol + word[i:]
                 for i in range(len(word) + 1) for symbol in 'ab'}
        good = {candidate for candidate in words if reset(candidate, n)}
        expected = n * n - 4 * n + 7
        assert len(good) == expected, (n, len(good), expected)
        assert all(is_subsequence(word, candidate) for candidate in good)
        print(f'n={n}: inserted candidates={len(words)}, resets={len(good)}')
    print('VERIFY_INSERTION_OK')


if __name__ == '__main__':
    main()
