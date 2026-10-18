#!/usr/bin/env python3
"""Exact finite cross-checks for the hiccup complement word and its discrepancy.
The asymptotic central limit theorem is proved analytically, not by this script.
"""


def complete_word(k, h):
    w = "0"
    for _ in range(h):
        w = w * k + "1"
    return w


def complement_word(k, x, length):
    t = x - 2
    stage = "0"
    chunks = ["0"]
    total = 1
    while total < length:
        chunk = stage * t + "1"
        chunks.append(chunk)
        total += len(chunk)
        stage = stage * k + "1"
    return "".join(chunks)[:length]


def direct_hiccup_complement(k, x, length):
    seen = {x}
    value = x
    index = 1
    while value <= length:
        index += 1
        value += 1 if index in seen else k + 1
        seen.add(value)
    return "".join("1" if i in seen else "0" for i in range(1, length + 1))


def discrepancy(k, s):
    return k * s.count("0") - (k - 1) * len(s)


def certify():
    block_checks = 0
    for k in range(2, 6):
        for h in range(8):
            w = complete_word(k, h)
            expected_length = (k ** (h + 1) - 1) // (k - 1)
            assert len(w) == expected_length
            assert w.count("0") == k ** h
            assert discrepancy(k, w) == 1
            running = 0
            for char in w:
                running += 1 if char == "0" else -(k - 1)
                assert 1 <= running <= 1 + h * (k - 1)
            block_checks += 1

    word_checks = 0
    for k, x in [(2, 3), (2, 4), (2, 7), (3, 3), (3, 4),
                 (3, 6), (4, 3), (4, 6), (5, 8)]:
        for length in (100, 2048, 10000):
            w = complement_word(k, x, length)
            direct = direct_hiccup_complement(k, x, length)
            assert w == direct, (k, x, length)
            assert discrepancy(k, w) == k * w.count("0") - (k - 1) * length
            word_checks += 1

    print(f"PASS: {block_checks} exact complete-tree and prefix-discrepancy checks")
    print(f"PASS: {word_checks} direct sequence/complement comparisons")
    print("NOTE: weak convergence is justified by the analytic block-coupling proof")


if __name__ == "__main__":
    certify()
