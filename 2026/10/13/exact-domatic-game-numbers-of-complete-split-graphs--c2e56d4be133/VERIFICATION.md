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

The analytic proof checks the exact terminal-color criterion and gives explicit lower and upper strategies in every parity and starting-player case. In particular, each upper strategy controls the number of colors represented in the universal clique and separately blocks the sole exceptional way a missing clique color could dominate, namely by occupying the whole independent set.

A standalone exact minimax checker reconstructs the graph and both games for every tested profile with \(u\le4\), \(m\le5\), and order at most \(8\). It checks Alice wins at the claimed value and loses one palette size higher, for both starting conventions. It also directly enumerates representative completed colorings and verifies the terminal-color lemma. The replay output is:

`ALL CHECKS PASSED; game_profiles=30; terminal_colorings=299; max_order=8`

The finite computation is a stress test only. It does not certify parameters outside the tested range; those are covered by the proof.
