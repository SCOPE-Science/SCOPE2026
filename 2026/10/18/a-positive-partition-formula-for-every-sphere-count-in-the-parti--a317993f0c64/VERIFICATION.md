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

Run `python3 verify_partition_graph.py` with a standard Python 3 interpreter, with no third-party dependencies. It enumerates the unordered partitions and all admissible transfer edges directly, then recursively enumerates every clique for \(1\le n\le15\). The output must end in `PASS`; it also checks the descending height links and their exact local Euler contributions against the formula, the independently published \(n\le25\) Euler table, and formal generating-function coefficients through degree 35.

Exact published sample comparisons: \(b_8=1\), \(b_{10}=5\), \(b_{25}=3324\). New coefficients from two exact symbolic/combinatorial pipelines: \(b_{26}=4480\), \(b_{30}=13653\), \(b_{35}=48227\).

The unbounded proof is written in `RESULT.md` and does not infer the general theorem from the finite computations. It relies on the known sphere-wedge theorem only for upgrading the newly determined Euler characteristic to the integral homotopy classification. The stand-alone check does not independently reprove that prior theorem, identify unpublished overlapping work, or certify publication priority.
