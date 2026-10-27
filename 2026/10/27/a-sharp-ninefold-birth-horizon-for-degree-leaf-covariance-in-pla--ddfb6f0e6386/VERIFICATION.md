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

# Reproducibility

Run `python checker.py` with Python 3 and SymPy installed. The executable checks the exact polynomial ratio identities and positivity of every numerator/denominator coefficient after cancellation, the two rational base-case inequalities, and 512 exact marginal and mixed-moment assertions from a joint-distribution dynamic program (including normalization and mean leaves) across nonroot birth labels \(2\le j\le9\). It additionally verifies the strict finite-size sign cutoff with rational arithmetic for every \(2\le j\le99\).

The dynamic program follows the three exhaustive possibilities for the next attachment: to the marked vertex, to another leaf, or to an internal vertex other than the marked one, with exact conditional gap weights. Its state explicitly retains whether the marked vertex is itself a leaf to handle the overlap of attachment indicators.

Exact polynomial certificates in `RESULT.md`, the finite-difference telescoping identity, and Wallis's double-factorial asymptotic establish the entire infinite parameter range. Finite dynamic programming is not claimed to prove all cases. No stochastic-order conclusion is established. Historical priority is not independently certified.
