---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Exact uniform arrangement counting gives the mixed falling-factorial expectation E C(U,r)C(K,s)=C(n-m,r)C(m,s)(m)_s/(n)_{r+s}, including r=0,s=0 conventions. Expanding E(1+z)^W from these finite moments gives coefficients relative to exp((mu+nu)z) with mu=(n-m)/n and nu=m²/n. For m in [a sqrt(n), b sqrt(n)] and r+s<=n^{1/8}, the two factors (m)_s/m^s contribute -s(s-1)/m, while other falling factors and second-order errors are O((r+s+1)^4/n). For the complementary high coefficients, factorial majorants plus a superfactorially small r>n/2 tail control the full entire generating polynomial uniformly on fixed complex disks; this justifies summing the local expansion, not merely pointwise moments. Thus F_n(z)=e^{lambda_n z}(1-m³ z²/n²)+O_R(n^-1). Substituting z=w-1 and applying Cauchy on |w|=2 gives an ℓ1 probability remainder O(n^-1), yielding Poisson second differences with sign from (w-1)². At lambda=2, Δ²q(j)=q_2(j)(j-1)(j-4)/4; its ℓ1 norm is 10e^-2/3, giving 5e^-2/3 after TV half-factor. Independent exact-rational factorial inversion for (n,m)=(6,2),(9,3),(16,4) verifies positivity, total mass, mean and signed correction trend, but these finite numbers do not prove uniform analytic error. Only one repeated symbol at m~c sqrt(n) with c in (0,infty) is proved; no result for general multiset profiles.

## originality

PASS

The full original Stark 2026 arXiv text was read, notably §2 factorial-indicator moments, §3 Theorem 2/Corollary 1 upper bound O(n^-1/2), and §4 Theorem 4/specific square-root example lower bound n^-1/2/log²n. It does not supply the signed total-distribution correction or constant 5e^-2/3; the present factorial transform plus complex-disk ℓ1 remainder closes that gap. Poisson–Charlier is established general technology, not claimed novel, and stronger general mod-Poisson expansions may furnish an alternate derivation.

## value

PASS

An existing primary paper explicitly singles out the one-heavy-symbol square-root example because its upper and lower Poisson errors fail to match. This result supplies a nonzero exact leading error and an entire signed ℓ1 asymptotic profile for a natural one-parameter critical family, closing a motivated quantitative gap. It uses a standard approximation framework but performs nonroutine exact mixed-moment summation with a uniform analytic remainder. The result is neither an arbitrary finite computation nor novelty based merely on applying the name Poisson–Charlier.

The dated certificate retains the supplied scientific assessment, sources and limitations.
