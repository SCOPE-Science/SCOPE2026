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

The target theorem was checked in the publisher full text, including its definition of the pseudoinverse/right inverse and the full proof of Theorem 4.2. The counterexample was then evaluated symbolically:

\[
H=\mathbb C,\qquad \Lambda_1=2I,\qquad \Gamma_1=0,
\]
so \(A=B=4\), \(T_\Lambda=2I\), \(T_\Lambda^\dagger=\tfrac12I\), and the source threshold is exactly \(2\). The relative inequality is equality at \(\lambda=1\), while the perturbed lower frame energy is zero.

For the corrected statement, the only estimate used is
\[
\|U_\Gamma f\|\ge\|U_\Lambda f\|-\|(U_\Lambda+U_\Gamma)f\|,
\]
together with the corresponding upper triangle inequality and the reference frame bounds. This proves the claimed quantitative lower and upper bounds for every Hilbert-space \(g\)-frame under \(\lambda<1\). The zero-family example proves sharpness for universal guarantees at every \(\lambda\ge1\).

The open ESI version of Sun's stability theorem was inspected to compare implications. Its Theorem 3.1 contains the repaired result as the specialization with comparison family \(-\Gamma\), \(\lambda_1=\sqrt\lambda\), and \(\lambda_2=\mu=0\). Therefore the general perturbation principle is treated as prior art rather than as a new theorem.

No finite computation, numerical search, or extrapolation is part of the proof. The only unresolved literature risk is the possible existence of an unindexed source-specific correction.
