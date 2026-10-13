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
The classification proof is symbolic.

The packaged checker `artifacts/verify.py` constructs
\[
\mathbf F_2,\quad
\mathbf F_4,\quad
\mathbf F_8,\quad
\mathbf F_{16}
\]
from explicit irreducible binary polynomials.

For each field it constructs the twisted dual-number ring
\[
R_q=\mathbf F_q+\mathbf F_q\varepsilon
\]
with
\[
\varepsilon^2=0,
\qquad
\varepsilon a=a^2\varepsilon.
\]

The checker verifies every unit inverse and confirms that the unit set has cardinality
\[
q(q-1).
\]
It then checks the explicit bijection
\[
(t,a)\longmapsto
a^{-1}+t a^{-2}\varepsilon
\]
from the standard affine multiplication
\[
(t,a)(s,c)=(t+as,ac)
\]
to \(R_q^\times\), for every ordered pair of affine transformations.

It also verifies the conjugation identity
\[
a(1+b\varepsilon)a^{-1}
=
1+ba^{-1}\varepsilon.
\]

The checker returns `VERIFY_OK`.

Finite computation is not used to prove the odd-field obstruction or the infinite even-field family.
