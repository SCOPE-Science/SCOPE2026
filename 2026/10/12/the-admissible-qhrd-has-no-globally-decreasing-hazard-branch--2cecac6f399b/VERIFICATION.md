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
For
\[
h(y)=\alpha+\beta y+\lambda y^2
\]
under
\[
\alpha\ge0,\qquad
\lambda\ge0,\qquad
\beta\ge-2\sqrt{\alpha\lambda},
\]
the derivative is
\[
h'(y)=\beta+2\lambda y.
\]

The checker verifies the admissible case split and representative parameter triples.

For the source's Figure 3 decreasing example
\[
(\alpha,\beta,\lambda)=(3,-0.05,0),
\]
it verifies
\[
h(60)=0,\qquad
f(61)<0,\qquad
F(120)=0,\qquad
F(121)<0.
\]

The numerical checks supplement the exact parameter-space proof.
