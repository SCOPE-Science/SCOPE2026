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

The anchor's Appendix D.2 gives
\[
Q(t,\delta,\varepsilon)\ge
\frac{1}{4\delta}
\log\frac{\sin(\pi t)}{4\varepsilon}.
\]
For \(t=c\varepsilon^\alpha\) or \(t=1-c\varepsilon^\alpha\),
\[
\frac{\log(\sin(\pi t)/(4\varepsilon))}{\log(1/\varepsilon)}
\longrightarrow 1-\alpha.
\]
The anchor's QSVT theorem gives the matching upper order for \(0<\alpha<1\).

For endpoint triviality, the eigenphases of \(U^t\) occupy an arc of length at most \(t(2\pi-\delta)\), so after centering by a global phase,
\[
\|\mathcal E_{U^t}-\mathcal E_I\|_\diamond
\le
4\sin\!\left(\frac{t(2\pi-\delta)}4\right)
<
2\pi t.
\]
Thus \(t=c\varepsilon^\alpha\) with \(\alpha>1\) is eventually solved by zero queries. Applying the same estimate to \(U^{t-1}\) proves that one query eventually suffices near \(t=1\).

The packaged script checks representative numerical ratios and the elementary endpoint inequalities. It is not a proof.

Unproved limits: the critical regime \(\alpha=1\), the full jump-adaptive upper bound conjectured in the anchor, and uncontrolled or average-case variants.
