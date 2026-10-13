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

Execute `python verify_stage.py` using Python 3.10+ and its standard library. The script enumerates every secondary-degree-multiset profile with at most seven total primary plus secondary species, all legal non-isolated binary incidence matrices for each profile after sorting secondary degrees, and every possible cardinality of uniformly surviving primary species.

For each matrix, the script computes exact rational means and variances (a) from the full set of primary-survivor subsets and (b) from the independently implemented pair-union moment identity, and asserts equality. It then finds every simultaneous variance maximizer in each profile, verifies that the unique failure is four primary and three secondary species with degree multiset \((2,2,2)\), and classifies and verifies all 114 labeled incidence matrices of the exceptional profile.

The checked census is 97 feasible profiles containing 1,600 incidence matrices with secondary degrees in sorted order. The exceptional class has 24 stars, 72 paths and 18 doubled-edge/disjoint-edge matrices. Their exact \((V_1,V_2,V_3)\) vectors are \((3/4,1/4,0)\), \((1/4,1/4,0)\) and \((1/4,7/12,0)\), respectively. The script prints `VERIFY_OK` only if all assertions pass.

The enumeration is exhaustive over the stated finite order range only. The probabilistic moment identity for arbitrary finite networks is proved separately by direct indicator expansion in `RESULT.md`. No statistical inference, infinite-size theorem or independent external review is asserted.
