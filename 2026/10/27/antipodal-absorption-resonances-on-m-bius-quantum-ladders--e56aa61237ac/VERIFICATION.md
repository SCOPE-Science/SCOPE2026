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

The finite graph is constructed from cycle edges plus opposite rungs, independently of its Fourier eigenvalue formula. The accompanying `verify_mobius.py` performs three checks: (i) all 78 half-sizes from 3 through 80 against independent Hermitian spectral decomposition for both the rank and the source survival; (ii) exact integer Krylov-rank computations for the first eight half-sizes from 3 through 10; and (iii) dissipative-generator eigenvalue-count checks for five sizes and two positive loss strengths. Execution returned PASS in all three groups.

To reproduce: use Python with NumPy and SymPy, and run `python verify_mobius.py`. The algebraic proof of the infinitely many cases is in RESULT.md; the finite matrix checks alone do not establish the theorem. No external independent scientific assessment has been performed.
