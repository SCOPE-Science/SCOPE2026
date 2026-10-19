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

The 23-word witness is checked by independent enumeration of six-position subsequences in `artifacts/verify_witness.py`. Every received six-bit word is compatible with at most three selected eight-bit words. The same program checks a 48-support rational primal feasible point with denominator \(35865\) and exact value \(1082/45\), plus all 256 integer dual inequalities, whose equal objective \(3246/135\) proves LP optimality; the slack distribution is 54 zero, 4 of value two, 4 of value three, 12 of value four, and 12 of value six.

Compile and execute `artifacts/verify_upper.cpp` using a C++17 compiler. It independently reconstructs the 256-by-64 incidence matrix, checks the rational dual exactly using integers, enumerates all 113 permitted positive-slack subsets, and searches for a feasible 24-word code over the 54 zero-slack words. Expected terminal status: `INFEASIBLE_24_EXACT cases=113 total_sets=113 nodes=30578 tight=54 other=32` and exit code zero. A found 24-word code, an exceeded node limit, or a failed prerequisite returns a nonzero exit code.

The finite enumeration proves only the stated eight-bit two-deletion three-list parameter; no other alphabet, length or list size is certified. Independent scientific audit: not performed.
