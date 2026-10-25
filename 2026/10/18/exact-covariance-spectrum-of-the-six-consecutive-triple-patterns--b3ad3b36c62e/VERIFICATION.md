---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Relative order patterns on disjoint position sets are independent under independent continuous ranks, so only overlaps at lags 0,1,2 contribute. Enumerating all 24 patterns of length four and all 120 of length five defines exact Q1,Q2; their weighted covariance matrix is M_n/360. An independently written symbolic SymPy check reconstructed the Q matrices and FACTORED the full characteristic polynomial identically for symbolic n; the fixed eigenmode v=(0,-1,1,-1,1,0) has eigenvalue 1/8. The peak-minus-valley indicator at each interior position telescopes to A_(n-1)-A_1, two independent fair Bernoullis for n>=4. This mode has variance 1/2, norm squared four. The other four eigenvalues are strictly >1/8 by the displayed radical comparison and have positive linear growth; the radical-plus root is largest. For n=4 two linear eigenvalues tie; the only zero is all-ones. All-size statement follows from fixed overlap enumeration and polynomial algebra, not numerical n<=300 examples.

## originality

PASS

Published multivariate feasible-region cycle-polytope identities explain one approximate conservation structure but not a finite-n covariance diagonalization. The published Crane/DeSalvo/Elizalde weak-dissociation framework determines single-pattern variances (the diagonal of the current matrix), not this exact joint cross-covariance spectrum on accessible evidence. Boundary telescoping alone is elementary and not a novelty claim; eigenbasis, exact eigenvalues, and sharp condition number are the assessed remainder.

## value

PASS

The complete joint finite-sample covariance spectrum of the six natural consecutive triple pattern counts is a nontrivial spectral invariant. It explicitly separates one boundary-fluctuation mode from four bulk-growing modes and quantitatively describes singularity/conditioning; future multivariate asymptotic analyses can use these exact numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
