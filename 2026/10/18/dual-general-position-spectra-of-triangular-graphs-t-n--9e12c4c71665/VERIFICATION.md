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

# Definition-level reproducibility

Run `python3 verify_dual_gp.py` from the directory containing the packaged standalone Python file. Python standard library is sufficient. The program independently constructs each graph's vertices and adjacency, runs breadth-first search for all vertex-to-vertex distances, and checks whether any selected graph vertex lies internally on a shortest path whose endpoints are both in the selected set or both in its complement. It then compares this geometric definition with the star/triangle classification.

Complete enumeration is performed for \(n=3,4,5,6\), totaling \(33864\) candidate subsets; the resulting nonzero size distributions are \(\{0:1,1:3,2:3,3:1\}\), \(\{0:1,3:8\}\), \(\{0:1,4:5\}\), and \(\{0:1,5:6\}\). Fixed-seed sampling probes \(5009\) additional masks for \(n=7\) and \(5010\) for \(n=8\). The exact output is included in `verification_output.txt`.

This verifier is not a proof for arbitrary orders: all infinite quantifiers are settled by the case analysis in `RESULT.md`. The listed status reports only self-review; no independent audit or certification was undertaken.
