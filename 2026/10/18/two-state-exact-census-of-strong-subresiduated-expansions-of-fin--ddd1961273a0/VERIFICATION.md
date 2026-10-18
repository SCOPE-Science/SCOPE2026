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

# Reproduction and verification

Run `python3 verify.py` with only Python 3 standard-library modules. The verifier lists selected layer vectors and their exact labeled and unlabelled counts, then checks every ordered composition of total size at most seven (127 profiles) by direct enumeration of regressive, isotone, idempotent maps. Fixed subsets are independently compared to the singleton condition and the counts to both two-state recurrences. Direct bounded-sublattice enumeration independently checks the expansion-lattice bijection on small lattices. For selected profiles of at most seven points, all actual layer-permutation conjugacies are generated and their orbit counts compared with the unlabelled recurrence. For additional selected profiles of up to nine points, literal enumeration checks further nontrivial outputs.

The exact intended final lines are:

```
ALL LAYERED PROFILES THROUGH SEVEN VERTICES VERIFIED: 127
DIRECT-LATTICE AGREEMENT OK
DP AND FIXED-POINT BIJECTION OK
ALL UNLABELED-ORBIT RECURRENCES AGREED, INCLUDING LITERAL GROUP ACTIONS
```

The verifier uses finite cases only; the unrestricted finite profile claim follows from the mathematical proof, not from sampled computations. Independent external mathematical audit has not been performed.
