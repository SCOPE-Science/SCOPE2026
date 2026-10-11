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

The defining scalar equation is
\[
\sum_{i=1}^n\operatorname{sgn}(m-x_i)|m-x_i|^{p-1}=0.
\]
Its unique root is translation-equivariant and monotone coordinatewise; consequently \(|m_p(x)-m_p(y)|\le\|x-y\|_\infty\) and \(\operatorname{Lip}(P_{n,p})\le n^{1/p}\).

For \(n=2\), exchange symmetry forces \(m=(x_1+x_2)/2\), giving norm one. For \(p=2\) in any dimension, \(m\) is the arithmetic mean and the orthogonal projection is contractive.

For \(1<p<2\), the exact test data
\[
x^0=(0,1,\ldots,1,-(n-2)^{1/(p-1)}),\quad x^\varepsilon=x^0+\varepsilon e_1
\]
has \(m(x^0)=0\), and the scalar implicit equation yields
\[
\frac{m(x^\varepsilon)}{\varepsilon}\longrightarrow1.
\]
This makes the Lipschitz ratio converge to \(n^{1/p}\), proving the upper bound sharp without assuming finite-pair attainment.

For \(p>2\), away from the constant-vector line the derivative of \(m_p\) has weights
\[
w_i=\frac{|x_i-m_p(x)|^{p-2}}{\sum_j|x_j-m_p(x)|^{p-2}}.
\]
The root equation forces \(w_i\le1/2\) for every \(i\). Hence its \(\ell_q\) norm is at most \(2^{-1/p}\) for \(q=p/(p-1)\), and the metric projection derivative has operator norm at most \((n/2)^{1/p}\). Integrate along segments and split where a segment meets the exceptional line. At \(x=(1,-1,0,\ldots,0)\), differentiation along \(h=(1,1,0,\ldots,0)\) gives equality, proving sharpness.

These are analytic equalities and inequalities for arbitrary quantified parameters, not numerical or finite-enumeration certificates. No independent audit has been performed.
