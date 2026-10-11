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

The primary input is the one-direction theorem: the stated \(\sigma_m\)-ordering along chords parallel to a unit direction \(e\) forces a reflection plane orthogonal to \(e\).

After translating the common centroid to the origin, reflection with unit normal \(e\) is
\[
R_e=I-2ee^T.
\]
For
\[
e_1=(1,0,0),\qquad e_2=(3/5,4/5,0),
\]
the exact product is
\[
R_{e_2}R_{e_1}=
\begin{pmatrix}
-7/25&-24/25&0\\
24/25&-7/25&0\\
0&0&1
\end{pmatrix}.
\]
Thus it is a \(z\)-axis rotation through \(2\theta\), where \(\cos\theta=3/5\). If \(\theta/\pi\) were rational, \(e^{i\theta}\) would be a root of unity and \(2\cos\theta=6/5\) a rational algebraic integer, a contradiction. Hence the cyclic rotation subgroup is dense in all \(z\)-axis rotations.

For
\[
e_3=(0,1,1)/\sqrt2,
\]
the exact reflection sends \((0,0,1)\) to \((0,-1,0)\). Conjugation therefore supplies the complete \(y\)-axis rotation group. The standard \(z\)-\(y\)-\(z\) Euler decomposition gives all of \(SO(3)\).

The bundled checker verifies the reflection matrices, the rotation entries, and the third-axis image using exact symbolic arithmetic. Density and Euler generation are analytic group facts, not conclusions from finite computation.

For sharpness, the analytic proof uses the full family
\[
\frac{\langle x,a\rangle^2}{\rho^2}+
\left|x-\langle x,a\rangle a\right|^2\le1,
\qquad \rho\ne1,
\]
with \(a\) chosen perpendicular to any prescribed pair of directions. Reflection in either corresponding normal plane fixes this quadratic form, so chord-endpoint curvatures agree exactly.
