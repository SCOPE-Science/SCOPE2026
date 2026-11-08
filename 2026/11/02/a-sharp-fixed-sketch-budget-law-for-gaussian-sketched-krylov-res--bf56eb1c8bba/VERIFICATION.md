---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Gaussian orthogonal decomposition yields independent chi-square(k) and chi-square(s-k+1) and expected excess k/(s-k-1), diverging for s<=k+1 unless exact residual zero. Chebyshev extremizer weights w_i proportional to 1/(lambda_i |prod_{j!=i}(lambda_i-lambda_j)|) satisfy all GMRES normal equations via barycentric identities. Discrete ratio e^{2a}t/(t+1) selects the asymptotic reserve; comparison bound confines all finite-s minimizers to a fixed finite reserve set, and the exact B_K integer tie is broken by the finite denominator. Independent high-precision tests resolved the numerical near-tie: B_K=1 exactly for K=17+12sqrt(2), and at s=20,100,180 the larger reserve 2 wins. A double-precision test at s=100 initially misclassified this tie; this was diagnosed as precision loss, not a mathematical counterexample.

## originality

PASS

Exact Gaussian regression Student law and classical Chebyshev worst-case approximation are established ingredients. Their combination into an attainable SPD GMRES fixed-row minimax risk and exact eventual integer-reserve law is not stated by the inspected sources; similar paper or routine optimization precedent remains a priority risk.

## value

PASS

For randomized Krylov solvers under a fixed row budget, depth improves Chebyshev contraction but destroys degrees of freedom in the Gaussian regression; the sharp finite-mean boundary and optimal sqrt(K)-scaled reserve give a structural algorithm-design tradeoff, independent of computational runtime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
