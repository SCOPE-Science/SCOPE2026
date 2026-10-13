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
For positive integer abundance profiles with fixed richness \(S\) and total \(N\), define
\[
Q_2=\sum_i n_i(n_i-1)
\]
and
\[
Q_3=\sum_i n_i(n_i-1)(n_i-2).
\]

The embedded `verify_simpson_rarefaction_boundary.py` independently constructs every abundance multiset through
\[
N=9
\]
in two ways: directly as a nondecreasing positive partition and as a canonicalized positive composition.

It verifies Hurlbert's hypergeometric expected-richness formula directly and checks
\[
R_2
=
2-
\frac{Q_2}{N(N-1)}
\]
for every profile with \(N\ge2\), and
\[
R_3
=
3-
3\frac{Q_2}{N(N-1)}
+
\frac{Q_3}{N(N-1)(N-2)}
\]
for every profile with \(N\ge3\).

Profiles are then grouped by the exact key
\[
(N,S,Q_2).
\]

The complete nonsingleton-group list through nine individuals is exactly
\[
(9,3,24,\{(1,4,4),(2,2,5)\}).
\]

The verifier checks all
\[
109
\]
within-\((N,S)\) unordered profile pairs in the domain.

For the first collision it verifies
\[
D_2=\frac13,
\qquad
R_2=\frac53,
\]
and
\[
R_3(1,4,4)=\frac{44}{21},
\qquad
R_3(2,2,5)=\frac{89}{42},
\]
with gap
\[
\frac1{42}.
\]

Run:

`python3 verify_simpson_rarefaction_boundary.py`

The first output line must be:

`VERIFY_OK`

The cutoff claim is a complete finite classification, not an extrapolation from sampled profiles.
