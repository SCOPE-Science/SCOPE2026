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

The attached `verify_retracts.py` is a standalone pure-Python program using exact arithmetic for prime fields. Run `python3 verify_retracts.py` from a directory containing the file. Its complete successful output is:

```text
COMPLEMENTS_OK 1 2 {(0, 0): 1, (1, 0): 12}
COMPLEMENTS_OK 2 2 {(0, 0): 1, (1, 0): 240, (2, 0): 480, (2, 1): 480}
COMPLEMENTS_OK 2 3 {(0, 0): 1, (1, 0): 3240, (2, 0): 9720, (2, 1): 19440}
CONJUGATION_ORBITS_OK [((0, 0), 1), ((1, 0), 240), ((2, 0), 480), ((2, 1), 480)]
VERIFY_OK
```

The first series exhaustively enumerates isotropic subspaces and complements, including the central-functional multiplicity. The direct binary test exhaustively enumerates all projections and compatible central functionals and traverses the automorphism orbits under symplectic transvections and central shears. It checks the four nonidentity orbit sizes; the identity is an additional singleton. The program does not enumerate arbitrary extension fields or prove the general formula; those statements follow from the proof. No independent audit has been performed.
