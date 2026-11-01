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

# Verification of the directed-linear-forest wheel classification

The Python 3 program `verify.py` is self-contained and reconstructs the graph, rather than loading a face list or a stale computation. Run:
```
python verify.py
```
It exhausts all \(65,536\) directed-arc masks, checking the indegree, outdegree, and no-directed-cycle conditions. It verifies \(261\) faces, of which 260 are nonempty. It then replays the fixed toggle order, checks \(116\) matching pairs and \(28\) critical cells (one of dimension zero, 19 of dimension two, eight of dimension three), checks every arrow in the reversed Hasse graph by topological sorting, and calculates all eight signed integral Morse boundary columns. Each such column vanishes **as an integer vector**, not merely mod two. The direct full simplicial \(\mathbb F_2\) boundary ranks are \(15\), \(61\), and \(40\), providing a separate finite consistency check.

These computer checks are exhaustive for the specified graph and use no third-party mathematical software. Discrete Morse theory and the Hurewicz isomorphism in dimension two are the conceptual steps translating the certified CW differential to the claimed wedge homotopy type. The certificate is not a theorem about larger wheels and is not an independent audit.
