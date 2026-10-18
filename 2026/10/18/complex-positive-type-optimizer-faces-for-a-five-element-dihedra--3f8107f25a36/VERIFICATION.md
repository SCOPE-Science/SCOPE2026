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

# Reproducibility and mathematical boundaries

Run `python3 checker.py` with Python 3 standard library. The checker was executed successfully from this package before submission. It checked all \(118\) orders \(3\le n\le120\), tested \(120\) endpoints/interior optimizer witnesses at orders divisible by three, and verified nonnegative eigenvalues of every dihedral two-dimensional Fourier block, including the reducible endpoint blocks. It additionally enumerated all two-variable LP vertex intersections independently and compared the resulting maxima against the closed formula.

The proof of the universal theorem is algebraic. Its essential certificates are the explicit full-block eigenvalue inequality, the positive two-contact multipliers, and the factorizations of the nonnegative sample polynomial. The checker cannot independently certify novelty, exact symbolic identities, or the claims for untested group orders. No external independent audit is claimed.
