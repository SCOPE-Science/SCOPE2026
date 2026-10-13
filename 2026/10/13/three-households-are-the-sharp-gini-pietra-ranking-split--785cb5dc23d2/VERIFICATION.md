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
The proof is algebraic and the embedded verifier provides an exact replay.

For two households \((a,b)\) with \(a\le b\), it checks
\[
G=P=\frac{b-a}{2(a+b)}.
\]

For three sorted households it verifies the exact representation
\[
G=\frac23(\ell+\nu),
\qquad
P=\max\{\ell,\nu\},
\]
where
\[
\ell=\frac13-\frac{x_1}{S},
\qquad
\nu=\frac{x_3}{S}-\frac13.
\]

For the witness
\[
A=(1,6,9),
\qquad
B=(3,3,10),
\]
the exact values are
\[
G(A)=\frac13,
\quad
P(A)=\frac{13}{48},
\]
and
\[
G(B)=P(B)=\frac7{24}.
\]

The verifier also performs a supplementary exhaustive check of positive integer three-household profiles with common totals below \(16\) and at \(16\).

Run:

`python3 verify_gini_pietra_minimal_support.py`

The first output line must be:

`VERIFY_OK`

The universal support-two lower bound and support-three formulas are proved in `RESULT.md`; they do not depend on finite enumeration.
