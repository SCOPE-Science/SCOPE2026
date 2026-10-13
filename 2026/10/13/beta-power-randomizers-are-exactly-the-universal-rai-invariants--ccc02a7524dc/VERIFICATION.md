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

The result is fully analytic and needs no finite computation or numerical certificate.

For a parent cdf \(F\) and randomizer cdf \(G\), the random-quantile cdf is \(H=G\circ F\). At every regular point with \(u=F(t)\in(0,1)\),
\[
\frac{\breve L_H(t)}{\breve L_F(t)}
=
\frac{u\log u\,G'(u)}{G(u)\log G(u)}.
\]
For \(G(u)=u^a\), direct substitution makes this ratio exactly one.

For necessity, use a rate-one exponential parent, whose cdf ranges over every \(u\in(0,1)\). Universal invariance then forces
\[
\frac{G'(u)}{G(u)\log G(u)}=\frac{1}{u\log u}
\]
almost everywhere. With \(y(u)=-\log G(u)\), integration gives
\[
\log y(u)=\log(-\log u)+C,
\]
so \(G(u)=u^a\). Cdf boundary behavior forces \(a>0\).

The different-randomizer order statement is then exact because \(\breve L_{Q_X(Z_a)}=\breve L_X\) and \(\breve L_{Q_Y(Z_b)}=\breve L_Y\) separately. For integer \(a=n\), the cdf \(F_X^n\) is exactly that of the iid maximum \(X_{n:n}\).

Unproved limits: the theorem does not address singular randomizers or classify all randomizer pairs that preserve one fixed parent comparison.
