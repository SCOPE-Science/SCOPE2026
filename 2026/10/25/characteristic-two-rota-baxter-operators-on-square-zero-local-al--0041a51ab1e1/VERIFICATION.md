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

The attached `check_rota_baxter.py` was run directly using Python 3 with no third-party dependencies. It enumerated every linear map of the stated algebra for the pairs of finite-field size and radical dimension (2,1), (2,2), (2,3), (4,1) and (4,2), directly checked the defining weight-zero identity on all pairs of basis elements, and compared exact rank and nilpotency-index distributions against the formulas. This covers 328,464 full linear maps, including 454 valid weight-zero operators. It additionally enumerated conjugacy orbits under the full binary general linear group for radical dimensions 1, 2 and 3.

Observed all-test terminal line: `ALL_SQUARE_ZERO_RB_CHECKS_PASSED 328464`. The code checks the finite-field instances only; the general theorem is proved separately in RESULT.md. No external independent audit has been performed.
