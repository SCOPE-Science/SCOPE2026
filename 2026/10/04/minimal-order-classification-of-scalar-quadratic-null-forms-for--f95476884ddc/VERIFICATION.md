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

The accepted claim is the restricted scalar quadratic classification stated in `RESULT.md`.

## Algebraic checks
For a polynomial symbol \(b\), the restrictions \(b(t,t)\) and \(b(-t,2t)\) are one-variable polynomials. Vanishing for every positive integer forces each restriction to vanish identically. Therefore \(k-\ell\) and \(2k+\ell\) divide \(b\). Symmetry forces a second factor \(k-\ell\) and the additional factor \(k+2\ell\). The three distinct line factors are coprime, giving
\[
(k-\ell)^2(2k+\ell)(k+2\ell)\mid b(k,\ell).
\]
The factor is symmetric and invariant under \((k,\ell)\mapsto(-k,-\ell)\), so the quotient inherits the stated symmetries. The converse is direct. Its degree in \(k\) is \(4\), and its degree in \(\ell\) is \(4\); multiplication by any nonconstant quotient raises at least one of these input degrees. Thus the differential order is at least \(4\), with equality only for a constant quotient.

The source differential expression has symbol
\[
2(k+\ell)^4-7k\ell(k+\ell)^2-4k^2\ell^2,
\]
and exact expansion gives
\[
2(k+\ell)^4-7k\ell(k+\ell)^2-4k^2\ell^2
=(k-\ell)^2(2k+\ell)(k+2\ell).
\]

## Normal-form support check
The general extraction formulas in arXiv:2608.24376v1 show that quadratic contributions to the cubic coefficients use only the critical mode \(m\) and the second harmonic \(2m\). The proof of Example 6.4 in arXiv:2609.22779v1 shows that vanishing at \((m,m)\) eliminates the added quadratic forcing and vanishing at \((-m,2m)\) eliminates the only added outer interaction that can project from the second harmonic back to the critical mode. The zero-output channel is annihilated by \(K\); the \(3m\) channel misses the critical projection. Hence the perturbation leaves all four cubic extraction coefficients unchanged.

## Boundary and limitation checks
The proof requires the two symbol cancellations for every critical integer \(m\), not merely one fixed \(m\). It assumes a polynomial constant-coefficient symmetric scalar bilinear operator and simultaneous-sign reflection parity. It does not exclude lower-order invisible perturbations using a different vector or cancellation mechanism. No existence, uniqueness, or classification claim is made outside this domain.
