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
# Reproducibility checks

Run `python3 verify.py` with Python 3 and its standard library. The program verifies all integer-domain applications in the proof: Bézout count, Tjurina numbers, Arnold bounds, the du Plessis–Wall upper and lower inequalities for every possible integral minimal-relation degree, and the minimal-plus-one Tjurina equality. Its expected final output is `VERIFY_OK`.

The actual successful run gave:

```
k=2; nodes=2; tacnodes=1; tau=5; Dimca-Sernesi_min_r=1; admissible_mdr=[2]; du_Plessis_Wall_r=k+1_upper=3; exponents=(2,2,3)
k=3; nodes=2; tacnodes=5; tau=17; Dimca-Sernesi_min_r=3; admissible_mdr=[3]; du_Plessis_Wall_r=k+1_upper=15; exponents=(3,3,4)
k=4; nodes=2; tacnodes=11; tau=35; Dimca-Sernesi_min_r=4; admissible_mdr=[4]; du_Plessis_Wall_r=k+1_upper=33; exponents=(4,4,5)
VERIFY_OK
```

These computations are *conditional verification of finite substitutions into published general theorems*, not a replacement for the theorems. No exhaustive classification of complex conics by computer, explicit syzygy bases, or independent audit is asserted. The proof is valid for every curve satisfying its stated hypotheses and not for neighboring baskets.
