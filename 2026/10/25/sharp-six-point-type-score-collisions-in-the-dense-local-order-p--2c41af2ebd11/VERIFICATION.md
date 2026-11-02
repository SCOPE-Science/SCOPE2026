---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Known identity E_T(z)=(1+z)sum_v z^{s_T(v)} reduces type-score equality to degree-multiset equality. Independent enumeration of all 2^(n choose 2) labeled orientations n<=6, checking in/out-neighborhood transitivity and canonical isomorphism representatives by all degree-preserving permutations, gives iso counts (1,1,2,2,4,6) and score-fiber counts (1,1,2,2,4,4). Six-point degree lists (1,2,2,3,3,4) and (2,2,2,3,3,3) each have multiplicity 2. Masks A=(14,28,56,48,33,3) and B=(14,12,56,48,35,3) are locally transitive, share (2,2,2,3,3,3), and have 2 versus zero regular 5-subtournaments. Substituting transitive h-chain at designated score-three vertices preserves local transitivity, common score lists and regular-five counts 2h versus zero; the analytic substitution proof covers all h, independently checked for 1..6.

## originality

PASS

Brouwer and Belkillani established circular representations, score-sequence symmetry and realizability for locally transitive tournaments; the type-score transform itself was also known. The inspected Belkillani 2014 complete article gives construction/realization theorems but does not give the exact six-vertex isomorphism-fiber multiplicities or the all-order regular-five-separated collision family.

## value

PASS

Complete determination of the first failure of a natural model-theoretic type invariant to separate finite structures, plus exact first fiber sizes and a uniform construction witnessing the obstruction at every larger size. The pair is distinguished by a meaningful independent substructure statistic, not mere relabeling of a known score sequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
