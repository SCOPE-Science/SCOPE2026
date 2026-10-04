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

The equality-critical polynomial from the high-support branch is
\[
f(w,z)=28z^2(w^2-3w+2)+20zw(2-w)+w^2(7w^2+3w-34).
\]
Direct expansion gives
\[
f(w,z)=(w-2)q(w,z),
\]
with
\[
q(w,z)=7w^3+17w^2+28wz^2-20wz-28z^2.
\]
After completing the square,
\[
q(w,z)=28(w-1)\left(z-\frac{5w}{14(w-1)}\right)^2+
\frac{w^2(7w-8)(7w+18)}{7(w-1)}.
\]
The relevant root \(w_0\) of
\[
w^3+w^2-2w-4=0
\]
satisfies \(w_0>8/7\): the polynomial equals \(-1196/343\) at \(8/7\), while its derivative is positive and increasing from that point onward. Hence \(q(w,z)>0\) throughout the high branch, so the sharp value requires \(w=2\).

For the low branch,
\[
\frac4{21}-\operatorname{cen}_y(P_w)
=-\frac{(w-2)(7w^3+17w^2+8w-28)}{21w(w^2+3w+4)}.
\]
The cubic factor is already \(4\) at \(w=1\) and has positive derivative for \(w\ge1\), while \(w<2\) on the low branch. The deficit is therefore strict.

The normalized candidate extremizer
\[
P_*=\operatorname{conv}\{(0,2),(-2,0),(-1,-1),(1,-1),(2,0)\}
\]
has exact shoelace area \(7\) and centroid \((0,4/21)\).

The embedded `verify.py` replays these algebraic identities with exact rational arithmetic. Polynomial equalities are certified on interpolation grids larger than their degree bounds, and the shoelace computation is exact. The replay output is

`VERIFY_OK centroid-hexagon equality rigidity`

Finite replay is not used as a substitute for the geometric proof. The final reversal of Steiner symmetrization uses convexity of the horizontal endpoint functions and the three fixed slice widths forced by the inscribed hexagon.
