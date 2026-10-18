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

# Verification and reproducibility

The attached standalone `verify.py` uses no external dependencies. Run `python verify.py` with Python 3. It directly enumerates perfect matchings of up to ten distinguishable half-edges for specified regular and nonregular degree profiles, reconstructs \(L\) and \(P\) directly from edge multiplicities, and compares the resulting covariance as an exact `fractions.Fraction` to the formula. It also evaluates the rational regular-degree formula for a broad finite range and checks the two strict sign cases, the four-stub boundary exception, and the fixed-degree limiting coefficient.

The code's checks are finite; the assertion count reported by its execution is evidence only for those stated instances. The all-parameter claims rest on the explicit six-stub joint-probability argument and algebraic sign proof in `RESULT.md`. The checker does not establish publication priority or provide independent scientific audit.
