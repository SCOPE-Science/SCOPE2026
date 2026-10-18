---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Read actual RESULT.md and verify_spiral.py. Composition diagonalizes on the given orthonormal monomials with eigenvalues (ae^{iθ})^n; its numerical range is their attainable probability barycenters. Let k=floor(π/θ), t={π/θ}. The most negative imaginary eigenvalue M=a^k max_{j≥1}a^j sin((j−t)θ), yielding upper bound rho≤M, uniformly M/(θa^k)=H_a(t)+O_a(θ²) by sin remainder and exponentially bounded j³a^j. A triangle of actual eigenvalues at indices 0, floor(π/(2θ)), and k+j* contains zero; stable edge-distance inequalities yield rho≥M/(1+a^k). The middle vertex ratio dominates θa^k since a^(p-k)/θ→∞. A finite j* bound follows from j a^j decay. Thus rho=θa^(π/θ)(a^(−t)H_a(t)+O_a(θ²+a^(π/θ))), uniform t; discrete differences give ceil-maximizer and period seam; the triangle absorbs the eigenvalue tail to prove closed finite polygonality for sufficiently small θ. Independent stable-trigonometric checks covered a=1/2,3/4 small θ, not continuum proof.

## originality

PASS

General convex-hull numerical range theory of composition operators is explicitly prior. Available indexed record and accessible abstracts do not exhibit the quantitative centered inradius phase law. However older Matache/Fatehi operator papers and directly related 2026 Dirichlet article were not available in full; any exact spiral polygon formula could dominate the claim. Conditional O PASS rests on mathematical distinction and explicit residual risk, not merely absence of search hits.

## value

PASS

The largest closed origin-centered disk in a canonical contracting composition-operator numerical range has a meaningful collapse scale as the phase tends to zero. Its exact exponential rate and nonconstant fractional-phase prefactor distinguish subsequential limits and are quantitatively stronger than qualitative interior inclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
