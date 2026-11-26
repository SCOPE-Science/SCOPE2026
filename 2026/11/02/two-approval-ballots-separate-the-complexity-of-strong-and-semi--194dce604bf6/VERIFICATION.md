---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

A one-cohesive group sharing c is contained in the cohesive full supporter set N_c, and testing that full group suffices for either axiom (intersection containment for SJR, voterwise representation for SSJR). With at most two approvals, a candidate generating a pair requirement has only voters approving exactly that pair. An incident edge to a different neighbor would produce a forbidden ballot; the generator has degree one. Every edge thus has a leaf endpoint, so components are stars. A center of a multi-edge star hits all its edge requirements and is the only vertex there that could have a singleton requirement. A single edge has at most one endpoint with a singleton requirement, which one can choose if present. Isolated positive-weight vertices are forced representatives. Distinct components have disjoint requirements; covering the k heaviest touched components is an upper bound, and one representative per component attains it with padding if necessary. This counts cohesive candidates, including two with identical intersections, and covers the no-cohesive-candidate case. At arity one, cohesive full supporter sets are pairwise disjoint, so at most k must be chosen. For SSJR, cubic edge ballots give n=3|V|/2 and each candidate has 3 supporters; k≥|V|/2 makes all cohesive, so the requirement is exactly a vertex cover. Below |V|/2 the graph is a NO by edge counting; at or above |V| it is a YES. The fixed K4 images with k=2 or 3 maintain all promises. Membership in NP follows by scanning full groups. The standard cubic hardness hypothesis can also be obtained from degree-at-most-three Vertex Cover: attach a K4 with one subdivided edge at each missing incident edge using the subdivision vertex as port. The gadget needs at least three vertices in a cover whether or not its port is chosen, and admits a size-three cover containing that port. The bridge adds no further cover cost, so adding three to the bound per gadget preserves the decision and makes the graph simple cubic. The supplied exact enumerator was inspected, not executed; it samples the coalition equivalence and does not enumerate empty ballots, which the proof covers.

## originality

PASS

The axioms and normalized objective are prior; the normalization changes no optimizer. Aziz et al.'s Example 7 already has ballots of size at most two, all candidates cohesive, and no SSJR (hence no SJR) committee. Arity-two infeasibility itself is not new. The supported distinction is the deterministic weighted-star optimum over all two-approval profiles and the separation from NP-complete SSJR feasibility, even on the exact-two, cubic, all-cohesive promise. The inspected general score-hardness reduction and interval-domain algorithms do not cover those claims.

## value

PASS

Arity is a natural data restriction, not a special population sample. The star theorem gives an exact optimal score even for infeasible SJR profiles, and the contrast with SSJR clarifies that a weaker voterwise requirement can be harder to decide. The hardness promise rules out large ballots and highly supported candidates as the sources of difficulty. Value is in the optimization/complexity boundary, not in reproducing an already-known infeasible instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
