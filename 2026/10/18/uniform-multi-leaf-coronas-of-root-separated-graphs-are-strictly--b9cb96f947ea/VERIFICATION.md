---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Exact independence-set split gives I(H∘overline(K_m),z)=(1+z)^(mn) I(H,z/(1+z)^m) and, when core roots are -a_j<=-1/4, factors as (1+z)^(m(n-alpha)) times ∏(z+a_j(1+z)^m)/∏a_j. For each m>=1,a>=1/4, roots of (1+z)^m+z/a begin close to -1 for a large and cannot cross the imaginary axis: z=iy (y>0) forces mθ=3π/2+2πk and a=sinθ cos^(m-1)θ. m<=3 admits no such phase; for m=4..6 the first admissible angle yields a<1/4; for m>=7 the GLOBAL maximum (m-1)^((m-1)/2)/m^(m/2)<=sqrt(6^6/7^7)<1/4 excludes all crossings. Conjugation handles negative y; zero is not a root. Path and cycle recurrence supplies exactly real roots -1/(4cos² θ)<-1/4 for all allowed orders. Independent approximate roots for 75 (m,a) scalar factors and exact elementary inequalities corroborate, not replace, the continuity proof.

## originality

PASS

Best-of-knowledge PASS for the scalar all-m Hurwitz lemma and its simultaneously m-leaf-at-each-original-vertex path/cycle families. Brown–Cameron (2018) contains classical corona/graph-star identities and strict/weak stability results for iterative single-whiskering, not the same operation after m>=2 leaves are added to original vertices. Hibi–Kara–Vien (2026) Proposition 3.1 contains general simultaneous whiskering polynomial enumeration, which is not new here, and Theorem 3.2 covers symmetry rather than half-plane roots. Zhang–Tu 2026 establishes spider stability, but multi-leaf path coronas have >=3 branching vertices for n>=5, so that theorem cannot cover them. The spider paper was only accessible by abstract; OAuth/Oxford returned VPN disconnected. Unknown more general stability theorem remains risk.

## value

PASS

Strict stability of independence polynomials is an active graph-polynomial problem with counterexamples among trees. This root-geometric sufficient condition transfers a simple quantitative core-root barrier into infinite stable caterpillar families with arbitrarily many branching vertices and non-tree cycle coronas, all leaf multiplicities m>=2. The scalar half-plane no-crossing argument is a reusable structural mechanism and exceeds the existing spider family; one does not rely on the old whiskering identity alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
