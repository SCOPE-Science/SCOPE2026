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

# Finite verification

The graph is \(\operatorname{GP}(8,3)\), with vertices and edges defined in `RESULT.md`. `verify_by_matchings.py` independently enumerates disjoint edge sets of cardinalities \(1\) through \(4\), tests dominating endpoint sets, constructs transition graphs and breadth-first distances, and writes `certificate.json` in deterministic JSON form. `verify_by_subsets.cpp` separately enumerates all qualifying vertex masks up to size \(8\), recursively verifies induced perfect matchings, then independently builds and measures all transition graphs.

Both programs produced their embedded outputs exactly. They agree on \(0,0,0,684\) paired-dominating sets at even sizes \(2,4,6,8\), token-jumping edges \(3504\), unrestricted adjacent-pair substitutions \(2016\), and partner-preserving substitutions \(1392\). Both find an edgeless token-sliding graph, identify the \(54\) induced-\(4K_2\) pair-substitution isolates, and reproduce the stated components and distance profiles. Each program uses exhaustive finite checks; no stochastic inference or finite-to-infinite extrapolation is employed.

Re-run the commands in `RESULT.md` after extracting the six documents and supporting files into a single directory. `certificate.json` contains the complete enumerated edge and vertex lists; its byte-level regeneration and the two output replays are inspectable checks. Distances refer to graph metrics within nontrivial connected components, with certificate sentinel \(-1\) indicating isolated configurations. These checks are computational and self-reviewed; independent scientific validation has not been performed.
