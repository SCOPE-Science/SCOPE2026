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

# Reproducibility of the sharp quadratic Walsh bounds

Run `python3 verify.py` using Python 3.9 or later and no third-party packages. The program enumerates all sign configurations for \(n=6,7,8\) with exact integer arithmetic, checks the quartic Walsh moment against four-cycle enumeration, re-evaluates the rational sum-of-squares certificate, verifies the vertex-row-zero decomposition, tests its quadratic stability consequence, and exercises the Kneser eigenvalue identity for star-shaped edge arrays. The script prints `VERIFY_OK` only after every assertion has passed.

The universal claim for all \(n\ge6\) and all real coefficient arrays rests on the explicit proof of the fourth-moment expansion and the three-subspace disjointness-graph eigenspectrum in `RESULT.md`. Finite enumerations, randomized test arrays, and an exit code cannot establish that universal claim alone. The exact identification of all equality cases and the ellipsoid symmetrization argument are proved in `RESULT.md` and are not represented as exhaustively checked in a finite-dimensional computer experiment.
