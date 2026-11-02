#!/usr/bin/env python3
"""Standalone finite verification of a closed-factor classification.

Uses direct substring enumeration and border-occurrence tests; the predicted
sets are constructed independently from the ruler-word parameterization.
"""
from collections import Counter


def zimin(rank):
    word = b""
    for letter in range(1, rank + 1):
        word = word + bytes([letter]) + word
    return word


def is_closed(word):
    if len(word) <= 1:
        return True
    length = len(word)
    for border_length in range(1, length):
        border = word[:border_length]
        if border != word[-border_length:]:
            continue
        # The substring window ends before the final occurrence, but allows
        # every possible strictly internal start, including overlaps.
        if word.find(border, 1, length - 1) == -1:
            return True
    return False


def predicted(rank):
    answer = set()
    for marker in range(1, rank + 1):
        core = zimin(marker - 1)
        answer.add(bytes([marker]))
        for level in range(marker - 1):
            low = 1 << level
            high = (1 << (level + 1)) - 1
            for left in range(low, high + 1):
                for right in range(low, high + 1):
                    answer.add(core[-left:] + bytes([marker]) + core[:right])
    return answer


def length_prediction(rank, length):
    if length == 1:
        return rank
    for level in range(rank - 1):
        d = 1 << level
        if 2 * d + 1 <= length <= 4 * d - 1:
            return (rank - level - 1) * min(length - 2 * d, 4 * d - length)
    return 0


def main():
    for rank in range(1, 9):
        word = zimin(rank)
        actual_factors = {word[i:j] for i in range(len(word))
                          for j in range(i + 1, len(word) + 1)}
        actual = {factor for factor in actual_factors if is_closed(factor)}
        expected = predicted(rank)
        assert actual == expected, (rank, actual - expected, expected - actual)
        expected_total = (4 ** rank + 6 * rank - 1) // 9
        assert len(actual) == expected_total, (rank, len(actual), expected_total)
        observed = Counter(map(len, actual))
        for length in range(1, len(word) + 1):
            assert observed[length] == length_prediction(rank, length), (
                rank, length, observed[length], length_prediction(rank, length))
        by_highest = Counter(max(factor) for factor in actual)
        for marker in range(1, rank + 1):
            expected_marker = (4 ** (marker - 1) + 2) // 3
            assert by_highest[marker] == expected_marker, (
                rank, marker, by_highest[marker], expected_marker)
        print(f"rank={rank} length={len(word)} factors={len(actual_factors)} "
              f"closed={len(actual)} checked=PASS")
    print("COMPLETE: direct enumeration, endpoint classification, and all-length counts PASS")


if __name__ == "__main__":
    main()
