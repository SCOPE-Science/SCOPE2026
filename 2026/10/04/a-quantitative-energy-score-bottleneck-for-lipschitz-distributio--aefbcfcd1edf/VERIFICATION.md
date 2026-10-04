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
The theorem is analytic. No simulation, finite enumeration, or numerical optimizer is used to establish it.

The following checks were reconstructed from the stated assumptions.

1. **Translation separation.** For \(P_x=\operatorname{Law}(x+Z)\), direct cancellation of the two within-law terms gives
\[
\mathcal D^2(P_{Ru},P_{-Ru})=2\mathbb E\!\left[\|Z-Z'+2Ru\|-\|Z-Z'\|\right].
\]
The triangle inequality yields the upper bound \(4R\). Energy distance is a metric, and no finite probability law can be invariant under a nonzero translation, so every direction has positive separation; continuity on the compact sphere gives \(\Delta_\mu(R)>0\).

2. **Topological collision.** Since \(q<p\), padding the encoder with zero coordinates if necessary gives a continuous map from \(S_R^{p-1}\) to \(\mathbb R^{p-1}\). Borsuk--Ulam supplies \(x\) with \(e(x)=e(-x)\).

3. **Endpoint score regret.** The common predictive law at that pair is \(Q\). The metric triangle inequality for \(\mathcal D\) implies one endpoint has energy-score regret at least \(\Delta_\mu(R)/8\).

4. **Lipschitz propagation.** Same-noise coupling gives
\[
W_1(Q_z,Q_x)\le L_eL_d\|z-x\|.
\]
The target--prediction cross term changes by at most \((1+L_eL_d)\|z-x\|\), while the predictive self-distance contributes at most another \(L_eL_d\|z-x\|\). Thus regret changes by at most \((1+2L_eL_d)\|z-x\|\).

5. **Cap integration.** With \(\rho=\Delta_\mu(R)/(16(1+2L_eL_d))\), the regret stays at least \(\Delta_\mu(R)/16\) on the chordal cap of radius \(\rho\). Its normalized surface mass is
\[
\frac12 I_{(\rho/R)^2-(\rho/R)^4/4}\!\left(\frac{p-1}{2},\frac12\right),
\]
which is exactly the factor in the theorem.

6. **Boundary normalization.** If \(\mu=\delta_0\), then \(\mathcal D^2(\delta_x,\delta_{-x})=4R\), recovering the stated noiseless formula. The small-cap expansion has exponent \(p-1\), yielding the necessary \((1+2L_eL_d)^{-(p-1)}\) order.

Scientific limits: the lower-bound constant is not asserted minimax-optimal, and the proof does not certify any claim outside the stated sphere/translation/Lipschitz setting.
