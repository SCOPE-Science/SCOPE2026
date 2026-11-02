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

# Reproducibility

Run `python3 VERIFY.py` with Python 3.9+ from the directory containing the extracted files. The script requires only Python's standard library. `verification_output.txt` records the actual execution.

The checker implements separate cyclic-edge and endpoint formulas for the exact minimum number of common zero insertions. It constructs minimum-padding witnesses and verifies that the two resulting binary words are cyclic rotations. It also independently enumerates every possible padding allocation for lengths \(3\) through \(8\) and checks every ordered pair of weight-two words in that range. For larger parameters, it checks all ordered pairs through length \(18\) against the formulas and construction, and uses a fixed-seed sample of \(10{,}000\) pairs at lengths up to \(199\).

The actual execution reported `VERIFICATION_OK`, including \(93{,}992\) formula/construction comparisons and \(1{,}595\) exhaustive padding enumerations. The general claim relies on the proof in `RESULT.md`, not finite testing. An independent mathematical audit has not been performed.
