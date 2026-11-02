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

# Verification evidence and limits

The attached standalone program `verify_cograph_matching.py` uses the actual adjacency matrix of two disjoint cliques joined by a matching and checks every induced four-vertex subgraph for a three-edge induced path. It separately tests whether each eligible vertex subset becomes ineligible after every possible single-vertex addition, validates the two structural classifications, and compares the resulting coefficient distributions to both formulas.

Run `python3 verify_cograph_matching.py` from the directory containing the file. The executed output was:

`VERIFY_OK graph_instances=57 direct_subsets=320832 cograph_and_maximal_structural_checks=PASS both_polynomials=PASS`

The test domain consists of all integer \(3\le a,b\le7\) and \(3\le t\le\min(a,b)\), together with \((a,b,t)=(8,8,8)\) and \((8,7,5)\). This includes nonuniform cliques, incomplete matchings, and fully matched boundaries. Every displayed coefficient was verified against direct graph enumeration on that domain. The proof in `RESULT.md` establishes the universal statement; finite tests cannot do so alone. There are no numerical extrapolation steps in the proof. No external or independent audit has been performed.
