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

# Verification instructions and limits

Run `python3 verify_transfer.py` and `python3 verify_direct.py` in the extracted directory with Python 3; no packages are required. `transfer_output.txt` and `direct_output.txt` are the outputs from actually executing those scripts, not synthetic examples.

The transfer calculation uses every one of 256 four-column binary-color states and enumerates every permissible shift, finding exactly 160 arcs. An explicit strongly-connected-component calculation identifies only two loops and two length-five directed cycles capable of closed walks. For a closed walk of length \(n\), those yield exactly two or twelve admissible labelled colorings as in the theorem. Extra checks cover orders \(5\) through \(30\) and selected higher orders including \(100\) and \(101\).

The independent direct implementation enumerates all \(2^n\) outer-layer color choices for each \(5\le n\le19\); each outer choice forces all spoke discrepancy bits and hence all inner colors, unless the outer constraint fails. It checks each inner condition and compares *the complete computed solution set* with the proposed templates. This tests all small cases exhaustively and makes no claim about unexecuted infinite computation.

The general theorem is established by the independent symbolic proof in `RESULT.md`: the opposite-edge outer indicators have period five, only six binary patterns survive the one-opposite-neighbor constraints, and each integrates to exactly two valid colorings. No stronger claim about all perfect matchings or all quotients is being made.
