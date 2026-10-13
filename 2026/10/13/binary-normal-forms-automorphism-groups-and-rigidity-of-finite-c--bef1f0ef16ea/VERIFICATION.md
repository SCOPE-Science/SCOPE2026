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
# Verification

The enclosed `verify.py` runs with Python 3 and no nonstandard packages. It derives every subset-support chain with a fixed Boolean first fiber of atom rank at most seven. All their size signatures coincide with the consecutive integer intervals predicted by the binary normal form. It also checks restriction-map interval isomorphisms; full symmetric-stabilizer orders via every permutation for ranks at most five; and the rigidity criterion for all enumerated chains. Finally it constructs the full Bochvar operation tables for all canonical ranks at most three, evaluating the 19 defining identities/quasi-identity directly.

Expected standard output finishes with:

```
VERIFY_OK 15154351 exact assertions; binary uniqueness through k=7; stabilizer symmetries through k=5
VERIFY_AXIOMS_OK 156475 exact checks of all 19 Bochvar axioms/quasi-axiom over all canonical forms with k<=3
```

The exhaustive finite tests do not prove the all-rank theorem. Its general proof uses finite Boolean algebra theory and the already published Bochvar Płonka representation. External independent audit has not been performed.
