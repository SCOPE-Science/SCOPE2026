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

# Mathematical verification record
The proof uses the published half-degree principle for symmetric quartic polynomials [1] and the elementary convexity of feasible ellipsoid matrices. The independent audit channel remains unperformed.

The standalone `verify.py` in the same directory uses SymPy to prove symbolically the two-level fourth-moment formula, both parity formulas, and the distortion quotient. It uses exact `Fraction` arithmetic to compare all two-level values for each integer dimension from \(3\) through \(150\); random centered samples in dimensions \(3\) through \(16\) are only diagnostic. It also proves symbolically the quartic identity on the three-coordinate zero-sum plane.

Actual replay command: `python verify.py`. Actual output: `VERIFY_OK: two-level identities, parity formulas, and n=3 identity exact; finite diagnostics passed`.

The computer checks do not establish nonnegativity at arbitrary vectors, which follows instead from Riener's Theorem 1.3, nor do they establish that no linear reparametrization improves the distortion, which follows from the explicit feasible-ellipsoid averaging argument. They are not substituted for either proof step.

[1] https://arxiv.org/abs/1001.4464
