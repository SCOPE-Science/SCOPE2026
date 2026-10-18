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

# Reproducible verification

Run `python3 checker.py` with Python 3 and its standard library. The file contains three independent counting procedures: the symbolic recurrences for power roots in symmetric and wreath permutation groups; direct enumeration of each induced-subgraph partial permutation, testing adjacency and permutation powers; and direct enumeration of global automorphisms followed by restriction to invariant domains.

The tests cover nine complete-multipartite size profiles, each at five positive powers, yielding 45 exact brute-force comparisons for the unrefined polynomial and 45 for power-preserving global extendibility. The symmetric-group root recurrence is separately tested against direct permutation enumeration for \(0\le s\le6\) and \(1\le d\le8\) (56 cases). The rank-two extension obstruction and the equal-part-size boundary are also tested on all nine graph profiles.

Expected terminal tokens: `ALL_EXACT_CHECKS_PASSED` and `POWER_PRESERVING_EXTENSION_CHECKS_PASSED`. No extra libraries, downloaded data, or external input files are needed. A finite computation does not prove the universal case; the exact combinatorial argument in `RESULT.md` covers all positive part sizes and powers.

Self-review: passed. Independent audit: not yet performed.
