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
For
\[
z=(\alpha,1-\alpha),
\qquad
0\le\alpha\le\frac12,
\]
the critical fibre identity is
\[
m_z(a)
=
\sup_{\|u\|_1=a}
\min\{\|z+u\|_1,\|z-u\|_1\}
=
1+\max\{0,a-2\alpha\}.
\]
For \(a\le2\alpha\), the witness \(u=(a/2,-a/2)\) makes both norms \(1\). For \(a\ge2\alpha\), the witness \(u=(a-\alpha,-\alpha)\) makes both norms \(1+a-2\alpha\).

The outer optimization is
\[
1-a^p+m_z(a)^p.
\]
Its first branch is at most \(2\), and its second branch is increasing because
\[
(1+a-2\alpha)^{p-1}\ge a^{p-1}.
\]
Thus the only competing endpoint values are \(2\) and \((2-2\alpha)^p\).

The bundled `verify.py` checks the fibre lemma by exact rational boundary enumeration and checks the endpoint maximization for representative integer exponents. These finite checks are supplementary; the proof in `RESULT.md` establishes all real \(1\le p<\infty\).

No independent audit or independent validation has been performed.
