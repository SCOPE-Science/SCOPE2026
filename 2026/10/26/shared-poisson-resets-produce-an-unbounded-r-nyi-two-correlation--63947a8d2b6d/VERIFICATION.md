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

# Computational and analytic verification

The theorem's infinite-lattice state, strict inequality and weak-reset asymptotics follow from the detailed analytic argument in `RESULT.md`: exponential-age stationarity, exact Bessel overlaps, a double-age convolution, strict Jensen, complete elliptic integrals and dominated convergence for the integrable fourth power of a Bessel function.

Run `python3 verify_coherent_reset.py` using NumPy and SciPy. The checker evaluates a truncated Bessel position basis with an independent quadrature in the reset ages, explicitly forms a stationary one-particle density matrix, derives the shared two-particle purity from Gram products, compares both with renewal single-integral formulas, and verifies the elliptic representation and small-rate scaling numerically. Finite summations, quadratures and sample rates are consistency evidence, not an exhaustive certificate for all rates or the infinite lattice. The stationary separability statement follows directly from the convex-product decomposition, not from any numerical negativity test.

Independent audit: not performed.
