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

`verify.py` implements the displayed transitions directly. Exact breadth-first search on the power automaton verifies the shortest reset length, total number of shortest paths to singleton subsets, and target distribution for every integer \(5\le n\le16\). It obtains exactly four shortest reset words in every checked case, with two ending at state \(1\) and two at state \(4\).

The same program separately constructs the four formula words \(x c (b c^{n-1})^{n-4} b c y\), checks their lengths, and replays them state-by-state for every integer \(5\le n\le100\). The finite checks end with `VERIFY_OK`.

The computation is only a bounded verification. The universal statement for all \(n>4\) depends on the symbolic equality-case proof in `RESULT.md`, especially the source lower bound on proper merges and transport occurrences.
