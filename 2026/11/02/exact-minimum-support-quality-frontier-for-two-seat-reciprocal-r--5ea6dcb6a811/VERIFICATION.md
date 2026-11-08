---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

From the strict rJR criterion 2*h_c*|N(c) intersect U(W)|<n, failure of a maximum-quality pair {a,b} gives a third candidate c with at least n/(2h_c) uncovered supporters. Since s<=n-d, h_c>=n/[2(n-d)]. Replacing b with c covers s+d>n/2 and is rJR; the ratio is >=(1+n/[2(n-d)])/2. At 2d=n the repair has identical maximum quality; when 2d>n no maximum pair can fail. The sharp example with disjoint T,S, supports T,T,S and qualities 1,1,n/[2(n-d)] attains the ratio. Integer boundaries and strict tie handled. Independent integer-grid enumeration covers 630342 3-candidate cases for n=4,5, not an all-instance proof.

## originality

PASS

The quantity is the quality price of reciprocal justified representation for two committee seats under minimum candidate support d>=2, not classical unweighted JR. The 2026 Boehmer et al. general 3/4 bound and an already-established finite-electorate d=1 exact frontier cover baseline only. The novel claim is support-dependent sharp curve and sharp lossless half-electorate boundary; no dominating parameter theorem was established from the literature accessible this run. Full principal arXiv text unavailable and authorized institutional access blocked, so historical novelty remains qualified.

## value

PASS

Candidate minimum approval degree is a meaningful parameter for representation-cost design. The exact support-dependent retained-quality ratio, tight three-candidate family, single-swap repair and half-electorate threshold constitute a natural full frontier rather than a routine substitution of the d=1 result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
