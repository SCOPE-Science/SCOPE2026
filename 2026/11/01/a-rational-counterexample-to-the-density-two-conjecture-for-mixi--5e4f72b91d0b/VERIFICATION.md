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

The attached `CHECK.py` replays the finite portion of the proof with exact rational arithmetic. It verifies the expansion and mixing parameter inequalities, the first seventeen orbit positions and inverse-derivative coefficients, the maximal initial orbit position, the partial density and normalization sums, the geometric bound on all later coefficients, and the strict rational density bound.

The checker is not a proof of the infinite density representation. That identity is Theorem 3.1 of arXiv:2004.01813v1, originally attributed there to Ito–Tanaka–Nakada. The remaining infinite series is bounded analytically using the branch-derivative lower bound, with no extrapolation from finite numerical tests.

An independent scientific audit and comprehensive publication-priority verification have not been performed.
