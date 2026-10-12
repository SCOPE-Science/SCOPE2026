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

The standalone Python/SymPy checker `verification/verify.py` reconstructs the infected comparison matrix \(Q=D^{-1}C\) from the equations and verifies exactly
\[
\det(zI-Q)=z(z^2-\mathcal R_0).
\]
For a fully rational instance it verifies \(\mathcal R_0=1/24\), the positivity of \((I-Q)^{-1}{\bf1}\), the strict supersolution identity, and the negative classical-order eigenvalue condition.

The general infinite-dimensional-in-time statements are analytic. In particular, the scalar resolvent identities and the asymptotic
\[
E_\nu(-at^\nu)\sim\frac{t^{-\nu}}{a\Gamma(1-\nu)}
\]
for \(0<\nu<1\) yield nonnegative kernels of mass \(1/a\) and nonintegrable homogeneous time tails. The proof then uses a vector limsup inequality and Tonelli's theorem to propagate divergence through the source network. This establishes the all-time statements for **every** admissible real order tuple, not by extrapolation of simulations or by a finite search.

The exact positive-rate witness uses
\[
(b,d,\beta,\sigma,p,\theta,\kappa,r_I,r_A,r_T)
=(2,1,1/5,1,1/2,1/2,1/2,1/2,1/2,1/2),
\]
initial state \((2,1,0,0,0,0)\), and unequal orders \((3/4,1/2,2/3,3/5,4/5,7/10)\). It belongs strictly to the verified subcritical regime and has a nonzero exposed infection seed. No independent audit has been performed.
