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
The proof uses the cyclotomic identity \(\Phi_{p^2}(z)=1+z^p+\cdots+z^{(p-1)p}\), the exact frequency-difference orthogonality criterion, and a bijection between residue-digit frequency blocks and the parameter functions. To reproduce finite checks run `python3 CHECK.py` from the folder containing the embedded artifacts; expected deterministic output is in `CHECK_OUTPUT.txt`.

The integer-only checker scans Fourier zeros at \(p\in\{2,3,5,7\}\), several lifts for each prime, constructs orthogonal bases, and exhaustively classifies all size-four frequency sets at \(p=2\). It does not inspect every function at large primes; no finite scan is offered as an infinite proof. The published-paper comparison is best-knowledge rather than a certificate of bibliographic uniqueness. Independent audit has not been performed.
