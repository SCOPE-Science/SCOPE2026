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

# Reproduction and check boundaries

Run `python3 verify.py` in a directory containing `certificate.json`; its standard-library-only graph traversal enumerates all \(64\) orientations of \(K_{2,3}\), tests acyclicity, computes VC and Littlestone dimensions, and replays all \(32\) paths of the explicit depth-five shattered decision tree. The reference orientation, query and leaf indexing are described in `RESULT.md` and `certificate.json`.

Run `g++ -std=c++17 -O2 independent.cpp -o check && ./check` to obtain a second certificate check implemented from the forbidden directed-four-cycle characterization. `verify_output.txt` and `cpp_output.txt` contain the actual successful replay outputs. The C++ program does not share version-space recursion with the Python program. The \(46<64\) cardinality bound proves that there can be no depth-six tree.

The global forest shattering criterion, additivity over disjoint query domains and bridge-connected construction are supplied as proofs in `RESULT.md`; these do not rely on finite enumeration. The code checks the finite six-edge base certificate only, not every member of the infinite construction. No independent mathematical audit or formal machine verification has occurred.
