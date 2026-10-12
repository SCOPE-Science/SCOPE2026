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
# Verification

The analytic proof is the primary evidence. The finite checker is an independent corroboration.

`artifacts/verify.py` constructs complete multipartite graphs directly from part profiles and evaluates the definition of proper conflict-free coloring from open neighborhoods. It separately evaluates the singleton-witness characterization and the Stirling-number counting formula.

The replay range is every nondecreasing part-size profile of total order \(2\) through \(6\), with at least two parts, and every possible number of used colors. It checks \(23\) profiles and \(114\) profile/color-count pairs.

Expected replay output:

`ALL CHECKS PASSED; profiles=23; profile_color_pairs=114; labeled_colorings=699753; surjective_colorings=50405; orders=2..6`

The finite computation does not prove the infinite theorem. Its purpose is to test boundary cases, including complete graphs, stars, bicliques, singleton parts, all-singleton colorings, and the exact enumeration formula.
