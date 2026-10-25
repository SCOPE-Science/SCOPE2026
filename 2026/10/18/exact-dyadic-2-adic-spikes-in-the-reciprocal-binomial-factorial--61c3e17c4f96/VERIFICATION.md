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

The claim is exactly for N=2^m,m>=4, with v2(2)=1, and b_N=sum_{k=1}^N2^k/k, a_N=N!2^{-N}b_N. The two infinite sums sum2^j/j and sum2^j/j^2 vanish in Q_2: log(-1)=0, and the dilogarithm reflection follows by differentiation on v2(z)>=1 and eval z=2. For H0=sum2^{j-1}/j^3, j=4 has unique term valuation -3 (j=2 and 8 valuation -2). For N=2^m the correction terms -N*2^{j-1}/(j^3(j+N)) have valuation >=-1: exhaust v2(j)<m,=m,>m and for j=2^m u use v2(u+1)<=u. Hence v2(H_N)=-3, b_N=-2^{N+1}N^2 H_N, v2(b_N)=N+2m-2; Legendre v2(N!)=N-1 gives v2(a_N)=N+2m-3. Checked first dyadic exceptions m=1,2,3 and independent exact integer recurrence vs factorial convolution for m through 9. No arbitrary-n or other-prime theorem.

## originality

PASS

Farhi's factorial-convolution identity and 2022 integrality are prior; the claim is not that these representations are new. Dubickas's 2024 inequality is sharp at 2^k-1, not at 2^m, and its lower bound is strictly weaker than the claimed exact valuation for m>=4. Full-text searches in the 2026 Kruchinin generating-function preprint identify no valuation statement in the inspected parts. Best-of-knowledge originality attaches to the explicit infinite sharp dyadic subsequence, with possible unindexed exact identities a residual risk.

## value

PASS

For a natural reciprocal-binomial factorial convolution connected to Genocchi integers, the unexpectedly large 2-adic divisibility spike on the entire unbounded 2^m subsequence is a meaningful exact arithmetic invariant; proving its sharp exponent requires nontrivial p-adic analytic cancellation beyond known lower bounds. This is more than a small data extension and identifies a precise structural infinite family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
