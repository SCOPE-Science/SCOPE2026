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

The exact comparison was checked algebraically from the stationary linearized matrix exponential.

For \(0<\alpha<\eta^2/4\), defining \(r_-=(\eta-\sqrt{\eta^2-4\alpha})/2\), \(r_+=(\eta+\sqrt{\eta^2-4\alpha})/2\), and \(q=\alpha/\eta\), the sign of \(R_2/R_1-1\) is the sign of
\[
F(\Delta)=r_+e^{-(r_--q)\Delta}-r_-e^{-(r_+-q)\Delta}-(r_+-r_-).
\]
The identities \(r_--q=r_-^2/\eta\) and \(r_+-q=r_+^2/\eta\) make \(F'\) a difference of two exponentials with exactly one zero. Since \(F'(0)>0\) and \(F(\infty)<0\), there is exactly one positive crossover.

At \(\alpha=\eta^2/4\), the ratio is \(e^{-s/4}(1+s/2)\) with \(s=\eta\Delta\). Its log derivative is \(1/(s+2)-1/4\), giving exactly one positive crossover. The quoted decimal \(5.0257248345\) is only a numerical evaluation of this proved scalar root, not part of the proof of uniqueness.

For \(\alpha>\eta^2/4\), \(R_2\) is a decaying sinusoid with bracket \(\cos(\omega\Delta)+(\eta/(2\omega))\sin(\omega\Delta)\). At every odd half-period the bracket is exactly \(-1\), while the matched first-order autocorrelation remains positive.

Limits: the verification does not test finite-window sample autocorrelation or nonlinear trajectories; those are outside the claim.
