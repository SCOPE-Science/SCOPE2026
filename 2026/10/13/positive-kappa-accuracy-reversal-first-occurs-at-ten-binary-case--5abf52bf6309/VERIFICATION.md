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
For a binary reference table with
\[
P+Q=N,
\]
\[
TP=x,
\qquad
FN=P-x,
\qquad
TN=y,
\qquad
FP=Q-y,
\]
the verifier computes
\[
A=\frac{x+y}{N}
\]
and Cohen's kappa in two exact forms.

The direct form is
\[
\kappa=\frac{p_o-p_e}{1-p_e},
\]
where
\[
p_o=A
\]
and
\[
p_e=\frac{PM+Q(N-M)}{N^2},
\qquad
M=x+Q-y.
\]

The independently simplified form is
\[
\kappa
=
\frac{2(Qx+Py-PQ)}{P(N-M)+QM}.
\]
The two are asserted equal for every enumerated table.

After quotienting positive/negative class exchange by restricting
\[
P\le Q,
\]
the numbers of admissible positive-kappa tables for
\[
N=4,5,6,7,8,9,10
\]
are
\[
0,1,2,5,9,13,22,
\]
and the corresponding strict accuracy-kappa reversal counts are
\[
0,0,0,0,0,0,1.
\]

The unique first pair is
\[
(1,2,5,2)
\]
versus
\[
(2,1,3,4),
\]
with metric pairs
\[
\left(\frac35,\frac1{21}\right)
\]
and
\[
\left(\frac12,\frac2{27}\right).
\]

The replay also checks the persistent family through
\[
N=500.
\]
Its validity for every \(N\ge10\) is proved symbolically in `RESULT.md`.

Run:

`python3 verify_accuracy_kappa_minimal_reversal.py`

The first output line must be:

`VERIFY_OK`
