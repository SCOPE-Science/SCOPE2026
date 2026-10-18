---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

For simplicial d-polytopes, the sharp stacked-polytope Lower Bound Theorem gives f0≤Λ(d,k,M) for each 0≤k≤d−1, including endpoints. HSW Thm3.7 applies at k=0 to actual v=f0(P), and x↦min{1,a x^(−2/(d−1))} is nonincreasing, so replacing v by Λ gives the inscribed q≠0 and q=0 inequalities. For simple circumscribed Q, polar Q° is simplicial and f_k(Q)=f_{d−1−k}(Q°); hence f_{d−1}(Q)≤Λ(d,d−1−k,M), allowing HSW Thm3.8 facet estimates. All q, d=2 endpoints, vacuous low M are handled. Finite d≤40 algebra tests are supplementary to the classical LBT.

## originality

PASS

Best-of-knowledge original restricted-class synthesis: HSW arXiv:2608.02554 gives endpoint dual-volume bounds and arbitrary-polytope half-vector bounds, not the explicit all-k simplicial/simple statement. The classical LBT is an ingredient, not itself a dual-volume theorem. This combination yields a natural additional result, with explicit limitation that it does not solve the general open problem.

## value

PASS

The source explicitly asks about the missing all-k nonasymptotic dual-volume range, and simplicial inscribed/simple circumscribed approximants form natural combinatorially controlled classes. The LBT inverse supplies a dimension- and face-count-sensitive explicit bound in precisely those missing ranges. It is a targeted natural subclass theorem, not an arbitrary parameter restriction or unexplained tiny improvement; no full all-polytope solution is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
