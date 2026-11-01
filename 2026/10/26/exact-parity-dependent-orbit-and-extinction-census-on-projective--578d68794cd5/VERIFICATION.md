---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For any existing finite projective plane of order q, v=q²+q+1 is odd, and point-line incidence N over F2 satisfies NNᵀ=NᵀN=(q mod 2)I+J and J²=J. Thus F=[[0,N],[Nᵀ,0]] has F⁴=F², and periodic states are exactly im F². Even q gives the 2-dimensional exchange subspace, four periodic states, two fixed and one 2-cycle; rank(F)=2ρ and the square-zero transient factor produce exact entry-time counts 4, 2^(2v-2ρ+2)-4, 2^(2v)-2^(2v-2ρ+2), and size-two zero blocks 2ρ-2. Odd q yields F³=F, recurrent dimension 2v-2, fixed dimension v-1 and precisely 3·2^(2v-2) states entering after one step. The q-even sharpness follows from ρ>1 (distinct nonzero incidence rows); q-odd sharpness from the two-dimensional zero factor. The source explicitly assumes plane existence, not arbitrary q. Independent binary matrix identities for PG(2,2), PG(2,3) and all 16384 states at q=2 reproduce entry counts (4,252,16128). These experiments corroborate, rather than prove, the all-plane assertion.

## originality

PASS

Best-of-knowledge PASS for the dynamical Jordan and exact transient-orbit census of the projective incidence graph, not for the classical symmetric-design incidence equation or known binary p-ranks. Compared to Resultary parity dynamics on hypercubes and complete multipartite graphs, the graph family, invariant rho and orbit formula are materially different. A general theorem on linear CA of symmetric designs could imply this elementary specialization, which remains a priority risk.

## value

PASS

The complete orbit partition and sharp extinction-entry times are mathematically natural dynamical invariants of a canonical finite-geometric incidence graph. The q-parity phase separation and explicit dependence on the binary incidence rank are useful even when the plane is non-Desarguesian; they distinguish states with immediate cyclic behavior from transient synchronization. This is more than a renamed incidence rank statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
