---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For commuting idempotents h=fg=gf is idempotent and fh=gh=hf=hg=h. Its image is exactly the common fixed set and its fibers are invariant. In each fiber the common root maps to itself under both functions, each f-only or g-only fixed label maps to the root under the other function, and each remaining label independently chooses its two images from the appropriate singly fixed sets augmented by the root. Both composites then return the same root. This gives exactly the stated weighted component EGF and the labeled-set exponential formula, including the empty object. An independent finite calculation instead fixes the three fixed-label sets globally, assigns the cross-images of singly fixed labels, then counts image pairs with equal common image for every other label. Its full profile agrees with testing the original identities on all ordered pairs of functions through n=4, and it gives all eleven displayed totals through n=10. These tests supplement the bijection; they do not prove it.

## originality

PASS

Credit the explicit three-rank EGF for unrestricted labeled total endofunctions, not the exponential formula for components, the tractability of unary logic in general, or priority over the closely related regressive-monoid census. The strongest inspected match counts a materially restricted population by the analogous three statistics and has different coefficients. General action decomposition does not supply the specific weighted component count.

## value

PASS

Commuting retractions are a natural transformation-monoid object and the individual ranks and common-image rank are canonical structural invariants. The explicit component EGF recovers every labeled rank profile and gives effective exact computation without enumerating endofunction pairs; it fills a more specific gap than deciding tractability or tabulating small monoids.

The dated certificate retains the supplied scientific assessment, sources and limitations.
