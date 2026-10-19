---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Exact finite verification

The claim is mathematically finite; verification supplies complete enumerations, with no sampling or unresolved search frontier. The graph is \(KG(5,2)\), defined explicitly through disjoint pairs. An undirected Hamiltonian path is represented once modulo reversal; **both** endpoint choices are allowed for each elementary Pósa rotation.

Run `python3 verify_posa.py` and `python3 verify_independent.py` with the supplied `cayley_certificate.json` next to the first script. They use Python's standard library only.

The first checker independently evaluates the subset recurrence for prescribed endpoints, enumerates all \(120\) elements of \(\mathfrak S_5\), applies them to the base path, constructs all four local rotations, determines the exact Cayley generators, performs breadth-first search on the generated group, and checks every path, neighbor, and distance field in all 120 certificate records.

The second checker is algorithmically distinct: it examines candidate vertex permutations, retaining each Hamiltonian path modulo reversal; it constructs actual rotation adjacencies without consulting the group generators or certificate, and runs breadth-first search from all 120 paths. This gives independently 120 vertices, 240 edges, degree four, one connected component, diameter six, and sphere distribution \((1,4,11,25,39,29,11)\) from every vertex.

These exhaustive verifications are mathematical evidence for one finite graph, not a statement about all cubic graphs or infinite parameter families. No independent mathematical audit has been performed.
