---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For p>1 and a,b>=1, weighted AM-GM shows w=lambda z1^a z2^b maps open ellipsoid inside unit disk and w=1 on boundary occurs on gcd(a,b) phase circles. The full, possibly disconnected, kernel H of the torus character (a,b) acts unitarily; Haar averaging a total-degree<=L multiplier removes every monomial except nonnegative integer multiples of (a,b), so unrestricted Q reduces to P(w) with degree <=floor(L/(a+b)). A residual polynomial e(w) of degree N+1 has e(1)=1; orthogonality gives diagonal weights M_n and weighted Cauchy-Schwarz exactly achieves inverse S_(N+1), including explicit optimizer. Stirling establishes M_n~sqrt(2*pi*p*a*b)*(a+b)^(beta-3/2)*n^(beta-1/2), proven for all fixed parameters, giving beta<=3/2 cyclicity and three error regimes. Bounded coordinate multipliers transfer approximation of 1 to cyclicity. On boundary, every probability measure has forced (an,bn) moments lambda^-n; Haar over full H suppresses others and attains exact energy S_infty, hence kernel capacity 1/S_infty. Independent numeric asymptotic checks at four parameter tuples supplement analytic proof; exact kernel normalization and disconnected H are essential.

## originality

PASS

The ellipsoid paper defining the spaces explicitly leaves one-dimensional boundary zero sets as Open Problem 2; ball cyclicity threshold 3/2 and diagonal reductions are known, but neither gives the exact nonball p,a,b,beta total-degree error and capacity. Novelty does not rest on numerical threshold 3/2 alone.

## value

PASS

A parameterized natural family of zero-free ellipsoid polynomials with one-dimensional boundary zero sets addresses a specific open case for Poletsky-Stessin coefficient spaces. The exact unrestricted ideal distance, optimizing polynomials, rates and capacity give independently useful analytic invariants even though the ball threshold is familiar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
