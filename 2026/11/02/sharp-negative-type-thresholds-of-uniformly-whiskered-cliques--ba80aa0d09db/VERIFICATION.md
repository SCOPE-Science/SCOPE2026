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

# Reproducibility and verification

The exact theorem is proved analytically in `RESULT.md` using the complete orthogonal decomposition of powered-distance matrices, a scalar root comparison, and convexity/concavity inequalities. Run `python check_corona.py` with Python 3 and NumPy. The completed run reported `PASS 1180 independent checks`.

The checker reconstructs shortest paths by breadth-first search, constructs the full powered-distance matrix, projects it to the mean-zero subspace, and computes its real eigenvalues. It compares positive semidefiniteness before and at the asserted threshold, endpoint nullity, negative eigenvalues immediately afterward, and the critical global load. It additionally tests parameter monotonicity and the two asymptotic expansions. Checks are independent numerical cross-checks for finite instances, not a proof of all parameter values; tiny floating-point tolerances are specified in the source.

The exact boundary family \(n=2\), a double-star tree, is included in checks only to test normalization and is excluded from the new classification. The exact comparison with previously published unpowered QEC is separated from the claimed new powered-distance result.

No independent audit has been performed.
