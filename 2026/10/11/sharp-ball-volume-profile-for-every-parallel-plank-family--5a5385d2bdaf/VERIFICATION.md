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

For parallel planks with common unit normal \(u\), rotate so that \(u=e_1\). If \(E\subset[-1,1]\) is the union of their normal-coordinate intervals inside the ball, then
\[
|E|\le W
\]
and
\[
\operatorname{vol}_d(B^d\cap\cup_iP_i)
=
\kappa_{d-1}\int_E(1-t^2)^{(d-1)/2}\,dt.
\]
The integrand is even and strictly decreases in \(|t|\), so symmetric decreasing rearrangement gives the centered interval of the same measure; using all available measure gives \([-W/2,W/2]\).

The exact normalized optimum is
\[
I_{W^2/4}\!\left(\frac12,\frac{d+1}{2}\right).
\]
In dimensions two and three this becomes, respectively,
\[
W\sqrt{1-\frac{W^2}{4}}+2\arcsin\frac W2
\]
and
\[
\pi\left(W-\frac{W^3}{12}\right).
\]

For the stability statement, equal measure of \(E\) and the centered interval makes the removed and added masses both equal to \(\delta\). Monotonicity of the slice density forces the least possible deficit to exchange two inner boundary layers of total measure \(\delta\) with the two immediately adjacent exterior layers of the same total measure. This gives the displayed sharp integral law.

`verify.py` numerically reconstructs these identities from the slice density, tests deterministic random interval unions in dimensions \(2\) through \(10\), and checks the layer-swap equality cases. These computations are diagnostic only; the proof is the exact rearrangement argument above.
