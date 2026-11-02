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

Run `python3 verify.py` after installing NumPy. Direct Fraction arithmetic verifies the projected-gradient recurrence and exact 2D termination for a non-diagonal SPD system, and checks nontermination through four explicitly chosen 3D exact steps. A seeded 450-trial Gaussian 2D experiment checks that final error stays at round-off scale; 40,000 seeded isotropic paths compare first and subsequent contraction-factor averages against beta expectations. No finite experiment certifies probability-zero or asymptotic claims; those follow from the proof in RESULT.md. Exact affine invariance is not claimed.
