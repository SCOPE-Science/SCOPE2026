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

`verify.py` performs two independent finite checks of the analytic theorem.

First, it enumerates every binary error-indicator pattern for each \(1\le b\le n\le9\). For each of four rational substitution probabilities, it reconstructs the cyclic \(b\)-symbol corruption count directly from the indicator pattern, computes the exact probability-weighted first and second moments using rational arithmetic, and compares them with the formulas in the finding. The symbol values themselves are irrelevant once an error is required to change the symbol.

Second, it evaluates the general cyclic-overlap variance and the simplified \(n\ge2b\) expression on a larger integer grid with exact rational arithmetic. This checks the algebraic reduction independently of floating-point evaluation.

These finite checks corroborate, but do not replace, the all-parameter proof. The proof's only probabilistic premise is independence of coordinate-error indicators with common probability \(p\).
