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
# Verification

The proof is analytic. The accompanying checker uses exact rational arithmetic.

It verifies the occupancy table
\[
(T_2,T_3)\in
\{(0,0),(1,0),(2,0),(3,1),(4,1),(6,4),(10,10)\},
\]
the two pointwise certificates
\[
\frac12T_2-T_3\le I
\]
and
\[
I\le T_2-\frac9{10}T_3,
\]
and the normalization, nonnegativity, and required pair/triple collision
moments of every endpoint formula over a large symbolic range of \(q\).

For small alphabets the checker explicitly enumerates every one of the
\(q^5\) five-coordinate output vectors, assigns its probability from the
occupancy-symmetric endpoint law, and checks every one of the ten
three-coordinate marginals. Each of the \(q^3\) ordered outputs has probability
exactly \(1/q^3\).

The checker also tests a midpoint convex mixture of the two endpoints.

Finite enumeration is not used to infer the universal theorem; it replays the
closed formulas and the symmetry-to-independence argument.

Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK certificate_checks=14 formula_checks=3992 explicit_joint_cases=15 triple_marginal_checks=57750`.
