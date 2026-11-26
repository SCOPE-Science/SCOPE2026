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

For f(x)=||x||²/2 and known f*=0 the LCD3 localization set is the C-ellipsoid centered at x−C⁻¹x with squared C-radius xᵀC⁻¹x−||x||². C-metric projection gives the frozen square-root step, also when the radius is zero. C≼I≼C+(1−1/κ)I establishes admissibility. If m and q are the first and second moments of B=C⁻¹ in the squared spectral weights of x, the exact ratio is 1−2αm+α²q. The chord bound q≤(κ+1)m−κ is sharp at every m in [1,κ] via a mixture of eigenvectors for 1 and κ, which are present for each allowed C. For u=√(1−1/m) substitution gives κu²(1−u)/(1+u); its derivative after division by κ is 2u(1−u−u²)/(1+u)². Hence the maximizing u is the stated clipped inverse golden ratio and the branch switches at κ=φ. For κ=1 the iterate is zero; at κ=φ the branches agree; above φ the envelope is κ(5√5−11)/2, attaining one exactly at (11+5√5)/2. Below φ the product κF(uκ) increases to a value less than one. The endpoint mixture with weight (φ−1)/(κ−1) on κ gives equality in the upper branch, including a strict witness at κ=12. The result concerns one step under the absolute eigenvalue normalization, not convergence or arbitrary scaling. The frozen verification notes and script were inspected, not executed; the sharp proof is analytic.

## originality

PASS

The exact projection rule and the Hessian-matched Newton special case are known. The supported distinct result is the attainable all-direction envelope and the resulting monotonicity frontier for a separately chosen admissible lower matrix. The closest indexed sharp Polyak-step frontier has a different step law; no inspected source gives or entails the present envelope as a stated specialization. This is a scoped best-of-current-knowledge decision.

## value

PASS

The objective can increase even when the true Hessian is the identity and both quadratic support assumptions hold. The sharp frontier distinguishes when using the lower-curvature metric is and is not safe for one-step descent, gives explicit worst-case directions at every condition number, and quantifies unbounded one-step loss. It is stronger and more useful than an isolated counterexample or the known exact-Hessian Newton case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
