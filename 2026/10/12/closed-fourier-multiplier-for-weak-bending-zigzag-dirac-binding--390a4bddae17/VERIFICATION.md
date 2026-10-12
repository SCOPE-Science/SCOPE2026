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

The standalone checker `verify_multiplier.py` uses high-precision arithmetic only as a replay aid. It independently verifies the exact transverse matrix-element formula by quadrature for several even and odd modes; evaluates the infinite weighted series and the elementary cotangent/coth formula at values below, at, and above \(q=1\); checks \(\sum_jw_j=1\) and \(\sum_jw_jA_j=4\); tests the proved rational bounds and representative monotonicity; checks the high-frequency limit numerically; and verifies the exact rationalization of the relativistic threshold gap.

The infinite identities, monotonicity and bounds are proved analytically in `RESULT.md`; the numerical replay is not an exhaustive proof. The result inherits the weak-bending hypotheses and remainder term of the cited source.
