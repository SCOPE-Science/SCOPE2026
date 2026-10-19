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

# Reproduction and boundaries

Run `python3 verify.py` with Python 3 and no external packages. The script enumerates all allowable cyclic words of lengths 1 through 13, compares every reflection axis with its independently predicted Fibonacci count (91 exact comparisons), checks 35 terms of the rational reflection generating function and the logarithmic coefficient recurrence, and computes scaled coefficient-to-asymptotic ratios through level 1200.

Observed output: `VERIFY_OK: 91 exact reflection checks; 35 rational generating checks;` with the first six exact coefficients `1, 1, 3, 14/3, 61/6, 163/10`. The computed ratios at indices 100, 200, 400, 800, and 1200 are approximately 1.085965, 1.061442, 1.043762, 1.031098, and 1.025446.

Finite word enumeration does not prove all-period subgroup identities; those follow from the geometric path argument in `RESULT.md`. Finite coefficient calculations do not establish the saddle asymptotic; that follows analytically from the two dominant singularities and contour estimates. An independent mathematical audit has not been performed.
