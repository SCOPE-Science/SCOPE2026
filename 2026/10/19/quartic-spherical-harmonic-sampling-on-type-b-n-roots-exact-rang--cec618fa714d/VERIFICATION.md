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

The exact symbolic proof establishes the sample-image relations, their independence, the harmonic interpolation formula, all eigenvalue branches and multiplicities, and the sharp minimizer of the positive Gram condition-number ratio for every integer dimension at least three.

The companion `check_bn4.py` script recomputes the symbolic two-by-two determinant identities, positive eigenvalue formulas and derivative factorizations. It builds the kernel from all squared inner products using exact rational arithmetic in dimensions 3–13, compares exact first and second Gram spectral moments, and numerically checks the entire spectrum. Additional exact-rational reconstruction checks cover dimensions 3–15. Finite tests do not replace the all-dimensional algebraic argument.

The source comparison includes full text of the relevant 2002 invariant-harmonics work and 2013 spherical-harmonics treatment. A located 1977 foundational spherical-design paper was not accessible in full, leaving an unresolved but nondecisive older-literature equivalence risk. No independent audit or formal external certification has been performed.
