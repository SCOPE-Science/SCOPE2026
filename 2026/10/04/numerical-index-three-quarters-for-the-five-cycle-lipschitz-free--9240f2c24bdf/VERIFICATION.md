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

The proof reduces the claim to an exact finite polyhedral calculation. `artifacts/verify.py` reconstructs the ten primal extreme points, thirty dual extreme points, and 120 norming incidence pairs of the unit five-cycle free space. It checks 300 sparse exact-rational LP dual certificates from `artifacts/dual_certificates.json` and then checks the explicit attaining operator.

Run `python3 artifacts/verify.py`. A successful replay prints `VERIFY_OK cases=300 incidence=120 operator_norm=1 numerical_radius=3/4`.

The certificate checks exact Fraction identities: dual-variable signs, all 17 stationarity coordinates, and a dual objective at least \(3/4\) in every active case. It separately verifies operator norm \(1\) and numerical radius \(3/4\). No floating-point computation is needed for replay. The verification establishes only the stated finite-dimensional five-cycle theorem.
