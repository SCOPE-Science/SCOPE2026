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

# Reproducibility and scope

Run `python3 VERIFY.py` using Python 3 with only the standard library. The verifier performs exact arithmetic throughout. It checks an identity of symbolic integer polynomials, enumerates every one of the 64 possible binary exponent-support words and their rotations, checks the strict all-positive-support inequality, verifies both candidate six-words and exact division exponents, and computes exact rational ranks of the two recurrence systems.

The expected successful output is:

`VERIFY_OK: exact symbolic trace, all 63 division supports, two rank-five kernels, both primitive cycles`

The unbounded conclusion additionally uses the written monotonicity proof showing that no surviving exponent can exceed one. A finite search through numerical starting pairs alone is not proof of the classification. No external review or independent certification has been performed.
