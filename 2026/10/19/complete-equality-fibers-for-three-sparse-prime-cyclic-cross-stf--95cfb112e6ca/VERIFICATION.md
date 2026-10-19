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

# Verification and mathematical limits

The analytic proof gives the global result for every prime \(p\ge7\). The crucial external inputs are prime cyclic Fourier uncertainty (Tao/Chebotarev) and Vosper's inverse Cauchy–Davenport theorem for \(5\le p-2\). They identify the necessary five translations and progression support geometry. Exact factorization of two linear sampled Fourier polynomials and one quadratic yields all four required zeros and every coefficient in the claimed family.

A standalone, standard-library-only `verify.py` was run with the file contents present in this package. It directly sums the cyclic STFT over the full group, rather than replaying the analytic row formula, for 962 parameter choices at primes from seven through 61. It verifies two central zeros, one in each adjacent row, no zeros in the two outer active rows, and the exact total support \(\(5p-4\)\). It exhaustively checks support-pair geometry for all three-element subsets at prime orders seven and eleven (752 sharp-five-translation cases).

Observed output:

`VERIFY_OK 962 direct cross-STFT extremizers; 752 equal-sumset supports at p=7,11`

These computations are finite consistency checks, and their floating-point zero threshold is not an infinite proof or an impossibility certificate. They do not establish historical originality, independent validation, or near-minimizer stability.
