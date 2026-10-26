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

# Verification

The proof is the exhaustive three-case cyclic-run-signature argument in `RESULT.md`. Run `python3 check.py` with the Python standard library, with no input files. It enumerates all unordered pairs of distinct deleted source positions and compares two independently defined canonicalizations: lexicographically least rotation of the resulting string and lexicographically least rotation of its alternating letter/run-length signature. It checks all parameter pairs with \(3\le a\le8\) and \(3\le k\le22\), compares all three composition-refined formulas, and reruns from a rotated input. The successful recorded run printed `CIRCULAR_TWO_DELETION_PASS cases=120 a=3..8 k=3..22 independent=word-rotations,run-cycles source_rotations=checked`.

These are exhaustive tests of the stated finite domain, not a proof for all integers. The proof for the unlimited domain is the run-pattern classification, with collisions handled explicitly at \(a=3\). No probabilistic simulation or unbounded computational certification is used.
