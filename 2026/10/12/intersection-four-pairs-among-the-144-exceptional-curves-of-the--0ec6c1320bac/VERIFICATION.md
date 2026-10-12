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

Run `python3 verify.py`.

The script uses only exact integer arithmetic. It reconstructs the two published \(10\times8\) representative matrices, generates the order-\(9\) group from the two published base-point permutations, produces \(144\) distinct Picard classes with degree counts \(9,36,54,36,9\), checks self-intersection \(-1\), and exhausts all \(10296\) unordered pairs.

Expected terminal line:

`VERIFY_OK curves=144 pairs=10296 counts=0:2232,1:4320,2:2880,3:792,4:72 max=4 cubic_partners=2 quartic_partners=8`

The script verifies global divisor intersections only; it does not compute local intersection multiplicities at individual points.
