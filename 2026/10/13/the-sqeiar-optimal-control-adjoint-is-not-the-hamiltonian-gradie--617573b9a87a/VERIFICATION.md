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
The bundled checker reconstructs the Hamiltonian symbolically with
\[
N=S+Q+E+I+A+R,
\qquad
F=\beta e^{-(u_1I+u_2A)/N}\frac{S(I+\theta A)}{N}.
\]

It verifies the exact state derivatives
\[
F_Q=F_E=F_R=F\frac{U-N}{N^2}
\]
and the corresponding formulas for \(F_S\), \(F_I\), and \(F_A\).

It verifies all six corrected adjoint equations by checking equality with
\[
-\frac{\partial H}{\partial(S,Q,E,I,A,R)}.
\]

It separately verifies that the source's printed recovered costate omits
\[
(\lambda_1-\lambda_3)F_R,
\]
that the susceptible quarantine term must involve \(\lambda_1-\lambda_2\), and that the exposed costate contains \(\sigma\rho(\lambda_5-\lambda_4)\).

An exact positive interior witness confirms that the omitted recovered-costate derivative is nonzero. No numerical optimal-control trajectory is used to establish the correction.
