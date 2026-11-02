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

# Reproducibility and scope of checks

The complete, self-contained C++17 source `verify.cpp` enumerates the words of each nontrivial weight for lengths \(3\) through \(15\), directly enumerates all possible cyclic rotations of three consecutive bits, checks that the resulting edge set equals the token-move graph on the squared path, and performs all-source breadth-first searches. The tested weight range is \(1\le k\le\lfloor n/2\rfloor\); complementing bits is a proved symmetry for all remaining weights. The complete replay processed 110,998,233 ordered source-target pairs and printed `VERIFY_OK`.

The independent standard-library-only Python 3 source `verify_transport.py` separately computes all graph distances by BFS and minimum-cost matching costs by subset dynamic programming for every weight and \(3\le n\le9\). All 66,174 ordered pairs matched, and the resulting diameters matched the claimed formula; it printed `TRANSPORT_VERIFY_OK`.

These are finite checks and do **not** establish the theorem for arbitrary \(n\). The general proof in `RESULT.md` independently reconstructs the matching transport metric, its integral Lipschitz dual, the two-connected sorted-value restriction, and the sharp extremal pair. No formal proof assistant, human audit, or external certification has been performed.

To replay:

```sh
c++ -O2 -std=c++17 verify.cpp -o verify
./verify
python3 verify_transport.py
```
