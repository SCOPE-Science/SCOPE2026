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

# Verification record

The theorem is established by a written analytic argument using period-two Fourier-series Parseval, Poisson summation, a rational-function monodromy contradiction, the Fredholm alternative, and norm continuity. The exact determinant \(ab'-a'b=-2rz(1-r^2)/[(1-rz)(1+rz)(z-r)(z+r)]\) is verified algebraically in the proof. The continuum of fiber parameters and all finite erasure sets is covered analytically.

Run the standalone script with `python3 CHECK.py` from the directory containing the research files. On the reviewed version it printed `CHECK_OK assertions=67`. The checks include exact-fraction determinant identities, finite Fourier-summation comparisons to the derived symbols for several positive widths, fiber positions and angles, and a one-sided comparison confirming decaying energy. These are auxiliary checks only; finite tests do not prove the all-parameter assertion. No numerical best bound and no independent audit are claimed.
