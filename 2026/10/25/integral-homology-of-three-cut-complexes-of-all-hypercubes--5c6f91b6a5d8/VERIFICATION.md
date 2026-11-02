---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

For d≥3, the ordinary cut complex facets are complements of disconnected induced triples, not independent triples. Its Alexander dual L has all edges, connected induced path triples, and exactly one tetrahedron for each square; no higher simplex. The proof shows any admissible induced four-set must be a K2,2 square and a two-edge path belongs to a unique cube square, excluding five-faces. The connected core C with distance-one/two edges is simply connected because every distance-two diagonal contracts to a cube two-step path and the standard cubical two-skeleton fills all fundamental cycles. Each square tetrahedron has a free private triangular face, so collapses to a simply connected 2-complex, homotopy equivalent to a wedge of a_d two-spheres by Hurewicz–Whitehead. Long edges (distance≥3) are triangle-free and independently add b_d circles. a_d=2^(d-2)(4-2d+binom(d,2))-1, b_d=2^(d-1)(2^d-1-d-binom(d,2)); independent face count and Euler checks for d=3,4,5 yield (1,4),(7,40),(31,256). Integral combinatorial Alexander duality yields Htilde_(2^d-5)=Z^a, Htilde_(2^d-4)=Z^b with no torsion and non-shellability. Inspected finite Smith-form code confirms d=3,4, mod-two d=5, but infinity rests on the structural proof.

## originality

PASS

Qualified best-of-knowledge: searched Resultary by semantic same-object aliases, inspected relevant primary theorem statements, distinguished direct and partial coverage, and found no proven dominating statement of the final claimed exact invariant. Residual risks and incomplete primary sections are explicitly documented.

## value

PASS

This is a uniform, closed-form integral classification and non-shellability certificate for the canonical infinite family of cube graphs, together with a stronger homotopy decomposition of the Alexander dual. It distinguishes ordinary versus total cut complexes and supplies explicit Betti growth not mechanically implied by small cube cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
