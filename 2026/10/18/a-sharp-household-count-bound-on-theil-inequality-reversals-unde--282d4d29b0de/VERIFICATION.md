---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For two n-component strictly positive income vectors with equal mean and common additive t>=0, derived T_X(t)-T_Y(t)=F(t)/(n(mu+t)) with F(t)=sum_i(t+x_i)log(t+x_i)-sum_i(t+y_i)log(t+y_i). Differentiation cancels n and equal first moments, yielding F′=log(P_X/P_Y), with polynomial Q=P_X-P_Y of degree <=n−2 due to monic leading and equal income sums. Positive roots of F′ are contained among <=n−2 roots of Q. F(t) ->0 as t->infinity by Taylor expansion and equal totals. If F has m>0 distinct positive zeros, Rolle yields m−1 derivative zeros between them AND one additional derivative zero strictly after the last zero by a nonzero return to 0, hence m<=n−2 (identical multisets excluded). Independently checked quartic polynomial Q=-3t²+314t-3155 for X=(1,7,25,35), Y=(2,5,29,32) and exact integer-power entropy signs + at t=0,5, negative 6,20,32, positive 33,40; two roots occur in (5,6),(32,33). Independent n=3 witness X=(1,11,24),Y=(2,9,25) has opposite exact signs at grants 0 and20; bound not asserted sharp beyond n=4.

## originality

PASS

Theil T and scale/translation discussions are established. Inspected Cowell 2003 full lawful OA text discussing translation parameter and Theil/entropy family and Liao 2016 related income inequality sources; no all-sample-size polynomial-degree bound on count of equal-cash-grant ranking reversals or explicit four-household double reversal was identified. The derivative logarithmic polynomial argument and n−2 bound appear new best of knowledge; translation-robustness literature may contain implicit implication, so priority remains qualified.

## value

PASS

Uniform grants and relative inequality rankings provide a natural non-arbitrary perturbation in distribution comparison. A universal household-count bound and explicit smallest four-household double sign reversal quantify non-monotone stability of comparisons despite monotone cash supplements; this is meaningful mathematical sensitivity structure, not merely numerical example or policy recommendation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
