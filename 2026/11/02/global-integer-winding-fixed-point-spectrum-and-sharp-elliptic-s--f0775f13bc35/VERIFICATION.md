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

Run `python verify.py` with Python 3 and SymPy. The standalone checker executes 145 separate finite tests and reports `PASS`. It checks symbolic factorization of the integer-winding quadratic, determinant-one residue algebra, exact positive/zero/negative root classifications for rational parameters, height counts based on independently reconstructed quadratic roots, strict positive-winding elliptic-index thresholds, and the sharp small-perturbation two-term expansion at numerical samples.

The full proof, including all integer windings, the monotonicity argument, the exact ceiling convention at a parabolic threshold, and the uniform bounded remainder, appears in RESULT.md. The checker tests representative finite instances and does not attempt an exhaustive parameter proof or mathematical independence certification. It does not check nonlinear ellipticity, measure-theoretic invariant islands, or model applicability at unbounded physical action. Relevant source comparisons and residual publication-priority risks are in REVIEW.md and AUDIT.json.
