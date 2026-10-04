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
The theorem is proved analytically from the printed ODEs.

The bundled checker verifies:

- the source reproduction-number identity
  \[
  \zeta_1\mathcal R_0
  =\beta S_*\left(1+\frac p{\zeta_2}+\frac{q\epsilon}{\zeta_3}\right);
  \]
- exact differentiation of
  \[
  \mathcal L=E+\frac{\beta S_*}{\zeta_2}A+\frac{\beta\epsilon S_*}{\zeta_3}V;
  \]
- the resulting identity
  \[
  \dot{\mathcal L}=\beta(S-S_*)h+\zeta_1(\mathcal R_0-1)E;
  \]
- positivity of the determinant of the homogeneous hospital/ICU block after expansion into positive rate products.

The checker does not infer global stability from finite trajectories. LaSalle invariance, the stable downstream cascade, and the Lyapunov-stability estimate are established in the proof.
