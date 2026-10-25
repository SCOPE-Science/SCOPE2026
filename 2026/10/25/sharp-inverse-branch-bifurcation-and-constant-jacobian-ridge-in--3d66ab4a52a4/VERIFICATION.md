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
The included standalone `check_geometry.py` uses exact symbolic algebra for the Jacobian, its constant-value ridge, and the cubic critical normal form, and high-precision arithmetic for the caustic width, a genuine three-physical-preimage output, and the sharp threshold scaling. Run `python check_geometry.py` in an environment with `sympy` and `mpmath` installed. Its standard output is preserved in `verification_output.txt`.

These checks are finite. The inverse-count theorem is proved by global monotonicity of the scalar inverse equation; the Lyapunov and area conclusions are proved analytically from an exact determinant identity and invariant-set hypotheses. No numerical run establishes all parameter values, invariant measures, or novelty.
