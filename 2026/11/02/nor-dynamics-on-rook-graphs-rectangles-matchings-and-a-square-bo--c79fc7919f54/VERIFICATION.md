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

# Reproducible checks

Compile the included `verify_rook_nor.cpp` with a C++17 compiler:

```sh
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_rook_nor.cpp -o verify_rook_nor
./verify_rook_nor
```

The program enumerates all configurations for fifteen pairs \((a,b)\) satisfying \(2\le a\le4\), \(a\le b\le10\), and \(ab\le20\). It independently implements the update through row/column occupancy counts, tests \(F^3=F\), tests the structural if-and-only-if recurrent-state classification on each configuration, checks the binomial census, counts fixed states, and checks the two-row exact family. It covers 2,811,728 configurations. The actual reproduced output is preserved in `verification_output.txt` and ends with `ALL_CHECKS_PASSED exhaustive_configuration_checks=2811728`.

The mathematical argument in `RESULT.md` covers every integer \(a,b\ge2\); the program is finite corroboration, not an infinite certificate. No independent audit was performed. No higher-dimensional or alternative-update claim is verified.
