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

# Reproducibility and verification

From the directory containing this file, run `python3 verify.py` with the Python 3 standard library. The complete exact output is embedded in `verification_output.txt` and ends with `VERIFY_OK`.

The program: (i) uniquely enumerates 350 restricted-growth representations of unlabelled four-block partitions on seven points; (ii) confirms the independent profile census 35+210+105; (iii) computes all 350 adjacency masks based on common within-block unordered pairs; (iv) proves absence of cliques of cardinality at least 66 using a full branch search with a proper-greedy-colouring upper bound; (v) enumerates all size-65 cliques and compares them to the 21 independently generated prescribed-pair stars.

A separately implemented C++ clique search is provided as `maxclique.cpp`. Compile with `g++ -O2 -std=c++17 maxclique.cpp -o maxclique` and execute `./maxclique 7 3`; its exact saved output begins `MAX_CLIQUE 65 nodes 86` and the diagnostic output reports 350 vertices. The independent implementation is a useful cross-check of the bound, while the Python verifier additionally exhausts all equality cases.

The two exact recursion-node counts are 396 (target 66) and 1827 (target 65). The exhaustive proof applies to this finite graph. A failure, unexpected runtime interruption or a partial enumeration would not establish the theorem. The mathematical pruning bound and its connection to partitions are explained in `RESULT.md`; do not treat a log alone as a proof. No general theorem beyond the specified parameters has been checked. Independent audit has not been performed.
