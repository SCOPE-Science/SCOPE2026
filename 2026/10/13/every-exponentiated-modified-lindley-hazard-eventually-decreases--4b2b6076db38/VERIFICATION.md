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
With \(u=\theta x\) and \(a=(1+\theta)^{-1}\),
\[
s_0=e^{-u}(1+aue^{-u}),
\qquad
\frac{h_0}{\theta}
=
\frac{1+a(2u-1)e^{-u}}{1+aue^{-u}}.
\]
For the exponentiated CDF,
\[
h=h_0
\frac{\alpha s_0(1-s_0)^{\alpha-1}}
{1-(1-s_0)^\alpha}.
\]
Expansion gives
\[
\frac{h}{\theta}
=
1+
\left[
a(u-1)-\frac{\alpha-1}{2}
\right]e^{-u}
+
O(u^2e^{-2u}),
\]
and exact differentiation followed by expansion gives
\[
\frac{d}{du}\left(\frac{h}{\theta}\right)
=
\left[
a(2-u)+\frac{\alpha-1}{2}
\right]e^{-u}
+
O(u^2e^{-2u}).
\]
These formulas prove approach from above and eventual strict decrease.

The included script evaluates the exact hazard at high precision and checks that both expansion remainders have the predicted \(u^2e^{-2u}\) scale. It also checks derivative signs near zero and in the far tail for representative parameters. Numerical checks are not the proof.

For \(\alpha\ge1\), positive near-origin slope and negative eventual slope imply at least one interior local maximum. Uniqueness is not claimed.
