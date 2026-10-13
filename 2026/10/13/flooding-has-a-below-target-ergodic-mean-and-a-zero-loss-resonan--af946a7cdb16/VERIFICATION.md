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
The package reconstructs full-batch Flooding on the scalar quadratic \(f(x)=a x^2/2\).

`verify.py` checks the exact multiplicative update, the logarithmic rotation relation, finite entry into the invariant band, the golden-ratio period-three resonance, and the \(h=1\) finite-time zero-loss collapse outside the exact boundary-hit set.

For an irrational rotation number it numerically checks the predicted long-run fraction of iterates above the flood level and the exact arithmetic mean raw loss.

Finite simulations are transcription guards only. The circle conjugacy, ergodic formulas, and endpoint classification are proved analytically in `RESULT.md`.
