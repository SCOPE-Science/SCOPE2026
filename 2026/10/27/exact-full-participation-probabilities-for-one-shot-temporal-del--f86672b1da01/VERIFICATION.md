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

# Verification

**Proved scope:** Each \(n\ge3\), with one designated root on the \(n\)-cycle, one distinct time label on every undirected edge, all retrospective trust horizons unrestricted, and one outgoing delegation for each nonroot. Every valid rooted confluence is one of the \(n\) deleted-edge trees. For cut \(j\), chronology is equivalent to the prescribed prefix/suffix inequalities. Pairwise and triple intersections give the exact histogram by inclusion-exclusion, with no appeal to finite enumeration.

**Executable check:** Run `python3 check_cycle.py`. It builds the oriented tree for every removed edge, starts at every delegating vertex, follows actual parent pointers to the casting root, rejects repeat visits and chronology violations, and tabulates every one of the \(n!\) time permutations for \(3\le n\le8\). It also checks that total incidence equals \(n2^{n-1}\). All six tested network sizes passed with exact integer arithmetic.

**Unproved scope:** No statement is established for general temporal graphs, repeated or tied time labels, multiple casting vertices, nonretrospective horizons or independently random time-presence processes. Computation is an independent finite consistency check, not a general proof or external audit.
