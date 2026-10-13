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
For a positive-integer party profile
\[
x_1\ge\cdots\ge x_k>0,
\qquad
N=\sum_i x_i,
\]
the two indices are evaluated exactly as
\[
N_{LT}=\frac{N^2}{\sum_i x_i^2}
\]
and
\[
N_G=\sum_i\frac{x_iN}{x_iN+x_1^2-x_i^2}.
\]

The embedded `verify_effective_party_boundary.py` independently generates every integer partition through total ten by two algorithms and asserts that their profile sets agree.

It then compares only profile pairs with common total, common party count, and common leading-party count. The verifier checks that there is no weak-order disagreement through
\[
N=9,
\]
and exactly one strict disagreement at
\[
N=10,
\]
namely
\[
(4,4,2)
\quad\text{versus}\quad
(4,3,3).
\]

It verifies the exact values
\[
\frac{25}{9}<\frac{50}{17}
\]
for Laakso–Taagepera and
\[
\frac{21}{8}>\frac{97}{37}
\]
for Golosov, together with the exact Golosov gap
\[
\frac1{296}.
\]

Run:

`python3 verify_effective_party_boundary.py`

The first output line must be:

`VERIFY_OK`

No floating-point comparisons are used.
