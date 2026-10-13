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

For
\[
|\Omega_1\rangle=q_0(|000\rangle+|011\rangle)+q_2(|101\rangle+|110\rangle)+q_4|111\rangle,
\]
direct partial traces give
\[
\det\rho_A=q_0^2(4q_2^2+q_4^2),
\qquad
\det\rho_B=\det\rho_C=(q_0^2+q_2^2)^2+q_0^2q_4^2.
\]
Their difference is exactly
\[
(q_0^2-q_2^2)^2.
\]
The normalization converts the \(C^2\) printed in Eq. (39) to \(4\det\rho_A\), so that equation's right-hand side is \(S(\rho_A)\). The coarse-graining theorem requires \(E_{MB}\ge S(\rho_B)\). Since trace-one qubit entropy is strictly increasing with determinant, every \(q_0\ne q_2\) member contradicts Eq. (39).

The bundled `verify_counterexample.py` uses exact `Fraction` arithmetic for the squared coefficients of the explicit witness. It verifies normalization, the determinants \(18/125\) and \(117/500\), the positive determinant gap, and the numerical entropy values quoted in the result. The universal parameter statement is proved analytically above rather than by finite computation.

No independent audit has been performed.
