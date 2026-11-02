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
The proof and definitions are in RESULT.md. To reproduce finite computational checks use Python 3 with NumPy:

`python3 verify_cyclic_cournot.py`

The script verifies inverse-word periodic points for dimensions 2–8 and iterate lengths 1–6, as well as binary-necklace counts, basin fractions and entropy first moments. It does not assert computer certification of all dimensions, all iterates, physical ergodicity, or the full literature comparison. The all-dimensional statements are proved analytically by contraction, tent-map mixing, cyclic ergodic decomposition and entropy of powers.
