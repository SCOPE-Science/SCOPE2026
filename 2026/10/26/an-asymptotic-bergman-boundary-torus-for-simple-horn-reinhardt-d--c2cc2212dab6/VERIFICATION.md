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

# Reproducibility and mathematical checks

Theorem inputs are: \(n\ge2\), simple horn \(\Omega\) of order \(a>n+1\), \(X^*\in S^+_\varepsilon\), monomial degree cutoff \(m=\max\{j:j<a-n\}\), and positive integrals \(c_p=\|z^p\|_{A^2(\Omega)}^{-2}\). This proof does not require measured or guessed coefficients: \(c_p\) are exactly defined by convergent domain integrals.

1. Theorem 3.1 of arXiv:2610.17527v1 identifies precisely the integrable monomials. Orthogonality follows by integrating phase variables of the Reinhardt domain.
2. The Fubini--Study Gram formula implies \(\|\gamma_\theta'(t)\|_B^2=\operatorname{Var}_{w(t)}(|p|)/t^2\), with \(w_p(t)=s_pt^{2|p|}/\sum_{|q|\le m}s_qt^{2|q|}\). The same formula gives \(\|\partial_u\gamma_{\theta+uv}(t)|_{u=0}\|_B^2=\operatorname{Var}_{w(t)}(p\cdot v)\).
3. Expand the exact polynomial denominator \(P(t)=A_mt^{2m}(1+(A_{m-1}/A_m)t^{-2}+O(t^{-4}))\). The total degree variance is \((A_{m-1}/A_m)t^{-2}+O(t^{-4})\), yielding speed \(\sqrt{A_{m-1}/A_m}t^{-2}+O(t^{-4})\) and integrated tail \(\sqrt{A_{m-1}/A_m}t^{-1}+O(t^{-3})\). Positivity of both adjacent degree layers follows from \(m\ge1\), \(x_j>0\), and positivity of monomial norms.
4. Check the torus relation by comparing top-degree coordinates \(me_i\) and \((m-1)e_i+e_j\). Their exponent difference is \(e_i-e_j\), which detects every phase difference. The same comparison identifies the one-dimensional covariance kernel. Projective distance gives the needed lower bound on intrinsic distance.
5. As an algebra diagnostic, substituting \(P(t)=1+ut^2+vt^4\) gives the variance expression in RESULT.md and its \(u/v\) limit. This is a finite consistency check, not the proof for all \(m\).

**Limits:** No full completion classification, geodesic minimality claim, or intrinsic completed-boundary metric is verified. Independent audit has not been performed.
