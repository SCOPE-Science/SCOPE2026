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
The verification is analytic.

Under the everywhere-equality boundary
\[
\frac{N}{|\Omega|}\beta\equiv\gamma,
\]
the reduced endemic equation in the corrigendum is
\[
d_I\Delta I+\beta I(dM-DI)=0,
\qquad
D=\frac{d_I}{d_S},
\qquad
d=D-1.
\]
Set
\[
q=\frac{dM}{D}.
\]
Then
\[
d_I\Delta I+D\beta I(q-I)=0.
\]
Multiplying by \(I-q\), integrating over \(\Omega\), and using the Neumann boundary condition gives
\[
-d_I\int_\Omega|\nabla I|^2
-D\int_\Omega\beta I(I-q)^2=0.
\]
For a positive solution both integrands are nonnegative before the minus signs, so equality forces \(I\equiv q\). Hence \(M=q\), while the definition of \(q\) gives \(q=(d/D)q\). Since \(D-d=1\), one obtains \(q=0\), contradicting positivity.

For a nonnegative growth gap that is not identically zero, the constant Rayleigh test gives a strictly positive principal eigenvalue of the infected linearization. This is the source's supercritical regime, so the corrigendum's existence and uniqueness results apply.

No numerical experiment is used in the proof.
