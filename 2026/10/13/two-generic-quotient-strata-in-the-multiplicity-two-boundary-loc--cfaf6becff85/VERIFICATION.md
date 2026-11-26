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

Reconstructed the two constructible kernel families over C, not a decomposition of the boundary. On a conic in a plane missing p the three entries of O(-4) -> O(-2)^3 are a basis of binary quadrics. By Serre duality the induced H^1 map is an isomorphism, so the rank-two cokernel has degree -2 and no sections and splits as O(-1)^2 on P^1. Its nonzero maps to the degree -1 target are onto and are parametrized modulo scalars by P^1. On a line missing p the restricted presentation is (x,y,0), giving O + O(-1) and a unique map up to scalar to O_L(-1). Disjoint supports let the two line maps be rescaled independently, giving exactly one kernel for each unordered pair. The hull is determined by the common zero p (different bases of the three linear forms give isomorphic hulls), and the kernel recovers the hull and quotient by double duality and the quotient map up to equivalence; hull automorphisms are scalar by stability. For algebraicity of the conic count one can work over the open 11-dimensional space of parametrized degree-two embeddings of P^1: the degree -1 target then exists in family, and constant rank Hom with vanishing H^1 gives a relative P^1. Adding p off the plane and forgetting the parametrization (fibers PGL2 of dimension 3) gives dimension 12 and an irreducible constructible image. Ordered skew lines and p form an irreducible open parameter base of dimension 11; unordered pairs only remove a finite ordering. In both cases E agrees with the reflexive hull off codimension two, is slope-stable by inclusion with equal slope, and the pure quotient has ch(Q)=2H^2-4H^3 by RR. Subtracting from ch(F) yields c(E)=(-1,3,7). The computation neither needs nor proves that all quotients in the boundary have one of the two displayed types.

## originality

PASS

The exact two dimensions and the difference in fibers of the quotient-map construction were not covered by the strongest compared statements. The proof uses existing inputs, but the restriction behavior of the specific non-locally-free hull is essential; neither the dimensions of quotient moduli nor ambient smoothness alone gives the dimensions of these images.

## value

PASS

Gives exact structural dimensions of the families arising over the two generic degree-two target types in a named, unresolved moduli boundary, with a geometric explanation of the difference (a genuine pencil of distinct conic kernels versus a single skew-line kernel). This distinguishes contributions to the boundary that a target dimension count alone would conflate, and supplies reference strata for studying closures and incidence degenerations. It does not claim to settle the full boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
