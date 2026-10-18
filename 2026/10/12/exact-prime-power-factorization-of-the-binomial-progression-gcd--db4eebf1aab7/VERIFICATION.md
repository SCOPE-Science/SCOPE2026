---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Newton interpolation at q=1..k+1 for F(q)=binom(qk,k) of degree k with F(0)=0 and F(1)=1 gives D(k)|(k+1), eliminating other primes. The source local criterion treats a≤t as exponent 0; for a>t, Kummer carries at j≤a give a−s when s=ν_p(q−1)≤a, and disjoint high boundaries a+t+1≤j≤a+s supply s−t when s>t, forcing every binomial valuation≥a−t. For b=1 the witness q=p produces exactly a carries. For b>1, u=b−p^t lies in (0,p^a) with p∤u, q=1+p^a u is in range; the base-p digit-sum identities for b−1, uk and their sum give exactly a−t carries. These arguments address all k, each p and all q, not just finite samples.

## originality

PASS

PASS best-of-knowledge for full quantitative p-adic gcd factorization beyond the published Boolean gcd-one criterion. The highly relevant original paper’s full text was inaccessible in this run; a concealed stronger proposition is a specific residual priority risk, not proof of coverage.

## value

PASS

The exact integer gcd and an explicit valuation-attaining factor are a natural complete refinement of a recent conjecture-resolution: quantitative prime-power content can matter even when D(k)≠1, and this theorem supplies it uniformly rather than merely classifying unit cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
