---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible checks and proof limits

Execute `python3 verify_prism_odd_independence.py` using Python 3 and no third-party dependencies.

The checker directly enumerates every one-vertex-or-empty choice on each rung for \(3\le n\le11\), testing graph independence and the parity of every unselected vertex's neighbourhood. This is \(265707\) direct candidate words in total. It also constructs a nine-state transfer matrix independently from the local three-rung predicate and confirms its coefficient sequence against the closed combinatorial formula for \(3\le n\le100\); all equality assertions passed in the supplied run. Extremal and maximum-count assertions were checked over the same interval.

The proof in RESULT.md, not these bounded experiments, establishes the theorem for every integer \(n\ge3\). The checks do not establish originality, make no statement about larger-width grids and do not constitute independent audit or certification.
