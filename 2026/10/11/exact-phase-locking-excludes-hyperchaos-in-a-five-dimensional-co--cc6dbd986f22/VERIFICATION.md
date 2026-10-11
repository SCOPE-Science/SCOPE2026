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

Running `python verify.py` checks exact multivariate-polynomial identities for the printed integer-order vector field. The script verifies:

- \(\dot J+(\sigma+1)J=0\) for \(J=x_1x_4-x_2x_3\);
- full five-dimensional divergence \(-2\sigma-2-\beta\);
- base-flow divergence \(-\sigma-1-\beta\);
- invariance of the real fixed-phase leaf \(x_2=x_4=0\);
- trace \(-\sigma-1\) of the imaginary variational block.

The script returns `VERIFY_OK` only if all identities hold exactly as polynomials. The bounded-completeness argument, fixed-phase consequence, recurrence-based zero exponents, and Oseledets/Liouville interpretation are analytic steps and are not replaced by the checker. No claim is made for the Caputo fractional system.
