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

PASS: The standard k-PIR distance bound forces any binary linear length-17 6-PIR code on s=8 bits to have d>=6. Published classification of binary [17,8,6] codes gives one equivalence class (representable by cyclic g(x)=1+x+x³+x⁶+x⁸+x⁹). Independently enumerate its 256 primal words (d=6) and 512 dual words (dual d=5, exactly 34 weight-5 words). Across 136 coordinate pairs, 68 lie in two and 68 lie in three weight-5 dual supports, so no pair lies in five. Six pairwise disjoint nonempty recovery sets for a fixed nonzero information syndrome would have pairwise unions of size >=5 and total size <=17, forcing sorted cardinalities (2,3,3,3,3,3). The five unions of the size-2 set with each size-3 set are distinct dual weight-5 supports through a fixed pair, impossible. Therefore length17 excluded, while Kurz–Yaakobi already construct length18, proving P(8,6)=18. Source literature class uniqueness and upper bound are explicitly external premises; finite enumeration certifies the representative obstruction, not all code isomorphism classes.

## originality

PASS

Best-of-knowledge PASS: direct PIR paper leaves 17<=P(8,6)<=18; the later code-classification source supplies unique [17,8,6] equivalence class but not a PIR recovery-set impossibility. Independent incidence proof joins them to obtain the first matched exact value found. Residual risk of an unindexed PIR table update remains.

## value

PASS

PASS: Closing a published exact small-parameter gap in P(s,k) is useful in its own right; the dual minimum-support pair-incidence obstruction provides a reusable method for ruling out disjoint recovery systems. The result is not just recomputing code minimum distances or giving a new length-18 example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
