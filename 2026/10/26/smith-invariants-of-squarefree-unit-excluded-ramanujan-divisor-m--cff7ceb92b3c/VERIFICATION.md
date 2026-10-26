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

# Reproducibility and scope

Run `python verify.py` with Python 3 and a SymPy installation. The verifier constructs every squarefree modulus formed from the selected small prime sets (46 cases), checks the integer Möbius/zeta incidence reduction, checks exact determinant values, and compares the computed Smith diagonal to the stated formula. Successful execution prints `VERIFY_OK` with the number of cases.

The executable checks integer instances only. The proof of the assertion for every squarefree modulus is the incidence reduction together with the determinant and local first-order Smith-pairing arguments in `RESULT.md`. Independent mathematical audit and broader historical priority certification have not been performed.
