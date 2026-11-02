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

# Computational verification

Run `python3 verify_wheel_minimal_forts.py` using only the Python 3 standard library. The script constructs each wheel from the definition, enumerates every nonempty vertex subset for the tested rim orders, checks the defining outside-neighbor condition directly, and checks inclusion-minimality against all smaller forts. It independently counts allowed cyclic gap words and maximal independent sets, and expands both rational generating functions by exact integer formal-series inversion.

Observed execution: `VERIFY_OK: 131028 subsets checked across 12 wheels, published sequence of 13 terms matched; rational generating functions checked through rim order 40`.

The exhaustive graph-level comparison covers rim lengths \(4\) through \(15\), with the rim-length-three boundary separately checked in the rational series and directly in the mathematical proof. Higher-order coefficient checking is a finite algebraic consistency check only; the general statement follows from the cycle-gap bijections and formal transfer-matrix identity in `RESULT.md`. Independent mathematical audit has not been performed.
