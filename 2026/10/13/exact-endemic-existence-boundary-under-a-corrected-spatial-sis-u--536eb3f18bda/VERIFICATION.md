---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The source assumes d_S<d_I and a bounded smooth Neumann domain, positive Hölder β,γ, total N and c=N/|Ω|≥γ(x)/β(x). Set w=cβ−γ≥0. If w≢0, the infected linearization L=d_I Δ+w has strictly positive principal Neumann eigenvalue by testing the constant function, giving R0>1 and existence by the source supercritical theorem; the corrigendum uniqueness proof handles the same pointwise regime. If w≡0, the linearized operator is pure Neumann diffusion and R0=1. The exact reduced steady equation is d_IΔI+DβI(q−I)=0 where D=d_I/d_S>1, q=(D−1)mean(I)/D. Multiply by I−q, integrate Neumann by parts, obtaining −d_I∫|∇I|²−D∫βI(I−q)²=0. Positivity forces I≡q, then q=(D−1)q/D implies q=0, excluding an endemic state. A separate algebraic identity check corroborates the sign factors. No numerical PDE computation is used.

## originality

PASS

The source corrigendum explicitly contains the weak inequality and the false R0>1 inference. Its uniqueness result is not rejected as an at-most-one assertion, but the positive-existence sentence needs a strict-somewhere hypothesis. The exact critical/elevated dichotomy is not formulated there. General epidemic threshold results are substantial background and may imply the critical nonexistence by other routes, so the novel component is the exact correction of this printed inference rather than a new universal threshold theorem.

## value

PASS

The error occurs inside an already published mathematical corrigendum to an epidemiological PDE theorem: a weak pointwise condition is used to infer strict supercriticality and existence. Isolating the everywhere-equality threshold and proving nonexistence changes the precise existential meaning of the corrected statement. The issue is more specific than a generic trivial zero check, because the source explicitly imports an incorrect threshold implication into a revised uniqueness proof; clarifying existence versus at-most-one is mathematically useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
