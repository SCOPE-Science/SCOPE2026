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

Run `python3 verify.py` using Python 3 and its standard library. The script derives reduced Laplacian cofactors directly with `fractions.Fraction` Gaussian elimination and compares them against the Chebyshev spanning-tree identity. It also checks published unweighted Möbius-ladder counts, the exact threshold derivative identity, and representative numerical convergence in both the fixed-price and linearly scaling-price regimes.

Expected successful output:

`VERIFY_OK exact_cofactors=72 unweighted_counts=4 threshold_cases=48 fixed_price_limits=3 critical_price_limits=3`

The 72 cofactor cases include all integers \(2\le n\le7\), \(0\le a\le3\), and \(1\le b\le3\), with exact rational determinants. The sign tests cover \(2\le n\le49\). The asymptotic comparisons are finite floating-point illustrations, not certified error bounds and not substitutes for the proof. Global uniqueness follows from strict log-determinant concavity; the finite-price and asymptotic classification follows from the exact stationary equation. Neither literature completeness nor independence is certified by this verifier.
