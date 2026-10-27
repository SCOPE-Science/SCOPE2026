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
The source file `verify.py` was executed with Python 3; its deterministic output appears in `verify_output.txt`. It independently evaluates the neighborhood definition for every nonempty fort and standard zero-forcing propagation for every initial vertex subset, for \(n=3,4,5,6,7\). It then identifies minimal forts by inclusion and compares the full combinatorial families and polynomial coefficients. The checks are finite, totaling \(21,824\) initial subsets, and cannot establish the theorem for all orders; the written proof supplies that argument. No independent audit has been performed.
