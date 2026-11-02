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

# Reproducibility and verification limits

The attached standalone `verify.py` requires only Python 3 and its standard library. Execute `python verify.py` after extracting the two files into one directory. The program implements the local graph forcing process directly, from neighbourhoods and arbitrary initial assignments over \(\{0,1,\ldots,Q\}\), and separately implements the Stirling-number expression. It then compares the full initial-domain distributions for 18 finite graph/palette combinations and independently checks the balanced minimum and leading coefficient at 16 parameter points.

The actual run printed:

```
DIRECT_FORCING_VS_STIRLING_FORMULA_OK 18 cases
K_2_2_2: {4: {6: 96, 4: 432, 5: 288, 3: 288}, 5: {6: 780, 5: 720, 4: 360}, 6: {6: 4080}}
BALANCED_MINIMUM_AND_MULTIPLICITY_OK 16 cases
VERIFICATION_OK
```

The first procedure is a finite exhaustive check of specified graph/palette pairs. It is not an exhaustive check of all part-size vectors or palette sizes. Infinite correctness rests on the proof of the complete forcing characterization and its exact surjective-colouring count. The code is a consistency check rather than an independent mathematical audit.
