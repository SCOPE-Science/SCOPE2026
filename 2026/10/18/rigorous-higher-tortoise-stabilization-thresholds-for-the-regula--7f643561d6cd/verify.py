#!/usr/bin/env python3
"""Finite residue-template certificate for iterated-tortoise complexity.

Run using Python 3 standard library: python verify.py
The theorem's infinite step is proved in RESULT.md, not inferred from a cutoff.
"""
import hashlib
import json
from pathlib import Path

CASES = ((2, 12, 13, 4), (3, 13, 14, 4),
         (4, 24, 25, 5), (5, 25, 26, 5))


def paperfold_bit(index):
    """One-based regular paperfolding bit from the odd part modulo four."""
    assert index >= 1
    while index % 2 == 0:
        index //= 2
    return "1" if index % 4 == 3 else "0"


def complete_factors(length, r):
    """All length-`length` factors by a proved two-adic residue cover.

    For length <= 2**r, each window has at most one multiple of 2**r.
    All other bits depend only on the window start modulo 2**(r+1).
    On fixed residue classes the exceptional bit independently attains 0 and 1.
    """
    assert 1 <= length <= 2**r
    modulus = 2**r
    factors = set()
    for start in range(1, 2 * modulus + 1):
        template = [None if j % modulus == 0 else paperfold_bit(j)
                    for j in range(start, start + length)]
        assert template.count(None) <= 1
        choices = ("0", "1") if None in template else ("0",)
        for choice in choices:
            factors.add("".join(choice if symbol is None else symbol
                                for symbol in template))
    return factors


def tortoise(word):
    """Binary tortoise: remove the first 1 and append it to the right."""
    i = word.find("1")
    return word if i < 0 else word[:i] + word[i + 1:] + "1"


def iterated_tortoise(word, k):
    for _ in range(k):
        word = tortoise(word)
    return word


def direct_factor_set(length, count=16384):
    sequence = "".join(paperfold_bit(j) for j in range(1, count + 1))
    return {sequence[i:i + length]
            for i in range(count - length + 1)}


def image_classes(factors, k):
    groups = {}
    for word in factors:
        image = iterated_tortoise(word, k)
        groups.setdefault(image, []).append(word)
    return groups


def summary(k, n, r):
    factors = complete_factors(n, r)
    groups = image_classes(factors, k)
    collisions = sorted([sorted(group) for group in groups.values()
                         if len(group) > 1])
    return {
        "k": k, "n": n, "template_power": r,
        "factor_count": len(factors),
        "distinct_image_count": len(groups),
        "minimum_ones": min(map(lambda w: w.count("1"), factors)),
        "factor_list_sha256": hashlib.sha256(
            ("\n".join(sorted(factors)) + "\n").encode("ascii")).hexdigest(),
        "collision_classes": collisions,
    }


def build_certificate():
    result = {"schema_version": 1, "cases": []}
    for k, previous_n, first_n, r in CASES:
        previous = summary(k, previous_n, r)
        first = summary(k, first_n, r)
        assert first["distinct_image_count"] == first["factor_count"]
        assert first["minimum_ones"] >= k + 1
        assert previous["distinct_image_count"] < previous["factor_count"]
        assert previous["collision_classes"]
        assert len(previous["collision_classes"][0]) == 2
        assert complete_factors(previous_n, r) == direct_factor_set(previous_n)
        assert complete_factors(first_n, r) == direct_factor_set(first_n)
        result["cases"].append({"k": k, "last_collision_length": previous_n,
                                "first_injective_length": first_n,
                                "previous": previous, "first": first})
    return result


def main():
    certificate = build_certificate()
    expected_path = Path(__file__).with_name("certificate.json")
    actual = json.dumps(certificate, ensure_ascii=False, indent=2,
                        sort_keys=True) + "\n"
    if expected_path.exists():
        expected = expected_path.read_text(encoding="utf-8")
        assert actual == expected, "finite residue certificate mismatch"
    else:
        expected_path.write_text(actual, encoding="utf-8")
    for c in certificate["cases"]:
        k, n = c["k"], c["first_injective_length"]
        p, f = c["previous"], c["first"]
        print(f"k={k} last_collision_n={n-1}: "
              f"{p['factor_count']} factors, {p['distinct_image_count']} images; "
              f"first_injective_n={n}: {f['factor_count']} factors, "
              f"{f['distinct_image_count']} images, min_ones={f['minimum_ones']}")
    print("PASS: exact residue classes; prefix cross-check; all four sharp thresholds")


if __name__ == "__main__":
    main()
