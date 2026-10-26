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

Run `python3 verify.py` from this directory. It requires Python 3.9 or later and no third-party packages.

The script recomputes the exact terminal-correlation numerator from products of binomials for path lengths \((2,3,4,9,10)\) and signs \((-1,+1,+1,-1,-1)\). It asserts the stated factorization and the exact 19 integer coefficients of the transformed degree-18 polynomial, then counts the two sign changes. It verifies the strictly alternating correlation signs at the exact rational points \(7/10\), \(3/4\), and \(4/5\).

For an independent small-graph check of path elimination, the script enumerates all spin configurations of two three-path graphs at two rational coupling variables and compares the resulting exact correlations with the path formula. It also checks a finite grid of the variable-length extension; the analytical monotonicity proof in RESULT.md, not the grid, covers all integers \(9\le d<e\).

The Descartes argument proves exactly two simple positive-temperature zeros for the base instance. Rounded root estimates are illustrative only. No independent scientific audit or machine-checked proof in a formal theorem prover has been performed.
