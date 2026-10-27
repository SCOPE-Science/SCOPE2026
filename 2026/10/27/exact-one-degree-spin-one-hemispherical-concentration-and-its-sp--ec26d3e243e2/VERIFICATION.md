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

The complete analytical proof is in `RESULT.md` and is not replaced by the finite checker.

Run `python check.py` with NumPy, SciPy and SymPy. The test program computes exact integrals independently from the proposed closed formula using Rodrigues derivatives, performs separate Gauss–Legendre hemisphere quadratures and trace checks, and verifies rational spectra, multiplicities, sharp gaps, and the degree recursion on finite ranges. Actual stdout appears verbatim in `verification_output.txt`.

The checker validates degrees only to the limits specified in its code. It does not establish the universal theorem by exhaustion, nor the priority of the result in the literature. No independent audit is claimed.
