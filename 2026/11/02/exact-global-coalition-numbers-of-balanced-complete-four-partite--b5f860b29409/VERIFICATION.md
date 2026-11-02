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

The proof in `RESULT.md` establishes the formula for every integer \(q\ge1\). The following computations test independent encodings of the original definition rather than replacing that proof.

Run `python verify.py` (Python 3.10+, NumPy, SciPy). It enumerates all set partitions of the original labelled graph for \(q=1,2\), constructs and directly verifies three families of lower-bound witnesses, and solves an exact mixed-integer program for the support-count description for every integer \(1\le q\le25\). Output includes `DIRECT_ORIGINAL_GRAPH_PARTITIONS_OK 1 15 2`, `DIRECT_ORIGINAL_GRAPH_PARTITIONS_OK 2 4140 4`, and `INDEPENDENT_MIXED_INTEGER_SUPPORT_OPTIMUM_OK` for each \(q\), ending `VERIFY_OK`.

Run `g++ -O2 -std=c++17 verify_direct.cpp -o verify_direct` and then `./verify_direct`. This independently constructs all graph and complement neighborhood checks, directly tests the global-dominating condition, and enumerates all unlabelled set partitions of the original labelled graphs, obtaining:

```
EXHAUSTIVE_ORIGINAL_GRAPH_PARTITIONS_OK 1 15 2
EXHAUSTIVE_ORIGINAL_GRAPH_PARTITIONS_OK 2 4140 4
EXHAUSTIVE_ORIGINAL_GRAPH_PARTITIONS_OK 3 4213597 6
EXHAUSTIVE_VERIFY_OK
```

The mixed-integer program's support variables count class incidences and their coalition partners. This finite optimization is not an assertion about all integers \(q\); the mathematical five-case proof supplies the universal result. Both scripts assume ordinary finite simple graphs and the global coalition definition stated in `RESULT.md`.
