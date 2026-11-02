---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The six disjoint support classes exhaust choices by whether each bipartition contains a selected original core. If both cores supported, all cores are observed. If only A is supported, all A pairs touched works; one untouched A pair can be forced only if a B pendant was selected; two untouched pairs stall. Symmetry supplies the B-only cases. If neither core is selected, selected leaves must leave at most one untouched pair per side to permit cross-forcing. Touched-pair choices contribute 2z+z², and subtracting the unique all-leaf choice produces A_n and B_n. These exhaustive mutually exclusive categories sum to the displayed polynomial. Direct independent power-domination propagation over every subset of five graph sizes confirmed all coefficients, including z² counts 22,15,19,9,12; formula and proof cover all p,q>=2, not the finite checks.

## originality

PASS

The general power-domination polynomial and related corona questions are prior (Brimkov et al.). The submitted six-category full polynomial is restricted to K_{p,q}◦K_1 with p,q>=2, not the known book/double-star/spider graph cases in Resultary. The 2018 highly relevant full paper could not be retrieved; its abstract gives no explicit K_{p,q} one-leaf formula, but abstract silence is not proof of noncoverage. Best-of-knowledge PASS with explicit high-priority residual risk.

## value

PASS

A natural complete two-parameter graph-family enumeration, not merely a minimum parameter, resolves all cardinalities of sensor placements under iterative forcing and exposes an exceptional min(p,q)=2 change in minimal sets. The pendant structure motivates the exact support classes; results for other graph types cannot simply be relabelled.

The dated certificate retains the supplied scientific assessment, sources and limitations.
