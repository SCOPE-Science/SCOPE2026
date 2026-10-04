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

The proof uses the exact source identities
\[
q=\frac{p}{p-1},\qquad
M=m(p-1)-1,\qquad
\beta=p+dM,\qquad
\gamma=\frac{p-1}{M},\qquad
\kappa=\frac{M}{mp}\beta^{-1/(p-1)}.
\]
From these,
\[
\gamma\kappa q=\frac1m\beta^{-1/(p-1)}
\]
and therefore
\[
A=m^{p-1}(\gamma\kappa q)^{p-2}
=m\beta^{-(p-2)/(p-1)}.
\]
The source coefficient becomes
\[
a(t,t^{1/\beta}y)=t^{-1+2/\beta}A y^{2-q}(C-\kappa y^q).
\]

For \(u=(\kappa/C)y^q\), exact differentiation yields
\[
\bar a(y)(u'(y))^2=A\kappa q^2u(1-u).
\]
Thus
\[
K=A\kappa q^2=\frac{pM}{(p-1)^2\beta}.
\]
The transformed drift is
\[
A\kappa q\{d-(d+q)u\}-\frac q\beta u.
\]
Since
\[
\frac{q}{\beta K}=\gamma,
\]
this equals
\[
K\{\alpha-(\alpha+\eta)u\},
\qquad
\alpha=\frac d q,\quad \eta=\gamma+1.
\]

At \(y=0\), the possible singularity of \(u''(y)\) when \(1<q<2\) is harmless because
\[
\bar a(y)y^{q-2}=A(C-\kappa y^q)
\]
is bounded. Hence a smooth approximation to \(y^q\) permits passage through the origin.

Braun's one-time density for \(Y=t^{-1/\beta}|X_t-o|\) is proportional to
\[
(C-\kappa y^q)^\gamma y^{d-1}
\]
on \(0\le y\le(C/\kappa)^{1/q}\). The change of variables \(u=(\kappa/C)y^q\) gives the density
\[
u^{\alpha-1}(1-u)^{\eta-1},
\]
so the exact marginal is \(\operatorname{Beta}(\alpha,\eta)\).

The generator can be written
\[
\mathcal L f
=
K\pi^{-1}\frac{d}{du}\{u(1-u)\pi f'\},
\]
where \(\pi\) is the Beta density, proving invariance and reversibility. The one-dimensional drift is Lipschitz and the diffusion coefficient satisfies the square-root modulus needed for pathwise uniqueness.

Finally,
\[
d(J_s-\mu)
=
-\Lambda(J_s-\mu)\,ds
+\sqrt{2KJ_s(1-J_s)}\,dB_s,
\]
where
\[
\mu=\frac{\alpha}{\alpha+\eta},
\qquad
\Lambda=K(\alpha+\eta).
\]
Because the stochastic coefficient is bounded on \([0,1]\), the integrating-factor stochastic integral is a true square-integrable martingale. This gives
\[
\mathbb E[J_v-\mu\mid\mathcal F_u]
=
e^{-\Lambda(v-u)}(J_u-\mu),
\]
and therefore the stated exact correlation.

Unproved limits: no claim is made for uncentered processes, fast diffusion, the full rescaled vector process, or a raw-radius correlation formula. No independent audit has been performed.
