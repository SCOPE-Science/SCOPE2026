---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: In PG(3,2), lines are triples {a,b,a⊕b} of nonzero F2^4 vectors. A wholly fresh exact enumeration of the 35 lines, all 35-choose-5 line subsets and valid 15-point partitions found exactly 56 spreads. For all 560 three-line subsets of spreads, independent complete nine-point partition enumeration found exactly two partitions (original and unique opposite regulus) and the resulting spreads are exactly all 280 pairs sharing two original lines. Every spread has degree ten. An independent NetworkX complement maximal-clique search found precisely 23936 maximal no-switch sets, with size counts 7:240, 10:13552, 12:8120, 14:1680, 16:336, 21:8. Each of the 56 spreads lies in exactly three of the eight maximum independent families, all signatures are distinct 3-subsets of eight symbols, and for every pair adjacency equals disjointness of signatures. This proves KG(8,3), diameter two, absence of triangles, Aut=S8 and GL4(2) order 20160 embedding by intrinsic maximal families. Finite domain explicitly complete; no higher-q claim.

## originality

PASS

PASS (qualified): Magaud (2021/2022) gives 56 spreads and 240 seven-spread packings, and Marcelis (2021) already encodes the 56 spreads as all 3-subsets of eight symbols via a hyperpacking. These discoveries are prior. The inspected primary material does not establish that the SINGLE opposite-regulus switch relation is disjointness in the intrinsic EKR labeling, nor classify all eight maximum 21-spread no-switch families. Closest inaccessible Jeurissen 1995 and Bruen--Silverman 1974 switching-set papers leave serious priority risk but their inaccessibility alone does not negate best-knowledge originality.

## value

PASS

PASS: Identifies a canonical and computationally exhaustive global structure behind an elementary local regulus surgery: an intrinsic EKR/Kneser graph model, exactly eight canonical maximum no-switch families, diameter, and a strict index-two symmetry enhancement beyond ambient geometry. Distinguishes the switch graph from simply counting 56 spreads or constructing arbitrary 8-symbol labels.

The dated certificate retains the supplied scientific assessment, sources and limitations.
