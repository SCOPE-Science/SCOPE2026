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

# Reproducibility and verification

Run `python3 check_scaling.py` using Python 3.9 or newer and the standard library. The checker computes exact rational matrix inverses and exactly compares the finite-candidate theorem with a bounded independent exponent enumeration for 168 nonsingular test matrices, representing 19,558 exponent assignments after common-shift normalization. The output records PASS and also tests nine diagonal examples against the analytic sharp constant using floating-point comparisons. The test set is finite; the accompanying proof, rather than enumeration, establishes optimality over unbounded integer exponents and all nonsingular matrices.

The critical proof steps are the two norm identities, monotonicity of the inverse norm under increasing a block scale at fixed maximal scaled row norm, and the largest-gap covering lemma for \(b\) points of the logarithmic circle. The sharpness example is computed from exact diagonal formulas. The historical-priority assessment remains subject to the explicit residual risks in `REVIEW.md` and `AUDIT.json`; no independent validation has been performed.
