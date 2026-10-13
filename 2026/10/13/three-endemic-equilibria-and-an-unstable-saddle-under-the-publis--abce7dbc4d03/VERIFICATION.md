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

It verifies for
\[
h(I)=I\left(1-\frac{3I}{(1+I)^2}\right)
\]
that
\[
h'(I)=1-\frac{6I}{(1+I)^3}
\]
and that the derivative is positive on the nonnegative half-line. It also verifies
\[
0<h(I)\le I=h'(0)I
\]
for \(I>0\).

With
\[
\Lambda=96,\quad
\pi=\frac12,\quad
\mu=1,\quad
\delta=2,\quad
\beta_b=\beta_v=\frac1{10},
\]
the checker obtains
\[
\mathcal R_0=\frac{16}{5}.
\]

The endemic-equilibrium residual factors exactly as
\[
-\frac{3I(I-2)(I^2-21I+11)}
{I^3+9I^2+21I+10}.
\]

At
\[
E_2=(45,45,2),
\]
the checker reconstructs
\[
J(E_2)=
\begin{pmatrix}
-\frac{16}{15}&0&-\frac52\\
0&-\frac{16}{15}&-\frac52\\
\frac1{15}&\frac1{15}&2
\end{pmatrix},
\]
with eigenvalues
\[
-\frac{16}{15},
\qquad
\frac{7-\sqrt{454}}{15},
\qquad
\frac{7+\sqrt{454}}{15}.
\]

It also verifies that the source proof quantity \(\widehat l_{33}\) equals \(-2\) at this equilibrium.

No numerical root-finding or simulation is needed for the accepted claim.
