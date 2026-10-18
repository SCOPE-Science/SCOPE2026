---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Let X=G∘K1 for any finite simple labeled G (n>=1). Positive support independence rules out label1, and each degree-one leaf forces exactly (core,leaf)=(3,0),(0,2),(0,3). The core 3-set I must be independent; any (0,2) leaf-core requires a core-3 neighbor, so its core belongs to N_G(I). Thus feasible functions biject with (I,J subset N_G(I)), and weight=3n-|J|, yielding F(z)=z^{3n}B_G(1+z^-1). Extending I to a maximal independent D gives max |N(I)|=n-i(G), so minimum 2n+i(G) and optimizer count highest neighborhood coefficient. Independent enumeration of all 4^8 labelings on P4 agrees with predicted full polynomial {10:5,11:12,12:8}; finite check corroborative only.

## originality

PASS

Mojdeh–Mansouri introduced independent double Roman domination; Nahani Pour et al. 2022 Theorem 3 establishes restricted tree-corona extremal number, not the complete feasible-weight polynomial or invertible all-base-graph neighborhood enumerator. Other Roman variants impose independence on zero set or different label rules and do not imply this transform. Resultary returned polynomial results for other graph families or invariants, not this exact transform.

## value

PASS

A complete bijection and reversible full weight distribution for every finite base graph, with exact count of optimal functions, materially strengthen known scalar minima. P4 example has 5 optimum corona functions but only 3 minimum independent dominating base sets, showing enumerative content beyond old extremal characterization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
