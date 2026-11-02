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

Run `python3 CHECK.py` with Python 3 standard library. Its output is `VERIFY_OK 106 checks`, followed by two degree-dependent coefficient pairs. The program independently computes scattering through matrix inversion and Fourier eigenvalues, checks permutation routing across sampled interpolation values, and numerically tests the leading optimized leakage for ten small degrees.

The exact proof is in `RESULT.md`. Finite tests support internal consistency but do not establish strict inequalities for all degrees, exact global optimizer uniqueness, or exhaustive publication originality. The proof covers those mathematical issues analytically; independent scientific review has not yet occurred.
