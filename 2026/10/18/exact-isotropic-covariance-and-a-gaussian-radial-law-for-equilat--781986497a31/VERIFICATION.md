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

# Verification scope

The standalone `verify.py` performs exact rational checks of the chamber-moment identity for every dimension \(n=2,\ldots,23\). For \(n=3,4,5,6\), it reconstructs the convex hull directly and integrates the squared Euclidean radius exactly over cones from the origin to a triangulated boundary; this check does not depend on the theorem's sign-chamber counting identity. Those four calculations also check the exact coordinate volume, with the Euclidean Gram factor treated explicitly. The script performs a seeded, non-exhaustive sampling diagnostic at three larger dimensions.

All these finite computations are corroborative only. The proof for every dimension is the chamber Jacobian and Vandermonde evaluation, while the normal limit follows from the conditional exponential representation, the multivariate central limit theorem, and the delta method. The finite checks do not imply the asymptotic statement and the probability simulations are not statistical certifications. Reproduce with `python verify.py` in an environment providing Python 3, NumPy and SciPy (the exact combinatorial checks themselves use only the Python standard library).

Independent scientific audit has not been performed.
