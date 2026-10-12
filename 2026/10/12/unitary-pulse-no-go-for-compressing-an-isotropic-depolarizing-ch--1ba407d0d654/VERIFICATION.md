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

The channel identity was checked symbolically:
\[
X\rho X+Y\rho Y+Z\rho Z=2I-\rho,
\]
so the source's depolarizing map is
\[
\mathcal N_p(\rho)=\left(1-\frac{4p}{3}\right)\rho+\frac{2p}{3}I.
\]
This form commutes with every unitary conjugation.

For the continuous-time isotropic realization,
\[
\mathcal D_t(\rho)=e^{-\kappa t}\rho+\left(1-e^{-\kappa t}\right)\frac I2,
\]
both unitary covariance and \(\mathcal D_s\circ\mathcal D_t=\mathcal D_{s+t}\) hold exactly. Moving every pulse through the channel segments proves that only the net unitary remains outside the unchanged total depolarizing evolution.

Appendix C of arXiv:2605.16463v1 was checked against these identities. Its literal average is a linear image of a random-unitary input average. The balanced four-Pauli input average is \(I/2\). With the natural inverse pulse applied to each output branch, covariance makes every branch exactly the uncontrolled \(\mathcal N_p(\rho)\).

The source's printed high-frequency formula was checked independently:
\[
\lim_{f\to\infty}p\exp(-\gamma/f)=p.
\]
This arithmetic point is not used to prove the covariance no-go.

The cited dynamical-decoupling reference, arXiv:quant-ph/0609203v2, was inspected at its actual Hamiltonian and pulse model. It assumes a qubit coupled through \(\sigma_z\) to a bosonic bath with finite correlation time and describes \(T_2\)-type phase decoherence with no spin flips. That microscopic model contains the time correlations on which DD acts and is not the same mathematical object as the fixed isotropic depolarizing map.

The bundled checker re-evaluates representative matrix identities and the printed frequency limit. Those finite checks are corroborative only; the universal claim is analytic.
