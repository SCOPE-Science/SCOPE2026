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

The proof was reconstructed from the published reduced system (18) and endemic-equilibrium equations (19)--(21). With \(k=a/b\) and \(c=(p+\mu)(\mathcal R_0-1)\), the source equation is
\[
c=I_k\left(\beta+\frac{k u_1}{1+k u_2 I_k}\right).
\]
Differentiation at fixed \(I\) gives
\[
F_I=\beta+\frac{k u_1}{(1+k u_2I)^2}>0,
\qquad
F_k=\frac{u_1I}{(1+k u_2I)^2}>0,
\]
so the unique positive equilibrium root has \(dI_k/dk<0\).

Multiplication by \(1+k u_2I_k\) yields the quadratic
\[
\beta k u_2I_k^2+[\beta+k(u_1-cu_2)]I_k-c=0.
\]
The three limits in RESULT.md follow by the sign of \(u_1-cu_2\), using \(I_k\), \(\sqrt{k}I_k\), or \(kI_k\) as the appropriate scaled variable.

The bundled `verify.py` uses high-precision decimal arithmetic for representative parameter sets in all three regimes. It checks the equilibrium residual, strict decrease on a geometric sequence of turnover ratios, and convergence toward each stated scaled limit. These finite calculations are not an exhaustive proof and are not used to infer the infinite-parameter result.
