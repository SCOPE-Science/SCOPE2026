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
The proof was reconstructed from the coordinate-ideal description of a direct product of fields and the definition of the annihilating-ideal graph.

Exact symbolic checks:
- vertices are the \(2^n-2\) nonempty proper coordinate supports;
- adjacency is exactly disjointness;
- intersecting pairs with nonfull union have distance exactly \(2\);
- intersecting pairs with full union have no common neighbor but have the explicit length-three path through the two complements;
- the distance-one count is an inclusion-exclusion count on three coordinate states;
- the distance-three count is the number of surjections onto three labeled coordinate states, divided by two;
- the remaining unordered pairs give the distance-two coefficient;
- differentiating the displayed Hosoya polynomial at \(1\) gives \(4^n-11\cdot2^{n-1}+7\).

`artifacts/verify.py` independently builds the graph and runs breadth-first search for every \(2\le n\le8\), checking every distance coefficient and the Wiener formula. The replay returns `VERIFY_OK`.

Finite computation is not used to justify the universal statement.
