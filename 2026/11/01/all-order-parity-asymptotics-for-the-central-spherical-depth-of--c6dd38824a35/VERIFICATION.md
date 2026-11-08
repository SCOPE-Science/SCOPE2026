---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Checked polar sec² angular density normalized on each facet-normal period and the exact Fourier depth formula, with sine parity. Uniform two-integration-by-parts control yields b_{k,n}=(-1)^k[2/(k²n²)+(2π²/k²-16/k⁴)/n⁴+O(k^-2 n^-6)]. Squaring and summing with Dirichlet beta(5), beta(7) gives 5π⁴/192 and 7π⁶/720 at orders n^-5 and n^-7, confirmed independently by exact rational beta arithmetic and high-precision integral Fourier values n=5,9,15,21 with shrinking n^-9 errors. Analytic even-power Taylor coefficients with summable k^-2 remainders justify arbitrary fixed-order odd inverse-power expansions. Even n is centrally symmetric and exactly 1/2.

## originality

PASS

An exact Fourier formula and mod-four sign for regular polygon depth were already present in 2025, and triangle formulas are known; here the original quantitative contribution is the rigorously uniform-in-mode all-orders odd-n asymptotic hierarchy with first two nonzero exact coefficients.

## value

PASS

Central spherical depth measures a natural geometric containment probability. The fifth-order cancellation rate and exact higher coefficient series provide sharp large-n benchmarks distinct from the earlier Fourier expression and parity sign alone; uniform-in-mode analysis is the substantive work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
