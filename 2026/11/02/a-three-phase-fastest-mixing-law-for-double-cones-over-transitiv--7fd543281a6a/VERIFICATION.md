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

# Numerical and symbolic reproducibility

The self-contained proof in `RESULT.md` establishes the theorem without reliance on finite computation. The auxiliary `verify.py` program (Python 3 with NumPy, SciPy and SymPy installed) independently reconstructs the graph transition matrices. Run:

```sh
python -m pip install -r requirements.txt
python verify.py
```

On the supplied source, it completed 43 exact-eigenmode versus full-matrix spectral comparisons, 43 separate linear-programming minimizations of the original four endpoint eigenvalue inequalities with stochasticity, 560 unrestricted asymmetric feasible design comparisons, three SymPy rational characteristic-spectrum checks, and six instances where the holding-probability bound clips the base-edge Chebyshev optimum. Numerical comparisons use floating-point tolerances displayed in the script; they are not exact mathematical certificates for infinite families.

The symbolic checks use explicit small cycle matrices with rational edge probabilities. The all-graph proof relies on convex graph-automorphism averaging, orthogonal invariant eigenspaces, the endpoint property of an affine spectral function and the exact piecewise affine minimax. The previous cyclic results at sizes three and four and the single-wheel formula are acknowledged as earlier literature; the general two-nonadjacent-apex trichotomy and larger-cycle consequences are the subject of this verification.

Self-review: passed. Independent audit: not yet performed.
