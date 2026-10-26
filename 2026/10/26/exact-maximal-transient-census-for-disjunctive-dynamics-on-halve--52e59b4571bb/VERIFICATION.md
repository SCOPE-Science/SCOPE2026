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

The Python 3 standard-library checker `verify.py` was executed from the package directory. It checks exact walk-shell reachability at dimensions 6 through 9, independently enumerates the maximal-delay seed supports on odd dimensions 7 and 9, and compares the analytic criterion with simulated first-entry time for sparse and random supports. The actual output was:

```text
n= 6 T= 3 A= 32 maximizers= 274877905920
n= 7 T= 3 A= 7072 maximizers= 260910748178547848043520
n= 8 T= 4 A= 128 maximizers= 87112285931760246646623899502532662116352
n= 9 T= 4 A= 124160 maximizers= 28753491599410357647581146997357381278124002592171864862278107260844988336773201920
VERIFY_OK walk_shell_checks= 36 state_checks= 246494 bad_supports= {(6, 0): 32, (6, 1): 32, (7, 0): 7072, (7, 1): 7072, (8, 0): 128, (8, 1): 128, (9, 0): 124160, (9, 1): 124160}
```

Finite tests do not certify the unrestricted dimensions. The proof handles all integers \(n\ge6\) by explicit length-of-walk constructions and exact combinatorial counting. No independent audit or external validation has been performed.
