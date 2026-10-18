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

# Verification and scope

Execute `python3 verify_sym_tensor.py` in an environment with Python 3 and its standard library. The program checks the finite binomial-sum identity underlying the Hilbert series, displays the first coefficients, and calculates the exact ranks of powers of the unipotent translation matrix on binary forms. A successful exit prints `VERIFY_OK`.

The script checks only finite values. The proof for all integers \(m\geq0\) rests on the global extension-class argument, direct-image identification and elliptic-bundle cohomology. The graded isomorphism between tangent and auxiliary-bundle symmetric sections is the theorem of Denisi–Höring, equation (10). The finite checker neither establishes the absence of undiscovered prior art nor constitutes an independent mathematical audit.
