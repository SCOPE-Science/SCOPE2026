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

PASS. Reconstructed signed-poset facet clearance from Beck–Hlavacek irredundant minimal-root inequalities and terminal signed box facets. Unit roots give doubled arcs of weight 1; two-coordinate roots weight sqrt(2). In the acyclic antipodal graph, each source-to-sink path of weight W bounds radius by rW <= 2-2r. At r=2/(2+H), longest-path lower potentials satisfy every arc and source/sink bound; averaging with the antipodal transform enforces z(-v)=-z(v), z(0)=0 without losing feasibility. The center formula and forced tangencies then follow by complementary slackness; empty signed poset H=0 gives r=1. Eight-case pinned active-set script inspected, not substituted for the all-poset proof.

## originality

PASS

PASS best of knowledge. Original Beck–Hlavacek facet/Fischer results provide combinatorial hypotheses but neither a Euclidean Chebyshev-radius theorem nor the antisymmetric weighted-longest-path optimization. Ordinary, enriched and marked order-polytope metric formulas differ in their irredundant facet systems and are not direct implications for all signed posets. Residual risk: a general antitone doubled-difference-constraint Chebyshev theorem could imply the statement under another formulation.

## value

PASS

PASS. Signed order polytopes form a natural type-B polytope class; exact metric inradius, canonical incenter, full incenter system and forced tangencies solve natural geometric questions not supplied by their Ehrhart/combinatorial theory. Weighted path algorithm exploits the source’s signed symmetry and handles unit/two-root facet normalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
