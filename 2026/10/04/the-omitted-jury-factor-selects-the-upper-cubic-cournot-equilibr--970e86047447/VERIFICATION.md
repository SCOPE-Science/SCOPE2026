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

The source equilibrium polynomial is
\[
P(q)=6c_1q^2+Bq-C,
\qquad
B=4(1+c_2)-d^2(\mu-1)^2.
\]
The source's omitted Jury condition is exactly
\[
k^2q_1^*q_2^*\bigl(B+12c_1q_2^*\bigr)
=k^2q_1^*q_2^*P'(q_2^*),
\]
and under its delayed-feedback map it is divided by \((1+m)^2\). This proves the branch criterion symbolically.

`verifier.py` uses exact arithmetic in \(\mathbb{Q}(\sqrt{70})\). It checks the witness
\[
\alpha=\frac75,\ c=\frac25,\ d=\frac12,\ \mu=1,\ c_1=1,\ c_2=-2,\ c_3=\frac32,\ c_4=0,
\]
with
\[
q_1^*=\frac12,
\qquad
q_2^*=\frac{10-\sqrt{70}}{30},
\qquad
k=\frac1{100}.
\]
It verifies the exact equilibrium identity, all stated cubic-cost restrictions, positivity of both equilibrium roots, positivity of the retained conditions (40) and (41), and
\[
1-\operatorname{tr}J+\det J
=\frac{7-\sqrt{70}}{150000}<0.
\]
It also checks the controlled case \(m=1\), where the retained conditions (48) and (49) are positive but the omitted Jury value is \((7-\sqrt{70})/600000<0\). In both cases the exact second multiplier is greater than one.

The script prints `VERIFY_OK` only after all exact sign and identity checks pass. The general theorem is not inferred from finite tests; the witness only demonstrates that the published retained inequalities are insufficient.
