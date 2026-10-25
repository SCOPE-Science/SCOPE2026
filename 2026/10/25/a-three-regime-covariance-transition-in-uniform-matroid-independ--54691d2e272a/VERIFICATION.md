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
# Verification notes

Run `python check_covariance.py` with Python 3 (standard library). It computes exact rational uniform-cube, simplex, and rank-capped cube volumes/moments for all 44 integer pairs with \(2\le n\le9\), \(1\le k\le n\). It checks positive covariance eigenvalues and independent fixed-seed rejection Monte Carlo moments for \((n,k)=(6,2),(7,3),(8,4)\), at the disclosed absolute tolerance \(0.008\). The checker samples from the ambient unit cube conditional on the rank cap, matching Euclidean uniform volume; it makes no infinite-dimensional certification claim.

The proof of balanced transverse rigidity is exact by reflection \(U_i\mapsto1-U_i\); the scalar central-window limit uses the ordinary CLT and bounded fourth moments. The subcritical asymptotic and exponential cap deficit rely on a uniform Fourier local-limit bound for the compact exponential-tilt family. That analytic premise and the novelty comparison still require independent expert verification. Simulations are supportive only, not a substitute for the infinite proof.
