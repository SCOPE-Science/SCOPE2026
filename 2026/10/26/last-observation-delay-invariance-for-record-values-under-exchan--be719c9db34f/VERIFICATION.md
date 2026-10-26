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

# Verification evidence

The analytical certificate is the threshold-defined, coordinate-exchange involution given in `RESULT.md`; its pointwise identities do not assume continuous observations. The proof separately derives the iid atomless covariance and correlation, including their exact boundary case.

Run `python verify.py` with Python 3. The code uses only the standard library and exhaustive deterministic iteration over ternary words at sizes two through seven, distinct-rank permutations at sizes two through eight, all eligible selected-index prefixes and adjacent moves, all joint distribution count arrays for distinct-rank permutations through length seven, and exact rational covariance checks through length eight.

Observed successful checker output:

`VERIFY_OK 49508 full words; 21170019 exact identity checks; ties and distinct ranks`

The enumeration is finite, not an exhaustive proof for arbitrary \(n\) or all exchangeable laws. The analytical measure-preserving involution proves the unrestricted result. There is no independent mathematical or historical-priority audit.
