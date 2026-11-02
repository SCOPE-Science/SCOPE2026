---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For m≥3, the graph has 2m+2 vertices, 3m edges, degree-m poles and degree-2 internal vertices; distances: d(p,q)=3; d(a_i,a_j)=d(b_i,b_j)=2 for i≠j, d(a_i,b_i)=1, d(a_i,b_j)=3 for i≠j, every pole to every internal vertex ≤2. Thus at scale 1 the Rips complex is the original connected triangle-free graph with cycle rank m−1. At scale 2 it is exactly S^0*L_m where L_m comprises two full disjoint simplices (on the a and b layers) plus m matched bridges; quotient of two contractible disjoint subcomplexes yields the m-edge banana graph, L_m≃∨^(m−1)S^1, suspension gives ∨^(m−1)S^2 and torsionfree integral homology. Diameter 3 gives a simplex at scale≥3 and no intermediate changes; reduced bars are (2m+1)×[0,1) in H0, (m−1)×[1,2) in H1, (m−1)×[2,3) in H2. Integral H1 of oriented pole-to-pole arms is the augmentation lattice with pole swap −1. H1(L_m) is augmentation on oriented a-to-b bridges with flip −1; H~0(S0) flip −1; the join tensor yields pole flip +1 on H2 and natural coordinate permutation S_m. For m≥3 the two poles alone have valence m≥3, identifying the entire Aut group as S_m×C2. A separate independent BFS/face enumeration and mod-2 reduction for m=3..6 plus 144 signed Lefschetz cases agreed after applying the correct (−1)^k homological Lefschetz convention. Finite checks corroborate, not prove, the uniform statements.

## originality

PASS

Best-of-knowledge originality for the exact infinite family with complete integral persistence AND full S_m×C_2 integral homology actions. Actual full-text comparisons rule out plausible stronger graph-power, glued-graph, hexagon-packing, Platonic-solid and configuration-space results by explicit hypotheses or different constructions. The exact database hit is the assigned result itself, not independent evidence. Residual unindexed or implicit equivalent descriptions remain.

## value

PASS

Natural, nontrivial complete integral Rips persistence invariant for an unbounded canonical theta-graph family at precisely the girth-six boundary outside general girth≥7 stabilization; its binomial(m,2) six-cycles share entire three-edge arms so disjoint-cycle methods fail. Exact all-scale wedge types, field-independent torsionfree barcodes and complete integral S_m×C2 actions give a useful structural test example. Especially the pole flip changes from −1 on degree-one cycles to +1 on degree-two spheres although Betti ranks match, a distinction not encoded in previously published nonequivariant sphere enumerations. This claim does not claim a general classification for all girth-six graphs or unequal path lengths.

The dated certificate retains the supplied scientific assessment, sources and limitations.
