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

# Reproducible verification and exact proof limits

Run `python verify_ellipsoids.py` using Python 3 and SymPy. The executable checks symbolic polynomial identities behind the scalar determinant stationarity and contact second-moment formula, five positive pairs of input disk radii, and 40000 independently sampled inclusion tests. It reports **40030 checks passed**.

The complete proof does not rely on numerical extrapolation. The two disks have explicit support function and exact slice integral. Coordinate support bounds and Hadamard prove the John maximizer. For the unique positive determinant-stationary parameter, a probability distribution supported on two finite levels of explicit boundary contact points has zero mean and covariance one-third of the outer-ellipsoid shape matrix. Integrating the quadratic containment inequality against those contacts and applying AM–GM proves minimum volume among **all translated, arbitrarily oriented ellipsoids** and uniqueness. The volume-ratio inequalities follow from the sign of an explicit one-variable derivative and the two extreme-radius limits.

**Unproved limits:** No results are claimed for oblique, translated or nonfilled input disks, for three or more disks, or for higher dimensions. Finite tests do not establish global inequalities and are not an independent audit. No independent validation or historical priority certification has been performed.
