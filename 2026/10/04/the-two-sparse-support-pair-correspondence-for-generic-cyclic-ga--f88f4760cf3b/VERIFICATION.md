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

The proof is analytic/algebraic and does not depend on finite enumeration. The bundled `verify_two_sparse_generic_stft.py` provides an exact stress test of the discrete ingredients.

It constructs, for each \(2\le N\le300\), the positive-prime window \(g(j)=p_j\). For every nonzero difference \(s\), it checks with exact rational arithmetic that all ratios \(g(j+s)/g(j)\) are distinct. Since a positive real root of unity is \(1\), this certifies pairwise disjointness of the cancellation cosets for that explicit witness. It also enumerates the character map \(\xi\mapsto-s\xi\pmod N\), verifying exactly \(N/\gcd(N,s)\) image values and constant fiber size \(\gcd(N,s)\). Finally it verifies the shifted support spectra for every difference and the least-prime-divisor extremal formula.

Expected replay tail:

`N_RANGE 2 300`

`RATIO_DISTINCTNESS_CHECKS 8999900`

`KERNEL_FIBER_CHECKS 8999900`

`DIFFERENCE_SPECTRA_CHECKS 44850`

`VERIFY_OK`

Limits: the computation checks finitely many orders and is not an infinite certificate. It does not test support size at least three and does not classify exceptional windows.
