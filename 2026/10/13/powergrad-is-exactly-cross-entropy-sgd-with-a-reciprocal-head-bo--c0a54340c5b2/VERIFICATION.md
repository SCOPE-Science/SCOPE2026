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
The package checks the PowerGrad identities on randomly generated multiclass models.

`verify.py` confirms that powered-and-renormalized softmax equals softmax of scaled logits, compares the analytic PowerGrad head and feature gradients with centered finite differences of \(\Psi_\alpha(W,\theta)=\alpha^{-1}\mathcal L(\alpha W,\theta)\), and verifies the exact one-step head/body learning-rate conjugacy.

It also runs a fixed-feature minibatch trajectory and verifies at every step that the matched ordinary cross-entropy classifier satisfies \(V_t=\alpha W_t\) and has identical predictions.

Finite numerical checks are transcription guards only. The all-dimensional identities are established by the chain-rule proof in `RESULT.md`.
