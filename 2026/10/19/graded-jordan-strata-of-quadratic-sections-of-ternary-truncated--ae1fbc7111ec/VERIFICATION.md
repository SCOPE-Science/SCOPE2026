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

# Reproduction
Run `python3 verify.py` in the directory containing this document. The program uses only the Python standard library. It reports `EXHAUSTIVE_GF3_N3_OK 729 {0: 1, 1: 26, 2: 234, 3: 468}`, followed by sampled-check indicators and `VERIFY_OK`.

The checker builds actual multiplication maps from coefficient arrays in the graded truncated polynomial algebra. It computes the ranks of multiplication by \(Q\) and \(Q^2\) independently, reconstructs graded Jordan starts from these two sets of ranks, and compares them with the closed formulas. It checks every one of the \(729\) quadratic forms in three variables over \(\mathbb F_3\), plus \(90\) seeded samples over \(\mathbb F_9\) in three variables, \(90\) samples over \(\mathbb F_3\) in four, and \(25\) in five. Its finite-field rank counts and integer rank-frequency identities provide supplementary tests.

The underlying theorem for arbitrary \(n\) and all finite characteristic-three fields is proved in `RESULT.md`; these finite computations are not a substitute for that proof. The status above records that independent audit has not been performed.
