---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The exact 48-root coordinates give the 24-cell on short roots, with 24 long roots indexing facets; at distance≤1, short cliques form the two-skeleton and coning all octahedral facets produces a facet-stellar boundary subdivision S^3. At threshold sqrt2 exact integer-distance clique enumeration gives f-vectors (48,240,384,192) and (48,408,1224,1560,840,168,24). Independently fetched the entire package collapse_pairs.txt (blob dbfde6054038619d33bdaa58a118bb2248993a5a) and rebuilt all root coordinates and both clique complexes in separate JavaScript: checked each of 1704 pairs for exact one-dimensional coface, unique remaining immediate coface, absence from K1 and removal ordering. No additional faces remained and exactly 864 K1 simplices survived; pair counts by free face dimensions 1..5 were 168,672,696,144,24. Hence the inclusion is a homotopy equivalence; W(F4) representation on H3 follows from equivariant 24-cell subdivision, not a purported equivariant collapse.

## originality

PASS

Best-of-knowledge comparison of statements and mathematical implications; the named comparisons identify prior facts without conflating them with the claimed new invariant or construction. Historical-priority risks remain explicit.

## value

PASS

Meaningful natural finite-object topological classification: proves integral persistence and a protected relative elementary collapse despite thousands of new simplices, and determines induced Weyl orientation character. Specific exact F4 root metric filtration is a natural, reusable root-system benchmark, not an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
