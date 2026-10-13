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

Use the two complete included source files independently, without external data or nonstandard packages:

```sh
python3 verify.py
g++ -std=c++17 -O2 -Wall -Wextra -pedantic crosscheck.cpp -o crosscheck
./crosscheck
```

The first program enumerates exactly 65,536 Boolean functions on sixteen feedback states, admits exactly 2,048 functions with one 32-state cycle, directly counts every cyclic factor modulo reversal, verifies the symbolic feedback formula for every admitted function, and checks the joint distribution. It reports `VERIFY_OK tables=65536 cycles=2048 r5=20` and the five-bin distribution.

The second program enumerates directed Hamiltonian cycles of the 32-state shift graph from a uniquely chosen all-zero root, directly builds their circular words, and computes the same length-six classes. It reports `GRAPH_DFS cycles=2048 nodes=92636 r22=576 r25=960 r26=192 r28=256 r29=64` and `GRAPH_DFS_VERIFY_OK`.

The two exact programs are independent enumerations of the same well-defined 2,048-word finite universe, though they are not independent external audits. They verify the finite table only. The general-order reversal identity and the feedback-to-cycle correspondence are established by the mathematical proof, not by extrapolation from finite tests. Independent audit status remains unperformed.
