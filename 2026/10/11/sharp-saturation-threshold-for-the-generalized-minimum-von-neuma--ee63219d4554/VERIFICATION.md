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
The verification target is the geometric lemma underlying the threshold:
\[
x,y,z\in B_{X_8},\quad
N_8(x-z)=N_8(x+y)=2
\quad\Longrightarrow\quad
N_8(y-z)\ge\sqrt2.
\]

`verify.py` represents \(\mathbb Q(\sqrt2)\) exactly using rational pairs. It constructs all eight regular-octagon vertices and all eight signed facet functionals. It checks every ordered pair of facets that can be simultaneously tight at a unit-ball point.

For equal facets, the same support functional gives the stronger separation \(2\). For every distinct incident pair, the checker searches the signed facet functionals and certifies one whose affine value on every endpoint pair of the two relevant exposed edges is at least \(\sqrt2\). Because a linear functional attains its minimum on a product of line segments at endpoint pairs, this is an exact certificate for the entire exposed-face product.

The checker also verifies exactly
\[
x=(1,\sqrt2-1),\qquad
y=(\sqrt2-1,1),\qquad
z=(-1,\sqrt2-1),
\]
with
\[
N_8(x-z)=N_8(x+y)=2,\qquad
N_8(y-z)=\sqrt2,
\]
and checks the algebraic inequalities used by the inward endpoint approximation.

The transfer
\[
C_{-\infty}(a,X)=1\Longleftrightarrow J(a,X)=2
\]
for \(0\le a\le2\) is a published theorem of Liu, Din and Li rather than a computation reproduced by the checker. No independent audit or independent validation has been performed.
