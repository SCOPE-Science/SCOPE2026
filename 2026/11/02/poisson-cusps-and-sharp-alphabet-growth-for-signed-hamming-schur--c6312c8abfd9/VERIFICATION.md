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

Run `python3 check.py` in the directory containing the embedded files. The checker uses only Python's standard library. It independently generates all graph vertices and adjacent pairs for eleven bounded Hamming graph cases, constructs an integer tensor eigenbasis, and verifies the signed matrix action at every coordinate. It then checks \(3392\) exact rational comparisons of the independent spectral-trace and binomial-boundary formulas and \(3328\) strict increasing-alphabet comparisons. Four independently stated small exact values are also checked.

Observed output:

`SIGNED_HAMMING_SCHUR_CHECK_OK exact_spectrum_mass_pairs= 3392 strict_alphabet_steps= 3328 direct_tensor_eigenmodes= 346 small_exact_values=4`

The proof, rather than finite arithmetic, establishes the exact norm, all-parameter monotonicity, the coupled Poisson limit, and Gaussian asymptotics. The real norm agrees with the complex norm because the extremal witness is real orthogonal and the factorization upper bound is real. The historical comparison is subject to the explicitly stated limitation concerning inaccessible 1999 bicirculant full text.
