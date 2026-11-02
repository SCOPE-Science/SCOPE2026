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

# Reproduction and scope

The proof is given in RESULT.md. The accompanying `verify.py` provides independent symbolic integration of the four terms in the exact mean, exact symbolic integration of the balanced mean, and reproducible randomized checks of the flow parametrization and entropy-production identity. Run with `python verify.py` after installing SymPy 1.12 or newer. It completed 5,007 assertions during preparation.

The exponential-integrability boundaries are proven analytically through a beta-simplex majorant and a compact interior lower bound; neither numerical truncation nor a finite sample is treated as an infinite-tail certificate. The upper-tail exponent is also an analytic consequence of matching Chernoff and interior-patch bounds, not a fitted slope. The available script does not perform an independent mathematical or literature-priority review.
