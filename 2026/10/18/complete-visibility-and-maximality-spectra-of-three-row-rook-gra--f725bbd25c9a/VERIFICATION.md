---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

An occupied diagonal of a rectangle is obstructed exactly when the other two corners are both occupied, so each of the three row pairs is used in at most one column. The disjoint choices for the columns using pairs are one triple or zero to three doubles of distinct types. Each remaining column gives 1+3z, yielding the full polynomial. For maximality a blank can always be filled, a lone double can be tripled, and with exactly two doubles the only allowed pair extension uses the unused type; hence a singleton is blocked exactly when its row is outside that type. A triple or all three pair types blocks every singleton extension. Counting these cases gives the two nonzero maximal coefficients and their ratio. Within the triple and three-double cases, any row permutation can be compensated on the nonsingleton columns, so the singleton counts are classified by their unordered multiplicities. The two-double case is transitive. This also handles n=3, including the empty singleton multiset when all columns are doubles. Independent enumeration by common neighbors and explicit row/column permutations gave maximal counts (45,6) and (144,72), orbit counts 4 and 5, and matched every visibility coefficient at n=3,4. Replay: python3 review_evidence/frozen_math_spot_checks.py. The frozen script and its recorded output were inspected, not executed; their larger ranges are not claimed as a new replay.

## originality

PASS

Credit the exact three-row census and its orbit refinement, not the rectangle criterion, the extremal sizes, or the isolated falling-factorial count. A distinct later-dated Resultary record demonstrably covers both labeled polynomials and the same three-family description, and extends their parameter range; it does not cover the coordinate-permutation orbits. This is real overlapping coverage, not a claim that the frozen formula is unique, nor evidence of earlier priority. No inspected earlier result supplied the joint enumeration and orbit refinement.

## value

PASS

Three rows are a natural first case with genuinely different maximal sizes. The result resolves inclusion-maximal shapes, their frequencies and their coordinate-equivalence classes, which neither extremal bound gives. The labeled and orbit polynomials are usable exact benchmarks for visibility and host saturation rather than an arbitrary finite sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
