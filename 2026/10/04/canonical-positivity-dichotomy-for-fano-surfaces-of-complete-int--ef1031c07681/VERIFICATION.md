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
The argument uses the exact canonical formula
\[
K_F
\simeq
\mathcal O_F(B),
\qquad
B=
\sum_i\binom{d_i+k}{k+1}-r-1.
\]

For
\[
q=k+1,
\qquad
R_i=\binom{d_i+k}{k},
\]
the expected-surface equation implies
\[
qB
=
\sum_i(d_i-1)R_i-(q^2+2).
\]
The proof then bounds each summand from below and treats separately one, two, or at least three defining equations. Equality survives only for two quadrics with \(q=2\), which forces \(r=5\).

The bundled checker exhausts a finite box of degrees, codimensions, and plane dimensions satisfying the exact expected-dimension equation and the standard ambient range. It verifies nonnegativity and finds the unique zero. It also rechecks the symbolic inequalities over a larger \(q\)-range.

Those finite checks are regression evidence only. The infinite statement is established by the displayed identities and inequalities.

Limits: general complex complete intersections, \(k\ge1\), expected dimension exactly two, and \(r\ge2k+m\).
