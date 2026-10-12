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
Every admissible table has equal treatment and control totals \(m\), two strata, and positive adverse/non-adverse cells.

For one arm, the four cells form a positive composition of \(m\), so there are exactly
\[
\binom{m-1}{3}
\]
arm profiles and
\[
\binom{m-1}{3}^2
\]
balanced two-arm tables.

The verifier tests the strict inequalities by exact integer cross multiplication:
\[
xb<ya,
\]
\[
u(m-b)<v(m-a),
\]
and
\[
x+u>y+v.
\]

For
\[
m=4,5,6,7,8,9,10,11,
\]
the exact table counts are
\[
1,16,100,400,1225,3136,7056,14400,
\]
and the strict-reversal counts are
\[
0,0,0,0,0,0,0,4.
\]

The four first-layer solutions form two orbits under stratum exchange. Orbit representatives have rates
\[
\frac13<\frac38,
\qquad
\frac58<\frac23,
\qquad
\frac6{11}>\frac5{11},
\]
and
\[
\frac14<\frac27,
\qquad
\frac57<\frac34,
\qquad
\frac6{11}>\frac5{11}.
\]

Run:

`python3 verify_balanced_positive_simpson_minimum.py`

The first output line must be:

`VERIFY_OK`

The lower bound is finite and exhaustive rather than experimental sampling: every positive-cell balanced table through the claimed boundary is generated exactly once.
