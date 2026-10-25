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

The proof uses the exact equations for the numbers of changed positions inside the four binary-coordinate agreement classes. These equations reduce the possible positive intersection types to eight; the proof evaluates each and counts labeled configurations before dividing by the six orders of a triple. The complete finite-dimensional experiment is a separate check, not a substitute for the all-dimensional argument.

Reproduce the check with `python3 verification/verify_triple_spheres.py` using only the Python standard library. For every integer dimension from three through eight, the program constructs each exact-two Hamming sphere directly from the Hamming distance, enumerates every unordered triple of distinct centers, compares its histogram to the symbolic formula, and checks the maximum. It also independently enumerates all admissible agreement-pattern types in a separate code path. The recorded output in `verification/verify_output.txt` terminates with `VERIFY_OK`.

The verifier explicitly checks the dimensions \(3\le n\le8\); it does **not** exhaust infinitely many dimensions. The all-dimensional classification, asymptotic frequency and sharp two-list threshold are established by the complete proof in `RESULT.md`. No external independent audit has been performed.
