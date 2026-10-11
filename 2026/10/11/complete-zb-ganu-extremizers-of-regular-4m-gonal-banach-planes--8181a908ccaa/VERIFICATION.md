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

For
\[
c_m=\cos\frac{\pi}{4m},
\]
the radial equation of each polygon edge gives
\[
E(z)\le N_m(z)\le\frac{E(z)}{c_m}.
\]
The lower equality occurs exactly on vertex rays and the upper equality exactly on edge-normal rays.

Therefore
\[
\frac{N_m(x+y)N_m(x-y)}{N_m(x)^2+N_m(y)^2}
\le
\frac{E(x+y)E(x-y)}
{c_m^2(E(x)^2+E(y)^2)}
\le\frac1{c_m^2}.
\]
The second equality is equivalent to \(\langle x,y\rangle=0\). Equality in the full chain additionally forces \(x,y\) to be vertex-ray vectors and \(x\pm y\) to be edge-normal vectors.

After a dihedral symmetry,
\[
x=a(1,0),\qquad y=b(0,1).
\]
Then the edge-normal condition is exactly
\[
\left|\frac ba\right|
=
\tan\frac{(2j+1)\pi}{4m},
\qquad j=0,\ldots,m-1.
\]
These conditions are also sufficient, proving both the complete equality set and
\[
C_Z(X_m)=\sec^2\frac{\pi}{4m}.
\]

Direct numerical stress tests for \(m=1,\ldots,6\) reproduced the predicted values and equality ratios, but no finite experiment is used to justify the quantified theorem.
