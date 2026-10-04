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

The proof is analytic. The accompanying checker uses exact integer and rational arithmetic.

It enumerates the complete permutation sample space through \(N=8\), computes the descent-indicator covariance matrix exactly, and checks every entry against (1).

For every dimension through \(k=80\), it verifies the even-Fibonacci determinant recurrence, multiplies the proposed inverse by the tridiagonal matrix to obtain the identity exactly, and checks strict positivity of every inverse entry.

For every tested pair it also verifies the exact rational identity obtained by squaring the displayed linear partial-correlation formula.

Finite replay does not prove the all-\(N\) theorem; the universal proof is the symmetry calculation and continuant derivation in `RESULT.md`.

Independent audit has not been performed.
