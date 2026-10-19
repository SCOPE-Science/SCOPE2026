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

# Finite verification and boundaries

Run `python3 verify.py` in the directory containing the packaged files; Python 3 standard library suffices. The included `verification_output.txt` is the output of a successful execution of this exact source.

The checker constructs the original 16-vertex, 24-edge graph directly from the definitions. It enumerates all perfect matchings recursively and checks that the resulting set of 20 one-factorizations agrees with independent direct edge-color backtracking under a fixed global color normalization. Two distinct adjacency algorithms produce the identical 20-state quotient. The reported explicit bijection to the original graph checks adjacency and nonadjacency on all 120 pairs of states in the 16-state component; the remaining 4-state component is verified to be a 3-leaf star. Expansion to all 120 named colorings and breadth-first searches from all component vertices check the edge counts, degree histograms, radii, diameters, and full ordered-distance distributions.

These checks are exhaustive because a perfect matching is uniquely determined by successive choices for the least unused vertex and an edge-coloring by successive choices of every edge color. The result concerns only the specified finite graph; computations alone imply no infinite case. Source comparisons are self-review and do not constitute an independent scientific audit.
