---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For positive-cell protective balanced n-per-arm tables (a,b), exactly 1≤a<b≤n−1, RR=a/b and OR=a(n−b)/[b(n−a)]. For two tables (a,b),(c,d), compare signs of ad−bc and ad(n−b)(n−c)−bc(n−a)(n−d), all denominators positive; a strict reversal exactly when their product<0. Direct independent Fraction exhaustive pair enumeration gives 0 reversals for n=2,3,4 and exactly one for n=5: (2,3) and (3,4), RR 2/3<3/4, OR 4/9>3/8. n=4 has weak mismatch via OR tie (1,2),(2,3). The exhibited all-n≥5 family A=(n−3,n−2), B=(n−2,n−1) has RR ordering by difference 1 in cross products and OR sign numerator n(n−4)>0. The infinite part is analytic, not extrapolated from finite enumeration.

## originality

PASS

Best-of-knowledge baseline-risk-dependent divergence between RR and OR is classic and is not claimed as new; Zhang–Yu, Davies et al., and Cummings explain the mapping and interpretation. The exact finite all-positive balanced sharp strict-reversal onset, unique first pair, weak mismatch onset and all-n realization are not stated in the inspected sources. The arithmetic is elementary; potential textbook/teaching counterexamples remain a material risk, but the sharp constrained boundary is a separate precise statement.

## value

PASS

Cross-study rankings of apparent protective effects can change by choosing OR versus RR at different baseline risks, a concrete interpretation issue. The result pins down the first possible fully positive 2x2 balanced clinical configuration, detects weaker order ties one size earlier, and exhibits persistence for all larger sizes. Despite low computational complexity, the exact natural threshold and unique witness are mathematically motivated rather than an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
