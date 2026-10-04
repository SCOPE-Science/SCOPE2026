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
The exact finite-population calculation is replayed by `verify.py`.

For without-replacement contacts, the checker evaluates
\[
1-\beta_{\mathrm{HG}}
=
\frac{1}{\binom{M}{N}}
\sum_{i,a}
\binom{y_I}{i}
\binom{y_A}{a}
\binom{M-y_I-y_A}{N-i-a}
(1-q_I)^i(1-q_A)^a
\]
using exact rational arithmetic and independently by direct enumeration of all \(N\)-subsets of the contact pool.

It verifies the saturation state
\[
M=N=2,\qquad y_I=1,\qquad y_A=0,\qquad q_I=1,
\]
for which
\[
\beta_{\mathrm{HG}}=1
\]
but
\[
\beta_{\mathrm{src}}=\frac34.
\]

It also checks a mixed symptomatic/asymptomatic finite example and the one-infective identity
\[
\beta_{\mathrm{HG}}=\frac{Nq_I}{M}.
\]

The checker is not used to infer an infinite or asymptotic statement; those parts are proved algebraically.
