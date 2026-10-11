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

The source routine was independently reimplemented from its frozen code path. For every integer from 24 through 49, the number of terms in its first depth-first solution equals the exact minimum found by an independent increasing-rank exhaustive search. At 50 the routine returns \(32+9+9\), while \(25+25\) is a valid two-term representation and one term is excluded by the paper's own requirement of at least two summands, so rank two is optimal. The showcased value also satisfies \(512550=659^2+5^7+2^7+2^4\), a four-term decomposition. These are finite claims and the enumerations are exhaustive over their stated finite ranges.

## originality

PASS

Originality passes as a precise correction of a released computational artifact. The source paper proves no minimum-rank theorem and only uses the listed representations as existence evidence. The accompanying repository README says the backtracking routine aims for the minimum number of terms, while the actual source code is a descending depth-first first-success search. Fresh exact and semantic searches found no prior identification of 50 as the first rank failure or the shorter decomposition of the showcased 512550 example.

## value

PASS

The released data are presented as computational evidence for a new additive conjecture, and the repository explicitly describes the routine as minimum-seeking while recording a solution length. Identifying the first exact rank error prevents those lengths from being used as minimum certificates and gives a compact regression test for any corrected search. The additional shorter decomposition of a prominent five-term example reinforces the methodological issue without being overstated as a refutation of the at-most-five conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
