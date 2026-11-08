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

For LCD planes with an associated neighbor, the common line has odd self-dot: even line forces both nonshared generators to pair 1 with it, contradicting orthogonality requirement. For odd u, every containing LCD plane has unique orthogonal basis {u,v} with Q(v)=1, v∈u-perp, and associated adjacency reduces to v·w=1. With t all-ones, f=t+u controls the parity character on u-perp, yielding h(h-1)/4 pairs for even n or h(h-2)/4 for odd n except forbidden u=t. Summing over 2^{n-1} odd lines gives the stated e_n for every n≥2; n=2 and 3 give zero. Independent exhaustive labeled-2-plane computations through n=7 matched 0,0,24,180,1920,15120; these corroborate, not replace, the argument.

## originality

PASS

Carlos Vela’s 2025 lecture introduces the associated relation and explicitly lists determining its edge count as ongoing work. De la Cruz et al. (arXiv:2609.07580) and a published Resultary finding treat the ordinary LCD Grassmann neighbor graph, whose edge regularity does not imply the narrower associated graph’s count. No complete count for binary dimension 2 found in inspected material; earlier 2025 institutional talk is an uninspected priority risk.

## value

PASS

This is the exact answer to a problem specifically raised in the primary literature for the first nontrivial LCD code dimension and all ambient lengths. The odd-line selection and exceptional all-ones line give structural information not obtained by substituting k=2 into ordinary neighbor counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
