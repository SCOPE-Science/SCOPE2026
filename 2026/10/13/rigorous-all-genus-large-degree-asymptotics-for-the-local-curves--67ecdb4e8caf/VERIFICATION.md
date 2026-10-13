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

The initiating source was inspected at the exact formulas needed for the proof. Its closed mirror map is
\[
Q=q(1-q)^{p^2-1},
\]
and for \(g\ge2\) its polynomiality theorem writes the closed potential as a polynomial numerator divided by \(\Delta^{5g-5}\), where
\[
\Delta=\frac{1-p^2q}{1-q}.
\]
Its all-genus double-scaling result evaluates the critical numerator at \(\Delta=0\) as
\[
P_g(0,p^2)
=
\frac{p^{6g-6}}{(p^2-1)^{2g-2}}
\frac{\langle\tau_2^{3g-3}\rangle_g}{(3g-3)!}.
\]

Solving for \(q\) gives
\[
q=\frac{1-\Delta}{p^2-\Delta}.
\]
Therefore
\[
\frac{Q}{Q_c}
=(1-\Delta)\left(1-\frac{\Delta}{p^2}\right)^{-p^2},
\qquad
Q_c=\frac{(p^2-1)^{p^2-1}}{p^{2p^2}}.
\]
The logarithmic expansion has zero linear term and quadratic term
\[
1-Q/Q_c=\frac{p^2-1}{2p^2}\Delta^2+O(\Delta^3).
\]
Hence
\[
\Delta^{-(5g-5)}
\sim
\left(\frac{p^2-1}{2p^2}\right)^{(5g-5)/2}
(1-Q/Q_c)^{-(5g-5)/2}.
\]
Multiplying by the exact critical numerator yields
\[
(-1)^{g-1}
\frac{p^{g-1}(p^2-1)^{(g-1)/2}}{2^{(5g-5)/2}}
\frac{\langle\tau_2^{3g-3}\rangle_g}{(3g-3)!}.
\]
Finally,
\[
[Q^d](1-Q/Q_c)^{-\alpha}
\sim
Q_c^{-d}\frac{d^{\alpha-1}}{\Gamma(\alpha)}
\]
with \(\alpha=(5g-5)/2\), giving the asserted coefficient asymptotic.

Differentiation gives
\[
\frac{dQ}{dq}=(1-q)^{p^2-2}(1-p^2q),
\]
so the principal inverse branch from \(q=0\) reaches its nonzero branch point at \(q=p^{-2}\), exactly the critical point used above. The nonzero Witten--Kontsevich intersection number makes the leading singularity genuine.

The prior local-curve asymptotic literature was also inspected. It contains the same predicted exponent and fixed-genus large-degree shape, but its all-genus critical input was conjectural or numerically tested. The present argument uses the 2026 theorem that proves that missing input.
