# Stationary energy-correlation tomography of a switching-temperature harmonic trap

## Finding

Fix a known trap relaxation rate \(\kappa>0\) and a known observation lag \(h>0\). Consider the stationary one-dimensional overdamped Langevin model
\[
 dX_t=-\kappa X_t\,dt+\sqrt{2D_{S_t}}\,dW_t,
 \qquad D_{\pm}=\bar D(1\pm\delta),
\]
where \(W\) is standard Brownian motion, the independent stationary environment \(S\in\{-1,+1\}\) flips from either state to the other at rate \(\lambda>0\), the mean diffusivity is \(\bar D>0\), and the contrast satisfies \(0<\delta<1\). Exchanging the state labels leaves the observed process unchanged.

Define the three observable stationary statistics
\[
 V=\mathbb E[X_0^2],\qquad
 K=\frac{\mathbb E[X_0^4]}{V^2}-3,\qquad
 C=\frac{\operatorname{Cov}(X_0^2,X_h^2)}{V^2}.
\]
Set \(a=e^{-2\kappa h}\), and define, for \(s\ge0\),
\[
 F(s)=a+2\kappa\int_0^h e^{-2\kappa(h-u)}e^{-2su}\,du
 =\begin{cases}
 \dfrac{\kappa e^{-2sh}-s a}{\kappa-s},&s\ne\kappa,\\[5pt]
 a(1+2\kappa h),&s=\kappa.
 \end{cases}
\]
Then a real triple \((V,K,C)\) is produced by **exactly one** pair of strictly positive diffusivities and one positive switching rate, up to exchanging the environment labels, if and only if
\[
 \boxed{\quad V>0,\qquad 0<K<3,\qquad
 F\!\left(\kappa\left(\frac3K-1\right)\right)<
 \frac{3(C-2a)}K-2a<1.\quad}
\]
These inequalities are strict and sharp. For every admissible triple the reconstruction is
\[
 \bar D=\kappa V,\qquad
 F(\lambda)=\frac{3(C-2a)}K-2a,\qquad
 \delta=\sqrt{\frac{K(\kappa+\lambda)}{3\kappa}},\qquad
 D_\pm=\bar D(1\pm\delta),
\]
where the equation for \(\lambda\) has exactly one solution in
\(\bigl(0,\kappa(3/K-1)\bigr)\).

In particular, ordinary positional covariance \(\mathbb E[X_0X_h]=V e^{-\kappa h}\) cannot see the hidden switching parameters; the fourth-order time-lagged observable supplies the missing rate information.

## Assumptions and scope

The result applies to the *unique stationary two-sided solution* of the stated linear stochastic differential equation with a stationary symmetric two-state continuous-time Markov environment, independent of \(W\). The physical temperature interpretation assumes fixed mobility, so the diffusion coefficient is proportional to bath temperature. No absorbing or reflecting spatial boundary is present. The observations \(V,K,C\) are exact ensemble expectations, not sample estimates. The positive contrast excludes the indistinguishable-temperature Gaussian limit; the upper bound \(\delta<1\) enforces strict positivity of both state diffusivities.

## Proof

**1. Conditional Gaussian variance.** The unique stationary stochastic convolution is
\[
 X_t=\int_{-\infty}^{t}e^{-\kappa(t-u)}\sqrt{2\bar D(1+\delta S_u)}\,dW_u.
\]
Conditional on the entire environment path, \(X_t\) is centered Gaussian with conditional variance
\[
 Y_t=\frac{\bar D}{\kappa}(1+\delta Z_t),\qquad
 Z_t=2\kappa\int_0^\infty e^{-2\kappa u} S_{t-u}\,du.
\]
The bounded filtered environment satisfies \(\dot Z_t=2\kappa(S_t-Z_t)\) between environment jumps, \(|Z_t|\le1\), and \(\mathbb E[Z_t]=0\). Write \(c=\kappa/(\kappa+\lambda)\). Using the environment generator and stationarity,
\[
 0=2\kappa\bigl(1-\mathbb E[Z_tS_t]\bigr)-2\lambda\mathbb E[Z_tS_t],\qquad
 0=4\kappa\bigl(\mathbb E[Z_tS_t]-\mathbb E[Z_t^2]\bigr).
\]
Consequently \(\mathbb E[Z_tS_t]=\mathbb E[Z_t^2]=c\).

**2. Variance and kurtosis.** With \(V=\bar D/\kappa\), conditional Gaussian fourth moments give
\[
 \mathbb E[X_0^2]=V,\qquad
 \mathbb E[X_0^4]=3V^2(1+\delta^2c),\qquad
 K=3\delta^2\frac{\kappa}{\kappa+\lambda}.
\]
Thus \(0<K<3\), and, when \(K\) is given, strict positivity of both diffusivities is equivalent to
\[
 0<\lambda<\lambda_{\max}:=\kappa\left(\frac3K-1\right).
\]

**3. Filtered-bath two-time covariance.** The Markov property yields \(\mathbb E[S_{t+u}\mid S_t]=e^{-2\lambda u}S_t\), hence
\(\mathbb E[Z_tS_{t+u}]=c e^{-2\lambda u}\) for \(u\ge0\). Solving the linear evolution equation for \(\mathbb E[Z_tZ_{t+h}]\) gives
\[
 \operatorname{Cov}(Z_t,Z_{t+h})=cF(\lambda).
\]
Conditionally on the environment path, the pair \((X_t,X_{t+h})\) is jointly centered Gaussian, with conditional cross covariance \(e^{-\kappa h}Y_t\). Isserlis' identity therefore yields
\[
 \mathbb E[X_t^2X_{t+h}^2\mid S]
 =Y_tY_{t+h}+2e^{-2\kappa h}Y_t^2.
\]
Averaging and subtracting \(V^2\) gives the exact normalized square covariance
\[
 C=2a+\frac K3\bigl(2a+F(\lambda)\bigr).
\]

**4. Global invertibility and sharp range.** The kernel has the strictly positive integral representation given above; its derivative exists and satisfies
\[
 F'(s)=-4\kappa\int_0^h u e^{-2\kappa(h-u)}e^{-2su}\,du<0
 \qquad(s\ge0,h>0).
\]
Moreover \(F(0)=1\) and \(F(s)\downarrow a\) as \(s\to\infty\). Therefore \(F\) is a strictly decreasing bijection from \((0,\lambda_{\max})\) onto \((F(\lambda_{\max}),1)\). Combining Step 2 with the formula for \(C\) proves the stated necessity and sufficiency, uniqueness, and reconstruction. Conversely every triple in that open region yields a positive \(\lambda\), a contrast \(0<\delta<1\), and \(\bar D>0\), so its forward observables equal the prescribed triple. The boundary \(\lambda\downarrow0\) excludes positive switching, and \(\lambda\uparrow\lambda_{\max}\) forces \(\delta\uparrow1\) and the smaller diffusivity to zero. Both boundaries are therefore sharp and unattainable within the hypotheses.

**5. Second-order blindness.** Conditional Gaussianity and independence of future Wiener increments give \(\mathbb E[X_tX_{t+h}]=e^{-\kappa h}\mathbb E[X_t^2]=Ve^{-\kappa h}\), irrespective of \(\lambda\) or \(\delta\). This establishes why a genuinely fourth-order observable is required for the stated reconstruction.

## Verification

Run `python3 check_claim.py` with Python 3 standard library; it independently solves the two-state stationary second- and fourth-moment linear systems, propagates conditional second moments across the observation lag by numerical quadrature, and compares these results to the theorem. It then reconstructs parameters over 600 independently chosen admissible cases. The analytical strict monotonicity and global range proof above are necessary; finite tests alone do not prove either assertion.

## Relationship to prior work

Huang, Jansen, Mandjes, Spreij and De Turck (arXiv:1412.7952v1, first public 2014-12-26), especially Sections 3.4 and 4, establish broad moment recursions and joint-transform equations for Markov-modulated Ornstein–Uhlenbeck processes. Those are forward tools; they do not assert the explicit sharp three-observable realizability region or its unique inverse in the symmetric fluctuating-diffusivity harmonic trap. Miyaguchi, Akimoto and Yamamoto (arXiv:1605.00106v1, first public 2016-04-30) study two-state fluctuating diffusivity and time-averaged observables predominantly *without harmonic confinement* and with general renewal holding times. Lanoiselée et al. (arXiv:2207.14068v1, 2022-07-28) analyze harmonic trapping with **continuously** fluctuating CIR diffusivity and derive forward distributional and kurtosis information, not this discrete-switching three-observable classification. The claimed contribution is the constructive global inverse and exact range, not the underlying forward stochastic models or generic conditional-Gaussian identities.

## Limitations

The inference assumes known positive \(\kappa\) and \(h\), symmetric switching with the same rate in both directions, and a stationary process. It determines the unordered diffusivity pair, not the hidden labels. It does not provide an error model or finite-sample confidence intervals; near the excluded boundaries, parameter recovery may be ill-conditioned. The conclusion does not extend automatically to unequal switching rates, switching stiffness or friction, colored thermal driving, or spatially dependent diffusivity. A general higher-moment framework in prior literature can imply the forward identities after specialization; no priority assertion is made for those elementary component identities separately.

## References

1. G. Huang, H. M. Jansen, M. Mandjes, P. Spreij and K. De Turck, *Markov-modulated Ornstein-Uhlenbeck processes*, arXiv:1412.7952v1 (2014-12-26); Advances in Applied Probability 48 (2016), 235–254. https://arxiv.org/abs/1412.7952
2. T. Miyaguchi, T. Akimoto and E. Yamamoto, *Langevin equation with fluctuating diffusivity: a two-state model*, arXiv:1605.00106v1 (2016-04-30). https://arxiv.org/abs/1605.00106
3. Y. Lanoiselée, A. Stanislavsky, D. Calebiro and A. Weron, *Temperature and friction fluctuations inside a harmonic potential*, arXiv:2207.14068v1 (2022-07-28). https://arxiv.org/abs/2207.14068
