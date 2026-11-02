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

# Verification record

The embedded `verify.py` is a complete Python-standard-library replay, with no external data files. It reconstructs the 18- and 84-state matrices from their definitions and verifies all coefficients of their characteristic polynomials by exact Newton identities from traces through the full matrix dimensions. It computes the degree-36 determinant polynomial, checks coefficients in the formal logarithmic derivative, and directly enumerates all 6,498,957 three- or four-colour vertex-assignment words for the specified small graph orders using edge and neighbourhood conditions independent of the transfer construction.

Successful actual execution reported:

```
CHARPOLY_OK dimensions 18 84
RATIONAL_SERIES_OK n=3..18
TRANSFER_OK n3=3..18 n4=3..10
DIRECT_OK assignments 6498957
HOMOGENEOUS_OK n=3..12
CONSTRUCTIVE_OK lengths 3,4,5 share a base
VERIFY_OK
```

Universal validity follows from the matrix-to-colouring bijection, finite exact characteristic identities, the formal trace identity, and explicitly concatenated length-three/four/five closed walks. The direct finite enumerations are cross-checks, not an infinite proof. The characteristic-polynomial arithmetic uses only integer operations and covers every coefficient. No independent external audit or historical-priority certification is asserted.
