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
# Finite verification

Compile `verify_antisquares.c` with `cc -std=c11 -O3 -Wall -Wextra -o verify_antisquares verify_antisquares.c`. For each integer `k` from 1 to 7, run `./verify_antisquares k $((4*k-2))` and `./verify_antisquares k $((4*k-1))` (substituting the numeric value for `k`). Run `./verify_antisquares 8 30` for the certified order-eight lower bound. The upper bound at length 31 is established mathematically by the alternating-host construction, not by enumerating all length-31 hosts.

Compile `verify_literal.c` with `cc -std=c11 -O3 -Wall -Wextra -o verify_literal verify_literal.c` and run `./verify_literal 5` for the independent direct, full-host literal subsequence check through order five. Tests of all reachable prefix states, not random trials, justify the finite computations. The verifier tracks exactly the target-greedy progress and prunes only an irrecoverable unfinished target.

Observed exact output for orders one through seven (host counts): `2 10 44 190 800 3266 13018`. For each of those orders, the previous length has zero covering hosts. Observed order-eight length-30 output: `good=0 nodes=30965979 prunes=15482990`. The host-palindrome and universality-index data printed by `verify_antisquares.c` agree with the table in `RESULT.md`. A standard arch scan is used to compute the ordinary universality index; reversal is checked literally.

The computations make no claim for orders beyond eight or for the order-eight number of length-31 hosts. Independent scientific review and external certification have not occurred.
