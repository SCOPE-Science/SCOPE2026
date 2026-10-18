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
# Exact verification of the mixed-theta orbit theorem

Execute `python3 verify_theta.py` with a standard Python 3 installation. The script uses only `itertools`, `collections`, and `math` from the standard library and performs exact integer calculations. It must terminate with `ALL EXACT MIXED-THETA CHECKS PASSED`.

It constructs each graph from two poles, one two-edge path, and \(m\) three-edge paths. For \(m=2,3,4\), it enumerates all assignments of edge increments \(-1,0,1\) on an arbitrary fixed spanning tree, reconstructs every integer-valued potential normalized at the first pole, tests every remaining graph edge, and checks that the tight-edge graph is connected and spanning. This exhaustive method does not presuppose the three-class theorem or that the chosen tree is tight. From this potential set, it independently computes complete symmetry orbits using arm transpositions, pole reversal, and central inversion. It compares the **entire class-tagged orbit-size multiset**, not just the orbit count, to the formula. For \(m=5\), it independently enumerates all facet potentials and tight-edge distributions (but does not compute the symmetry orbits).

The exact passing outputs are \((126,23)\), \((594,48)\), \((3078,94)\) for the facet/orbit counts at \(m=2,3,4\), and \(17010\) facets at \(m=5\). The tight-edge histograms are respectively \(\{6:90,7:36\}\), \(\{8:486,10:108\}\), \(\{10:2754,13:324\}\), and \(\{12:16038,16:972\}\). These are fully exhaustive **finite** checks; the general \(m\) theorem follows from the combinatorial proof in `RESULT.md`. No independent external audit is claimed.
