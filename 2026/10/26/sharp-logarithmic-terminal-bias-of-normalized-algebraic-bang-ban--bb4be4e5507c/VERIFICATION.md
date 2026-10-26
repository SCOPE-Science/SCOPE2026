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

The theorem is proved by a local inverse-switch coordinate and an exact odd kernel moment. The proof establishes every infinitesimal claim; finite computations are supporting checks only.

`verify.py` (dependency `mpmath>=1.3,<2`) uses 65-digit arithmetic to compare independent quadrature with both exact terminal-coordinate formulas for three interval/switch configurations and four positive parameters; checks the zero-velocity symmetry at centered switches; evaluates the sharp limiting position coefficient at three logarithmically separated parameters; and tests the curvature contribution for two nonzero curvature signs and three parameters. It prints `VERIFY_OK 37` when every stated bound succeeds. The script was executed from the materialized package during the self-review.

No formal proof assistant, external expert audit, global control optimizer, or floating-point exhaustive certificate is asserted. Limitations are a prescribed smooth switch, interior simple zeros, a fixed endpoint, and exact real arithmetic.
