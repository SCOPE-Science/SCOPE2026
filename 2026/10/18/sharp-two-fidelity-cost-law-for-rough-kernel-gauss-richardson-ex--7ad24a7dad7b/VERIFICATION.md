---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The proof applies to two distinct noiseless locations, exact saturated cost, fixed ell>0 and unit GP scale. Writing u=1/x, v=1/y, rho=exp(-(y-x)/ell), inversion (or scalar affine GLS) gives J=(u-v)^2/(1-rho^2)+2uv/(1+rho). Set w=(u-v)/C; the feasible range is 0<w<=1-2/C, nonempty for C>2. Then y-x=4w/[C(1-w^2)]. The two elementary bounds 1/s <= 1/(1-exp(-s)) <= 1+1/s give 0 <= J/C^3-(ell/8)w(1-w^2) <= 1/C uniformly, including both endpoint regimes. This proves the finite-budget bound by reciprocation. The leading cubic has its only maximizer at w=1/sqrt(3), feasible for C>=3+sqrt(3); this proves the sharp infimum limit. Compactness and the strict maximum prove the 'if and only if' for all admissible families, via y/x=(1+w)/(1-w). One simulator at x=1/C has scalar covariance and free-intercept variance C^-2. Independent replay: python3 /workspace/reproduction/frozen_checks.py 5; affine minimum-variance weights from the original covariance at two length scales, two budgets and four ratio regimes (including coalescence and y=1). For ell=2, C=10^6, the sharp ratio gave C^3 V=10.39226884551 versus limiting 6 sqrt(3); the endpoint regimes were much worse. The finite checks corroborate but do not prove uniformity. The source checker was inspected, not executed; the recorded 114 checks are not independent attestation.

## originality

PASS

The GRE variance, cost criterion, first-order envelope and use of a rough Matérn family were already established. The supported distinct claim is the evaluated continuous two-location sharp law at unit scale, rigidity of the limiting allocation, and the uniform finite-budget inequality. The inspected grid, integration and multidimensional design problems do not cover that claim. This is a best-of-knowledge judgment, not an exhaustive priority certificate.

## value

PASS

Two fidelities are the smallest nontrivial comparison to one fidelity in the published inverse-cost setting. The exact continuous optimal ratio gives a concrete design, and the sharp cubic law establishes an entire extra inverse-budget power despite rough covariance. The uniform bound and uniqueness distinguish a genuine design benchmark from a pointwise Taylor expansion. This is fixed-scale model variance, not guaranteed simulator error or unrestricted many-point optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
