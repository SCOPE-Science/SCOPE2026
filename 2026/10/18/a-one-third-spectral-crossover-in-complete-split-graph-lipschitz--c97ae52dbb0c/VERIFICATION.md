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

The included `verify_split.py` was executed using Python 3, NumPy, SciPy and SymPy. All six independent polytope cases passed: \((p,q)=(2,1),(3,1),(4,1),(2,2),(2,3),(3,2)\). For each case the script constructs active-edge vertices, triangulates the polytope using a convex hull, integrates the anchored volume and all quadratic monomials over exact rational simplices, and compares the full zero-sum covariance matrix to the closed three-projector formula. It also checked positivity and equilateral boundary identities in 323 rational moment instances.

These finite tests do not establish asymptotic claims. The proof of the density-ratio crossover rests on explicitly stated moment-convergent Laplace limits, while the exact finite-dimensional formulas follow from the disintegration and covariance identities. No independent scientific audit or external certification has been performed.
