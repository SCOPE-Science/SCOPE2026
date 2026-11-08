---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For k(s,t)=min(s,t)-st and noiseless two draws, integrated conditional Brownian-bridge variance is sum of three cubed gaps divided by 12, including ties. The exact quadratic functional S=6∫_{0<u<v<1}(v-u)(1-mu((u,v)))^2 du dv is convex; equality for zero-total signed perturbations fixes interior law. Proposed density 2(1+r²)/[1+(2x-1)²]^2 on central support, r+(1+r²)atan r=1, has constant potential on support and U=c+(3/2)dist² outside. This global Euler obstacle and convexity show unique minimizer among all Borel measures, excluding endpoint redistribution. Independent scipy quadrature verified normalization, potential at nine interior/exterior points, exact optimum 0.0160494871749149 versus uniform 0.025; these tests do not prove all-measure uniqueness. Supremum is inside expectation; no correlated-design conclusion.

## originality

PASS

PASS qualified: Santin 2022 Theorem 5 proves optimal deterministic equally spaced nodes for sup pointwise power, not the iid sampling-law functional. Briol et al. study sampling distributions and supremum-before-expectation error rather than E of squared fixed-node worst-case error. Explicit compact support density and all-measure uniqueness not found in these inspected theorems.

## value

PASS

Selecting random-node distributions is a natural kernel-quadrature design problem. For the smallest genuinely random two-node case a unique support-truncated design attains a 35.8% risk reduction relative to uniform sampling; exact obstacle and all-Borel uniqueness provide a mathematically useful benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
