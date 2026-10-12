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

# Finite verification and boundaries

The standalone `verify.py` uses only the Python 3 standard library. Running `python3 verify.py` reconstructs each generator matrix by enumerating all nonzero ternary column vectors, computes the projective lines through each column, enumerates the exact minimal two-helper recovery pairs, and solves maximum matchings by recursive bitmask DP independently for every local line. It tests dimensions 2, 3, 4, respectively of lengths 10, 29, 84. The predicted counts of nonparallel three-coordinate dual circuits are 60, 572, and 4808. Success prints `VERIFY_OK`. The script is exhaustive only for these finite dimensions. No infinite proof, literature novelty, statistical storage reliability, or external audit is inferred from its execution; the all-dimension statement uses the projective-line incidence proof given in RESULT.md.
