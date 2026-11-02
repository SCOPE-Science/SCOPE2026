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

# Reproducibility

Invoke `python3 checker.py` from the directory containing the embedded file. Its first independent test loops through every partial bijection of labelled sets with \(1\le n\le5\), determines open-path and closed-cycle lengths, brute-force enumerates each compatible permutation, checks odd order by cycle lengths, and compares with the claimed formula. Output includes `ALL_CHECKS_OK 1798`.

Its second test adds a distinguished isolated vertex to each admissible partial bijection with no odd open paths and at least one even open path. It checks that there are zero odd-order completions before enlargement and precisely the factorial of the number of even open paths after enlargement. Output includes `ONE_POINT_CHECKS_OK 296`.

The checker uses only Python standard-library routines and integer arithmetic. Exhaustive verification is confined to the above finite input sizes; the argument for arbitrary finite sets is the path-component bijection and labelled-cycle generating-series coefficient proof in RESULT.md.
