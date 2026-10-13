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
The checker enumerates matrix-coordinate pairs for
\[
2\le a\le12,
\qquad
a\le b\le12.
\]

For each
\[
X=E_{ji},
\qquad
Y=E_{\ell k},
\]
it checks the two compositions directly. The pair survives exactly when
\[
\ell\ne i
\qquad\text{and}\qquad
k\ne j.
\]
The surviving count is compared with
\[
a(a-1)b(b-1).
\]

For every
\[
1\le c\le a-1,
\]
the checker also verifies that every surviving pair has ranks bounded by
\[
(c,a-c),
\]
so the fixed-point count does not depend on the component label.

It separately verifies the zero case
\[
a=1
\]
and the ratio to the ambient Euler characteristic
\[
(ab)^2.
\]

These finite checks are regression evidence only. The all-parameter proof is the torus-localization argument in `RESULT.md`.
