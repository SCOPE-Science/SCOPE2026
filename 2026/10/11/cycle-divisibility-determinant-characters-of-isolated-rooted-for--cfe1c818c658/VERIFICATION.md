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

# Reproducibility and limits
Execute `python3 verify.py` from the directory containing this document and the enclosed script. It requires Python 3 with only its standard library.

The script independently enumerates all rooted forests through acyclic parent functions, checks the isolated-original-vertex criterion, and calculates signed simplicial fixed-face Lefschetz traces from the actual action on directed arcs. Separately, a fraction-free integer determinant routine computes the theorem's cycle-divisibility formula. Equality was tested on all cycle types for original vertex counts \(\(\(m=3,4,5\),6\)\) and four selected cycle types for \(\(m=7\)\) (30 comparisons in total). It also computes augmented mod-two simplicial homology through exact bitset Gaussian elimination for \(\(m=3,4,5\)\), recovering ranks \(\(5,25,189\)\) in degrees \(0,1,2\), respectively, and zeros in all other degrees of the tested complexes.

The script was executed from its real packaged source path and returned `VERIFY_OK`. These are finite sanity checks; the universal result rests on the published homology-concentration theorem and the independent uniform proof in `RESULT.md`. No computation establishes novelty or independence.
