---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For logits W h_theta, p_i^alpha normalized is exactly softmax(alpha W h)_i. With V=alpha W, d[alpha^-1 CE(alpha W,theta)]/dW=(p_alpha-y)h^T and d/dtheta=J_h^T W^T(p_alpha-y), matching the specified PowerGrad pseudo-backward rule in BOTH blocks. Transforming the update by V=alpha W yields eta_V=alpha eta_W and eta_theta^CE=eta_theta/alpha, hence exact ratio alpha^-2 for equal step sizes and identical fixed-feature class predictions. Independently checked random softmax probabilities, centered finite differences and 15 exact matched SGD steps. Alpha=0, non-linear final heads, optimizer momentum/adaptive state excluded.

## originality

PASS

Best-of-knowledge structural novelty is the explicit full head/body conservative surrogate and reciprocal two-block SGD conjugacy, not the known powered-softmax=temperature identity. The origin paper distinguishes backward tampering and forward temperature but does not integrate the complete vector field or calculate the alpha^-2 relative-rate effect. Full relevant sections were read; unindexed equivalent derivation remains possible.

## value

PASS

Identifies the mathematically exact objective behind a nominally non-conservative altered-backward procedure and an operationally meaningful alpha^-2 head/body learning-speed shift in trainable networks. The fixed-feature boundary explains which dynamics are merely reparameterized; this is a motivated optimizer-mechanism characterization, not an unmotivated scalar substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
