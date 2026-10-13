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
The verification reconstructs the equality chain rather than inferring it from examples.

For \(r=p_g(V)-1>0\), Setting 2.4 and Remark 2.6 of arXiv:2610.02689v1 give a Stein-base line bundle of degree \(a\) with
\[
a\ge r.
\]
Lemma 2.8 gives
\[
\operatorname{Ivol}(V)=\deg L\ge a.
\]
Under equality \(\operatorname{Ivol}(V)=r\), both inequalities are equalities and Remark 2.6 forces the Stein curve to have genus zero.

Writing \(e\) for the finite degree from the Stein curve to the canonical image \(T\), one has
\[
a=e\deg T.
\]
Nondegeneracy of \(T\subset\mathbf P^r\) gives \(\deg T\ge r\). Hence
\[
r=a=e\deg T\ge er,
\]
so \(e=1\) and \(\deg T=r\). The classical minimal-degree classification then identifies \(T\) as the rational normal curve. The effective divisor measuring the difference in Lemma 2.8 has degree zero, so it is zero; on \(\mathbf P^1\), the resulting degree-\(r\) line bundle is \(\mathcal O_{\mathbf P^1}(r)\).

The initiating source was checked at its definition of Iitaka volume, Setting 2.4, Remark 2.6, Lemmas 2.7--2.8, Theorem 1.2, and Example 4.5. A full-text search found no 'rational normal' statement. No computation, finite enumeration, or inaccessible certificate is used.

Limits: characteristic zero over \(\mathbf C\), dimension three, \(\kappa=1\), and \(p_g\ge2\). The result identifies the resolved canonical map and Iitaka base but does not classify the fibers.
