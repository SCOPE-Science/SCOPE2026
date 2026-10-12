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
The bundled checker reconstructs a three-state parameter set that lies outside the extra sign condition in the published multi-state theorem.

It uses
\[
\beta(N)=e^{-2(N-1)},
\qquad
N_0=1,
\qquad
\mu=0,
\qquad
\kappa_i=0,
\]
with
\[
(p_1,p_2,p_3)=(0.3,0.4,0.3),
\qquad
(\gamma_1,\gamma_2,\gamma_3)=(0.2,1,5).
\]
The equilibrium fractions are exactly
\[
(0.5,0.4,0.1),
\]
and the three sign-test quantities in the source are
\[
\frac23,\quad0,\quad-\frac23.
\]
Hence the printed sufficient condition does not apply.

The exact Jacobian has eigenvalues
\[
-2,\qquad
\frac{-18+8\sqrt3}{5},\qquad
\frac{-18-8\sqrt3}{5},
\]
all negative.

The general finite-\(n\) result is analytic rather than experimental. It follows from the exact characteristic factorization and the positive-real calculation on the closed right half-plane; the finite checker is only a strictness witness and algebra replay.
