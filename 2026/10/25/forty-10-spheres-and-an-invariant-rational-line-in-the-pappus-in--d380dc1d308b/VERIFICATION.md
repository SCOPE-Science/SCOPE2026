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

# Reproduction of exact mathematical checks

The standalone `pappus_forest_verify.py` is included alongside this document. Run:

```sh
python3 pappus_forest_verify.py
```

No external package, network call, database, downloaded graph, or input file is required. The script constructs the labeled Pappus graph using its LCF description; exhaustively checks all \(262144\) vertex subsets with two independent cycle tests; builds a deterministic vertex-toggle matching; and performs a full directed-Hasse topological sort. It computes signed Morse differentials in degrees \(11\) and \(10\) by finite gradient recursion, tests the chain condition, then carries out \(21\) literal integer unit-pivot eliminations. A separate exhaustive permutation backtrack generates all graph automorphisms using graph distances; the signed fixed-simplex formula computes their complete rational top-homology character.

Expected decisive values are \(204492\) faces including the empty simplex, \(102203\) nonempty Morse pairs, critical cell counts \((1,1,62,21)\) in dimensions \((0,9,10,11)\), \(1704456\) Hasse incidences, matrices of sizes \(1\times62\) and \(62\times21\), and automorphism-character multiplicities \((0:135,1:48,4:32,40:1)\). The program emits a JSON data line and `VERIFY_OK`; compare it with `verification_output.txt`.

Finite enumeration here is exhaustive because the graph has exactly eighteen labeled vertices. No inference from a sample to a larger graph family is made. The homotopy conclusion additionally uses the standard discrete Morse, Hurewicz and homological Whitehead theorems; the verifier is not a formal proof assistant or independent audit. The rational character does not certify an integral representation decomposition.
