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

Execute `python3 verify.py` in a Python 3 environment. This uses only the standard library, generates both sets of spherical vertices for dimensions two through eight, computes intrinsic angular squared distances, compares known minimizer values and two fourth-moment bounds, and verifies the Rademacher fourth-moment identity over a deterministic seed. At packaging it passed 2,114 sampled numerical checks. Numerical tolerance is \(2\times10^{-13}\) for the quartic identity and \(10^{-11}\) for sampled energy bounds; see executable code for precise arithmetic.

The all-dimensional proof does not depend on these samples. Its critical check is the positive recurrence for the coefficients of \(\arcsin^2\sqrt s\), followed by the strict Jensen equality case and explicit signed-coordinate fourth moments. Arithmetic overflow or floating-point errors at high dimensions do not affect the analytic theorem. No independent verification or certified computation has been performed.
