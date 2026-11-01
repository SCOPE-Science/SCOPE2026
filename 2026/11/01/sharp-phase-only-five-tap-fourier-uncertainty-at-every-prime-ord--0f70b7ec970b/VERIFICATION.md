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
# Verification and limitations

The proof in `RESULT.md` gives the all-prime upper bound using the exact integer Sylvester determinant \(900\), plus a separate constructive proof of a two-zero polynomial for every prime at least seven. The fifth-order boundary is exact because the cyclotomic polynomial has four nontrivial zeros and degree four. The standalone program `artifacts/verify.py` independently computes the integer determinant using a permutation formula and samples constructed polynomials at 22 prime orders, including the full Fourier grids. Run with `python3 artifacts/verify.py` from the extracted package root.

The executable finite tests support, but do not replace, the analytic claims for arbitrarily large primes. The original-result comparison is bounded, not proof of historical uniqueness. Independent mathematical audit and validation have not been performed.
