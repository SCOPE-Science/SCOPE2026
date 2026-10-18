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

# Reproducibility and limits

The two included Python files `verify_orbits.py` and `verify_direct.py` were executed and returned the same counts. The orbit program constructs the whole group of order 120 and all 17 section orbits, then applies exact four-chart Jacobian Gröbner tests to each representative. The direct program performs a separate exact lexicographic Gröbner test on all 511 sections, with an independently coded monomial ordering. Both give 240 smooth curves and point-count histogram 1:60, 2:90, 3:60, 4:30. `EXPECTED.json` records the integer results and orbit representatives. No randomized search, finite-extension sampling as a substitute for algebraic-closure smoothness, or unproved infinite extrapolation is used.

The 15 anti-canonical sections vanishing at every rational point have an additional purely geometric classification as two-secant plane sections; they are all singular. This also rules out smooth curves with five rational points. See `RESULT.md` for the argument, and `REPRODUCE.txt` for exact commands and dependencies.

These are computational and mathematical checks on the stated finite F2 scheme. External independent audit or validation has not been performed.
