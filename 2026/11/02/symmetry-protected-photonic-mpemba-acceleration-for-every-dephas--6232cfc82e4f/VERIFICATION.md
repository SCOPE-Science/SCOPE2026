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

The proof is self-contained in `RESULT.md`. For an independently constructed finite-dimensional check, run `python check.py` in a directory containing the attached script with Python 3, SymPy, NumPy and SciPy installed. The checker constructs the Liouvillian from Hamiltonian matrix units rather than relying on the claimed block spectrum, compares characteristic polynomials, and symbolically verifies both shifted Routh–Hurwitz sets of identities. It also samples positive dephasing ratios and reconstructs time-evolved physical density matrices. The recorded run passed 387 checks.

The symbolic identities and the analytical cubic stability argument prove the global strict inequality. Finite sampling cannot establish it alone. The state-pair comparison uses natural-log relative entropy against the uniform density matrix, and the large-time logarithmic rates are insensitive to polynomial Jordan factors. Independent scientific audit has not been performed; no third-party certification is implied.
