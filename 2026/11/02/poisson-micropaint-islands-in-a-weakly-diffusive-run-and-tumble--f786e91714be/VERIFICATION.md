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

# Verification evidence and limits

The mathematical claim is established in `RESULT.md` by a finite-dimensional backward-equation identification and an explicit coupling of spatial alternating-exponential color intervals. The singular-limit proof includes almost-sure arrival of all positive levels, exact rates, convergence of island start locations and full diffusivity-scaled widths, boundary truncation, and an independent Feynman–Kac Laplace calculation.

Execute `python3 checker.py` with a Python 3 standard-library interpreter. Its 202 tracked assertions cover generator equations, positivity, agreement with the published one-point color fraction, finite-diffusivity Laplace transforms and their limit; two seeded alternating-renewal simulations draw 25,000 samples each. These are numerical consistency tests, not a proof of weak convergence or a claim of independent verification.

Only fixed positive propulsion speed, flip rate and spatial window with diffusivity tending to zero are covered. The initial orientation is positive, and the color at each spatial level refers to first passage over unlimited physical time. The proof does not cover finite physical observations or interacting paint.
