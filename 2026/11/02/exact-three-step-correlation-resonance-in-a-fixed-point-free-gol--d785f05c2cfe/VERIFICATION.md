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

# Reproducibility and verification

Run `python check.py` using Python 3 and SymPy. The executable reads no external data and constructs every mathematical constant and matrix directly in the algebraic field \(\mathbb Q(\sqrt5)\). It verifies the displayed transfer equation for the step density, its integral and mean, the cubic eigenvector relation for the four-dimensional transfer restriction, seven consecutive exact autocovariance values, and the closed-form Green--Kubo limit. The general \(n\)-lag statement follows analytically from the exact cubic eigenvector relation together with the first three functional values; testing only seven values is not presented as exhaustive enumeration. No independent audit or external proof certification has been carried out.
