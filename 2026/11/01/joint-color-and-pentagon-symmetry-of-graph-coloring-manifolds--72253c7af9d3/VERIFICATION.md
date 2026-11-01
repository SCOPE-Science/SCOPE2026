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

The standalone `verify.py` enumerates the finite graph-multimorphism cells for 4, 5, and 6 colors, computes exact signed cellular Lefschetz traces for the identity, source reflection, source rotation, target color transposition, and their mixed action, and checks a maximal top cell fixed orientation-preservingly by the color transposition.

Run `python3 verify.py`. The checked transcript is in `verify_output.txt`, ending in `FINITE_CHECKS_PASS`. This tests the sign formulas but does not prove the infinite family. The all-size proof uses the published 2005 Stiefel theorem, the one-reflection identification, rational Gysin theory, a coordinate-color projection to the simplex boundary, and Poincaré duality. The independent audit has not been performed.
