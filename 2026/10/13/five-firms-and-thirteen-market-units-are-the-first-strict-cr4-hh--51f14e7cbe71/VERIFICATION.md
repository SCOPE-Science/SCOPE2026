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
For a five-firm market with positive integer share counts
\[
a_1\ge\cdots\ge a_5>0,
\qquad
\sum_i a_i=S,
\]
the two fixed-total comparison keys are
\[
CR_4\ \longleftrightarrow\ S-a_5
\]
and
\[
H\ \longleftrightarrow\ \sum_i a_i^2.
\]

The proof uses exact extremal bounds:
- the largest square sum among profiles with minimum at least \(2\);
- the smallest square sum among profiles with minimum \(1\).

Those bounds exclude strict reversal through \(S=12\) and isolate the total-\(13\) equality layer.

The embedded `verify_cr4_hhi_minimal_reversal.py` independently generates every positive five-part partition for
\[
5\le S\le13
\]
using both recursive partition generation and canonicalized positive compositions.

It verifies partition counts
\[
1,1,2,3,5,7,10,13,18
\]
and strict-reversal counts
\[
0,0,0,0,0,0,0,0,2.
\]

The two total-\(13\) reversals are exactly
\[
(5,2,2,2,2)\ \text{versus}\ (4,3,3,2,1)
\]
and
\[
(5,2,2,2,2)\ \text{versus}\ (3,3,3,3,1).
\]

It also checks the two symbolic continuation families through \(x=500\). Their validity for all integers \(x\ge5\) follows from the exact formulas
\[
Q(A_x)-Q(B_x)=2x-8
\]
and
\[
Q(A_x)-Q(C_x)=4x-16.
\]

Run:

`python3 verify_cr4_hhi_minimal_reversal.py`

The first output line must be:

`VERIFY_OK`
