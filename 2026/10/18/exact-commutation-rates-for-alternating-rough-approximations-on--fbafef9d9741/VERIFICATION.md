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

# Verification details

Run `python3 verify_cycle.py` using Python 3's standard library. No external dependency or input files are required. The checker directly implements the lower approximation as a union of complete equivalence blocks. It constructs each set partition once using restricted-growth strings; for each ordered pair of partitions on sizes one through five, it examines all subsets of the universe and compares literal composition equality to the explicit two-step-neighborhood criterion (90,346 cases). For alternating pair partitions on \(2n\) points with \(n=2,\ldots,8\), it independently checks all \(87,376\) subsets and verifies agreement with the four-window avoidance criterion and the integer transfer-matrix count. It also checks the trace recurrence through length 44.

Observed output:

`VERIFY_OK general_partition_subset_cases=90346 cycle_subsets=87376 cycle_counts=[(2, 16), (3, 52), (4, 192), (5, 709), (6, 2632), (7, 9776), (8, 36320)] recurrence=YES`

The unrestricted claims are established by the componentwise proof, the finite-state closed-walk correspondence, and Perron--Frobenius theory, not by finite exhaustive search. There is no machine-checked formalization or independent external validation.
