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

# Reproducible finite verification

Run `python3 verify_cantor.py` with Python 3 and no extra dependencies. The script independently tests the all-parameter formula through finite ranges in three ways:

1. A power-of-two congruence recognizer decides true factor membership for each tested binary word without consulting the proposed antidictionary. All \(2^n\) binary words are considered for every \(1\le n\le14\) and \(3\le q\le8\); minimal absent words are rebuilt by matching present length-one-deleted prefixes and suffixes.
2. Finite substitution iterates are built independently of the congruence test. They are cross-checked against the base-\(q\) digit rule for the indicator of ones. For \(q=3,4,5,6\), these finite prefixes are used to enumerate minimal absences at respectively \(110,100,85,70\) successive lengths. These prefix-derived answers agree with the claimed infinite-family formula. The verifier additionally checks every enumerated finite factor by the congruence criterion.
3. For \(q=3,\ldots,13\), the two special forbidden words indexed by \(j=0,\ldots,4\) are shown absent by exact congruence calculations, while both of their length-one-deleted factors satisfy the same occurrence criterion.

Output from the program packaged with this finding:

`VERIFY_OK exhaustive_q=3..8_lengths=1..14 direct_prefix_cases=365 highscale_candidates=110 distinct_absences=81`

These tests cover finite parameter ranges only. The exact all-rank conclusion follows from the proof in RESULT.md, not from extrapolation. The congruence recognizer itself follows from elementary 2-adic congruence arithmetic and is used as an independent implementation check, not as a separate externally certified theorem.
