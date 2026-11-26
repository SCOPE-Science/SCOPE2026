---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and verification

The fixed-part-count extremum follows from the cited per-edge formula and the strict discrete optimization in `RESULT.md`. As a bounded check, for each \(2\le N\le30\) one can generate nondecreasing integer partitions of \(N\), with at least two parts, by recursively appending a part between the previous part and the remaining sum. For each partition, compute the maximum of \(2+f_N(u)+f_N(v)\) over distinct part indices using rational arithmetic. Group the partitions and their maxima by part count, retaining all ties for the largest value; each of the 435 \((N,r)\) groups has exactly the maximizing multiset in the Finding. This finite check uses the per-edge formula as input and does not prove it or the arbitrary-size result.

The unchanged `verify.py` also computes the underlying canonical projectors from grounded graph Laplacians using exact rational arithmetic for \(2\le N\le10\). This is a separate check of finite examples of the per-edge formulas, not a priority claim for them. Its previously recorded output was `MULTIPARTITE_GRADIENT_EXACT_OK 174858 configurations 128 edge_rows 2926`.
