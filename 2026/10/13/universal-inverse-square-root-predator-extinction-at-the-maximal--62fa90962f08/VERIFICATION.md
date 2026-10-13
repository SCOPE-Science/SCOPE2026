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

Execute `python verifier.py` using SymPy. The code symbolically simplifies the exact nonnegative mortality gap, computes the maximum-response value and curvature, checks the quotient differential identity, and verifies the two exact numerical threshold coefficients. The expected single-line output is `VERIFY_OK`.

The noncomputational proof in `RESULT.md` establishes for **all** strictly positive initial densities: positivity, global boundedness, absence of a nonzero predator limit, prey convergence, convergence of the deficit-to-predator quotient, and reciprocal-square-density growth. The checker only validates the algebraic premises and a concrete parameter witness; no grid, floating-point trajectory or finite run is used to infer a global or infinite-time theorem.

Publicly verified primary paper: Verma et al., arXiv:2606.26340v1, equations (1) and (14)--(27), Theorems 4, 7 and 8. Main rival model: Prakash and Vamsi, arXiv:2504.09078v1, equation (4) with explicit quadratic crowding. The abstract-only 2019 predecessor remains a literature-access limitation. This is a self-review only; independent audit was not performed.
