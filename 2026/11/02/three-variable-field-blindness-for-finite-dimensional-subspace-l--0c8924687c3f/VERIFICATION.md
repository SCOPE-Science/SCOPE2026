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

# Reproducibility and limits

Run the two embedded Python 3 scripts without external packages:

```sh
python3 verify_extension_support.py
python3 verify_three_pebble.py
```

`verify_extension_support.py` enumerates RREF subspace bases and determines all intersection-dimension extension supports for each ordered pair profile. Tested fields: orders 2, 3, 5 for dimensions 1–3, and orders 2, 3 for dimension 4. Recorded result: PASS.

`verify_three_pebble.py` independently builds subspaces by closure and refines ordered three-subspace atomic colours using **sets**, not multiplicities, under all three single-coordinate replacements. Tested orders 2, 3, 5 for dimensions 1–2 and orders 2, 3 in dimension 3; controls at unequal dimensions are separated. Recorded result: PASS.

The exact output JSON files are included. Re-execution against the embedded code matched these records byte-for-byte. The general theorem is mathematical, using the classical D4 three-subspace decomposition; no finite computation certifies all fields or dimensions. The source comparison is not an exhaustive priority proof.
