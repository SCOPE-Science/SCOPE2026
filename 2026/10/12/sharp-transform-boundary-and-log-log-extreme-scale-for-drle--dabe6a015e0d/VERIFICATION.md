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
Set
\[
\lambda=\alpha/\beta,
\qquad
q=e^{-\lambda},
\qquad
c=\lambda/(\beta-1).
\]
Survival discretization gives
\[
S_n=(1+cn)q^n.
\]
Therefore
\[
p_n
=
q^n\{1-q(1+c)+c(1-q)n\}.
\]

Writing
\[
A=1-q(1+c),
\qquad
B=c(1-q),
\]
the exact PGF is
\[
G(z)
=
\frac{A}{1-qz}
+
\frac{Bqz}{(1-qz)^2}
\]
for
\[
|qz|<1.
\]
Since \(p_n\sim Bnq^n\), this disk is sharp. Thus
\[
\mathbb E[e^{tX}]<\infty
\]
exactly for
\[
t<\alpha/\beta.
\]

The exact hazard is
\[
h_n
=
1-q-\frac{qc}{1+cn},
\]
so
\[
n\{(1-q)-h_n\}\to q.
\]

Solving
\[
(1+cm)e^{-\lambda m}=u
\]
gives
\[
m
=
\lambda^{-1}
\{\log(1/u)+\log\log(1/u)-\log(\beta-1)\}
+o(1).
\]
Integer quantiles differ from this continuous root by only \(O(1)\).

The included checker independently evaluates exact probabilities, hazards, transform partial sums, and lattice quantiles for representative parameters. The infinite-domain conclusions are analytic.
