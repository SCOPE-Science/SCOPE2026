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
The proof was reconstructed from the scalar Kalman covariance map itself.

The fixed-point equation has one positive and one negative root. Conjugating the Möbius map by
\[
t(P)=\frac{P-p}{P-m}
\]
gives exact multiplication by \(\rho=F'(p)\). A symbolic calculation with the inverse coordinate
\[
\phi(t)=\frac{p-mt}{1-t}
\]
verifies
\[
\operatorname{Aitken}\bigl(\phi(t),\phi(\rho t),\phi(\rho^2t)\bigr)
=
\phi(\rho^2t^2).
\]

For \(|a|\le1\), the identity
\[
2q-(p+m)=q+\frac{r(1-a^2)}{h^2}>0
\]
forces \(t(P_1)\in(-1,0)\), which proves the upper bracket for all subsequent triples. For \(|a|>1\), choosing \(h=r=1\) and \(0<q<a^2-1\) gives the exact negative first Aitken value
\[
-\frac{q(q+1)}{a^2-1-q}.
\]

The embedded `verify.py` uses SymPy for the symbolic Aitken identity and Python exact rational arithmetic for stable and unstable witnesses. Finite examples are verification witnesses, not substitutes for the universal proof.

Unproved limits include matrix-valued Riccati equations, arbitrary over-starts, recursive feedback of extrapolated covariance values, and finite-precision covariance consistency.
