# Fourth-cumulant separation of covariance-matched active dimers

## Finding

Two nonreciprocal Brownian dimers can have the same complete center-of-mass mean-square displacement and the same stationary entropy-production rate, while their fourth displacement cumulants differ strictly at **every** positive observation time.

For any \(D_x,P,Q,\mu,\nu>0\), let \(Y\) be a centered, stationary Ornstein–Uhlenbeck process with covariance \(\mathbb E[Y_sY_t]=Qe^{-\nu|t-s|}\). Independently of \(Y\), choose one of two stationary centered asymmetry processes:

1. **Gaussian driver** \(\Psi^{\mathrm G}\): the stationary Ornstein–Uhlenbeck process with covariance \(Pe^{-\mu|t-s|}\).
2. **Telegraph driver** \(\Psi^{\mathrm T}=\sqrt P\,S\): the symmetric sign process with values \(\pm1\) and flip rate \(\mu/2\); it has the same covariance \(Pe^{-\mu|t-s|}\).

Let \(W\) be standard Brownian motion independent of the other processes and, for \(A\in\{\mathrm G,\mathrm T\}\), set
\[
X_t^A=\sqrt{D_x}\,W_t-\frac12\int_0^t\Psi_s^A Y_s\,ds,\qquad t\ge0.
\]
Both centered displacements have the **same variance for every** \(t\ge0\):
\[
\mathbb E[(X_t^A)^2]=D_xt+\frac{PQ}{2(\mu+\nu)^2}\left[(\mu+\nu)t+e^{-(\mu+\nu)t}-1\right].
\]
Write \(K_A(t)=\operatorname{cum}_4(X_t^A)=\mathbb E[(X_t^A)^4]-3\mathbb E[(X_t^A)^2]^2\). Then
\[
\boxed{K_{\mathrm G}(t)>K_{\mathrm T}(t)>0\quad\text{for every }t>0.}
\]
The exact limiting fourth-cumulant growth rates are
\[
\boxed{\begin{aligned}
\lim_{t\to\infty}\frac{K_{\mathrm G}(t)}t
&=\frac{3P^2Q^2}{2}\,
\frac{\mu^2+3\mu\nu+\nu^2}{\mu\nu(\mu+\nu)^3},\\
\lim_{t\to\infty}\frac{K_{\mathrm T}(t)}t
&=\frac{3P^2Q^2}{2}\,
\frac{\mu}{\nu(\mu+\nu)^3}.
\end{aligned}}
\]
Consequently their exact rate ratio is
\[
\boxed{\frac{\lim_{t\to\infty}K_{\mathrm G}(t)/t}
{\lim_{t\to\infty}K_{\mathrm T}(t)/t}
=1+3\frac{\nu}{\mu}+\left(\frac{\nu}{\mu}\right)^2>1.}
\]
At short times, the two fourth-cumulant exponents also differ:
\[
K_{\mathrm G}(t)=\frac38P^2Q^2t^4+O(t^5),\qquad
K_{\mathrm T}(t)=\frac{\mu}{20}P^2Q^2t^5+O(t^6).
\]
The error statements hold for fixed positive parameters as \(t\downarrow0\).

For the original two-particle fluctuating-interaction model, take \(\nu=2\bar k\), \(Q=D_x/\bar k\), and \(\bar k>0\). Then both are exactly the maximally nonreciprocal, zero-steric-repulsion models in Cocconi–Alston–Bertrand (2023), with matching Gaussian and telegraph stiffness-asymmetry amplitudes. Their full stationary entropy-production rate as defined in that work agrees at
\[
\dot S_{\mathrm i}=\frac{PQ}{2D_x}=\frac{P}{\nu}.
\]
Thus neither the full mean-square displacement curve nor this entropy-production rate separates these two realizations, whereas the fourth displacement cumulant does.

## Assumptions and scope

All parameters are finite and strictly positive. The processes \(Y\) and both driver processes start in their unique stationary distributions. Every process in each model is independent except for its specified temporal self-correlations. The telegraph sign is initially uniform. The observation \(X_t\) is a displacement relative to zero, not a stationary position. A Gaussian Brownian center-of-mass thermal term is included, and its fourth cumulant is zero. No steric interaction, direct external force or correlated thermal noise is present.

One concrete realization in terms of stochastic differential equations is
\[
dY_t=-\nu Y_t\,dt+\sqrt{2\nu Q}\,dB_t^y,
\qquad
 d\Psi_t^{\mathrm G}=-\mu\Psi_t^{\mathrm G}\,dt+\sqrt{2\mu P}\,dB_t^\psi.
\]
For the physical dimer, \(Q=2D_x/\nu\) makes the relative-coordinate noise amplitude equal to \(\sqrt{4D_x}\). A telegraph flip rate of \(\mu/2\) gives the exponential covariance decay rate \(\mu\).

## Proof

**1. Matching two-time statistics.** Independence gives, for either choice of driver,
\[
\mathbb E[\Psi_s^A Y_s\Psi_t^A Y_t]=PQe^{-(\mu+\nu)|t-s|}.
\]
The independent Gaussian thermal term contributes \(D_xt\) to the displacement variance. Integrating the displayed covariance over \([0,t]^2\) with the prefactor \(1/4\) yields the common variance in the Finding section. Therefore the two processes have the same displacement covariance \(\operatorname{Cov}(X_s,X_t)\) for all \(s,t\ge0\), since they both have stationary increments and zero mean.

**2. Fourth cumulants at four ordered times.** Write \(Z_t^A=\Psi_t^A Y_t\) and let \(t_1<t_2<t_3<t_4\), with gaps \(a=t_2-t_1\), \(b=t_3-t_2\), \(c=t_4-t_3\). Define \(L=\mu+\nu\). The independent Gaussian variable \(Y\) obeys Wick's pairing identity. So does \(\Psi^{\mathrm G}\). For the telegraph sign, independence of successive Poisson-flip increments instead gives the exact fourth moment
\[
\mathbb E[\Psi_{t_1}^{\mathrm T}\Psi_{t_2}^{\mathrm T}
\Psi_{t_3}^{\mathrm T}\Psi_{t_4}^{\mathrm T}]
=P^2e^{-\mu(a+c)}.
\]
Subtracting the three products of two-point covariances from the respective four-point products yields
\[
\begin{aligned}
\operatorname{cum}(Z_{t_1}^{\mathrm G},Z_{t_2}^{\mathrm G},Z_{t_3}^{\mathrm G},Z_{t_4}^{\mathrm G})
&=2P^2Q^2e^{-L(a+c)}\left(e^{-2\nu b}+e^{-2\mu b}+e^{-2Lb}\right),\\
\operatorname{cum}(Z_{t_1}^{\mathrm T},Z_{t_2}^{\mathrm T},Z_{t_3}^{\mathrm T},Z_{t_4}^{\mathrm T})
&=2P^2Q^2e^{-L(a+c)}\left(e^{-2\nu b}-e^{-2Lb}\right).
\end{aligned}
\]
Both kernels are strictly positive when all three gaps are positive, and their difference is strictly positive.

**3. Integration over observation time.** Joint cumulants are multilinear. The independent Gaussian Brownian term has zero fourth cumulant and no mixed cumulants. Integrating the preceding stationary fourth-cumulant kernels over \([0,t]^4\), summing the \(24\) chronological orders, and setting \(u=a+c\), \(v=b\) (whose fixed-\(u\) gap decompositions have measure \(u\)) gives the exact finite-time expressions
\[
\begin{aligned}
K_{\mathrm G}(t)&=3P^2Q^2\int_{\substack{u,v>0\\u+v<t}}
(t-u-v)u e^{-Lu}
\left(e^{-2\nu v}+e^{-2\mu v}+e^{-2Lv}\right)\,du\,dv,\\
K_{\mathrm T}(t)&=3P^2Q^2\int_{\substack{u,v>0\\u+v<t}}
(t-u-v)u e^{-Lu}
\left(e^{-2\nu v}-e^{-2Lv}\right)\,du\,dv.
\end{aligned}
\]
Every integrand in the second formula is strictly positive in the interior, and subtracting the second from the first leaves the strictly positive factor \(e^{-2\mu v}+2e^{-2Lv}\). This proves the strict all-time ordering.

**4. Long- and short-time asymptotics.** Divide both integrals by \(t\). The kernel is exponentially integrable on the positive quadrant, and \((t-u-v)_+/t\) is bounded by one and tends pointwise to one. Dominated convergence and elementary integrations
\[
\int_0^\infty u e^{-Lu}\,du=L^{-2},\qquad
\int_0^\infty e^{-2qv}\,dv=(2q)^{-1}
\]
give the stated exact growth rates and ratio. For \(t\downarrow0\), expanding the exponentials in the finite-domain formulas uses \(\int_{u,v>0,\,u+v<t}(t-u-v)u\,du\,dv=t^4/24\) and \(\int_{u,v>0,\,u+v<t}(t-u-v)uv\,du\,dv=t^5/120\); the displayed short-time coefficients follow. All remainders are uniform on each fixed compact positive parameter set.

**5. Matching entropy production in the physical realization.** The entropy-production decomposition of Cocconi–Alston–Bertrand, their Eq. (4), reduces at zero total stiffness fluctuation to \(\langle\Psi^2Y^2\rangle/(2D_x)\). Since both drivers have variance \(P\), the independent stationary displacement variable has variance \(Q\), and both isolated drivers are reversible, this equals \(PQ/(2D_x)\) for either model. This equality is for that paper's stated microscopic pathwise convention and not a claim about entropy reconstructed from observing \(X\) alone.

## Verification

The standalone script `checks/verify.py` uses (i) direct four-time Wick/telegraph moment reconstruction, (ii) independently discretized conditional-Gaussian variance mixtures—Gaussian matrix traces versus explicit four-sign Markov moments—and (iii) numerical integration of the ordered-time kernels. It confirms the algebraic ordering, exact growth-rate ratio, and convergence of independent grid calculations in three disparate parameter regimes. Run from the package root with `python checks/verify.py`; it requires `numpy`, `scipy`, and `sympy`.

The verification script is finite numerical and symbolic support. The universal signs, parameter quantifiers, and limits are established by the explicit analytic kernels and dominated-convergence proof above, not by testing parameter samples.

## Relationship to prior work

Cocconi, Alston, and Bertrand introduced the underlying fluctuating nonreciprocal Brownian dimer. Their main text derives the exact mean-square displacement and mean entropy-production rate separately for maximally anticorrelated Gaussian OU stiffnesses and synchronized discrete telegraph stiffnesses, with the corresponding cases fully developed in the supplementary material. At matched covariance parameters, those second-order and entropy expressions agree. Their main text and supplement do not evaluate or compare the complete fourth displacement cumulants, all-time ordering, short-time exponents, or the rate ratio proved here.

Lemaitre, Sokolov, Metzler, and Chechkin analyze non-Gaussian displacements in active-particle models with *randomly distributed particle speeds or diffusivities*. Their heterogeneity-based superstatistical mechanisms are distinct from the covariance-matched stationary Gaussian-versus-telegraph *interaction-fluctuation* comparison considered here. The two-time and fourth-order formulas above are not consequences of matching mean-square displacements alone; they require separate fourth-time driver laws.

Ordinary Wick/Isserlis identities and the elementary telegraph moment rule provide general machinery for the proof; neither generic moment method is claimed as new. The contribution is the evaluated model-specific all-lag separation, its sharp asymptotic rates and exponents, and the exact compatibility with matched mean-square displacement and the source-defined entropy production.

## Limitations

The theorem needs stationary independent drivers, harmonic relative motion, independent Gaussian translational noise, and no excluded volume. It compares fourth cumulants of a single observed displacement, not full pathwise distinguishability or finite-sample estimation power. Equality of the source-defined entropy-production rates does not imply equality under every coarse-graining or alternative thermodynamic accounting convention. More general coupled driver/relative-coordinate dynamics are not covered. The existence of generic Gaussian moment formulae creates residual mathematical-priority risk even though this particular evaluated comparison was not found in the inspected primary texts. Independent audit and priority assessment have not been performed.

## References

1. L. Cocconi, H. Alston, T. Bertrand, *Active Bound States Arise From Transiently Nonreciprocal Pair Interactions*, arXiv:2304.07738v1 (first posted 2023-04-16), esp. main Eqs. (2), (3), (4), (11), (13), (17), (19) and the supplementary derivations; subsequently *Physical Review Research* **5**, 043032 (2023), DOI: 10.1103/PhysRevResearch.5.043032. https://arxiv.org/pdf/2304.07738
2. E. Lemaitre, I. M. Sokolov, R. Metzler, A. V. Chechkin, *Non-Gaussian displacement distributions in models of heterogeneous active particle dynamics*, arXiv:2208.02780v1 (2022-08-04); *New Journal of Physics* **25**, 013010 (2023), DOI: 10.1088/1367-2630/acb005. https://arxiv.org/abs/2208.02780
