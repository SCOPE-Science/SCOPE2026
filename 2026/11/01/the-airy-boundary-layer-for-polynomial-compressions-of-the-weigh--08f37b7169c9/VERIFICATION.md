---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

Weighted Bergman moment ratios give b_n=sqrt((n+1)/(n+p+1)), p=alpha+1>0; rotation-invariance and convexity reduce the finite compressed shift numerical radius to the maximal eigenvalue of the symmetric Jacobi b_n/2 matrix. With μ_N=1−b_{N−1}, exact edge-energy identity is 1−r_N−μ_N=1/2Σb_n|Δu_n|²+Σ[V_{N,n}−μ_N]|u_n|². Positivity of b_n increments and the last-index boundary barrier localize the ground vector to j=N−n=O(N^{2/3}); rescaled discrete Dirichlet forms converge to q_p(φ)=1/2∫(|φ′|²+p x|φ|²). Smooth compact trials give limsup, energy tightness, boundary control, H1 interpolation compactness and weak lower semicontinuity give liminf and L2 eigenvector convergence. The lowest half-line Dirichlet Airy eigenvalue a1 p^{2/3}/2 and normalized Ai profile follow by scaling. μ_N=p/(2N)+O(N^-2), producing the N^-4/3 term. Independent finite Jacobi eig tests at p=0.5,1,2,4 showed scaled terms approach Airy values, but do not prove the limit.

## originality

PASS

Gorkin–Partington treats compressions of the shift on Hardy model spaces (fixed p=0 regime), while the closest SCOPE Airy result has q↑1 damping of an infinite periodic/geometric shift, not N→∞ truncation of algebraically weighted Bergman shifts. Lukic studies infinite Jacobi spectral edges rather than this moving finite top eigenpair and Dirichlet Airy coefficient. Best-of-knowledge technical specificity survives; general Jacobi turning-point theorems may imply this as a special case.

## value

PASS

The explicit N^-4/3 correction and normalized Airy maximizing polynomial describe a natural sharp spectral boundary transition between Hardy and fixed weighted Bergman finite sections, giving a nontrivial quantitative eigenvalue/eigenvector theorem beyond routine norm estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
