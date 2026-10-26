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

# Reproduction and limits

Execute `python verify.py` after installing the package in `requirements.txt`. The standalone symbolic calculator checks all displayed spectral-projector entry formulas, the strict comparison polynomial, the exact derivative and discriminant identities, and the exact cubic monotonicity certificate. It also independently constructs 36 full rational RK4 matrices on graph products and compares every ordered vertex-pair entry (19,134 entries) to the four-type formulas. Rational boundary signs are sampled for additional regression coverage.

Observed completed run:

`VERIFY_OK 9 symbolic identities, 36 exact full RK4 matrices, 19134 exact vertex-pair entries; all finite endpoint tests`

The theorem for all positive integer graph sizes is **analytical**: the program does not enumerate infinitely many graphs. The strict no-reentry and aspect-ratio inequalities are consequences of the exact sign certificates explicitly proved in `RESULT.md`. No external certification or independent audit has been performed.
