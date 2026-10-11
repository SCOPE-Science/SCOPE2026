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
The verification target is
\[
S_P(X_{12})=\frac{2-\sqrt3}{2}
\]
for the regular dodecagonal norm displayed in `RESULT.md`.

`verify.py` works with exact elements \(a+b\sqrt3\), where \(a,b\in\mathbb Q\). It constructs the twelve signed facet functionals and derives all twelve unit-ball vertices from adjacent facet intersections. It then verifies for every ordered facet pair \(f,g\) that
\[
\|f+\sqrt3g\|_*+\|f-\sqrt3g\|_*\le4
\]
and the swapped companion inequality. It reproduces the seven dihedral separation cases listed in the proof.

The checker next verifies all six vertices of the feasible \((A,B)\)-polygon and checks exactly that the quadratic
\[
A^2+B^2-(2-\sqrt3)AB
\]
is at most \(4\) there. Finally, it checks that
\[
x=(1,2-\sqrt3),\qquad y=(-1,2-\sqrt3)
\]
are unit vectors and attain the P-angle cosine \((2-\sqrt3)/2\).

The continuum upper bound is not inferred from enumeration or sampling. It follows from the dual inequalities and convexity argument in `RESULT.md`; the script certifies only the finite polyhedral computations used by that analytic proof.

No independent audit or independent validation has been performed.
