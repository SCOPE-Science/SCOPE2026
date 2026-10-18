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

Primitivity is equivalent to absence of a proper common invariant state partition for both generators. Exhaustive map-pair enumeration for n=2,3,4,5 has exactly n^(2n) candidates; subset-image BFS from the full set is an exact synchronizability test. Independently compiled C++ program enumerated this complete finite space, obtained 0,0,0,2880 and 12 symmetry canonical keys with orbit sizes 240; rank split 1920 and 960. The original source verify.cpp also rechecks congruence generation and pair compressibility. The exclusion of two-permutation-letter cases and input interchange was observed; no extrapolation to larger n.

## originality

PASS

The five-state primitive nonsynchronizing examples with rank deficiency two are already known, but inspected published work supplies individual examples and general low-rank synchronizability results, not this complete twelve-orbit binary census. Resultary related five-state synchronizing/extremal automata address different properties. An unpublished/full supplementary census remains possible.

## value

PASS

The first nontrivial state size for primitive non-group nonsynchronizing binary automata is a naturally motivated boundary to general synchronization theorems; the complete isomorphism and rank classification is an independently usable finite classification, not merely a restatement of known examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
