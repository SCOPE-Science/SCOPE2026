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
The bundled checker uses exact rational representations of every printed decimal parameter entering the first-dose calculation.

It verifies the algebraic identity
\[
\mathcal R_F
=
K\left[
\epsilon+(1-\epsilon)\frac{\mu(1-u_1)}{u_2+\mu}
\right]
\]
from the source's full reproduction number after setting
\[
u_3=u_4=0.
\]

At the source values it obtains
\[
K\approx20.0314888219,
\qquad
K\epsilon\approx1.4022042175,
\]
and
\[
u_{1,c}\approx1.0215898907.
\]

It also verifies that the first-dose-only reproduction number decreases with each first-dose control on the interior but cannot fall below \(K\epsilon\).

No numerical parameter sweep is used as proof.
