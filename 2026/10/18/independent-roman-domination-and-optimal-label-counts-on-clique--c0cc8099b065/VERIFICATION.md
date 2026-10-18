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

The proof in `RESULT.md` applies to all integers \(q\ge3\) and \(n\ge3\). The included executable `verify.py` requires only Python's standard library. Run `python verify.py` from a directory containing it; the expected output is:

`VERIFIED: 13 independent layer-state enumerations and 7 direct graph enumerations`

The first test exhausts legal fiber assignments for \(q=3,n=3,4,5,6,7,8\), \(q=4,n=3,4,5,6\), and \(q=5,n=3,4,5\), checking both optimum weight and count against the formulas. The second generates actual Cartesian-product adjacency masks and independently exhausts all independent positive supports and \(1/2\)-labelings for \((q,n)=(3,3),(3,4),(3,5),(3,6),(4,3),(4,4),(5,3)\). It tests every zero for an adjacent label two. These bounded computations are finite cross-checks, not substitutes for the general proof; there is no formal proof-assistant certificate. Independent audit has not been performed.
