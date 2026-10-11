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

# Verification and reproducibility

The result is proved by direct infinite-dimensional analysis. For \(a=\gamma+1/p\in(0,1)\), the integrals \(\int_0^\infty t^{-a}/(1+t)\,dt\) and \(\int_0^\infty t^{a-1}/(1+t)\,dt\) are both \(\pi/\sin(\pi a)\); the decreasing-integrand comparisons establish the two needed Schur inequalities. The logarithmic-kernel identity in the proof can be rechecked term by term:
\[
\frac{1}{n}\frac{e^{(1-a)\log(n/k)}}{1+e^{\log(n/k)}}
=\frac{k^a n^{-a}}{k+n}.
\]
For every fixed \(A<T\), the normalized lower-bound vectors are supported in an interval whose least index tends to infinity and are therefore weakly null; the weak-null argument does not rely on numerical computation. The central output window has harmonic mass converging to \(2(T-A)\), while the full input window has harmonic mass converging to \(2T\). The order of limits is: first \(N\to\infty\), then \(T\to\infty\) for fixed \(A\), and finally \(A\to\infty\).

A supplementary numerical beta-integral check was performed at \(a=0.5\): the integral of the logarithmic kernel and \(\pi/\sin(\pi a)\) both evaluate to \(3.141592653589793\) at the reported precision. This finite computation is only a normalization check; it is not the proof. At the classical Hilbert case \(p=2\), \(\gamma=0\), the constant equals \(\pi\).

No independent external audit or certification has been performed. The mathematically essential reproducibility data are the explicit kernel, hypotheses and full analytic proof; the result depends on no separate software package or inaccessible log. Overlap with an uninspected full-text statement or with a general Mellin limit-operator result remains a residual literature risk.
