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

# Verification instructions and limits

Execute `python3 verify.py` with SymPy installed. The script works entirely in finite fields and polynomial rings and does not use external data. An observed successful run printed:

```
MOD5_TORUS_SEXTIC_IDENTITY_OK
FOUR_RATIONAL_NODES_NON_SPLIT_DISCRIMINANT_3_OK
SIX_F5_CUSP_SUPPORTS_OK
GF5_PROJECTIVE_POINTS_OK: 10
GF25_PROJECTIVE_POINTS_OK: 22
ARITHMETIC_GENUS_AND_DELTA_OK
VERIFY_OK
```

The polynomial identity and node-discriminant calculations are exact. The finite-field counts exhaust every projective point over the indicated two fields; they are supplementary checks, not proofs for all extensions. The proof in `RESULT.md` independently handles the geometric singular locus over the algebraic closure, irreducibility, normalization, local Picard group and extension-field counts. The ordinary cusp and node local forms are established analytically by the coordinate changes displayed there. No external independent audit or certified computer algebra proof has been performed.
