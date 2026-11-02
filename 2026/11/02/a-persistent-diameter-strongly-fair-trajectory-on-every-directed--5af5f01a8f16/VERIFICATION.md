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

The derivation has four independently checkable steps: (1) exact ideal singleton rotation by the ordered pair of full-copy maps; (2) exact repeated-activation residual \((1-p_i)^N\); (3) sup-norm error accumulation below \(1/8\) and untouched zero/unit anchors at every intermediate activation; (4) two-agent gap contraction at every action by a factor bounded strictly below one. The proofs handle every integer \(n\ge3\), arbitrary strictly interior fixed weights, and infinitely many activations.

Run `python verify_cycles.py` with Python 3; no third-party packages are required. It checks ideal support and anchors, chooses finite block lengths by rational inequalities, asserts the bound on every individual update for sizes \(3,4,5,7\) and two full rotations, and verifies contraction on the bidirected two-vertex case. Its finite reach cannot replace the general nonexpansive/series proof and does not test randomized schedules or source priority.

Independent scientific validation has not been performed.
