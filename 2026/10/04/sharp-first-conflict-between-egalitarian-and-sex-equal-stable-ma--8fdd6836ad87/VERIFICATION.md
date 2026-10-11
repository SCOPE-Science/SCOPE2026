---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

A fresh independent exhaustive enumeration checks every one of the 16 two-pair and 46656 three-pair strict preference profiles, every perfect matching, blocking-pair stability, the two rank-sum objectives and complete tied argmin sets. It reproduces exactly the four stated three-pair counts and the published stable-count marginal 34080, 11484, 1092. The explicit two-stable-matching witness also has objective pairs (12,2) and (11,3), yielding disjoint unique optima. Because the domain is finite and completely enumerated, this establishes the stated boundary without extrapolating beyond three pairs.

## originality

PASS

The literature defines and optimizes both fairness objectives, while the closest exact small-instance source tabulates stable-matching counts and egalitarian data. No inspected source gives the four-way complete argmin-set relation census or the first disjoint-optimum boundary. A fresh exhaustive replay independently reproduces every stated count, so the novelty-bearing object is the new joint finite classification rather than either objective separately.

## value

PASS

Egalitarian and sex-equal matching are standard but genuinely different fairness goals. The smallest market where they force incompatible stable choices is a natural finite boundary, and the complete joint census is substantially more informative than an isolated witness or a one-objective table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
