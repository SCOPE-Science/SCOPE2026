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
\mu(X_{12})=5\sqrt3-7.
\]

`verify.py` uses exact SymPy arithmetic in \(\mathbb Q(\sqrt3)\). It reconstructs the twelve facet normals and the relevant regular-dodecagon vertices, confirms their active facets, and checks the Birkhoff--James support-functional conditions in the canonical edge and vertex configurations.

It verifies the three lower-bound certificates:
\[
h_E=cn_1+(1-c)n_2,
\qquad
h_2=cn_2+(1-c)n_3,
\qquad
c=\frac{17+\sqrt3}{26},
\]
together with the single-facet certificate \(n_2\) on the middle triangle. Every required vertex value is checked exactly.

The equality point
\[
z_*=\frac1{4-\sqrt3}(1,1)
\]
is checked against all twelve facets, yielding
\[
N_{12}(z_*)=\frac{7+5\sqrt3}{26}.
\]
The checker also verifies
\[
\lambda=3-\sqrt3
\]
and
\[
\left(\frac{7+5\sqrt3}{26}\right)(5\sqrt3-7)=1.
\]

The finite symbolic checker validates the algebraic certificates; completeness of the three-triangle reduction follows from the analytic support-functional classification in `RESULT.md`, not from finite sampling. No independent audit or independent validation has been performed.
