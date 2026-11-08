---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For the metric retaining every vertex of K_{m,n} plus one t>0 pendant leaf attached to A, the core powered zero-sum distance form splits exactly as [2(2^p-1)-2^p(1/m+1/n)]sigma²-2^p(||a||²+||b||²); its endpoint is p0=log2(2mn/(2mn-m-n)) with one-dimensional radial kernel. Moving the leaf coefficient to its attachment vertex yields the exact extended quadratic form -u(||a||²+||b||²)+2h[sigma F(t)+Delta a0]-2t^{p0}h². If F !=0, unbounded sigma gives a positive form, so endpoint failure. If F=0, concave-power Delta<=min(t^p,u) and completing squares shows strict negativity except along the core radial null line; dimension m+n-1 and inherited strict lower exponents follow. The derivative sign of F is governed by strictly log-convex Laplace transform g(t)=t^{p-1}-(t+1)^{p-1}, proving exactly one positive root if m>n and no root if m<=n apart from (2,2) p=1 identity. The near-balanced t/n limit 2/(k log2) and fixed n singular power limit follow from the stated uniform expansions. Independently numerical-scanned m,n=(3,2),(5,2),(8,7) show one root; (2,5),(7,7) none; K_{2,2} is analytically identity F=0 for all t. Finite scans were not used to prove uniqueness.

## originality

PASS

Qualified PASS. Sánchez computes p0 for an unmodified complete bipartite graph; Li–Weston proves general strictness inheritance. The new variable-length pendant perturbation endpoint preservation condition, nullity rigidity, and two asymptotic regimes are not stated in those sources. Robertson studies core distortion and Ferdi et al. multiple-vertex coronas at exponent one. None provides a directly dominating one-leaf variable-exponent theorem in the inspected material.

## value

PASS

One-leaf attachment is the simplest local perturbation of a symmetric graph metric, and supremal negative-type exponent controls Hilbert snowflake embeddings. The asymmetric unique tuning on the larger class vs strict drop on the smaller class is a sharp structural resonance; its two scaling laws describe natural balanced and unbalanced graph-growth limits. It answers a natural preservation problem rather than a random chosen matrix instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
