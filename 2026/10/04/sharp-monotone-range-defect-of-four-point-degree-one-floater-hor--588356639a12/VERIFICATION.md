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
The checker uses only the Python standard library and exact rational arithmetic.

It rebuilds the uniform four-node, degree-one Floater–Hormann weights from the published formula and checks the cardinal basis at selected rational points. It verifies the monotone-increment representation and the exact midpoint identities
\[
g(1/2)=7/38
\]
and
\[
R[(1,2,98,99)/100](1/2)=-4/25.
\]

Rational bisection brackets the unique edge critical point near
\[
0.516232808495147
\]
and the sharp defect near
\[
0.18441311642853.
\]
The checker confirms opposite signs of the critical quartic across the point bracket and opposite signs of
\[
15z^4+30z^3+671z^2+656z-144
\]
across the defect bracket.

The proof that these brackets correspond to the global extrema is analytic in RESULT.md. Finite computation is not used as a substitute for the sign and uniqueness arguments.
