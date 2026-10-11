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

The proof has two independent layers.

First, the symbolic argument uses the positive-equilibrium balances of the printed system. The infected-prey balance forces \(X_S>d_2/\beta\). The predator response
\[
G(s)=\frac{c\alpha(1-m_1)\sqrt{s}}{1+k_1(1-m_1)\sqrt{s}}
\]
is strictly increasing because, with \(t=\sqrt{s}\), its derivative with respect to \(t\) is a positive constant divided by \((1+k_1(1-m_1)t)^2\). This gives a strict lower bound on \(X_I\). The susceptible-prey balance then forces the stated necessary inequality because \(Y>0\) makes both the denominator loss in the recruitment term and the predation term strict.

Second, `verify.py` recomputes the Section 7.2 specialization entirely with `fractions.Fraction`. It verifies
\[
G(1)=\frac{89}{375},\qquad
\xi\delta(1-m)=\frac{609}{5000},\qquad
X_I>\frac{80}{261},
\]
and the contradiction margin
\[
(r-d_1)-(b+\beta)\frac{80}{261}=-\frac{1156}{6525}<0.
\]
It also checks the independent reported-point residual
\[
\beta X_S-\delta(1-m)Y-d_2=-\frac{624357}{1000000}
\]
at \((X_S,X_I,Y)=(0.6002,0.0355,0.0971)\), giving \(\dot X_I=-44329347/2000000000\ne0\).

The exact arithmetic verifies the terminating decimals as printed. No numerical integration, finite search, or assumption about long-time dynamics is used. The conclusion does not determine a corrected parameter set or the source of the discrepancy.
