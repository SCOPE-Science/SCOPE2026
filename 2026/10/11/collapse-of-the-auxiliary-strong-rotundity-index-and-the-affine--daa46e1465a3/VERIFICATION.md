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
The main identity is exact and requires no numerical approximation. For every norming pair \((x,x^*)\) and every \(y\in B_X\),
\[
d\!\left(y,(x^*)^{-1}(\{1\})\right)
=
1-x^*(y).
\]
The lower bound follows from \(\|x^*\|=1\); equality is attained by
\[
z_y=y+\bigl(1-x^*(y)\bigr)x.
\]
Infimizing over \(\|x-y\|\ge\epsilon\) proves
\[
\eta_X(\epsilon,(x,x^*))
=
\upsilon_X(\epsilon,(x,x^*)).
\]

Under symmetric Birkhoff orthogonality, writing
\[
y=x^*(y)x+w
\]
gives \(w\perp_B x\) and therefore
\[
\|w\|\le\|y\|.
\]
This yields
\[
\|x-y\|\le2-x^*(y)
\]
and the lower bound
\[
\eta_X(\epsilon)\ge\max\{0,\epsilon-1\}.
\]

For the affine-regular hexagon, `verify.py` checks that
\[
J(a,b)=(-b,a)
\]
maps the six dual vertices exactly onto the six primal vertices, verifies the canonical norming-functional reversal certificates for Birkhoff symmetry, and checks both explicit sharp witness families at all rational values
\[
\epsilon=\frac{k}{200},
\qquad
0\le k\le400.
\]
The finite grid is supplementary only; the formulas in `RESULT.md` prove the continuum profile.

No independent audit or independent validation has been performed.
