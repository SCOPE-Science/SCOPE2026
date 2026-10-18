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

Run `python verify.py` with SymPy (`requirements.txt`). The program symbolically reconstructs both Bernoulli update matrices, their second-moment operator, the determinant identity, and derivative/factorization identities. It performs 240 exact rational path-moment comparisons, enumerating all binary sequences of length up to five at each of 48 parameter triples. It printed `PASS: symbolic determinant, first-moment stability identities, monotonicity and 240 exact path-moment identities` in the present check.

Proof-level check: positivity of the covariance operator guarantees a Perron eigenmatrix; the strictly positive definite one-step covariance from a nonzero scalar initial error detects that eigenmatrix, so the spectral crossing is not merely a formal determinant zero. Monotonicity in selection probability reduces the multidimensional condition to \(p_*\). The factorization at \(p=0\) concerns the limit of positive probabilities, not an actual unselected coordinate.

Boundaries: \(0\le M\le1\), \(0\le\beta<1\), \(0<p_i<1\), \(d\ge2\). No Monte Carlo trial, finite enumeration, or numerical estimate establishes the infinite-time theorem. The equal-probability two-row case is previously indexed, and an inaccessible complete closely related manuscript remains an originality risk.
