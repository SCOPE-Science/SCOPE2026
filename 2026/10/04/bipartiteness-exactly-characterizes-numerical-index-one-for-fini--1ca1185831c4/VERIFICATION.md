---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

The exact claim is for real Lipschitz-free spaces F(V,d_G) of every finite connected simple unit-edge shortest-path graph with |V|>=2; it is the threshold n(X)=1 iff G is bipartite, not an exact value for nonbipartite graphs. The dual Lip_0 unit ball is the edge-difference polytope |f(u)-f(v)|<=1. Its vertices are exactly the potentials whose graph of saturated/tight edges spans connectedly: averaging at a tight edge forces equal endpoints, and on a disconnected tight component not containing the root a sufficiently small signed constant shift preserves every crossing nontight edge due to finite positive slack. In the primal ball the extreme unit molecules are exactly graph-edge molecules, because only a unit graph edge has trivial metric segment, whereas nonedges have an interior shortest-path point. For a bipartite G, every tight-edge path joining adjacent endpoints has odd length, hence signed unit steps sum to odd integer; the original edge constraint reduces it to +/-1. McGregor's finite-dimensional modulus-one extreme-pairing criterion yields n=1. Conversely tree-depth parity defines an extreme dual vertex (all tree edges tight) with zero slope on some same-parity edge for every nonbipartite G; McGregor excludes n=1. The graph checker was inspected and its integer-potential enumeration is corroborative only; the symbolic argument covers arbitrary finite orders.

## originality

PASS

Best-of-knowledge PASS for an all-finite-unweighted-graphs bipartiteness threshold. The already published same-work Resultary entry is not independent prior art; related later quantitative graph results concern distinct statements.

## value

PASS

A finite-graph structural invariant theorem rather than a textbook plug-in: bipartiteness exactly decides the maximal numerical-index threshold for every order. The tight-edge connectivity lemma ties combinatorial paths to extreme dual polytope geometry and produces a reusable certificate; the parity counterpotential supplies a sharp obstruction on odd cycles. It extends the known three-vertex dichotomy to arbitrary finite graph metrics without claiming exact nonbipartite indices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
