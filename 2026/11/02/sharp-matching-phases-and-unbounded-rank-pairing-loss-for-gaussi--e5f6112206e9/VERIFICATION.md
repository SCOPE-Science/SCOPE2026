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

# Reproducibility

Run `python3 verify.py` in a directory containing the supplied file. It needs only the Python standard library. Expected output begins `VERIFICATION_OK checks= 2492` and also reports the curvature threshold ratio and a descending rank-to-best gain-ratio sequence.

The checker compares analytic and centered-difference second derivatives at four Gaussian scales, tests the curvature signs on both sides of the exact threshold, exhaustively checks all bijections for particle counts two through five in the strict near/separated regimes, and checks several two-pair examples. The strict analytical statements for arbitrary particle count and vanishing approximation ratio are established by the proof in `RESULT.md`, not by these finite checks.

Review status is self-review only; independent audit and external validation have not been performed. No finite-precision numerical output is claimed to certify a universal inequality or a zero asymptotic limit.
