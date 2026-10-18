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

# Exact verification

From the same directory, run `python3 verification.py` with Python 3.9 or later. No downloads or third-party dependencies are needed. The checker constructs the graph on unordered pairs of a five-element set, then tests all \(59049\) ternary words for edge-Lipschitz inequalities and connectedness of the tight-edge graph.

Actual local execution printed `ALL EXACT CHECKS PASSED`, followed by \(1032\) facets, \(17\) signed symmetry orbits, incidence counts \(110,300,330,280,12\) at tight-edge counts \(12,14,16,18,20\), and level counts \(922,110\). The same execution independently re-enumerated all binary cuts and nonadjacent pairs of level-zero/level-two sets, verified all automorphism orbit sizes and disjointness, computed the Burnside fixed-point sum \(4080\), and identified the twelve maximally incident facets with complementary Hamiltonian cycle decompositions.

The proof in `RESULT.md` shows why every possible facet arises in the finite ternary search. The code certifies an exhaustive finite classification, not infinite-dimensional behavior. The analytic bound of twenty and its equality case do not depend on computational termination or timing. No external scientific audit is claimed.
