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

# Reproduction and scope of checks

Requires standard Python 3; no third-party Python packages, network access, randomness, downloads or external proof assistants. In a directory containing the two bundled program files, run:

```
python3 verify_franklin.py
python3 verify_franklin_chain.py
```

The first script constructs the Franklin LCF graph, computes its full automorphism group and verifies the complete six-plus-twelve edge-orbit partition. It exhaustively enumerates the five matching complexes (the graph itself; representative edge deletions; representative endpoint-deletion links). It checks explicit, disjoint discrete-Morse pairs and topologically sorts *every* oriented nonempty-face incidence graph, rejecting any directed cycle or incorrect critical-cell profile. For the class-\(B\) edge deletion, it computes the signed integral Morse boundary from the actual paired simplicial faces: \((-1,-1,-1,-1,1,-1,0,-1,0,-1,1)\). A unit degree is required and verified. The success marker is `INTEGRAL_MORSE_VERIFIED`.

The independently coded simplicial-chain script enumerates all graph matchings in its own recursion, and computes boundary ranks using row reduction over characteristics two and three. It checks the complete face vector \((18,117,336,417,186,17)\), degree-three reduced Betti rank twelve for the full complex, *all eighteen* edge-deletion/link mod-two homology profiles, and characteristic-three results for representatives of each orbit. The success marker is `SECOND_CHAIN_VERIFIED`.

The algorithms exhaust all finite faces of the stated twelve-vertex graph; no extrapolation from bounded enumerations to an infinite graph family occurs. The topological conclusion uses acyclic discrete-Morse theory, the integral degree-one cancellation, and the mapping-cone homotopy splitting; field-rank checks alone would be insufficient. A separate external scientific audit and proof-assistant formalization have not been performed.
