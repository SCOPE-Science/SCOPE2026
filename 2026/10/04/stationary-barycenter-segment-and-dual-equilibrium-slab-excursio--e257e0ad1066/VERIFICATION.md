---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Invariance against arbitrary antiderivatives of continuous functions of \(x\) gives \(\mathbb E[z\mid x]=-(a/b)x\). The coordinate generators and \(L(x^2)\) yield \(\mathbb E x=\mathbb E y=-(b/a)p\), \(\mathbb E x^2=(b/a)^2p\), and \(\operatorname{Var}(x)=(b/a)^2p(1-p)\), forcing \(0\le p\le1\). The exact coboundaries \(L(\tfrac12x^2-b(y+z))=a x(x+b/a)\) and \(L(-\tfrac a2x^2-bx-ab(y+z))=b^2z(z-1)-(ax+bz)^2\) give the slab balance and height defect. Equality in the height defect forces \(\dot x=0\) on the invariant support and hence only the two equilibria. The signed balance similarly forces every other invariant measure to place positive mass on both signs of \(x(x+b/a)\). For a nonconstant periodic orbit, continuity on the periodic circle converts the sign/height information into at least two boundary crossings for both slabs. The packaged exact sparse-polynomial verifier was read and independently confirms every polynomial identity.

## originality

PASS

Sprott's primary-author technical note gives the exact generalized Case G equations and parameter-plane motivation, but no invariant-measure identities. The complete 2001 statistics paper retrieved in this audit studies generalized Sprott B and N, not G, and develops approximate two-point spectral fits rather than exact stationary moments. The 2004 Panchev paper is a plausible analytical comparison, but the authorized retrieval for its DOI returned the wrong two-page Rössler 1976 paper; that transport/content mismatch was not retried or bypassed, so Panchev remains an explicit residual risk rather than grounds for failure. Resultary searches returned analogous stationary-moment findings for other vector fields but no Sprott G theorem covering the conditional regression, variance parabola or dual slab constraints.

## value

PASS

The identities impose sharp global geometry on every compact recurrent statistical state of a canonical chaotic flow: an exact equilibrium-segment barycenter, a variance parabola, a derivative-energy defect with rigid equality, and forced excursions across both equilibrium slabs for periodic recurrence. These are natural structural restrictions tied to the system's two equilibria rather than arbitrary computed moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
