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

For the published Type-II log likelihood l(alpha)=r log alpha+(n-r)log(1-z^alpha)+affine(alpha), direct differentiation gives l''=-r/alpha²-(n-r) z^alpha(log z)²/(1-z^alpha)²<0 when 1<=r<=n, 0<z<1 and 0<alpha<1. The printed Hessian instead uses 3 and n-3 and lacks the entire alpha^-2 factor; for r=3 H_print=alpha² l''. Thus at (n,r,alpha,xr)=(10,3,1/2,1/2) literal inverse information is four times correct. Independent SymPy differentiation, common-denominator polynomial algebra and numerical substitution confirmed the two errors and strict concavity. Concavity guarantees at most one constrained maximizer if one exists, not automatic existence on the open interval.

## originality

PASS

The source article gives the incorrect second derivative immediately after a general-r likelihood and score. Exact-DOI, model, erratum and information-formula searches did not surface a corrigendum or earlier explicit identification of both defects among retrieved matches. A pre-existing unindexed correction remains possible.

## value

PASS

The mistake changes inverse observed-information variance and therefore potentially nominal interval widths; at alpha=1/2 the variance differs fourfold. Fixing both the hard-coded failure count and missing scale restores general censoring inference, and strict log-likelihood concavity rules out multiple interior shape-parameter optima. This is an inferentially material correction, not a cosmetic formula revision.

The dated certificate retains the supplied scientific assessment, sources and limitations.
