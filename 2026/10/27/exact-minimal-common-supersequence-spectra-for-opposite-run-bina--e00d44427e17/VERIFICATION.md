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

# Verification and scope

The theorem is established by the general proof in `RESULT.md`. The standalone C++17 program `check_minimal.cxx` is a supplementary fully exhaustive *bounded* check of every binary candidate length from \(3m\) through \(4m\) for each \(m=1,2,3,4,5\). It does **not** extrapolate these experiments to arbitrary \(m\).

## Reproducible command

```
g++ -O3 -std=c++17 -Wall -Wextra -pedantic check_minimal.cxx -o check_minimal
./check_minimal
```

Expected output after replay from the embedded source:

```
m=1 checked=24 counts: 2
m=2 checked=448 counts: 2 8
m=3 checked=7680 counts: 2 18 72
m=4 checked=126976 counts: 2 32 200 800
m=5 checked=2064384 counts: 2 50 450 2450 9800
VERIFY_OK
```

The test independently checks the actual subsequence property after each individual deletion and compares it against the derived structural membership test and closed-form counts. A successful `VERIFY_OK` checks those finite cases only. The asymptotic proof additionally relies on the stated binomial ratio bound, dominated convergence and Stirling's formula. No independently performed scientific audit or certification is claimed.
