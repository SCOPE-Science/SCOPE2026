---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Scale weights to lambda2=1 and dualize via the geometric maximum-variance unfolding with unit distance constraints. A feasible symmetric m-page simplex embedding has hub distance s<=1 and centered variance V(s)=m+1+s^2-[((m+2)s/2)-1]^2/(m+3). Maximizing this concave quadratic yields s=1 for m=2,3,4 and s=2(m+2)/(m^2-8)<1 for m>=5, giving D_m. Explicit primal conductances x,a,b,c are nonnegative, have total D_m and yield an m-1 dimensional page-standard eigenvalue 1 and one additional axial eigenvalue 1. The quotient characteristic polynomial factors t(t-1) times a quadratic with its remaining eigenvalues strictly larger than 1, by positive shifted product and their sum >2. This matches the dual bound and proves the full optimal gap. For m>=5 the dual hub-spine edge is strictly slack (distance s<1), and complementary slackness forces x=0 in every optimizer, not merely the symmetric candidate. Independent SymPy exact quotient/weight identities and full Laplacian eigenvalues for m=2,3,4,5,6,10,20 corroborate the proof.

## originality

PASS

Qualified best-of-knowledge original contribution: A five-page spine-deletion threshold for fastest diffusion on pendant book graphs. Closest prior work and limits are compared by implication, not title; priority risk retained.

## value

PASS

A uniform budgeted spectral-gap optimization on a natural graph family with redundant hub edge is structurally motivated. The exact all-size rational optimum, constructive optimal weights and mandatory deletion of an apparently useful central edge at precisely five pages form a nontrivial network-design phase transition with a tight spectral/Euclidean dual certificate, not an arbitrary tiny numeric improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
