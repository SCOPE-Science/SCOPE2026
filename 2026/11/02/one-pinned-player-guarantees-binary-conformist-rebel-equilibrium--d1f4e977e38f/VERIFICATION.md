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

# Reproducibility and limits

The self-contained C++17 program `verify_cycle.cpp` performs direct best-response enumeration, without relying on the four-state proof representation. Compile and run in the directory containing the file:

```sh
g++ -O3 -std=c++17 -Wall -Wextra -pedantic verify_cycle.cpp -o verify_cycle
./verify_cycle
```

Expected output:

```text
exhaustive 4-type instances n=3..8: 87360, with stubborn=86856, no PNE=2
exact alternating single-pin counts n=4..16: 280
randomized stubborn-cycle checks n=9..15: 7000
ternary R-C-R-S0 cycle equilibria=0
VERIFY_OK checks=94641
```

The first enumerator ranges over all \(4^n\) types for each \(3\le n\le8\). It directly checks each action profile and both candidate best responses where appropriate. The second enumerator compares the observed exact count to \(n/2\) or \(n/2+1\) for every allowed original alternating phase, pin site and fixed action with even \(n\le16\). The third test uses a fixed built-in pseudo-random state for deterministic reproducibility. The last directly searches all \(3^4\) three-action profiles. These are finite tests and cannot establish the general result on their own. The formal parity-state induction and transformed-edge parity argument appear in `RESULT.md`. External independent validation has not been performed.
