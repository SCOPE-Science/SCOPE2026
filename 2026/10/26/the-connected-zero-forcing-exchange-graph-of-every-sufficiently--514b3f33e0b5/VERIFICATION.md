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
# Verification of the connected zero-forcing classification

The theorem is proved symbolically in RESULT.md for all integers \(n\ge6\). The two programs below check independent aspects of its finite instances, and their outputs must not be mistaken for a proof of the unrestricted quantifier.

`python3 bruteforce.py 15` exhaustively generates **all** four-subsets of the \(2n\) labelled vertices for each \(6\le n\le15\), independently checks initial connectedness and synchronous zero-forcing closure, constructs the complete exchange graph, verifies all degrees, and runs BFS to check connectivity. For \(6\le n\le11\), it separately excludes connected forcing seeds of sizes one, two, and three. Expected recorded output: `bruteforce.out`.

`python3 structural.py 35` constructs all four symmetry classes by rotation, reflection and swapping layers; independently checks that the classes have the expected sizes and do not overlap, computes and checks the class-to-class exchange table, and verifies that each representative forces the entire graph for each \(6\le n\le35\). Expected recorded output: `structural.out`.

These tests have been executed successfully. Both scripts use only the Python standard library. The hand-checkable exchange table in RESULT.md establishes the all-size degree rule and connectivity; no unexecuted script or inaccessible certificate is needed to understand the theorem.

**Limits.** A computational timeout would not imply impossibility. Testing finitely many prisms cannot replace the structural classification. An independent audit of the derivation, sources and priority has not been performed.
