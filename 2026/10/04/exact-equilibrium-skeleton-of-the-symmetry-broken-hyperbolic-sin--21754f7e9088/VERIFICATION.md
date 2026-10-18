---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS: Set y=z=0, solve F_a(x)=a x-d sinh(x)=0.01 and k=a-d cosh(x); the linearized cubic is lambda^3+0.2 lambda^2+lambda+k, Hurwitz iff 0<k<0.2. The fold function M(q)=q arcosh(q)-sqrt(q^2-1) is strictly increasing for q>1. Independent scalar root brackets reproduce -1.0483518312766908 for Case D fold and a_C=1.2012399862498022 in Case C. The two Case-D outer imaginary-pair thresholds are a_L=-1.116233346441185 and a_R=-1.0769969279698952, and their ordering yields a_R<a<a_SN as the two-sink window. Three roots persist throughout Case C [1.1,1.656]. At the double root at fold a zero eigenvalue is present; 'two distinct equilibria' means one non-simple equilibrium and one simple one. These are equilibrium/linear classifications, not Hopf nonlinear criticality claims.

## originality

PASS

PASS best of knowledge: The paper studies the forced Cases C/D mainly through orbit bifurcation plots; the exact equilibrium skeleton and branchwise Hurwitz thresholds are not in the examined case analysis. A separate symmetric (unforced) compact-recurrence theorem is not equivalent under adding 0.01 forcing.

## value

PASS

PASS: An exact fold and a quantitative two-stable-equilibria interval explain the organizing fixed-point structure of a natural symmetry-broken jerk model used for numerical period-doubling. A complete linear-stability partition over the original study's parameter windows is more than arbitrary parameter sampling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
