# Fourth-cumulant separation of covariance-matched active dimers

## Finding

Two solvable nonreciprocal Brownian-dimer protocols can have **identical center-of-mass mean-square displacement at every time and identical stationary mean entropy-production rate**, yet their displacement fourth cumulants are strictly ordered at every positive observation time. The separation has a closed, dimensionless long-time ratio.

Let \(a,b,g,\sigma,\eta>0\). Let \(Y\) be a stationary Ornstein–Uhlenbeck process with
\[
 dY_t=-bY_t\,dt+\sqrt{2b\sigma^2}\,dB_t^Y,
 \qquad \mathbb E[Y_sY_t]=\sigma^2e^{-b|t-s|}.
\]
Independently, let \(P\) be either (G) a stationary Gaussian Ornstein–Uhlenbeck process
\[
 dP_t=-aP_t\,dt+\sqrt{2ag^2}\,dB_t^P,
\]
or (T) a stationary symmetric telegraph process with values \(\pm g\), each switching sign at rate \(a/2\). Both satisfy \(\mathbb E[P_sP_t]=g^2e^{-a|t-s|}\). The two protocols drive
\[
 X_t-X_0=-\tfrac12\int_0^t P_sY_s\,ds+\sqrt{\eta}\,B_t^X,
\]
where \(B^X\) is an independent Brownian motion and \(X_0\) is a deterministic reference point. Denote by \(\mathcal K_G(t)\) and \(\mathcal K_T(t)\) the fourth cumulants \(\mathbb E[(X_t-X_0)^4]-3\operatorname{Var}(X_t-X_0)^2\) of the centered displacements.

**Exact second-order degeneracy.** At every \(t\ge0\),
\[
 \operatorname{Var}(X_t-X_0)=\eta t+\frac{g^2\sigma^2}{2(a+b)}\left[t-\frac{1-e^{-(a+b)t}}{a+b}\right]
\]
in both protocols.

**Strict finite-time ordering and sharp asymptotic ratio.** For every \(t>0\),
\[
 0<\mathcal K_T(t)<\mathcal K_G(t).
\]
Writing \(s=a+b\), the exact long-time rates are
\[
 \lim_{t\to\infty}\frac{\mathcal K_G(t)}t
 =\frac{3g^4\sigma^4(a^2+3ab+b^2)}{2ab(a+b)^3},
 \qquad
 \lim_{t\to\infty}\frac{\mathcal K_T(t)}t
 =\frac{3g^4\sigma^4a}{2b(a+b)^3}.
\]
In particular, the ratio of the two asymptotic fourth-cumulant rates is
\[
 \boxed{\frac{a^2}{a^2+3ab+b^2}\in(0,1)}.
\]
This ratio is independent of forcing amplitude, thermal separation variance and independent center-of-mass readout diffusion.

**Physical calibration.** For the two-particle model without repulsion in Cocconi–Alston–Bertrand (2023), set \(b=2\bar k\), \(\sigma^2=D_x/\bar k\), \(\eta=D_x\), \(g=2\kappa_0\), and \(a=\mu=2\lambda\). Match continuous and discrete nonreciprocal force fluctuations by setting \(D_\kappa=\mu\kappa_0^2\). Here \(\bar k,D_x,\kappa_0,\mu,\lambda>0\). Both protocols then have precisely the same entire center-of-mass MSD and, under the source's thermodynamic convention, the same mean entropy-production rate \(2\kappa_0^2/\bar k\), although their fourth cumulants differ at every positive lag. In physical rates the long-time ratio is \(\lambda^2/(\lambda^2+3\lambda\bar k+\bar k^2)\).

## Assumptions and scope

All stochastic processes are jointly stationary at the level of their instantaneous force and relative coordinate, and \(P\), \(Y\), and \(B^X\) are independent. Initial states of the OU and telegraph variables have their stated invariant distributions. The displacement process \(X\) itself need not have a stationary position law. The assertion concerns increments from the observation origin, not a stationary unconfined center-of-mass position. There is no excluded boundary within \(a,b,g,\sigma,\eta>0\). The particle mapping assumes exactly antisymmetric stiffness fluctuations, no steric repulsion, and independent equal-strength thermal particle noises.

## Proof

Let \(H_t=-P_tY_t/2\). Both protocols have the same stationary velocity covariance
\[
 \mathbb E[H_sH_t]=\frac{g^2\sigma^2}{4}e^{-(a+b)|t-s|}.
\]
The covariance integral for \(\int_0^t H_u\,du\), together with independent Brownian variance \(\eta t\), gives the claimed common second moment.

For four ordered instants \(t_1<t_2<t_3<t_4\), let \(x=t_2-t_1\), \(u=t_3-t_2\), \(z=t_4-t_3\), and set \(P_c=e^{-c(x+z)}\), \(Q_c=e^{-c(x+2u+z)}\). Wick's theorem gives the Gaussian forcing four-point function \(g^4(P_a+2Q_a)\). For the telegraph force, independent Poisson flip counts on the three consecutive intervals give the exact four-point function \(g^4P_a\). Independence and Wick's theorem for \(Y\) give \(\mathbb E[Y_{t_1}\cdots Y_{t_4}]=\sigma^4(P_b+2Q_b)\).

The three covariance-pairing subtractions in the fourth joint cumulant are the same in both protocols. Expanding these subtractions therefore yields the ordered four-time cumulant densities
\[
 \operatorname{cum}_G(H_{t_1},\ldots,H_{t_4})
 =\frac{g^4\sigma^4}{8}(P_aQ_b+Q_aP_b+Q_aQ_b),
\]
\[
 \operatorname{cum}_T(H_{t_1},\ldots,H_{t_4})
 =\frac{g^4\sigma^4}{8}(P_aQ_b-Q_aQ_b).
\]
The second expression is positive for \(u>0\) because \(Q_a=P_ae^{-2au}<P_a\). Their difference is strictly positive whenever the temporal gaps are positive. Integrating over all \(4!\) orders proves the strict finite-time inequalities. An independent Gaussian increment has zero fourth cumulant and does not modify them.

More explicitly, setting \(s=a+b\), the change of variables \(w=x+z\) yields the exact, nonasymptotic representations
\[
 \mathcal K_G(t)=3g^4\sigma^4
 \int_{\substack{u,w\ge0\\u+w\le t}}
 w(t-u-w)e^{-sw}
 (e^{-2au}+e^{-2bu}+e^{-2su})\,dw\,du,
\]
\[
 \mathcal K_T(t)=3g^4\sigma^4
 \int_{\substack{u,w\ge0\\u+w\le t}}
 w(t-u-w)e^{-sw}
 (e^{-2bu}-e^{-2su})\,dw\,du.
\]
Both kernels are integrable over the positive quadrant after division by \(t\); dominated convergence applies because \(0\le(t-u-w)_+/t\le1\). Using \(\int_0^\infty we^{-sw}\,dw=s^{-2}\) and \(\int_0^\infty e^{-2cu}\,du=(2c)^{-1}\) gives
\[
 \lim_{t\to\infty}\frac{\mathcal K_G(t)}t
 =\frac{3g^4\sigma^4}{2s^2}(a^{-1}+b^{-1}+s^{-1}),
 \qquad
 \lim_{t\to\infty}\frac{\mathcal K_T(t)}t
 =\frac{3g^4\sigma^4}{2s^2}(b^{-1}-s^{-1}),
\]
which simplify to the displayed formulas and ratio.

The source's continuous maximally nonreciprocal protocol has independent \(P\) and \(Y\), with the stationary \(P\) variance \(4D_\kappa/\mu\); its synchronized discrete protocol has \(P=\pm2\kappa_0\) switching at rate \(\lambda\). The given calibration makes the variances and temporal decay rates identical. The source's entropy formulas, respectively \(2D_\kappa/(\bar k\mu)\) and \(2\kappa_0^2/\bar k\), coincide under that calibration. These prior formulas are not claimed as new.

## Verification

The self-contained Python program `verify_cumulants.py` independently propagates exact polynomial moment equations for the Gaussian and telegraph force models, without using the ordered-four-time cumulant formula. It compares the resulting fourth cumulants with independent one-dimensional quadratures of the displayed integral representations, tests three nondegenerate parameter sets and four finite time horizons per set, checks exact second moments and rate identities, and reports 84 successful deterministic checks. Dependencies are Python, NumPy, and SciPy. Run `python verify_cumulants.py`. Numerical checks are corroboration, not a proof of the inequalities for all parameters and times.

## Relationship to prior work

Cocconi, Alston and Bertrand (arXiv:2304.07738, main Eqs. (2), (11)–(19), supplement Eqs. (S32)–(S37)) introduced the nonreciprocal Brownian dimer and derived its mean-square displacement and mean entropy-production rate for continuous and synchronized discrete forcing. The matching of the two protocols' second-order statistics under the stated parameter calibration uses those source formulas. The finite-time strict fourth-cumulant separation and its evaluated long-time ratio are the specific new assertions assessed here.

Allegrini, Grigolini, Palatella and West (arXiv:cond-mat/0402494, Eqs. (2), (4) and (21)) develop Gaussian Wick and dichotomic four-time factorization laws, including a more general non-Poisson aging analysis. Those underlying four-time identities are prior mathematics. The present result uses them to evaluate a different physical composite observable involving an independent OU relative mode and derives an explicit all-time positive ordering and universal long-time ratio. No claim is made that the Gaussian or telegraph four-time identities are themselves new.

## Limitations

The theorem does not apply automatically when the relative coordinate and fluctuating nonreciprocal force are correlated, when the force follows non-Poisson renewal statistics, or when finite-size steric interactions are added. Fourth-cumulant ratios concern ensemble increment statistics and are not finite-sample power or measurement-efficiency guarantees. The comparison of relevant accessible literature does not certify publication priority against every potentially broader cumulant theorem.

## References

1. L. Cocconi, H. Alston and T. Bertrand, *Active Bound States Arise From Transiently Nonreciprocal Pair Interactions*, arXiv:2304.07738v1 (16 April 2023), https://arxiv.org/abs/2304.07738, full text https://arxiv.org/pdf/2304.07738.
2. P. Allegrini, P. Grigolini, L. Palatella and B. J. West, *Non-Poisson dichotomous noise: higher-order correlation functions and aging*, arXiv:cond-mat/0402494 (2004), https://arxiv.org/abs/cond-mat/0402494, full text https://arxiv.org/pdf/cond-mat/0402494.
