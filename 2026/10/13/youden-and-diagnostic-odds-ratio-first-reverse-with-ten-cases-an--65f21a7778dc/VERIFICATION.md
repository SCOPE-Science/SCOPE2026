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
The theorem is checked in exact arithmetic.

For balanced case and control counts \(m\), an admissible table is represented by
\[
(TP,TN)=(a,d)
\]
with
\[
1\le a,d\le m-1,
\qquad
a+d>m.
\]

The embedded `verify_youden_dor_minimal_reversal.py` computes
\[
J=\frac{a+d-m}{m}
\]
and
\[
\mathrm{DOR}
=
\frac{ad}{(m-a)(m-d)}
\]
directly from the confusion matrix.

It verifies admissible-table counts
\[
0,1,3,6,10,15,21,28,36
\]
for
\[
m=2,\ldots,10
\]
and strict-reversal counts
\[
0,0,0,0,0,0,0,0,6.
\]

The first-layer witness is
\[
(3,7,9,1)
\]
versus
\[
(6,4,7,3),
\]
with
\[
J=\frac15,\frac3{10}
\]
and
\[
\mathrm{DOR}=\frac{27}{7},\frac72.
\]

The verifier also checks the fixed-Youden DOR extrema used in the proof and replays the structural family through \(m=500\).

Run:

`python3 verify_youden_dor_minimal_reversal.py`

The first output line must be:

`VERIFY_OK`

The all-\(m\) persistence statement is proved by the exact inequality
\[
m(m-9)>0,
\]
not inferred from the finite replay.
