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
The proof is analytic.

For the disease-free spatially constant subsystem,
\[
H(t)=
\frac{K_GH_0e^{r_Gt}}
{K_G+H_0(e^{r_Gt}-1)}.
\]
With the source values
\[
H_0=0.015,
\quad r_G=0.209,
\quad K_G=5.524,
\quad r_s=0.103,
\quad t_s=95,
\]
the bundled checker verifies
\[
H(t_s)\approx5.5239951659
\]
and
\[
-r_sH(t_s)\approx-0.5689715021<0.
\]

The checker also symbolically sums the four host equations and obtains
\[
\partial_tN
=
r_GN\left(1-\frac{N}{K_G}\right)
-2hr_s(H+L+I),
\]
and verifies that the first displayed Euler update after switching from \(h=0\) to \(h=1\) sends \(R=0\) to a negative value on the disease-free trajectory.

No simulation is used to infer the sign failure.
