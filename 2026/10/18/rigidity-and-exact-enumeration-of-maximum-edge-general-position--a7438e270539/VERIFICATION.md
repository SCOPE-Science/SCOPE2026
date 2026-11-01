---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Reconstructed exact edge-geodesic definition (no shortest vertex-to-vertex path contains >=3 selected edges). Every full arm is an s-t geodesic; disjoint edge partition gives at most 2 chosen per arm and gp_e<=2m. For any a in [1,floor(L/2)], the positions a and b=L+1-a on every arm are feasible: a two-arm geodesic through s requires x+y<=L, whereas a forbidden triple would force x>=b and y>=a, hence x+y>=L+1; the t route needs x+y>=L, but a triple forces x<=a-1 and y<=b-1, hence <=L-1. One-arm and terminal-endpoint cases cannot contain a triple. At equality 2m, let selected positions be a_i<b_i. For ordered distinct i,j, a forbidden s route exists if b_i+a_j<=L, forcing b_i+a_j>=L+1; a forbidden t route exists if a_i+b_j>=L+2, forcing a_i+b_j<=L+1. These forced endpoints lie inside arms under the respective contradiction assumptions, so no boundary loophole. Swapping ordered indices yields a_i+b_j=L+1 for all i!=j. For m>=3 a third arm forces all a_i equal and all b_i=L+1-a. The inequality a<b gives exactly floor(L/2) distinct labelled maxima. I independently constructed each graph, computed distances with Floyd-Warshall, enumerated geodesics by increasing-distance DFS, formed all forbidden triples and checked maximum candidate subsets: 13 cases (m=3,L=2..7; m=4,L=2..5; m=5,L=2..4), 12 full edge-subset cases and one full two-per-arm candidate space; observed count floor(L/2) in every case. Those finite checks corroborate but do not prove the all-integer theorem; the written inequalities do.

## originality

PASS

Best-of-knowledge original for the full all-m, all-L maximum-set rigidity and labelled-extremizer enumeration. The known edge-geodesic-cover inequality proves only the 2m upper bound. The 2025 theta argument supplies a five-edge witness only within a gp_e=4 exclusion theorem. A published generalized-theta proposition concerns dual VERTEX general position, not edge general position. The 2021 foundational paper computes hypercubes, trees, and grids, and the 2024 extremal work treats block graphs/small values. Two relevant published Resultary calculations were read: spider TREE all-set enumeration (one pole, different geodesic constraint) and complete-multipartite edge-geodesic covers (only L=2 is a theta member). No inspected stronger statement implies all paired levels synchronized for arbitrary m>=3,L>=2; lack of an indexed match is not a novelty proof.

## value

PASS

The invariant edge general position is established and the two-terminal equal-arm theta graph is a canonical cyclic network family with unbounded m and L. The sharp value 2m is not the entire contribution: a generic cover argument does not construct extremizers or decide which of exponentially many two-edges-per-arm patterns are feasible. The all-extremizers rigidity theorem proves global edge-level synchronization, exactly floor(L/2) labelled maxima independent of the number of arms. The m>=3 condition is essential to the structural argument and the m=2 cycle differs, giving a motivated boundary rather than arbitrary parameter slicing. The exact count is a useful nontrivial combinatorial invariant of a natural graph family; no downstream theorem is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
