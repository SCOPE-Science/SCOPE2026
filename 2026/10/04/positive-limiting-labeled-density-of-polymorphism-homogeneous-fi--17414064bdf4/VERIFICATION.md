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

`verify.py` performs the following independent finite checks.

1. It enumerates every integer partition of \(a\) for \(1\le a\le8\), interprets each partition as an abelian \(p\)-group type, and computes its automorphism order from the standard partition formula.
2. For \(p\in\{2,3,5,7\}\), it sums reciprocal automorphism orders over all partition types and checks equality with \(p^{-a}/\prod_{j=1}^a(1-p^{-j})\).
3. It independently computes the reciprocal mass of homocyclic types by ranging over divisors \(m\mid a\) and using \(|\operatorname{GL}_m(\mathbb Z/p^{a/m}\mathbb Z)|\).
4. It checks that the quotient of those two masses equals the displayed closed formula for \(\rho_p(a)\).
5. Whenever the labeled set has at most 256 points, it multiplies both masses by \((p^a)!\) and verifies that the resulting counts are integers.
6. Through \(a=24\) for \(p=2,3,5\), it checks the explicit bound that the contribution from divisors \(m\ge2\) is at most \(\tau(a)p^{-a}\).

A successful replay prints `VERIFY_OK`, 101 exact checks, the first six density values for \(p=2,3,5\), and numerical approximations to the limiting products.

The verifier is finite and does not by itself prove the infinite limiting statement; that limit follows analytically from the explicit remainder bound and convergence of the infinite product. The verifier also does not assess literature priority.
