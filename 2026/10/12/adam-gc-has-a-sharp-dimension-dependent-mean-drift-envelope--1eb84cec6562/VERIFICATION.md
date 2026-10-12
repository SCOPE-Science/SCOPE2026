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
The package verifies the first-step Adam-GC mean-drift theorem.

`verify.py` reconstructs bias-corrected Adam from zero moments, checks the closed mean-drift formula for randomized centered gradients, verifies the dimension-two cancellation, tests the sharp envelope through dimension \(64\), and confirms that the explicit extremal family approaches the stated supremum.

It also checks that centralizing the final adaptive update gives exactly zero component sum.

The finite computations are transcription guards. The sharp infinite-dimensional-family statement for each fixed finite \(d\) is proved analytically in `RESULT.md`.
