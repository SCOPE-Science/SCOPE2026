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

Run `python3 verify.py` with Python 3 standard library. The script reconstructs the unrestricted-odd/distinct-even partition product, forms the theta convolution, and independently computes the residue formula; it also enumerates integer partitions directly through index 22. The completed run reported `VERIFY_OK coefficient_indices=601 independent_partition_enumerations=23` and did not encounter a mismatch. Exact loop ranges and the observed residue frequencies are printed by the script. The computation is finite and does not establish the theorem for all indices or establish density; these rely on the formal-series and prime-arithmetic proofs in RESULT.md.
