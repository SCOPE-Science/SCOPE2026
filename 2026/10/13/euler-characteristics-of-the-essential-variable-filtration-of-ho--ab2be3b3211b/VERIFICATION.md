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
For every tested
\[
2\le m\le9,
\qquad
3\le d\le9,
\]
the checker enumerates every degree-\(d\) exponent vector in \(m\) variables.

For each monomial it computes support size and verifies, for every
\[
1\le r\le m,
\]
that the cumulative count is
\[
\sum_{s=1}^{\min(r,d)}
\binom ms\binom{d-1}{s-1}.
\]

It also verifies the exact support histogram
\[
\binom mr\binom{d-1}{r-1}
\]
for
\[
r\le\min(m,d),
\]
and zero fixed-point contribution for
\[
r>d.
\]

Finally it checks the ambient identity
\[
\sum_{s=1}^{\min(m,d)}
\binom ms\binom{d-1}{s-1}
=
\binom{m+d-1}{d}.
\]

Finite checks are regression evidence only. The infinite proof uses base-\(B\) weight separation, monomial support, and Euler localization.
