# The printed fixed-latency simulation attenuates infections before the delay

## Finding

Alanazi's 2024 model first treats \(\ell(a)\) as the per-capita transition rate out of the latent class:
\[
\partial_t I(x,a,t)+\partial_a I(x,a,t)=-\ell(a)I(x,a,t),
\]
while the non-quarantined infectious class receives the corresponding distributed outflow
\[
(1-\gamma)\int_0^\infty \ell(a)I(x,a,t)\,da.
\]

Section 4.2 then states that the latent period is fixed at \(\rho\), sets
\[
\ell(a)=1\quad(0\le a<\rho),\qquad \ell(a)=0\quad(a\ge\rho),
\]
but replaces the distributed outflow by the single boundary value
\[
\partial_tQ(x,t)=(1-\gamma)I(x,t,\rho)-qQ(x,t).
\]
These two choices are incompatible as a fixed-latency specialization.

For the printed Section 4.2 system, characteristics give
\[
I(x,\rho,t)
=\eta S(x,t-\rho)Q(x,t-\rho)
\exp\left(-\int_0^\rho 1\,da\right)
=\eta e^{-\rho}S(x,t-\rho)Q(x,t-\rho).
\]
Linearizing at a disease-free state with susceptible density \(S_0\) therefore gives
\[
\dot Q(t)=(1-\gamma)\eta S_0e^{-\rho}Q(t-\rho)-qQ(t).
\]
Its exact threshold is
\[
\mathcal R_{\mathrm{sim}}
=\frac{S_0\eta(1-\gamma)e^{-\rho}}{q}.
\]

With the paper's numerical values
\[
S_0=10,\qquad \eta=0.59,\qquad \rho=3,\qquad q=\frac1{1.61},
\]
one obtains
\[
\mathcal R_{\mathrm{sim}}(0)
=\frac{10(0.59)e^{-3}}{1/1.61}
\approx0.4729273624<1.
\]
Thus the printed numerical system is already linearly subcritical when \(\gamma=0\), and increasing quarantine only decreases this number further.

A deterministic fixed latent time \(\rho\) is obtained instead by transporting infected individuals without progression loss for \(0<a<\rho\) and transferring them at age \(\rho\). Then
\[
I(x,\rho,t)=\eta S(x,t-\rho)Q(x,t-\rho),
\]
so
\[
\mathcal R_{\mathrm{fix}}
=\frac{S_0\eta(1-\gamma)}q
=9.499(1-\gamma).
\]
Therefore the fixed-delay containment threshold is
\[
\gamma_c=1-\frac1{9.499}\approx0.8947257606.
\]
At the paper's \(75\%\) quarantine level,
\[
\mathcal R_{\mathrm{fix}}(0.75)=2.37475>1.
\]

Hence Figures 1--4 and the associated statement that \(75\%\) quarantine controls the disease within two months cannot validate the fixed-delay spreading theory from the equations as printed. The numerical equations contain the extra attenuation factor \(e^{-\rho}\), which makes the Section 4.2 dynamics qualitatively different from the intended fixed-delay model.

## Assumptions and scope

The calculation uses the equations printed in Sections 2 and 4.2 of the source, the source's initial susceptible density \(S_0=10\), and the parameter values \(\eta=0.59\), \(\rho=3\), and \(1/q=1.61\).

The stability statement concerns the linearization of the printed Section 4.2 system about a disease-free state. It does not assert what undocumented implementation code actually solved.

The comparison model called fixed latency uses deterministic residence time \(\rho\): latent individuals are transported in infection age until \(a=\rho\) and then enter the infectious class. This is the standard discrete-delay construction and matches the source's analytic reproduction number when all latent infections eventually progress.

## Proof

For the printed Section 4.2 transport equation,
\[
\partial_tI+\partial_aI=-\ell(a)I,
\qquad
I(x,0,t)=\eta S(x,t)Q(x,t),
\]
with \(\ell(a)=1\) on \([0,\rho)\), the characteristic through \((x,\rho,t)\) gives
\[
I(x,\rho,t)
=I(x,0,t-\rho)
\exp\left(-\int_0^\rho \ell(a)\,da\right)
=\eta e^{-\rho}S(x,t-\rho)Q(x,t-\rho).
\]
Substituting into the printed \(Q\)-equation yields
\[
\partial_tQ(x,t)
=(1-\gamma)\eta e^{-\rho}S(x,t-\rho)Q(x,t-\rho)-qQ(x,t).
\]

At a disease-free state, replace \(S(x,t-\rho)\) by \(S_0\). For a perturbation proportional to \(e^{zt}\), the characteristic equation is
\[
z+q=Ae^{-z\rho},
\qquad
A=(1-\gamma)\eta S_0e^{-\rho}.
\]
If \(A<q\) and \(\operatorname{Re}z\ge0\), then
\[
|z+q|\ge \operatorname{Re}(z+q)\ge q>A\ge |Ae^{-z\rho}|,
\]
a contradiction. Hence every characteristic root has negative real part.

If \(A>q\), the real function
\[
f(z)=z+q-Ae^{-z\rho}
\]
satisfies \(f(0)<0\), \(f(z)\to\infty\) as \(z\to\infty\), and \(f'(z)>0\); therefore it has a unique positive root. Equality \(A=q\) gives the zero root. Thus the exact threshold is
\[
\mathcal R_{\mathrm{sim}}=\frac Aq=\frac{S_0\eta(1-\gamma)e^{-\rho}}q.
\]

For deterministic fixed latency, there is no progression loss before age \(\rho\), so the characteristic transport relation is instead
\[
I(x,\rho,t)=\eta S(x,t-\rho)Q(x,t-\rho).
\]
The same argument gives
\[
\mathcal R_{\mathrm{fix}}=\frac{S_0\eta(1-\gamma)}q.
\]
Substituting the source parameters gives the stated numerical values and the exact quarantine threshold.

## Verification

The bundled `verify.py` uses exact rational arithmetic for the paper's parameters where possible and independently checks
\[
\frac{S_0\eta}q=9.499,
\]
\[
\mathcal R_{\mathrm{sim}}(0)=9.499e^{-3}\approx0.4729273624,
\]
\[
\mathcal R_{\mathrm{fix}}(0.75)=\frac{9.499}{4}=2.37475,
\]
and
\[
\gamma_c=1-\frac1{9.499}\approx0.8947257606.
\]

The checker also verifies the characteristic-equation sign test numerically on both sides of threshold. The infinite-dimensional stability criterion itself is proved analytically above and is not inferred from finite computation.

## Relationship to prior work

Alanazi (2024), DOI 10.3934/math.2024945, is the source under examination. Its general model defines \(\ell(a)\) as the latent-stage transition rate and its Section 4.2 prints the hybrid system analyzed here. The paper reports Figures 1--4 for \(\gamma=0\), \(\gamma=0.25\), \(\gamma=0.5\), and \(\gamma=0.75\), states that the disease is under control within two months when \(75\%\) of infected people are quarantined, and elsewhere reports a positive spreading speed for \(S_0=10\) and \(\gamma=0.75\).

Li and Zou (2009), DOI 10.1007/s11538-009-9457-z, derive a spatial epidemic model with a genuinely fixed latent period. Their infection-age derivation transfers individuals across the fixed age boundary and produces a discrete-delay infection term. That construction supports the distinction used here between deterministic residence time and a continuous hazard before the boundary; it does not contain the source-specific \(e^{-\rho}\) calculation or the corrected \(89.47\%\) quarantine threshold.

No inspected publication supplied the same correction for the 2024 source.

## Limitations

This finding does not reproduce the unpublished numerical code. If the implementation differed from the printed system, the numerical figures could correspond to another model; the publication does not document such a change.

The result does not dispute the general qualitative statement that increasing quarantine reduces transmission. It identifies the exact mismatch between the published fixed-delay interpretation, the printed simulation equations, and the claimed \(75\%\) containment level.

## References

1. K. M. Alanazi, “The asymptotic spreading speeds of COVID-19 with the effect of delay and quarantine,” AIMS Mathematics 9 (2024), 19397--19413. DOI: 10.3934/math.2024945.
2. J. Li, X. Zou, “Modeling spatial spread of infectious diseases with a fixed latent period in a spatially continuous domain,” Bulletin of Mathematical Biology 71 (2009), 2048--2079. DOI: 10.1007/s11538-009-9457-z.
