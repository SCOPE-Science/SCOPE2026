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

For k>=2 and precisely k+1 distinct ordered agents on the real line, the nearest-facility social optimum is min adjacent gap m by pigeonhole and triangle inequality. Product-Gap selection omits one position; for the product P of k adjacent gaps, omission weights are P/g1 for the first, P(1/g_{i-1}+1/g_i) internally, P/g_k for the last, total Z=2PΣ1/g_j. The omitted agent alone pays its nearest adjacent gap, giving the exact expected social-cost identity [k+1+Σ min(g_j,g_{j+1})/max(g_j,g_{j+1})]/[2Σ 1/g_j]. At m=g_t, set h_j=m/g_j,A=Σ_{j≠t} h_j>0; adjacent ratio terms are bounded by adjacent h and all others by 1, leading ratio≤(2k-1+A)/(2(1+A))<k-1/2. Gap family g1=eps,g2..k=1 tends to the bound, never reaches for positive m. Independent exact rational direct weighted-selected-subset enumerations on 350 profiles across k=2..8 reproduced normalization, identity and strict bound.

## originality

PASS

Both Jia and Chan–Lin–Wang define identical product-of-selected-gaps mechanism and general 2k bound; this mechanism is not new. The exact k+1-agent first-surplus sharp ratio k-1/2 and omission law do not appear in fully accessible Chan–Lin–Wang section 5, and Jia accessible metadata does not provide it. Broader priority qualified since Jia full text inaccessible.

## value

PASS

Exactly one more agent than facilities is the first natural nonzero-optimum regime, so an exact sharp ratio there is a meaningful performance invariant of a named stochastic allocation mechanism. Its omission distribution and nonattained k-1/2 supremum quantify a substantial gap from its known global factor 2k, rather than changing names or computing isolated instances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
