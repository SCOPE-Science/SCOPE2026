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

# Verification and reproducibility

The exact scientific artifact is `dsr_verify.c` in this package. Run:

```sh
cc -O2 -std=c99 -Wall -Wextra -Werror dsr_verify.c -o dsr_verify
./dsr_verify
```

Output reproduced from the packaged source:

```text
orbit_size=5040
n=2 total=2 exceptions=0
n=3 total=8 exceptions=0
n=4 total=64 exceptions=0
n=5 total=1024 exceptions=0
n=6 total=32768 exceptions=0
n=7 total=2097152 exceptions=5040
witness=1324
DSR: 6 3 2 4 5 14 14
Copeland: 3 3 2 2 2 5 4
```

Every labeled tournament is generated exactly once by an unpruned integer loop covering all \(2^{\binom n2}\) bit strings. The eligibility logic includes every active partition case of the original 2024 scoring definition. In addition to the census, the checker compares the derived scoring routine against the paper's four-candidate Table 7 and tests every failing seven-candidate tournament against the full relabeling orbit of the witness. The certificate is reproducible finite computation, not a formal proof about unbounded orders. A separately coded matrix implementation independently found the same \(5,040\) failures and first witness. There is no external audit certificate, no independently confirmed publication priority, and no assertion concerning the later distinct scoring rule.
