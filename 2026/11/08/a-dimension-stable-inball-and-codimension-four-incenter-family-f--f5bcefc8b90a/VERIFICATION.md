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

# Verification of the Catalan matroid inball theorem

The proof uses an exact description by ballot-prefix halfspaces, intrinsic projections of their normals, and a matching radius upper bound/feasible-center construction. Integrality of the ballot polytope follows from the totally unimodular difference-constraints matrix in cumulative-sum variables.

Run `python verify.py` after installing NumPy and SciPy. The script checks the full radius linear program for integers \(3\le n\le34\); checks the explicit sign-block incenter satisfies every inward-shifted inequality; and checks that small-\(n\) feasible binary vertices coincide with the Dyck-path enumeration and Catalan counts for \(3\le n\le8\). It also checks the unique rank-two case algebraically. The verification marker is `CATALAN_INRADIUS_ANALYTIC_LP_VERTEX_CHECKS_PASSED`.

All computation is finite and numerical apart from finite integer enumeration. Numerical linear-programming tolerances are not mathematical proof of the claimed all-dimension theorem, which is supplied in the proof. No computer algebra, external service, or independent audit was used to establish historical priority. The incenter-locus affine dimension is proved analytically; the numerical program does not constitute an exhaustive face computation.
