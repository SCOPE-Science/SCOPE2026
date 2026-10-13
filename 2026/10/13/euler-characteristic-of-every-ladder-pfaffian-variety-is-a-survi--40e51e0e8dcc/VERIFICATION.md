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
The checker constructs deterministic mixed ladder-Pfaffian examples inside generic skew-symmetric matrices for
\[
4\le n\le10.
\]

At every ladder-coordinate projective point it evaluates each Pfaffian generator exactly using a recursive Pfaffian routine.

It verifies both directions of the fixed-point criterion:
\[
[x_{ij}]\in V_{Y,t}
\]
if and only if
\[
x_{ij}
\]
does not lie in any square subladder with
\[
t_a=1.
\]

It also verifies directly that every Pfaffian of size at least \(4\) vanishes on every coordinate point.

Finite checks are regression evidence only. The infinite theorem follows from the rank-\(2\) coordinate-point observation, distinct torus weights, and Euler localization.
