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
Put
\[
r=\sqrt2-1,
\qquad
b=r^2,
\qquad
c=2\sqrt2-1.
\]
After the dihedral reduction
\[
x=(1,a),
\qquad
-r\le a\le r,
\]
and after exchanging \(z\) with \(x-z\) when needed, the complete feasible branch list is
\[
z=(r-a,1+a),
\qquad
-r\le a\le-b,
\]
\[
z=
\left(
\frac{1-a}{2},
\frac{1+2r+a}{2}
\right),
\qquad
-b\le a\le b,
\]
and
\[
z=(1-r-a,1),
\qquad
b\le a\le r.
\]

For the first branch,
\[
N_8(2x-z)=c,
\qquad
N_8(x+z)=\sqrt2-a.
\]
For the middle branch,
\[
N_8(2x-z)=\frac{2+r-a}{\sqrt2},
\qquad
N_8(x+z)=\frac{2+r+a}{\sqrt2}.
\]
For the third branch,
\[
N_8(2x-z)=\sqrt2+a,
\qquad
N_8(x+z)=c.
\]
The interval bounds give both target lengths at most \(c\).

The bundled `verify.py` reconstructs intersections of all pairs of octagonal edges on a finite parameter grid, checks the three branch formulas and their exchanged points, and verifies the sharp pair and the three derived constants. The finite grid is supplementary; the analytic edge list and formulas above prove the full continuum statement.

No independent audit or independent validation has been performed.
