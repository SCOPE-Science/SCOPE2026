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

# Verification record

The analytical argument is fully contained in `RESULT.md`. Its central checks are an exact shortest-path distance table, a complete invariant-space decomposition, positive determinant identities for the exponential-distance contrast blocks, an explicit constant-sector quadratic form, a uniqueness argument for the first critical determinant root, strict concavity at the balanced endpoint, and implicit differentiation for the fixed-part asymptotic.

The standalone file `check_incidence.py` rebuilds graph distances from incidence adjacencies and breadth-first search, rather than assuming the theorem's distance formulas. It evaluates all centered powered-distance eigenvalues for twelve small parameter pairs, compares threshold nullities and equality vectors, and checks the inverse-size expansion numerically for fixed part sizes. Executing `python check_incidence.py` in an environment with Python 3, NumPy and SciPy produced `CHECK_OK 86 assertion groups`.

The numerical checks are finite sanity checks; they are not proofs of any universal statement. No code dependency outside the submitted file and NumPy/SciPy is required. The ordinary mathematical derivation establishes the infinite-family result. An independent audit has not been performed.
