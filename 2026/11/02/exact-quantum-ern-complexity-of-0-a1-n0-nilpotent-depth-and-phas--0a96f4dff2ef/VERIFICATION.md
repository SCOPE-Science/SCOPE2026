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

The all-parameter proof is in `RESULT.md`. Its pivotal steps are (i) stabilization of successive image ranks, (ii) the rank-one-loss bound for occurrences of the singular letter, (iii) the first zero of \(\cos(j\pi/(2n))\), (iv) uniqueness of the surviving candidate word, and (v) complete positivity under sufficiently small depolarizing perturbation.

`verify.py` is standalone Python 3 code requiring no external packages. Running `python3 verify.py` enumerates the complete binary word languages up to the proposed first mortality length for each \(a\in\{1,\ldots,8\}\), \(n\in\{1,\ldots,5\}\). It performs 126400 real-matrix product evaluations, tests absence of any shorter zero matrix and uniqueness of the target at the boundary, and checks the dimension ceiling for \(a\le32\). The recorded output in `verification_output.txt` reports all checks passing and the smallest nonzero max-entry found as approximately \(0.293892626146\). The enumeration uses floating-point trigonometric values with a strict near-zero threshold; it is not a proof of exact algebraic identities or the unrestricted infinite family.

All infinite statements are justified by the explicit algebra and finite-dimensional Choi perturbation in `RESULT.md`. No independent audit has been performed.
