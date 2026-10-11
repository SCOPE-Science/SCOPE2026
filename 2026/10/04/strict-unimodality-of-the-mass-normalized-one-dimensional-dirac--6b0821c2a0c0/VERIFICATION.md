---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Starting from the exact one-dimensional source formula, mass normalization gives \(A(p)^p=p^p(2/(p-1))^{p-1}B(1/2,p-1/2)\). Differentiating \(F=\log A\) yields \(F'(p)=H(p)/p^2\), and another derivative gives \(H'=-1/(p-1)+p[\psi_1(p-1/2)-\psi_1(p)]\). The trigamma integral converts the bracket into \(4\int_0^\infty s e^{-(2p-1)s}/(1+e^{-s})\,ds\). The strict inequality \(1+e^{-s}>2e^{-s/2}\) gives the stated rational upper bound, which is strictly below \(1/(p(p-1))\); hence \(H'<0\) for every \(p>1\). The signs \(H(1^+)=+\infty\) and \(H(3/2)=4\log2-3<0\) give exactly one zero and therefore strict increase followed by strict decrease. I independently evaluated \(H'\) across the domain and recomputed the unique root \(1.317094285913839\ldots\); this numerical replay only corroborates the analytic proof.

## originality

PASS

The complete open primary article was inspected around Theorem 1.3, the one-dimensional derivation and Figure 1. It gives the exact beta-function threshold and labels a numerical maximum near \(p=1.32\), but the inspected text does not prove a global monotonicity theorem or uniqueness of that maximum. Targeted web and Resultary searches using the exact formula, the numerical maximizer and digamma/trigamma terminology did not locate a later analytic proof. The accepted novelty is therefore the rigorous strict-unimodality theorem, not the already plotted location or the source formula.

## value

PASS

The critical norm is a central sharp parameter of the source theorem, and its nonmonotone dependence on the Lebesgue exponent is highlighted by the source itself. Replacing a plotted numerical observation by a global strict-increase/strict-decrease theorem with a unique analytic critical equation is a motivated structural result rather than a routine recomputation of the decimal peak.

The dated certificate retains the supplied scientific assessment, sources and limitations.
