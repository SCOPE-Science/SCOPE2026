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

# Reproducible finite checks
Run `python3 verify_finite_chain.py` in this directory with Python 3 standard library. The program constructs transition probabilities from independently enumerated focal voters and distinct panels and compares them with the symbolic closed formulas using exact rational arithmetic. It also checks finite-size Moran domination, the exact one-seed transition ratio and the birth–death product formula, with a numerical convergence illustration. The observed output terminates with `ALL_CHECKS_PASSED` and reports 420 microstate comparisons.

# Analytical verification and limits
The infinite-population result is established in `RESULT.md` by (i) exact transition enumeration; (ii) injection of mixed panels containing exactly one supporter; (iii) optional stopping of a bounded supermartingale; and (iv) a birth–death potential formula, dominated convergence in the supercritical region and a growing denominator at and below criticality. The program is a finite, nonexhaustive corroboration only. The result uses the explicitly stated media-on-mixed-panel rule, focal-first distinct sampling and fixed seed count. Independent audit and validation have not been performed.
