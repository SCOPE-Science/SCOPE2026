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

The claim has two exact components.

First, the scalar equation \(\dot w=x-bw\) gives the variation-of-constants identity
\[
w(t)=e^{-b(t-t_0)}w(t_0)+\int_{t_0}^{t}e^{-b(t-s)}x(s)\,ds.
\]
For \(b>0\), bounded complete lifts therefore have the unique memory representation \(w(t)=\int_0^\infty e^{-bs}x(t-s)\,ds\). Two lifts above the same base orbit differ by \(e^{-bt}\) times a constant, so compactness in both time directions forces that constant to vanish. This verifies the graph and conjugacy step.

Second, on either smooth branch of \(|x|\), the Jacobian has a zero upper-right block and lower-right entry \(-b\). The packaged `verify.py` constructs both branch Jacobians symbolically and checks
\[
\det(\lambda I-J_4)=(\lambda+b)\det(\lambda I-J_3).
\]
It also verifies that the first three equations contain neither \(w\) nor \(b\), and that the vertical difference equation has the exact solution \(e^{-bt}\). Running the packaged file returns `VERIFY_OK`.

On a compact complete trajectory, \(x=0\) cannot occur with \(y=0\): otherwise uniqueness fixes \(x=y=0\) while \(z(t)=z(0)-at\), contradicting compactness. Hence every \(x=0\) crossing is transverse. The continuous vector field has identity saltation at such a crossing, so the piecewise variational cocycle preserves the same vertical invariant line and quotient cocycle.

Limits: no numerical integration is used as proof; no classification of the base attractor is asserted; no claim is made about finite-time Lyapunov estimates. The spectral conclusion is for asymptotic tangent exponents of compact regular ergodic invariant measures.
