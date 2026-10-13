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
Run `python3 verify.py` in the directory containing this file.

The verifier performs an exhaustive exact census of every integer partition of each total size from \(1\) through \(17\). It asserts the standard partition counts \(1,2,3,5,7,11,15,22,30,42,56,77,101,135,176,231,297\), for a total of \(1211\) signatures. For each signature it evaluates the defining recursive-divisor recurrence and the least odd representative.

For total sizes through \(16\), every signature satisfies \(A(\lambda)\le m(\lambda)\). At total size \(17\), exactly three signatures satisfy the strict reverse inequality; their exact values are written to `partition_certificate.json`.

The verifier then independently evaluates the defining recurrence on the actual divisor lattices of the boundary example and the source's least odd ample example. These calculations use \(1080\) and \(720\) divisors and reproduce the signature-based values exactly.

No finite numerical interval in \(n\) is used to infer an infinite statement. Exhaustiveness comes from the complete finite list of exponent partitions at the bounded values of \(\Omega\). A successful run ends with `VERIFY_OK`.
