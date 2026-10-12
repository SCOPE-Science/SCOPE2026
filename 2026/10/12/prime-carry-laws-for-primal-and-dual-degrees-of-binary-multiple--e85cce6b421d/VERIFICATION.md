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
\lambda=(1^{m_1}\cdots q^{m_q}),
\qquad
d=\sum_jm_j,
\]
the checker evaluates Hilbert's formula
\[
\deg\Delta_\lambda
=
\frac{d!}{\prod_jm_j!}\prod_jj^{m_j}.
\]

For every tested prime \(p\), it compares the direct valuation with
\[
\frac{\sum_js_p(m_j)-s_p(d)}{p-1}
+
\sum_jm_j\nu_p(j).
\]

When \(m_1=0\), it also evaluates Oeding's formula
\[
\deg(\Delta_\lambda^\vee)
=
\frac{(d+1)!}{\prod_{j\ge2}m_j!}
\prod_{j\ge2}(j-1)^{m_j}
\]
and verifies
\[
\deg(\Delta_\lambda^\vee)
=
(d+1)\deg(\Delta_{\lambda^-}).
\]

The package separately checks the prime-avoidance criteria and the parity specializations.

All finite checks are regression evidence only. The proof for all partitions and primes follows from the two published degree formulas and Legendre's factorial valuation identity.
