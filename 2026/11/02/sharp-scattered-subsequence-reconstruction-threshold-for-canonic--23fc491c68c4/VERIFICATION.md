---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Every order-five binary necklace corresponds to a bijective shift-append map with one complementary pair of outgoing bits per 4-bit suffix, i.e. one of 2^16 feedback tables. Requiring a single orbit of length 32 selects exactly 2048 canonical words starting at the unique 00000. Scattered subsequence membership has an elementary greedy earliest-position characterization and a dynamic set-of-subsequences recurrence; exhaustive partition by full k-deck, not sampled examples, gives class counts [1,1,21,629,1520,2016,2048] at k=8..14. At k=13 exactly 32 doubletons (each distance-two letter swaps) and 1984 singletons; at k=14 2048 singleton classes. Deck downward determination excludes all smaller k. Independent freshly compiled C++ implemented feedback-table enumeration and greedy complete candidate deck classification, confirming 2048 cycles and every count, 32 doubletons and no non-swap k13 collision. Finite exhaustive verification is the complete finite proof because all 65536 tables and all applicable binary patterns are enumerated; unlike a partial experiment.

## originality

PASS

A natural restricted language of canonical order-five de Bruijn cycles has sharp subsequence separation at 14, sharper than universal length32 bound 17. This precise finite deck-class census is not furnished by general Simon-congruence theory.

## value

PASS

The order-five de Bruijn family is a canonical nontrivial constrained class of length-32 words; its precise threshold relative to the universal 17 bound and full 32-pair obstruction set are useful finite reconstruction benchmarks, including algorithm tests. Complete 2048-case enumeration, rather than an unmotivated isolated example, gives a natural exact classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
