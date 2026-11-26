---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For a full-row-rank gradient G=AO, the first updated gradient is BO with OO^T=I and B=A−(tr A/tr H)H symmetric and traceless. Its two eigenvalues are opposite, so its Gram matrix after multiplication by O is a scalar identity, including the zero case. On the nonzero equal-singular-value manifold the nuclear-scaled polar direction is 2G. The multiplier C=I−2H/tr H preserves that manifold because C^2=ρ^2 I; it commutes with H, giving the stated error and objective identities. G1=0 iff A=(tr A/tr H)H, equivalently the initial error is a positive multiple of a row isometry on the full-rank stratum. At rank one the canonical polar direction scales to G, and the invertible multiplier I−H/tr H gives the claimed slower factor along the low-curvature eigenspace. Nonterminating rank-two starts approach that rank-one start because the nonzero equal-singular-value termination set cannot accumulate there.

## originality

PASS

The optimizer, the isotropic rank-two finite-identification mechanism, and general spectral convergence are not new here. The supported distinct claim is universal one-step identification for anisotropic two-row curvature and the exact nonterminating GD tail (with its termination and rank-boundary characterization). The strongest available matching statement is isotropic and does not encompass that anisotropic dynamics.

## value

PASS

The result replaces an asymptotic bound for a nonlinear optimizer by an exact identification time and complete linear tail for arbitrary full-rank two-row starts, including noncommuting polar and curvature factors. The rank-one discontinuity explains why this sharp tail rate cannot be transferred across rank, and the termination criterion identifies the exception rather than obscuring it in a worst-case bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
