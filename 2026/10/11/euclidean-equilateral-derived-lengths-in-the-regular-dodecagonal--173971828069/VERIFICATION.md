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
The verification target is the pointwise statement
\[
N_{12}(x)=N_{12}(y)=N_{12}(x-y)=1
\quad\Longrightarrow\quad
N_{12}(x+y)=N_{12}(2x-y)=\sqrt3,
\]
for the regular dodecagonal norm displayed in `RESULT.md`.

`verify.py` uses only exact rational arithmetic in the quadratic field \(\mathbb Q(\sqrt3)\). It represents an element as \(a+b\sqrt3\) with rational \(a,b\), performs exact sign comparisons, and enumerates all \(12^3=1728\) choices of one tight signed facet for each of \(x\), \(y\), and \(x-y\).

For each consistent rank-three triple, the checker computes the affine line exactly and intersects it with all \(36\) unit-ball inequalities. It verifies that the resulting nonempty faces are only points or segments. At all endpoints it checks both derived norms are exactly \(\sqrt3\). For each segment it also checks that one signed facet of \(x+y\) and one signed facet of \(2x-y\) attain \(\sqrt3\) at both endpoints, which is the finite certificate used by the affine lower-bound and convex upper-bound argument in `RESULT.md`.

The checker also verifies the explicit pair
\[
x=(\sqrt3-1,\sqrt3-1),
\qquad
y=(1,\sqrt3-2).
\]

No floating-point search or finite sampling is used as a proof of the continuum statement. No independent audit or independent validation has been performed.
