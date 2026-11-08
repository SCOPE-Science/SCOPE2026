---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

A circular word with positive counts (a,b,c) induces an Eulerian undirected multigraph with three labeled vertices, loop counts h_ii and symmetric off-diagonal multiplicities x,y,z. Vertex degrees 2a,2b,2c require x,y,z all share one parity; parameterization x=2i+delta,y=2j+delta,z=2k+delta with nonnegative loops yields exactly G=(1+tuv)/[(1-t)(1-u)(1-v)(1-tu)(1-tv)(1-uv)]. At positive compositions only the all-loop case and exactly one positive cross-edge type are disconnected: subtract 1+min(a,b)+min(a,c)+min(b,c). Euler's circuit theorem gives a constructive inverse preserving half-degrees and exact counts. Summing integer triples at a=b=c=m gives m(m²+3m-2)/2. The zero-error capacity is the number of outputs by one representative word per distinct image. Independent exhaustive circular-word histogram enumerations checked every positive composition at lengths 3 through 8 (56 cases) and balanced evaluations for m through 7.

## originality

PASS

Kiah–Puleo–Milenkovic defines directed/order-sensitive DNA sequence profiles, Raviv–Schwartz–Yaakobi analyzes rank permutations of such directed profiles, and Jacquet–Knessl–Szpankowski studies directed Markov types. Collapsing reciprocal edge directions changes the graph type from directed to undirected Eulerian and the feasible image counts; the exact generating function plus connectivity correction is not found in inspected statements.

## value

PASS

The unordered-pair observation channel models orientation-free adjacent-pair counts at controlled ternary composition, a natural information-theoretic invariant. The theorem solves feasibility, exact three-variable output counting, a balanced cubic count, and constructive Eulerian encoding; the directed-profile counts do not directly furnish these.

The dated certificate retains the supplied scientific assessment, sources and limitations.
