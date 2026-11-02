---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the nine-square minimum

Two separate complete enumerators were executed in Python 3. Run `python3 verify_shortest.py` and `python3 verify_bits.py` from the directory containing these standalone files.

The first enumerator builds all overlap-free binary prefixes through length 48. For each new character, only newly ending periodic suffixes need checking for overlaps. For each retained word, a separate complete dynamic program maximizes the number of nonempty squares in a whole-word factorization. Its final count is 416 overlap-free words at length 48, exactly two permitting nine squares, zero at every smaller length. It also checks all nine-square decompositions of the two extremizers, finding one each.

The second verifier independently uses integer bit masks for all overlap tests and the two equal half-blocks of each square, yielding the same two extremizers. First marker: `NINE_SQUARES_MIN_LENGTH_AND_UNIQUENESS_OK`; second marker: `INDEPENDENT_INTEGER_OVERLAP_CHECK_OK`.

The domain is finite, and exhaustive by the inductively proved two-extension recurrence; no extrapolation to longer words is claimed. Third-party historical priority and independent expert correctness audit remain unperformed.
