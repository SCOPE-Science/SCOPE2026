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

Running `python verify.py` using Python 3 with SymPy prints a successful exact-symbolic-check message, the numerical critical point and an illustrative pair of stationary points. Two independent symbolic derivations reproduce the mean and variance: the first differentiates the exact backward Laplace transform, and the second solves the first and second backward-moment differential equations directly. Further assertions check the quartic derivative identity, curvature and detachment monotonicity, and exact rational boundary witnesses. The analytic proof in RESULT.md—not finite numerical tests—establishes the phase classification for all real positive parameters.

The model prescribes initial rightward motion at the left boundary without holding, independent direction reversals in the interior, exponential wall holding after leftward arrival, and immediate absorption on rightward arrival at the right endpoint. The proof does not address other initial states, relative variance, higher cumulants, or model perturbations. Numerical critical values are approximations and do not constitute standalone root-exhaustiveness certificates.
