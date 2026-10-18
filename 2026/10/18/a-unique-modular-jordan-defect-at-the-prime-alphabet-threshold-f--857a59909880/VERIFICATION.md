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

`verify.py` directly builds the complete free left-regular band multiplication table and the uniform-letter left action over \(\mathbb F_p\). It uses elementary modular Gaussian elimination to check the proposed eigen-kernel dimensions, generalized zero eigenspace, the nonzero rank-one polynomial defect, its square zero, and its annihilation of the original action. The executed tests cover primes \(p=2,3,5\), with full module dimensions \(5,16,326\), respectively, and end with `VERIFY_OK_MODULAR_FIRST_COLLISION`.

The word-count recurrence and absorption argument in `RESULT.md` provide the uniform proof. Finite computations do not prove statements for untested primes. The nonmodular multiplicity formula is sourced to the full-module theorem of Brauner, Commins and Reiner; historical priority remains a separate concern.
