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
# Verification of the entropy–distance envelope

The theorem is proved analytically in RESULT.md; there are no auxiliary programs, numerical inputs, or external certificates. The following checks were independently reconstructed within the same scientific review:

- With conditional \(p_t\ge1/2\), the Bernoulli maximal coupling sets \(Y_t=1\) only on an \(X_t=1\) event of conditional probability \(1/(2p_t)\), giving fair output and mismatch \(p_t-1/2\).
- With conditional \(p_t<1/2\), all \(X_t=1\) events remain one and a fraction of zero events become one, giving fair output and mismatch \(1/2-p_t\).
- Conditioning on the complete strict past of \((X,U)\) gives the fair bit, which implies the joint output sequence has independent fair coordinates. Shift-equivariance gives an invariant joining.
- Concavity of the binary entropy function and monotonicity of the increasing inverse branch yield the direction of the bound; the two endpoint cases require no continuity extrapolation.
- The one-site marginal total-variation lower bound and iid optimal coupling prove equality for every prescribed entropy; the one-sided natural extension preserves the quantity.

This is a same-model mathematical check, not a claim of independent audit or formal proof certification. Limitation: a full classification of all equality cases and a higher-alphabet analogue are not established. Literature originality comparisons and their residual risks are recorded in REVIEW.md and AUDIT.json.
