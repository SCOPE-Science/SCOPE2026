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

# Verification procedure

Run `python3 verify.py` with Python 3.9+ and no third-party packages. The code enumerates all possible incident vertex-edge pairs on the stated graph, rejecting repeated matched cells and directed cycles; independently constructs all Hasse covers and proves that the specified discrete-Morse matching is acyclic using a topological sort. It then enumerates all 48 graph automorphisms and all fixed oriented simplices, computes the reduced Lefschetz character, and verifies both irreducible decomposition formulas class by class. The expected stdout begins `VERIFY_OK`.

The verified finite domain is the entire simplicial complex of the single \(K_{2,4}\) graph; no finite sample is used as evidence for an infinite family. Rational Specht decompositions are inferred by the exact ordinary \(S_4\) character table. This is reproducibility evidence, not independent external auditing.
