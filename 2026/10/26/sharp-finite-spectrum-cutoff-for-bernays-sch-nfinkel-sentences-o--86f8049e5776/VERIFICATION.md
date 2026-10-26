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

# Verification performed

The analytic proof verifies that the two local pumping moves preserve all complete diagrams in equality and one equivalence relation for the fixed existential witness tuple and \(\ell\) universally quantified variables. It then bounds structures with neither move and constructs a model satisfying the three quantifier-free prohibitions at the exact cutoff.

The supplementary checker `artifacts/verify_equivalence_cutoff.py` was executed from its actual output path. It enumerates finite partition shapes, witness assignments, and quantifier-free atomic diagrams for five parameter pairs, tests every proposed local extension, and checks the exact extremal prohibitions. Recorded output:

```
CHECK k=0 ell=2 B=1 cases=5 sharp=YES
CHECK k=0 ell=3 B=4 cases=18 sharp=YES
CHECK k=1 ell=2 B=3 cases=55 sharp=YES
CHECK k=1 ell=3 B=7 cases=446 sharp=YES
CHECK k=2 ell=2 B=5 cases=1131 sharp=YES
VERIFY_OK pointed_cases=1655
```

Bounded execution cannot certify the universal proof or historical originality. No formal proof assistant, independent audit, or external scientific validation was used.
