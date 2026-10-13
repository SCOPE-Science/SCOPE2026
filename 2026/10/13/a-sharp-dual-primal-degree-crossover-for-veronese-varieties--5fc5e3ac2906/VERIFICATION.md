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
The exact inputs are
\[
P_{n,e}=e^n
\]
and
\[
Q_{n,e}=(n+1)(e-1)^n.
\]

The sign is controlled by
\[
\frac{Q_{n,e}}{P_{n,e}}
=
(n+1)\left(1-\frac1e\right)^n,
\]
which is strictly increasing in \(e\).

The real equality point is
\[
T_n=\frac{1}{1-(n+1)^{-1/n}}.
\]
Integral equality reduces to
\[
(n+1)(e-1)^n=e^n.
\]
Coprimality of \(e\) and \(e-1\) forces \(e=2\), and then \(n+1=2^n\) forces \(n=1\).

The bundled checker verifies all integer pairs
\[
1\le n\le300,
\qquad
2\le e\le300
\]
and independently recomputes the first overtake order for each \(n\).

Finite checks are regression evidence only; the classification is symbolic.
