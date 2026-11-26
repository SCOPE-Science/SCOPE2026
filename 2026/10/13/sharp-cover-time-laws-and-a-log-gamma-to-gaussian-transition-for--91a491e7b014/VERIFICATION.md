---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and scope

The critical-window law is proved analytically in `RESULT.md`: the monotone two-count coupling covers all admissible policies, the two clock laws follow from disjoint independent count transitions, and the exact geometric transform converges on a two-sided neighborhood of zero. In particular, the proof uses bounded real shifts in the gamma ratio, not interpolation from integer values of the limiting steering intensity.

The unchanged companion `verify.py` contains bounded finite-clock checks and numerical transform comparisons at selected critical parameters and arguments. Those checks diagnose parity offsets and transform normalization; they do not certify distributional convergence or independence for every parameter sequence. No check of a fixed-positive or a supercritical limit is needed for this statement.
