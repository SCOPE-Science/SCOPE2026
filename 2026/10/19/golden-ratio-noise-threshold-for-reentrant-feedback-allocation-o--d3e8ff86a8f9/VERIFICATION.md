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

# Reproducible verification and limits

Run `python verify.py` using Python 3 with NumPy, SciPy and SymPy. The included program reported **3,371 passed assertions** when executed from the actual file path. It verifies the exact symbolic boundary-derivative identities, strict-support inequality algebra, golden-ratio maximum, three-vertex example factorization, and many numerical full-matrix traces and independently asymmetric admissible allocations. The budget and inverse matrix are reconstructed for each numerical example. Numerical optimization is carried out only to cross-check finite samples.

The proof of unconditional uniqueness comes from the strictly positive second derivative of the weighted inverse trace, not from observing optimizer agreement in finite experiments. The existence of two positive switching budgets and the unique cusp point comes from monotonicity of the explicit rational envelope; no numerical root search is needed to establish it. Source comparisons support only a best-knowledge originality assessment, and no independent audit has been performed.
