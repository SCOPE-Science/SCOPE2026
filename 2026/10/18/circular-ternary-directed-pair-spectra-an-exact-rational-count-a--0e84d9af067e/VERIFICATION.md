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

The accompanying standalone `verify.py` requires Python 3 and the standard library only. The command `python3 verify.py` completed with the exact output:

```
ALL CHECKS PASSED: exact coefficients n=0..13; circular words n=1..9; balanced connected matrices n=1..14
```

It compares the rational coefficient formula against two independently implemented finite constructions. The direct-word experiment identifies cyclic adjacent-pair matrices from all ternary words through length nine; the second construction enumerates balanced matrices by signed net triangle flux and tests support connectivity through length fourteen. The proof of the infinite formulas and asymptotics is mathematical, not experimental; beyond these finite ranges no exhaustive verification is claimed. The ordinary Euler-circuit existence theorem is used as a classical result and is proved sufficiently for this setting in the accompanying text.
