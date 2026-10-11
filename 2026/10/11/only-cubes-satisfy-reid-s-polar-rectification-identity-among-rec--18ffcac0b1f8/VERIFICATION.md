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

For the cube
\[
C=[-1,1]^3,
\]
the twelve edge midpoints are the sign-permutations of
\[
(1,1,0).
\]
Their convex hull is
\[
C\cap\{x:|x_1|+|x_2|+|x_3|\le2\}.
\]
Diagonal scaling by \(\operatorname{diag}(a,b,c)\) gives the exact box rectification formula used in the proof.

For the three facet points, the scaled-polar boundary functionals are
\[
L_1=\frac{4a^2+3b^2+3c^2}{5},
\quad
L_2=\frac{3a^2+4b^2+3c^2}{5},
\quad
L_3=\frac{3a^2+3b^2+4c^2}{5}.
\]
Their differences are exactly
\[
L_1-L_2=\frac{a^2-b^2}{5},
\qquad
L_2-L_3=\frac{b^2-c^2}{5}.
\]
Thus one common \(\lambda\) forces \(a=b=c\).

`verify.py` enumerates the cube edges, confirms the twelve distinct edge midpoints, checks their cuboctahedral constraints, and checks the exact rational obstruction for the box with half-lengths \((1,2,3)\).

The computation is diagnostic only. The all-parameter theorem is the exact boundary-facet argument in the proof.
