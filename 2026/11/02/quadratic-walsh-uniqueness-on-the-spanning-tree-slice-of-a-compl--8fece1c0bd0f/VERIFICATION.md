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

For every s>=3, a vanishing linear combination of edge indicators on all trees has every coefficient zero: use tree exchanges across a cut and fixed tree size. Induct on n for a vanishing pair sum: attach reserved vertex n by different leaf edges to force mixed coefficients equal via linear uniqueness; restrict to old trees to determine old pairs; use full star and one-old-edge near-star evaluations to eliminate common mixed weights; omit two star edges and connect omitted vertices via old edges to eliminate remaining pairs. Base n=3 incidence matrix is identity. Fixed tree-size relation reduces constants and singleton indicators to pairs, yielding m+1 independent relations. Exact independent enumeration of Prüfer trees/linear algebra confirmed n=3,4,5 pair ranks 3,15,45; no finite extrapolation.

## originality

PASS

Filmus develops orthogonal basis for a complete fixed-weight Boolean slice but spanning trees are a strict subset, and restriction may lower rank. Burton–Pemantle and Kassel–Wu compute transfer-current joint edge statistics but do not state this exact all-degree-two function independence. Best-of-knowledge O PASS, with larger risk of a general matroid-basis inclusion matrix theorem implying the special case.

## value

PASS

Exact dimension and complete kernel of low-degree Fourier/Walsh observations on a canonical graphically constrained Boolean slice under every positive sampling law; structurally useful for identifiability and covariance/Gram rank, not a rederivation of a generic fixed-slice rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.
