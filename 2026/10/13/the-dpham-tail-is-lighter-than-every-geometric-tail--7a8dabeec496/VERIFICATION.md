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
The published DPham probability mass function is
\[
p_n
=
e^{1-\mu^{n^\alpha}}
-
e^{1-\mu^{(n+1)^\alpha}},
\qquad n=0,1,2,\ldots,
\]
so
\[
\Pr(X\ge n)=e^{1-\mu^{n^\alpha}}.
\]

The proof checks four analytic facts:

1. Since
\[
\log\!\left(\frac{\mu^{n^\alpha}}{n}\right)
=
(\log\mu)n^\alpha-\log n\to\infty,
\]
the survival is lighter than every geometric tail.

2. The mean-value theorem gives
\[
\mu^{(n+1)^\alpha}-\mu^{n^\alpha}
=
\alpha(\log\mu)\xi_n^{\alpha-1}\mu^{\xi_n^\alpha}\to\infty,
\]
so the adjacent survival ratio tends to \(0\).

3. For each \(t>0\), eventually \(\mu^{n^\alpha}\ge2tn\), and therefore
\[
e^{tn}p_n\le e^{1-tn},
\]
proving \(\mathbb E[e^{tX}]<\infty\).

4. Exact inversion of
\[
F(n)=1-e^{1-\mu^{(n+1)^\alpha}}
\]
gives the upper-quantile formula. Applying the same survival expression at \((1\pm\varepsilon)\{\log\log m/\log\mu\}^{1/\alpha}\) gives the maximum concentration theorem.

The included script checks the exact finite formulas for representative parameter values, including slow-onset cases. No finite experiment is used to prove an infinite-domain statement.
