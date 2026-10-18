---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Under the stated descendant condition for coalitions of at most two, a violation requires exactly a forbidden unordered triple of distinct ternary 3-words with one descendant of the others. Independent generation of the entire 27-word hypergraph yielded exactly 972 forbidden triples. A fresh increasing-index bit-set search enumerated ALL size-nine and size-ten valid subsets (pruning solely forbidden triples and insufficient remaining candidates): zero size-ten sets and exactly 12 size-nine sets, after 2,340 search nodes. For every maximum, all three pair-coordinate projections have nine distinct pairs, so each code is the graph of a 3×3 Latin square. Direct enumeration of Latin squares of order three gives 12 and the same equality codebooks. Independent coordinate/symbol relabeling acts transitively on Latin squares of order3: the group has (3!)^3·3!=1296 elements, orbit 12, stabilizer 1296/12=108, consistent with inspected full finite verifier. The bound |C|≤9 is also known from separating hash theory; the new claim is equality classification. No claim for larger alphabets or n≠3.

## originality

PASS

Staddon–Stinson–Wei and Bazrafshan/Bazrafshan–van Trung supply the frameproof/separating-hash equivalence, sharp q² upper bound and Latin-square constructions. Those source statements alone establish existence of some Latin-square extremizers, not that every ternary length-three maximum is one. Later length-four ternary 2-frameproof census and length-three STRONG separability or IPP records are different parameters/properties, hence do not dominate this equality theorem. Complete q=3 classification is supported by independent exhaustive 27-word search. The Bazrafshan thesis may contain an obscure equality theorem/table; the accessible 2009 precursor and general bounds were inspected but full thesis was not obtained, so retain residual risk.

## value

PASS

Classifying ALL equality cases in the first ternary sharp 2-frameproof/separating-hash setting is mathematically useful as a rigidity and design correspondence: not just achieving the known bound q² but proving every optimum is a Latin-square graph, enumerating exactly 12 labels and computing a single orbit/stabilizer. This finite result concerns a natural exact extremal-design parameter, not an arbitrary slice or routine recomputation of the published numerical optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
