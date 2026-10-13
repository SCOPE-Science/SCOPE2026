# Extreme survivors identify the heaviest F-LLoM tiers
## Finding
Consider the finite-mixture survival model with component survival functions
\[
S_m(y\mid x)
=
\left(1+\frac{y}{\kappa_m(x)}\right)^{-\lambda_m},
\qquad
\kappa_m(x)=\frac{\lambda_m}{\theta_m(x)},
\]
and softmax mixing weights
\[
\pi_m(x)>0,
\qquad
\sum_{m=1}^M\pi_m(x)=1.
\]
This is the component form of the F-LLoM model.

For fixed finite \(x\), define
\[
\lambda_*=\min_{1\le m\le M}\lambda_m,
\qquad
I_*=\{m:\lambda_m=\lambda_*\},
\]
and
\[
C_*(x)=
\sum_{m\in I_*}
\pi_m(x)\kappa_m(x)^{\lambda_*}.
\]
Then
\[
\boxed{
S_Y(y\mid x)
\sim
C_*(x)y^{-\lambda_*}
}
\qquad(y\to\infty).
\]
The corresponding density and hazard satisfy
\[
\boxed{
f_Y(y\mid x)
\sim
\lambda_*C_*(x)y^{-\lambda_*-1}
}
\]
and
\[
\boxed{
h_Y(y\mid x)\sim\frac{\lambda_*}{y}.}
\]
Thus covariate-dependent weights and scales affect the leading tail constant, but they cancel from the first-order terminal hazard.

The same asymptotics identify the latent risk tier among sufficiently extreme survivors. For every component,
\[
\Pr(M=m\mid Y>y,x)
=
\frac{\pi_m(x)S_m(y\mid x)}{S_Y(y\mid x)}.
\]
Consequently,
\[
\boxed{
\Pr(M=m\mid Y>y,x)
\longrightarrow
\begin{cases}
\displaystyle
\frac{\pi_m(x)\kappa_m(x)^{\lambda_*}}{C_*(x)},
&m\in I_*,\\[8pt]
0,&m\notin I_*.
\end{cases}}
\]
If there is a unique heaviest-tail tier \(m_*\), then
\[
\boxed{
\Pr(M=m_*\mid Y>y,x)\longrightarrow1.
}
\]
Writing
\[
\Delta=
\min_{m\ne m_*}(\lambda_m-\lambda_*)>0,
\]
the convergence has the quantitative rate
\[
1-\Pr(M=m_*\mid Y>y,x)
=
O\!\left(y^{-\min\{1,\Delta\}}\right).
\]

The result gives a sharp distinction between ordinary covariate-dependent tier allocation and extreme-survivor allocation. At ordinary times, the softmax weights can vary strongly with \(x\). In the far right tail, every tier with a larger shape parameter loses all posterior mass; only the minimum-shape tier or tied minimum-shape tiers remain.

## Assumptions and scope
There are finitely many tiers. The covariate vector \(x\) is fixed and finite, so the multinomial-logit weights satisfy
\[
0<\pi_m(x)<1.
\]
Each component has
\[
\lambda_m>0,
\qquad
\theta_m(x)>0,
\qquad
\kappa_m(x)=\lambda_m/\theta_m(x)>0.
\]

The theorem concerns conditional tail behavior given \(x\). It does not claim that covariates are irrelevant at moderate survival times: they affect both \(\pi_m(x)\) and \(\kappa_m(x)\), and therefore affect the multiplicative tail constant and the finite-time posterior tier probabilities.

If the minimum shape is tied, extreme observations do not identify a single tier. They identify the tie set and leave the explicit limiting weights displayed above.

## Proof
For each component,
\[
S_m(y\mid x)
=
\left(1+\frac{y}{\kappa_m(x)}\right)^{-\lambda_m}
=
\kappa_m(x)^{\lambda_m}y^{-\lambda_m}
\left(1+\frac{\kappa_m(x)}{y}\right)^{-\lambda_m}.
\]
Hence
\[
S_m(y\mid x)
=
\kappa_m(x)^{\lambda_m}y^{-\lambda_m}
\{1+O(y^{-1})\}.
\]
Summing with the positive mixture weights gives
\[
S_Y(y\mid x)
=
\sum_m\pi_m(x)S_m(y\mid x).
\]
Terms with \(\lambda_m>\lambda_*\) are \(o(y^{-\lambda_*})\), while the terms in \(I_*\) have common power \(y^{-\lambda_*}\). Therefore
\[
S_Y(y\mid x)
\sim
\left[
\sum_{m\in I_*}
\pi_m(x)\kappa_m(x)^{\lambda_*}
\right]y^{-\lambda_*}.
\]

The component density is
\[
f_m(y\mid x)
=
\frac{\lambda_m}{\kappa_m(x)}
\left(1+\frac{y}{\kappa_m(x)}\right)^{-\lambda_m-1},
\]
so
\[
f_m(y\mid x)
\sim
\lambda_m\kappa_m(x)^{\lambda_m}y^{-\lambda_m-1}.
\]
The same dominance argument yields
\[
f_Y(y\mid x)
\sim
\lambda_*C_*(x)y^{-\lambda_*-1}.
\]
Dividing density by survival proves
\[
h_Y(y\mid x)\sim\lambda_*/y.
\]

For the posterior tier probability among survivors,
\[
r_m(y,x)
=
\frac{\pi_m(x)S_m(y\mid x)}{S_Y(y\mid x)}.
\]
If \(m\notin I_*\), its numerator is \(o(y^{-\lambda_*})\), so \(r_m(y,x)\to0\). If \(m\in I_*\), numerator and denominator have the same power, and cancellation gives
\[
r_m(y,x)
\to
\frac{\pi_m(x)\kappa_m(x)^{\lambda_*}}{C_*(x)}.
\]

If the minimizer \(m_*\) is unique, expand its own Lomax factor to relative order \(O(y^{-1})\). Every competing tier has relative order
\[
O\!\left(y^{-(\lambda_m-\lambda_*)}\right).
\]
The largest error is therefore
\[
O\!\left(y^{-\min\{1,\Delta\}}\right),
\]
which proves the quantitative localization rate.

## Verification
The accompanying checker evaluates exact finite-mixture survival functions, densities, hazards, and survivor-posterior tier probabilities for both a unique-minimum example and a tied-minimum example.

For the unique-minimum example it verifies numerically that
\[
y^{\lambda_*}S_Y(y\mid x)\to C_*(x),
\qquad
yh_Y(y\mid x)\to\lambda_*,
\]
and that the posterior probability of the unique heaviest-tail tier tends to one at the predicted polynomial rate.

For the tied example it verifies convergence of posterior survivor weights to
\[
\frac{\pi_m(x)\kappa_m(x)^{\lambda_*}}{C_*(x)}.
\]
These finite calculations are consistency checks only. The infinite-domain statements follow from the explicit Lomax equivalents above.

## Relationship to prior work
Rahmouni introduces F-LLoM as a finite mixture with multinomial-logit tier weights and component-specific Lomax distributions. The source states that the overall tail is governed by the smallest component shape and notes that the proportionality constant depends on the mixing proportions and scales. It does not state the exact constant \(C_*(x)\), the terminal hazard equivalent, or the posterior localization of latent tiers among extreme survivors.

Earlier work on two-component Lomax mixtures focuses on Bayesian estimation, censoring, and prior choice rather than extreme-survivor latent-class localization. General finite-mixture theory explains the posterior-ratio identity, but the model-specific asymptotic collapse depends on combining that identity with the distinct regularly varying Lomax powers and the F-LLoM covariate-dependent scales.

The theorem therefore sharpens the source's qualitative statement that latent tiers represent distinct tail regimes: with a unique minimum shape, sufficiently extreme survivors asymptotically identify that tier with probability one; under a tie, the surviving ambiguity has an explicit closed form.

## Limitations
The result is first-order in the tail. It does not give second-order hazard constants or a uniform approximation over unbounded covariate regions.

The covariate vector is fixed while \(y\to\infty\). If covariates themselves vary with the tail threshold, softmax weights or scales could shrink or grow at competing rates and require a separate joint asymptotic analysis.

The finding does not reassess the source's EM estimation, identifiability conditions, simulation study, or empirical application.

## References
1. M. Rahmouni, “Frailty-Augmented Logistic-Weighted Lomax Mixture regression for survival analysis,” AIMS Mathematics 11 (2026), 6329–6349. DOI: 10.3934/math.2026261.
2. F. Younis, M. Aslam, and M. I. Bhatti, “Preference of Prior for Two-Component Mixture of Lomax Distribution,” Journal of Statistical Theory and Applications 20 (2021), 407–424. DOI: 10.2991/jsta.d.210616.002.
