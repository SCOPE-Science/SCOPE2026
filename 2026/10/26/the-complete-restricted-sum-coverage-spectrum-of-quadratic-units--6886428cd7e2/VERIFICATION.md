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

Run `python3 verify.py` with the Python 3 standard library. It computes all attainable subset sums by cardinality in a cyclic bit-mask convolution for \(p=3,5,7,11,13,17,19,23\). For each prime, the computed complete universal-cardinality set is asserted equal to the theorem's predicted set. The program also checks the exact missing residues for five squares modulo \(25\) and prints `VERIFY_OK` if all checks pass.

This finite test does not prove the theorem for arbitrary prime \(p\). The infinite steps are the elementary Hensel lifting of unit squares, Dias da Silva--Hamidoune restricted-sum inequality, Cauchy--Davenport inequality, and the explicit quadratic-character calculation, all reconstructed in `RESULT.md`. The three related prior full texts identified in `RESULT.md` were not available for complete coverage inspection. No independent validation or audit has been performed.
