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

# Reproducible finite checks and proof boundary

From the directory containing both Python scripts, execute `python3 verify_skeleton.py` and `python3 verify_hull.py` (Python 3, NumPy and SciPy). The first independently solves a linear-programming support-margin problem for every unordered pair of the \(2M\) oriented graph edges of each of nine small multipartite graphs. It compares the optimizer's strict exposed-edge condition with the exact part-class combinatorial formula, checks all vertex degrees and verifies that the two orientations of every underlying edge form fibers matched exactly once when their part pairs intersect. It checks the tripartite degree equality separately.

The second, logically different finite check uses the convex hull of the explicit root-coordinate vertices, collects every facet inequality simultaneously tight on a given pair, and determines the dimension of their minimal face from the rank of those normals. It exhausts all pairs in five cases: \((1,1,1)\), \((2,1,1)\), \((2,2,1)\), \((3,2,1)\), and \((2,2,2)\).

The first script passed cases \((1,1,1)\), \((2,1,1)\), \((3,1,1)\), \((2,2,1)\), \((2,2,2)\), \((3,2,1)\), \((2,1,1,1)\), \((3,1,1,1)\) and \((1,1,1,1)\). The second passed all five cases listed above, including edge counts \(6,20,56,110,132\) respectively. These tests do not numerically certify any untested parameter: the exact supporting-potential proof and inclusion-exclusion identities establish the stated universal quantifiers.

The finite linear programs use numerical tolerances and are not formal certificates of exact arithmetic or novelty. No independent scientific audit has been performed.
