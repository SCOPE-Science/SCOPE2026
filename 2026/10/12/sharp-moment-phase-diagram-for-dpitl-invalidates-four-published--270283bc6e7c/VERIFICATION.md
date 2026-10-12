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
The exact DPITL survival is
\[
S_n=
\left[
\frac{1+2n^\eta}{(1+n^\eta)^2}
\right]^\kappa.
\]
Its continuous interpolation satisfies
\[
S(x)\sim2^\kappa x^{-\kappa\eta}
\]
and
\[
\frac{d}{dx}\log S(x)
=
-\frac{2\kappa\eta x^{2\eta-1}}
{(1+2x^\eta)(1+x^\eta)}
\sim-\frac{\kappa\eta}{x}.
\]
The mean-value theorem therefore yields
\[
p_n=S_n-S_{n+1}
\sim
2^\kappa\kappa\eta\,n^{-\kappa\eta-1}.
\]

Thus
\[
n^r p_n
\asymp
n^{r-\kappa\eta-1},
\]
and the positive moment of order \(r\) is finite exactly when \(r<\kappa\eta\).

For \(t>0\),
\[
e^{tn}p_n
\sim
2^\kappa\kappa\eta
e^{tn}n^{-\kappa\eta-1},
\]
so the MGF series diverges.

The bundled checker evaluates the exact survival and PMF, verifies the two normalized tail constants for representative table parameters, and checks finite partial-sum behavior on opposite sides of the theoretical threshold. Those computations are consistency checks only.
