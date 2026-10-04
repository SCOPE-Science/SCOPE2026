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
The analytic checks are:

- characteristics of the printed Section 4.2 equation give
  \[
  I(\rho,t)=\eta e^{-\rho}S(t-\rho)Q(t-\rho);
  \]
- the disease-free characteristic equation is
  \[
  z+q=(1-\gamma)\eta S_0e^{-\rho}e^{-z\rho};
  \]
- this delay equation is linearly stable exactly when
  \[
  (1-\gamma)\eta S_0e^{-\rho}<q;
  \]
- a deterministic fixed latent period has no continuous progression loss before age \(\rho\), yielding
  \[
  \mathcal R_{\mathrm{fix}}=\frac{S_0\eta(1-\gamma)}q.
  \]

The bundled checker replays the source values \(S_0=10\), \(\eta=0.59\), \(\rho=3\), and \(1/q=1.61\). It verifies
\[
\mathcal R_{\mathrm{sim}}(0)\approx0.4729273624,
\]
\[
\mathcal R_{\mathrm{fix}}(0.75)=2.37475,
\]
and
\[
\gamma_c\approx0.8947257606.
\]

The general stability result is analytic; finite numerical checks are not used as an infinite-dimensional proof.
