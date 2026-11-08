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

On a strict projection active face with k free and b=N-k clipped coordinates, KKT gives Q_s(x)_i=[x_i-lambda]_0^1. Tangent input perturbations v have sum zero and derivative v_i+sum_B v_j/k on free indices; clipped derivatives vanish. The restricted cube section bound with v_i=1 gives the exact face modulus 1+min(b,k-2)/k for k>=2, zero for k=1. Explicit zero-sum sign vectors attain both branches. Maximizing over k gives 2-2/(floor(N/2)+1); piecewise affine segment integration gives global upper bound. For each interior mass s, either s<k or s>b allows an active face with all b bound outputs equal 0 or 1, and a strict-face tangent witness attains the bound. For N=2 the feasible interior identity achieves 1. Independent exact vertex enumeration over 36 (N,k) cases N=2..9 and the explicit N=4 s=2 witness factor 4/3 corroborate the unrestricted argument.

## originality

PASS

The 2026 limiter paper derives Euclidean metric nonexpansiveness; the 2015 capped-simplex paper supplies KKT and computational projection, both acknowledged. The exact l-infinity modulus restricted to equal-mass tangent hyperplane requires a distinct active-face operator-norm optimization and every-mass equality construction. Resultary sharp projection results on cross-polytopes or Euclidean balls use distinct domains and do not dominate this claim. A general older polyhedral-projector sensitivity theorem might supply this by specialization.

## value

PASS

Gives the first exact dimensional frontier for maximum-norm amplification by a conservative limiter, distinguishing Hilbert nonexpansiveness from maximum-norm sensitivity and identifying the smallest expansive four-cell example. A sharp optimizer for every mass is a natural complete quantitative classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
