---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The zero-sum polar has one bounded edge-potential difference per tree edge. All 2^(a+b+1) polar vertices are signed gradients. With small/large leaf counts U,L, centering the potential gives S(k,l)=U+1+4l-[2(k+l)-U+1]^2/(U+L+2), and the exchange argument forces k=0 at every optimum. Its finite difference 4(2U+L-2l)/(U+L+2) determines the balanced and parity-split maximizers; exact binomial counts give contacting facets. Their linear span has rank 1,L,L+1, respectively, and positive slack on other facets gives the full incenter affine dimensions N-2,U+1,U. Central symmetry rules out larger off-center inballs. Independently enumerated signed-edge norms and exact contact counts for (a,b)=(2,2),(2,5),(2,6),(2,7),(2,8),(3,9). All-dimensional proof is algebraic, not extrapolated from these examples.

## originality

PASS

Tree symmetric-edge polytopes are unimodularly equivalent to cross-polytopes by D'Alì–Delucchi–Michałek, but the transformation is generally not orthogonal, so the Euclidean variance maximum, contact counts and incenter locus cannot be deduced from lattice equivalence. Closest published Resultary STAR/PATH inball classifications concern one hub or one path rather than the bistar double branching transition. General facet-potential statements provide the polar feasible set but no formula for maximizing its Euclidean squared norm for two variable hub leaf counts. Best-of-knowledge originality PASS, with residual graph-Lipschitz maximum-variance alias risk.

## value

PASS

The double-star is the first tree family with independently variable branching hubs. Its natural Euclidean embedding distinguishes geometrically even though every tree has the same lattice cross-polytope type. The exact L=2U+2 contact and incenter-dimension transition is a motivated all-parameter structural classification, not a recomputation of one table entry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
