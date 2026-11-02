---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For q in (0,1), λ,ℓ,c>0 the two action payoffs give G(p)=ℓ(e^{-λq m(p)}-e^{-λ m(p)})-c with m(p)=1-(1-q)p. Differentiating H shows unique strict maximum at m*=ln(1/q)/(λ(1-q)); q<m*<1 is exactly the strict λ interval. A horizontal cost level intersects both monotonic branches precisely when above H(q) and H(1), below H(m*). The resulting G signs are (-,+,-), giving precisely p0 and interior roots as pure/mixed Nash and the claimed one-dimensional replicator stabilities, excluding p=1. At equality/tangency one cannot infer two distinct interior fractions. The exact q=1/2,λ=2,c/ℓ=63/256 factorization y-y²-c=-(y-7/16)(y-9/16) produces p-=0.34664285 and p+=0.84927171. Independently verified rational identity, window, endpoint and interior signs.

## originality

PASS

The criterion isolates Poisson at-least-one-infection saturation as a cause of two interior Nash masking rates in an otherwise homogeneous no-conformity game. The 2022 Altman et al. mask game treats bilinear infection-rate payoffs as main model and explicitly mentions a nonlinear Poisson probability alternative as a future extension; networked mask papers study distinct coupled epidemic-feedback systems. The full 2025 Pei–Xu–Zhang paper was not inspected and institutional access was safety-blocked; material priority risk acknowledged rather than fabricated noncoverage.

## value

PASS

The exact bistability window is a substantively motivated boundary between two local adoption attractors produced solely by infection-probability saturation. It identifies an explicit stable all-unmasked state coexisting with partial masking, establishes necessary and sufficient parameter inequalities and a rationally certified witness. The distinction from the linear infection-rate approximation changes qualitative equilibrium predictions and is mathematically useful for game-model comparison without requiring empirical public-health claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
