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

# Reproducibility checks
The bundled `verify_binary_cycles.py` uses only Python 3 standard-library operations on exact integers and binary vectors. Run `python3 verify_binary_cycles.py` from the folder containing this file. It checks every state at ring sizes 4 and 8; for sizes 4, 8, 16 and 32, it uses independently assembled binary matrices to compute the nullities of fixed-point operators at all relevant dyadic times. The supplied program ran and printed `ALL CHECKS PASSED`.

Finite enumeration cannot establish an all-size claim. The mathematical certificate is the invertible commuting factorization \(M-I=DL\), the characteristic-two Frobenius identity, and the exact kernel identity \(\ker C^{2^j}=\ker(S^{2^{j+1}}-I)\). These equalities imply the theorem for every \(m\ge2\).

The result does not cover moduli other than the field with two elements, non-dyadic ring lengths, or couplings other than \(S+S^{-1}\). No independent audit or external validation is asserted.
