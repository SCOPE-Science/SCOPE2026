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
# Verification record

The edge-list graph is checked against the standard two-pentagon presentation of the icosahedron. `verify_morse_character.py` enumerates all 323 nonempty valid subsets, forms and checks all 151 matching pairs, constructs all 972 Hasse-cover arrows and checks a complete acyclic topological ordering. These exact finite operations establish the claimed discrete Morse proof. It then exhaustively enumerates all 120 automorphisms by complete adjacency-preserving backtracking and calculates the signed simplicial chain traces, whose values determine the rational symmetry character.

An independent implementation `crosscheck_mod2.py` uses the two-pentagon graph and computes simplicial boundary ranks \((11,55,85)\) over \(\mathbb F_2\), giving reduced Betti ranks \((0,0,0,20)\). These ranks are corroborative and not an integral proof. The stdout files record the actual deterministic executions of both packaged verifiers. The matching certificate is an exhaustive proof for one finite graph, not a theorem about every graph or every higher-independence parameter. No independent audit or external mathematical validation is claimed.
