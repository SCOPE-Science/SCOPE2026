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

The argument is a symbolic lower-bound proof over every integer \(k\ge3\). Its essential points to check are the uniqueness of the group-phase label of each useful NFA state; the existence of a distinct lifted graph edge for every Boolean-cube edge; the connectedness of the trimmed graph; and \(E\le4(N-1)/3\) for connected bipartite cacti.

Run `python3 checker.py` in the directory containing this document. Expected output: `VERIFY_OK cube_dimensions=12 cactus_graphs=3500 words=97742`. The executable checks finitely many dimensions and examples; it does not exhaust the class of all NFAs and is not an infinite proof or an independent validation.

The minimum cactus-NFA state count is not claimed exact; the proof only gives a lower bound. The recent principal primary paper was inspected in full. Its stated open problem on tight representation-size bounds does not imply the present quantitative result; unindexed earlier coverage and independent mathematical validation remain open.
