---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The L² boundary-trace reduction works in both directions by Fourier–Poisson representation and convexity of the closed sector. In the real L² pairing, the two independently chosen coefficient phases give K=2 exp(−iτ) cos(nt+δ). The pointwise projection residual is polar to the cone and orthogonal to the projection, so the exact maximum for a fixed K on the unit cone is ||PβK||₂, attained only by positive multiples of the projection for nonzero optimum. Each cosine half-wave has squared mass 1/4. For 0≤τ≤π/2 the squared norm is u²+v², where u=1 up to β and then cos(τ−β), and v=max(0,−cos(τ+β)). If β<π/4, the one-wave exterior branch is strictly below 1 and the two-wave branch has value 1+cos(2τ)cos(2β)<1. If π/4<β<π/2, the portion with u=1 is at most 1+cos²(2β)<1−cos(2β), and on the remaining branch the latter bound is attained only at π/2. At β=π/4 all phases maximize; at β=π/2 use u²+v²=1+sin²τ directly, and β=0 is the one-ray case. This proves the stated constants and all equality cases by the equality condition in Cauchy–Schwarz and reflection symmetry. The bundled trace tests were inspected, not executed; no limiting or exhaustiveness claim depends on them.

## originality

PASS

The unrestricted coefficient estimate, dual cosine test, and rotated-cosine equality examples are known. The supported distinction is the sector-dependent sharp law for the specified harmonic L² problem, including the sharp whole family of optimizers at the critical sector. Neither the closest published coefficient theorem nor the closest indexed equality classification supplies that constrained result.

## value

PASS

The sector is a natural quantitative restriction interpolating from a nonnegative real trace to a half-plane. The result tells when coefficient maximizers require both signs of the dual cosine and exactly which boundary rays they occupy. The full critical equality family, not simply an improved numerical constant, identifies where support ceases to be rigid. This is useful information for sector-constrained harmonic coefficient problems even at a single exponent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
