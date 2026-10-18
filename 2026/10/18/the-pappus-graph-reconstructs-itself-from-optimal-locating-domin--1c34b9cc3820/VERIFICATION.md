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
# Exact verification and reproducibility

Run `python3 check_pappus.py` and `python3 independent_check.py` from the same directory. Python 3 standard library alone is sufficient. The first program constructs the incidence graph from \(y=mx+d\) modulo three and counts all subsets of cardinality at most eight by checking pairwise nonempty open-neighborhood traces. Its independent graph traversal calculates both state graphs and all optimum-to-optimum shortest paths. The second builds an LCF cycle/chord graph (with a verified explicit relabeling to the affine graph), uses actual Python sets rather than integer incidence masks, and separately regenerates eligible codes, moves, components, and distances.

Expected exact results: minimum size \(6\), exactly \(18\) optima, size-seven feasible sets \(540\), size-eight feasible sets \(4869\). Distinct optimum intersections have sizes \(0,1,2,4\) with respective frequencies \(18,54,54,27\). The four-overlap graph has \(18\) vertices and \(27\) edges and is isomorphic to the original graph via the displayed explicit bijection.

Capacity-seven state graph: \(558\) vertices, \(216\) edges, eighteen components each with \(13\) vertices and \(324\) isolated states. Capacity-eight state graph: \(5427\) vertices, \(6156\) edges, one component of \(4419\) vertices containing all minima and \(1008\) isolated states. For all 153 pairs of different minimum codes, the distance at capacity eight equals the symmetric-difference size. The distances \(4,8,10,12\) have frequencies \(27,54,54,18\).

`check_pappus.out` and `independent_check.out` give observed program output. The optional `representative_paths.json` provides a shortest feasible transition path for each intersection-size class; the graph labels are the vertex integers declared by `check_pappus.py`. Each successive subset differs by exactly one vertex, all sizes are at most eight, and the paths have lengths equal to their endpoint symmetric differences. These recorded finite checks, while exact within their enumerated domain, do not prove novelty, a theorem for other graphs, or an independent external audit.
