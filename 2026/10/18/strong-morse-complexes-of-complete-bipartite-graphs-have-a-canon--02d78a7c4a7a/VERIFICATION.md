---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Theorem reconstructed for m,n>=2 on the one-dimensional simplicial graph: strong matchings are the downward closure of gradients of strict vertex orders, with exactly one earlier neighbor at a matched vertex. For every b in B, U_b is built from the full incoming simplex E_b and m outgoing-wing simplices; analogously V_a. Every order belongs to this cover and every generator arises from an explicit order. The wing vertices collapse one-by-one, so each U_b,V_a is contractible. Different same-side stars are disjoint, U_b intersect V_a in exactly the two isolated opposite incidence vertices (no simplex can match one edge twice), and triple intersections have empty realization. The graph-of-spaces homotopy pushout thus yields the doubled-edge K_mn graph with m+n vertices and 2mn edges: a wedge of 2mn-m-n+1 circles, free fundamental group and integral H1 of that rank. Naturality under graph automorphisms identifies H1 with ker(arc-incidence boundary); splitting into backtracks Z[A x B] and zero-row/column matrices aug(A) tensor aug(B) is integral for S_m x S_n. From the equivariant exact graph-chain sequence the character is 2f_A f_B-f_A-f_B+1 and part-exchange trace is 1. Direct independent all-order enumeration agrees with exact cover and reduced H1 ranks for K_2,2 (rank5), K_2,3 (rank8), K_3,3 (rank13); it is only finite corroboration, not the proof.

## originality

PASS

Full strong-Morse complex of complete bipartite graphs is not the ordinary acyclic matching complex. The foundation Knudson--Owens-White introduces full SM and proves star K_1,n contractible but does not state the K_m,n classification with both m,n>=2 or integral equivariant double-arc module. Ordinary bipartite Morse complex and two-matching complex results in Resultary use different face predicates. Best-of-knowledge original for m,n>=3 plus exact natural cycle lattice; unindexed and thin-family overlap remains possible.

## value

PASS

Complete natural two-parameter family of full strong-matching complexes, unexpectedly one-dimensional homotopy despite high-dimensional simplices. The integral cycle-lattice and full automorphism character distinguish genuinely natural structure beyond the scalar Betti rank; the new global gluing is not a routine star deduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
