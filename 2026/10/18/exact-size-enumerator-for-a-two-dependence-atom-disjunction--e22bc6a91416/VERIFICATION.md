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

# Verification and reproducibility

Run `python3 verify.py` in the directory containing this file and the standalone checker. Python's standard library suffices. Expected output includes `ALL_16_RECTANGULAR_FIBER_CENSUSES_OK`, `BINARY_256_FULL_TEAMS_OK`, and the final `DEPENDENCE_RECTANGULAR_SIZE_ENUMERATOR_OK`.

The first group independently enumerates every subset of every \(r\times s\) grid with \(1\le r,s\le4\), tests containment in a cross directly by bit masking, and compares the full cardinality histogram against the polynomial. The second group separately implements disjunction by enumerating every possible split of every team in a two-element, three-variable domain, comparing all \(256\) truth values with the derived geometric condition. It counts \(225\) satisfied teams.

These are finite verification tests, **not** substitutes for the all-parameter proof in `RESULT.md`. No mechanized proof or independent mathematical audit has been performed. The proof's noncomputational critical step is the classification of intersections of two distinct row-column crosses, stated explicitly in `RESULT.md`.
