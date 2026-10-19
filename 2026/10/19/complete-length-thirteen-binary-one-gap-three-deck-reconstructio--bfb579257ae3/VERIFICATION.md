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

# Reproduction of the finite census

Extract `gapped_verify_dp.cpp` and `gapped_verify_direct.py`, then execute:

```sh
c++ -std=c++17 -O2 gapped_verify_dp.cpp -o verify_dp
./verify_dp
python3 gapped_verify_direct.py
```

The C++17 program generates all \(8192\) words at length \(13\) and all smaller binary words down to length \(1\) via an exact prefix-deck recurrence. It sorts complete 14-integer profile keys and asserts the histogram \(8184\) singleton/4 doubleton/0 larger, and the exact four reverse pairs. Successful output ends with `VERIFY_DP_OK`.

The separate Python 3 program enumerates all allowed spaced index tuples literally and groups the resulting profile vectors; no recurrence code is shared. It independently asserts the class histogram and the exact pairs. Successful output ends with `VERIFY_DIRECT_OK`.

These are exhaustive computations over a finite set. They do not establish uniqueness beyond the stated lengths or any result about general alphabets or separation values. No independent external audit has been performed.
