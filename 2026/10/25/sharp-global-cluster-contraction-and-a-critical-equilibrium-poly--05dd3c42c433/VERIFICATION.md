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

The complete mathematical argument is in `RESULT.md`. `CHECKER.py` uses exact fractions and can be executed with `python CHECKER.py` in any standard Python environment. Its direct signed-incidence construction independently computes the normalized hyperflower Laplacian rather than trusting the simplified block formulas. It then checks the cluster diameter inequality and multiple subsequent iterates over a range of center sizes, leaf sizes, leaf counts, rational tent parameters and positive/negative/zero couplings.

The checker reports `Exact rational assertions passed: 15159`. The checks include equality in the uncoupled sharp-rate example, fixed critical balance states (including nonsynchronized ones), and existence of two distinct scalar fixed points above threshold. The first-class proof establishes all parameter and infinite-time claims without extrapolating from these finite checks.

Scientific limits: no claim of convergence between clusters, of chaotic quotient dynamics, of global classification of every critical fixed point outside the lower cube, or of any independent mathematical certification. The critical fixed-set equality near a strictly interior point assumes nonzero coupling. Historical priority cannot be established by finite database search alone.
