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

Let
\[
c_m=\cos\frac{\pi}{4m}.
\]
For the regular \(4m\)-gon \(P_m\) of Euclidean circumradius \(1\),
\[
c_mB_2\subseteq P_m\subseteq B_2.
\]
Hence
\[
N_m(z)\le\frac{\|z\|_2}{c_m}.
\]

For \(x,y\in S_{X_m}\),
\[
\|x+y\|_2^2+\|x-y\|_2^2
=
2\|x\|_2^2+2\|y\|_2^2
\le4,
\]
so
\[
J(X_m)\le\frac{\sqrt2}{c_m}.
\]

If \(m\) is odd and
\[
x=v_j,\qquad y=v_{j+m},
\]
then \(x\) and \(y\) are Euclidean orthogonal and the sum/difference directions are
\[
\frac{(2j\pm m)\pi}{4m}.
\]
Because \(m\) is odd, these are edge-normal directions. Their polygonal radial boundary distance is \(c_m\), so
\[
N_m(x+y)=N_m(x-y)=\frac{\sqrt2}{c_m}.
\]

If equality holds for any unit pair, then both Euclidean chord lengths are at least \(\sqrt2\). The parallelogram identity forces
\[
\|x+y\|_2=\|x-y\|_2=\sqrt2
\]
and
\[
\|x\|_2=\|y\|_2=1.
\]
The only unit-ball boundary points with Euclidean norm \(1\) are vertices, and equal Euclidean chord lengths force
\[
\langle x,y\rangle=0.
\]
Thus the equality set is exactly
\[
x=v_j,\qquad y=\pm v_{j+m}.
\]

No numerical sampling or external certificate is used as proof.
