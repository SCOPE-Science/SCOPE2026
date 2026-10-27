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

# Reproducible verification
Run `python verify.py` with the versions declared in `requirements.txt`; `verification_output.txt` records the output obtained from the bundled source. The script verifies the trigonometric factorization and continuous normalization exactly in symbolic algebra, evaluates the defining piecewise integral independently at nine frequencies to high precision, checks ten exact double-zero lattice sites, samples two simple roots in each of twelve periods with derivative signs, and symbolically differentiates the two-variable ambiguity function at four resonant nodes.

The proof of exhaustive existence and uniqueness for infinitely many half-periods is the sign-at-roots argument in RESULT.md, not numerical enumeration. The indefinite Hessian and analytic Morse lemma, not a plot, prove nodal crossing. The checks do not certify priority, full complex zero geometry, or behavior at arbitrary delays.
