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

# Verification of exact weight-two deletion capacity

The supplied `check.py` uses only the Python standard library and must be run with Python 3.8 or newer. Execute `python3 check.py` in the directory containing the script. It explicitly creates each proposed code and enumerates every distinct exactly-one-deletion descendant, checking disjointness and the exact cardinality for all lengths \(2\le n\le80\). For each \(2\le n\le9\), it independently constructs the entire compatibility graph on the \(\binom n2\) weight-two binary words and solves its maximum-clique problem exactly by branch-and-bound; the result matches \(\lfloor(3n-2)/4\rfloor\).

The script completed with `PASS: construction and deletion-ball disjointness at every n=2,...,80` and `PASS: exhaustive optimum through n=9`. Larger instances have not been independently optimized by this packaged script. The infinite statement is established by the separate mathematical proof using deletion-output occupancy and a matching explicit construction.

Independent mathematical auditing was not performed. The script's exhaustive finite search is not an external certificate of the infinite result.
