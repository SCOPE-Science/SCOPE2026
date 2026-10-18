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

# Verification of the exact ordinal-frequency covariance spectrum

The accompanying `verify_spectrum.py` is a standalone Python 3/SymPy certificate. It enumerates all possible rank orders of four through seven independent continuous observations, constructs all 24-by-24 overlap matrices as exact rationals, and computes the characteristic polynomial of the resulting integer matrix. It checks the proposed factorization by an exact polynomial identity, verifies that the one constant and five independent three-point flow differences lie in the kernel, and verifies a finite-size covariance increment identity.

The enumerations cover the entire finite set of relative orders required for the exact covariance matrix, rather than a sampling experiment. The extension from the finite covariance identity to all sample lengths and the limiting normal distribution are proved in `RESULT.md`. The certificate does not analyze ties or dependent data, nor does it verify earlier historical priority or constitute independent audit.
