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

The reproducible checker `verify.py` uses no third-party dependencies and can be run with `python3 verify.py`. It computes the minimal element in each residue class by a Dijkstra shortest-path calculation, independently computes membership using forward dynamic programming over the actual generators, and calculates all isolated gaps up to the exact largest gap. It checks exact identity of the resulting sets with the classification and counts by floor-quotient level, rather than comparing sampled isolated gaps.

In the executed run it passed all 20 complete cases \(3\le a\le22\), covering 435,045 exact membership decisions. The asserted theorem is for \(a\ge5\); the two smaller values were included as explicit boundary controls. For every parameter tested, Apéry representatives also matched the independently calculated Zeckendorf thresholds.

The unrestricted statement relies on the written proof and a previously published Apéry-set theorem. Neither the finite tests nor this self-review constitute independent validation or a formal proof-checker certification.
