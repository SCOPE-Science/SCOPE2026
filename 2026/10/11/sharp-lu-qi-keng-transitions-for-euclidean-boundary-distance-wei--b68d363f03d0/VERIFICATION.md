---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

Under unnormalized planar area and t>−1, ||z^n||²=2π B(2n+2,t+1); angular Parseval establishes complete orthogonal monomials. Their reciprocal moments yield K_t(s)=(t+1)[(1−x)^−a−(1+x)^−a]/(4πx), a=t+2>1 and x²=s, with K_t(0)=(t+1)(t+2)/(2π). For |x|<1, the Cayley q=(1+x)/(1−x) lies in Re q>0 so |Im Log q|<π/2; the zero equation a Log q=2πik demands 0<|k|<a/4. Inverting yields x=i tan(πk/a), s=−tan²(πk/a); ±k denote one scalar root. Differentiating the odd numerator gives F′=2ac/(1−x²)≠0 at every nonzero zero, establishing simplicity and completeness. Strict j<a/4 excludes s=−1 at t=4j−2 and yields N(t)=ceil((t+2)/4)−1; zero-free iff t≤2 within t>−1. No branch ambiguity or fixed-section/root-count conflation.

## originality

PASS

Best-of-knowledge PASS after full-text primary review: Perälä 2017/2018 §§1–3 proves finite radial-kernel section zeros and constructs special iterated-associated weights with arbitrarily many, not the full exact real-t Euclidean-distance power zeros. Marinescu–Xing 2026 Theorem 1.3 proves real-analytic dependence of distance-weight kernels over general domains, not location, multiplicity or transition of zeros. Zeytuncu treats other radial comparable weights. Resultary higher-dimensional complex-ball integer-t classification excludes disk d=1 and real t. None has an implication establishing this all-t disk phase diagram; possible older hypergeometric zero classifications remain residual risk.

## value

PASS

PASS: exact entire parameter transition between zero-free and vanishing Bergman kernels for natural geometric distance weights, with multiplicities and explicit zero locations, provides a genuine sharp phase diagram; not just a known positivity check or arbitrary finite case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
