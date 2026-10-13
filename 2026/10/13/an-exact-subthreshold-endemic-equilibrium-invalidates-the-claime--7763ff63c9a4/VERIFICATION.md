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
The bundled checker uses exact symbolic arithmetic.

For
\[
\Lambda_h=\frac{871}{5000},\quad
\Lambda_v=\frac{121}{400},\quad
\mu_h=\frac1{10},\quad
\mu_v=\frac12,
\]
\[
\beta_1=\beta_2=1,\quad
\alpha_1=\alpha_2=\frac1{10},\quad
\delta_h=\frac1{10},\quad
\gamma=2,\quad
u=1,\quad
b=20,
\]
it verifies that
\[
E_*=
\left(
\frac{1313}{1500},
\frac1{10},
\frac23,
\frac{101}{200},
\frac1{10}
\right)
\]
annihilates all five right-hand sides.

It verifies
\[
R_0^2=\frac{9581}{10000}<1,
\]
and the source-region bounds
\[
S_h+I_h+R_h<\frac{\Lambda_h}{\mu_h},
\qquad
S_v+I_v=\frac{\Lambda_v}{\mu_v}.
\]

The positive-equilibrium reduction factors exactly as
\[
-\frac{
I_h(10I_h-1)(286420I_h-4609)
}{
50(20I_h+1)(14321I_h+1000)
}.
\]

Finally, the expression printed as the source's equation (3.8) evaluates at the equilibrium to
\[
-\frac{264869}{3030000},
\]
whereas the true orbital derivative along an equilibrium trajectory is zero.

No numerical approximation is needed for the accepted claim.
