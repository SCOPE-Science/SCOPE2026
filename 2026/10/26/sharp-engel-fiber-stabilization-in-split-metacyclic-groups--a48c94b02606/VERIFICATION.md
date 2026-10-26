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

# Reproducibility and limitations

Execute `python3 verify_engel_word.py` using standard Python 3. No third-party packages are required. The checker computes group inverses, commutators, and iterated commutators independently of the closed-form arithmetic calculation and compares all output values. It also verifies sharpness of the least stabilization length for 1,965 units with moduli from \(2\) to \(80\), checks complete mass normalization, and tests the two lifts \(u=2\) and \(u=8\) modulo \(27\) with complement of order \(18\).

Successful checker output: `VERIFY_OK: exact cutoff checked for 1965 units modulo 2..80; exhaustive group-pair computations: 32 ; lift comparison: [(2, 4, 122472), (8, 3, 122472)]`.

The integer-arithmetic computational checks are finite. They do not prove the theorem in untested cases; the unrestricted argument is in `RESULT.md`. No independent audit has been conducted.
