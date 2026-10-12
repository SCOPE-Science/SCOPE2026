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

The theorem is proved analytically in `RESULT.md`. The standalone checker `artifacts/verify.py` constructs exact rational Fourier-coordinate vectors for the tangent-image generators and verifies that their span has dimension \(2dL+1\), the full dimension of \(\mathcal P_{dL}\), for \(1\le d\le7\) and \(1\le L\le5\).

The finite rank sweep is a regression check on the product-to-sum argument, not an exhaustive proof of the quantified statement. The general proof rests on the explicit identities in `RESULT.md` and the finite-dimensional open-mapping implication used in the cited source.

The result is limited to the source-defined scalar-rescaled fixed-observable family. No claim of generic-observable behavior, optimality, or saturation at \(m-1\) is made.
