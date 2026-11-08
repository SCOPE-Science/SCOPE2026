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

Distance from core landmark c_a to cycle c_i is d_C(a,i), to its leaf ℓ_i is d_C(a,i)+1. Cross-layer ambiguity occurs only if all core landmarks lie within an m-vertex consecutive arc (equivalent to a cyclic gap >=m+1). Thus valid triples are exactly gap vectors g_i≥1,g_i≤m,sum 2m; subtract unique long-gap count from binom(2m,3) to obtain m(m−1)(m+4)/3. Legal unit transfers between donor/receiver gaps preserve [1,m], reduce target L1; for m>=3 reach (m−1,m−1,2) and use front-to-back slides for a repeatable clockwise labelled patrol; for m2 four triples form the vacancy-sliding cycle. Moving a core robot out/back to its leaf preserves distinct signatures. Explicit two-projection witness configurations show no resolving pairs for m>=3; for m2 four adjacent-leaf pairs resolve but freeze when moving inward. Independent BFS on n=4,6,8,10,12 confirmed all pairs, 210 valid core triples total, the gap iff, allowed pendant detours and connected legal configurations. General proof, not extrapolation, supplies all m.

## originality

PASS

Camacho Moreno et al 2026 primary theorem concerns completely mobile robots on odd unicyclic graphs; cannot directly imply even sunlet triple movement or frequency. Ali–Rahim–Ali 2014 ordinary sunlet metric dimension is static (no move constraints). Resultary hits concern mobile general position, a different invariant. Similar mobile reconfiguration under alternative terminology remains a priority risk.

## value

PASS

Resolves the natural even-parity gap in a studied completely mobile resolving problem and gives explicit all-configuration classification, exact count, reconfiguration connectivity and individual patrol (not merely the mobile-dimension number). Distinguishes static and dynamic optimality at m2.

The dated certificate retains the supplied scientific assessment, sources and limitations.
