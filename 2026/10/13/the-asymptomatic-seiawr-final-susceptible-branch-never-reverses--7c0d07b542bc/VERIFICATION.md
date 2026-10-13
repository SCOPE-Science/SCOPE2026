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
The bundled checker verifies the implicit derivative identity and the source numerical branch.

With
\[
F(x,R)=\log(1/x)-R(1-x),
\]
it checks that the implicit derivative is
\[
\frac{dx}{dR}=\frac{1-x}{R-1/x}.
\]

At
\[
R=1.188808,
\]
the checker finds the lower root
\[
x=0.700135812028657\ldots
\]
and verifies both
\[
F(x,R)=0
\]
and
\[
\frac{dx}{dR}<0.
\]
It also checks that \(x=1\) is the second root of the same zero-seed implicit equation.

The root-location inequality and uniqueness theorem are analytic and do not depend on numerical sampling.
