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

For a two-piece hyperplane division, the proof first establishes the exact identity between the max-min inradius and the largest radius of two equal disjoint balls in the body.

For the orthotope
\[
R=\prod_i[0,L_i],
\]
a radius-\(r\) ball center lies in
\[
R_r=\prod_i[r,L_i-r].
\]
Thus two such balls fit exactly when
\[
D(R_r)^2-4r^2
=
\sum_i(L_i-2r)^2-4r^2
\ge0.
\]
The checker reconstructs this quadratic, verifies exact monotonicity bounds on rational test families, checks the branch transition at \(r=\ell/2\), and compares the closed form against direct bisection of the feasibility inequality on deterministic multidimensional examples.

It also verifies the cube identity
\[
\sqrt d\,(1-2r)=2r
\]
for
\[
r=\frac{\sqrt d}{2(\sqrt d+1)},
\]
and the rectangle transition at aspect ratio \(2\).

The embedded `verify.py` was replayed from its actual package path. The replay output was:

`VERIFY_OK orthotope max-min inradius profile`

Finite computations are consistency checks only. The proof in `RESULT.md` establishes the formula and optimizer classification for every dimension \(d\ge2\) and every positive orthotope side-length vector.
