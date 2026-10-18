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

# Verification and limits

The analytic verification is contained in the Gram factorization and the determinant factorization in `RESULT.md`. The finite positive Toeplitz operators are \(E^*E\), with the same two nonzero eigenvalues as the explicitly written \(EE^*\) matrices. At the critical radius the normalized Gram matrices are related by a sign-diagonal unitary.

Execute `python CHECK.py` with Python 3, NumPy, and SymPy available. The script checks three exact symbolic identities and 1,296 numerical diagnostics of Gram spectra and Schatten comparisons, including the phase boundary. Finite numerical diagnostics do not prove the infinite-parameter theorem, but its exact two-by-two proof does. The scope excludes arbitrary signed measures and measures with more than two support points.
