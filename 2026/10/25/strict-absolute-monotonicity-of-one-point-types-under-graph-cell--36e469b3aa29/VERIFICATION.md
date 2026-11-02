---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The random-poset Fraïssé extension identifies each nonalgebraic one-type with a compatible ideal L and filter U of the finite parameter poset. For graph incidence P_H, downsets are formed by choosing vertex subset A and any subset of edge points wholly supported by A, giving Z_H=Σ_A 2^{e_H(A)}. Nonempty L,U require L to be one lower vertex with a nonempty incident-edge upper subset, or exactly the two endpoints of a unique edge with U that edge, yielding Σ_v(2^{deg v}-1)+|E|. The single-empty-side cases total 2Z_H-1. For each missing-edge family F, Δ_F 2^{e_{H∪S}(A)}=2^{e_H(A)}∏_{f∈F}(2^{1_{f⊂A}}−1), equal to 2^{e_H(A)} iff V(F)⊂A and zero otherwise. The vertex-degree contribution is nonzero exactly for v common to every new edge and the linear |E| term contributes precisely at |F|=1. This proves the exact Δ_F formula and strict positivity from A=V for every order, including n=0 boundaries when no F exists. Möbius inversion at E=∅ gives the claimed all-positive coefficients. Crown ideals are antichains of a 2m-cycle, counted by known Lucas L_{2m}. Inspected actual verification script; separate ternary-extension enumeration reproduced all 76 labeled graph cases n≤4 and a second-order difference of 10 for a disjoint-edge test; these tests are not the all-size proof.

## originality

PASS

Published finite-parameter random-poset type-count work gives the classical ideal/filter bijection and a #P-completeness reduction, so the pointwise count is prior/derivable; the crown Lucas ideal count is also prior. The inspected full published Resultary result has no all-orders edge-cell addition positivity relation. The new discrete derivatives compare 2^{|F|} different named parameter sets, rather than adding a comparability between existing elements. The explicitly positive Möbius coefficients for every nonempty F and arbitrary existing E survive the comparison. Derivability as an unstated immediate corollary from older partition-function formulas is a residual priority risk.

## value

PASS

The family of naturally marked graph incidence posets offers a structural quantification of how adding new edge parameters changes available complete types. The theorem gives simultaneous strictly positive mixed derivatives in every order with exact coefficients, a nontrivial global qualitative property not captured by one count or a crown formula; it is mathematically motivated by the insertion operation and useful for order-theoretic type-growth comparisons. No complexity improvement or novel Lucas identity is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
