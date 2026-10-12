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
The proof is analytic; the checker replays finite consequences.

For the one-dimensional Dirichlet matrix
\[
T_n=\operatorname{tridiag}(-1,2,-1),
\]
the continuants satisfy
\[
D_0=1,\qquad D_1=1+2s,\qquad
D_k=(1+2s)D_{k-1}-s^2D_{k-2}.
\]
The boundary inverse diagonal is
\[
d_n(s)=D_{n-1}(s)/D_n(s).
\]

The completed three-dimensional Douglas–Rachford step is
\[
R_{\mathrm{DR}}
=
I+3P_xP_yP_z-P_xP_y-P_xP_z-P_yP_z.
\]
On a cube the sharp condition is
\[
d_n(s)\ge\frac23.
\]

The embedded `verify.py` performs the following checks using the Python standard library only:

1. exact construction of \(P_2(7/25)\);
2. exact construction of the full \(8\times8\) step matrix;
3. certification that its minimum entry is
\[
-\frac{3241875}{3189506048};
\]
4. exact verification of the \(n=2\) threshold polynomial;
5. bisection of several \(\tau_n\) values and verification that they increase toward
\[
(3-\sqrt6)/2.
\]

Finite replay is corroborative only. The all-\(n\) and rectangular if-and-only-if statements follow from the displayed tensor-entry proof, not from enumeration.

Unproved limits include nonhomogeneous boundary forcing, nonrectangular domains, variable coefficients, intermediate-stage positivity, and later Douglas-type ADI variants.
