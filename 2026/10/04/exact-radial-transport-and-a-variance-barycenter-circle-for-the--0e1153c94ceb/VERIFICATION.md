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
The packaged `verify.py` uses only the Python standard library and exact rational arithmetic.

Starting from the invariant second-moment relation
\[
(1-u^2)M_2-2A m_x+A^2=0,
\]
it checks symbolically by coefficient comparison that choosing
\[
c=\frac{A}{1-u^2}
\]
gives
\[
M_2-2cm_x+c^2
=
\frac{A^2u^2}{(1-u^2)^2}.
\]

For the customary value
\[
u=\frac9{10},
\qquad
A=1,
\]
it verifies exactly
\[
c=\frac{100}{19},
\qquad
R=\frac{90}{19}.
\]

The checker also verifies the variance decomposition numerically on several exact rational test triples satisfying the second-moment relation.

The complete radial pushforward law itself is an analytic consequence of invariance and
\[
|T(z)-A|=u|z|;
\]
it is not inferred from finite orbit sampling.

The stored output in `verification_output.txt` is `VERIFY_OK`.
