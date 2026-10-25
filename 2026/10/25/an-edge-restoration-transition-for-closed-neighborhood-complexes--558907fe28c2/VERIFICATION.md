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

# Reproduction and boundaries
Run `python3 verify.py` with the standard Python library. The accompanying `verification_output.txt` was produced by execution of exactly the included checker source.

It reconstructs all closed-neighborhood faces and both hemispheres, compares the exact intersection with the graph, replays valid elementary free-face removals in each hemisphere, computes complete reduced mod-two homology and tests the two-homology inclusion ranks for the first five- and four-index crown sequences. The execution inspected 26 full crown-filtration cases with sizes four through seven, 64 seeded random opposite-universal bipartite graphs, 19,036 nonempty crown faces, 8,352 hemisphere elementary-collapse pairs, and nine inclusion-rank calculations. Every check completed successfully.

The attached finite computations are exhaustive for their specified finite examples, not for the infinite graph families. The integral theorem and naturality rest on the written hemisphere collapse, homotopy-pushout, graph cycle-space, and Mayer–Vietoris arguments. A comparison against prior literature and mathematical records was undertaken; bibliographic priority is not mechanically certified. No independent audit or validation is claimed.
