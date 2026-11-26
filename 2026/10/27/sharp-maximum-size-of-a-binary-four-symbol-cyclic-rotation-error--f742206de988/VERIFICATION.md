---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

A nonidentity rotation preserves weight and must change at least two coordinates. Two windows at distance at least three share at most one coordinate, so their nonidentity outputs cannot coincide. The number of new outputs contributed by the latest window therefore depends only on it and the two preceding windows, and comparing their padded outputs on the joint six-bit string is exact. Splitting off the first two windows gives the correct five-bit initial states and suffix transition: for each terminal tb only at followed by b can be a predecessor, and its increment is independent of the earlier prefix. An independent bit-mask verifier (python3 /workspace/audit_evidence/rotation_ball_certificate.py) enumerated every full word at lengths 6 and 11, verified the displayed v6 and the shift of +11 for all 32 suffix states, and directly obtained bases [4,7,9,11,13,15,18] at lengths 4–10. The max-plus update commutes with adding the same scalar to every state, so this certifies the identity at all n≥6. The independent verifier checked the witness at 4 and 5 and the complete six-bit increment period [2,2,2,2,3], which repeats structurally and proves attainment at every length. There is no assumption of wraparound or allowance of shorter windows.

## originality

PASS

The same channel is prior work, and an exact maximum for this window size is available for q≥3, but the inspected results do not give this binary exact-window maximum. A strict superchannel and an adjacent window length likewise do not dominate this exact invariant.

## value

PASS

This is the worst-case neighborhood size of a previously motivated channel at a window length with genuine overlap at two different offsets. It quantifies how collisions depress the binary extremum below the simple count of rotations and the q≥3 extremum, and supplies a uniform extremal pattern. The exact maximum gives a precise local degree input for coding bounds; it is not presented as the optimum code size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
