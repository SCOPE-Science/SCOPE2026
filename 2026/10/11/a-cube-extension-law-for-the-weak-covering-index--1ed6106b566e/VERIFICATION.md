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

The verification is symbolic and definition-level; no floating-point computation is required.

For every \(0<\lambda<1\), with
\[
m=N_\lambda(K),
\]
one has
\[
\gamma_m(K)\le\lambda,
\]
hence
\[
\frac{N_\lambda(K)}{1-\lambda}
\ge
\frac{m}{1-\gamma_m(K)}
\ge
\operatorname{coin}_{\mathrm w}(K).
\]
Conversely, for every \(m\) with \(\gamma_m(K)<1\), ratios arbitrarily close above \(\gamma_m(K)\) admit an \(m\)-homothet cover. This proves
\[
\operatorname{coin}_{\mathrm w}(K)
=
\inf_{0<\lambda<1}
\frac{N_\lambda(K)}{1-\lambda}.
\]

The externally sourced exact covering-number identity is
\[
N_\lambda(K\oplus C^r)
=
N_\lambda(K)
\left\lceil\frac1\lambda\right\rceil^r.
\]
It follows from Bezdek--Khan Proposition 4.2 because the \(r\) segment factors are tightly covered.

Therefore
\[
\operatorname{coin}_{\mathrm w}(K\oplus C^r)
\ge
2^r\operatorname{coin}_{\mathrm w}(K).
\]
At any attaining ratio
\[
\lambda_*\in[1/2,1),
\]
the ceiling factor equals \(2\), proving equality.

For the two advertised families, the inspected source gives
\[
m=3,\qquad
\gamma_3=\frac23,\qquad
\operatorname{coin}_{\mathrm w}=9.
\]
Thus
\[
9\cdot2^r
\]
is exact, including the one-dimensional extension value \(18\).

The result does not rely on finite enumeration, numerical optimization, or an unverified limiting computation.
