# Fourth-order identifiability and a sharp kurtosis floor in active dimers

## Finding
In the continuously fluctuating nonreciprocal dimer of Cocconi–Alston–Bertrand, the exactly decoupled stiffness-fluctuation case has a drift-only center-of-mass velocity equal to the product of two independent stationary Ornstein–Uhlenbeck processes. Its covariance reveals only the **sum** of the two relaxation rates, and every odd joint moment vanishes. Nevertheless a **single positive-lag connected fourth-order measurement** reconstructs both rates, up to exchange. Thus order four is the first possible moment order at which this hidden relaxation split is identifiable.

More precisely, let independent, centered, stationary Ornstein–Uhlenbeck processes \(U,V\) have covariance functions \(\mathbb E[U_0U_t]=u^2e^{-a|t|}\) and \(\mathbb E[V_0V_t]=v^2e^{-b|t|}\), with \(a,b,u,v>0\). Let \(H_t=cU_tV_t\), with \(c\ne0\), and \(X_T=\sqrt{2D_0}\,W_T+\int_0^T H_s\,ds\), with \(D_0\ge0\) and independent standard Brownian motion \(W\). Put \(s=a+b\), \(Q=u^2v^2\), and \(\operatorname{cum}\) for the joint fourth cumulant. Then for each \(t>0\),
\[
R(t):=\frac{\mathbb E[H_0H_t]}{\mathbb E[H_0^2]}=e^{-st},\qquad
F(t):=\frac{\operatorname{cum}(H_0,H_0,H_t,H_t)}{2(\mathbb E[H_0^2])^2}
=e^{-2at}+e^{-2bt}+e^{-2st}.
\]
Set \(S=F(t)-R(t)^2\). The unordered pair \(\{e^{-2at},e^{-2bt}\}\) is **exactly** the root multiset of \(z^2-Sz+R(t)^2=0\). Consequently one such fourth-order measurement, the covariance at the same lag, and the equal-time variance determine \(\{a,b\}\) uniquely; the remaining interchange symmetry cannot be resolved from \(H\). Every family with fixed \(s,c^2Q,D_0\) has the same complete second-order statistics of \(H\) and of \(X\), and all third-order joint moments are zero. At fixed \(s\), the excess \(F(t)-3R(t)^2\) is zero exactly when \(a=b\), and is strictly increasing with \(|a-b|\).

The same fourth-order distinction survives integration to displacement. For all \(T>0\), \(\kappa_4(X_T)>0\), where \(\kappa_4(X_T)=\mathbb E[X_T^4]-3\mathbb E[X_T^2]^2\). Define the positive asymptotic active variance fraction
\[
\eta=\frac{2c^2Q/s}{2D_0+2c^2Q/s}\in(0,1].
\]
The long-time standardized fourth cumulant has the **sharp rate**
\[
\lim_{T\to\infty}T\frac{\kappa_4(X_T)}{\operatorname{Var}(X_T)^2}
=\eta^2\frac{6(a^2+3ab+b^2)}{ab(a+b)}
\ \ge\ \frac{30\eta^2}{a+b},
\]
with equality exactly when \(a=b\). Given \(s\) and \(\eta\), the limiting coefficient \(L\) also identifies the unordered rates through
\[
ab=\frac{6s}{L/\eta^2-6/s},\qquad
\{a,b\}=\left\{\frac{s+\sqrt{s^2-4ab}}2,\frac{s-\sqrt{s^2-4ab}}2\right\}.
\]
This is an exact identifiability statement for population moments, **not** a finite-sample estimation guarantee.

## Assumptions and scope
All rates and the two stationary variances are strictly positive; \(c\ne0\). The two OU drivers are independent of each other and the added Brownian noise. The OU processes are initialized jointly in their stationary product Gaussian law. The displacement is observed relative to \(X_0=0\), and all cumulants refer to that displacement, not a purported stationary position law.

For the nonreciprocal dimer, set the correlation parameter of the two fluctuating trap stiffnesses to \(\theta=-1\), omit steric repulsion, and initialize the stiffness sum at its equilibrium value zero. The published reduction identifies \(U=\psi\), \(V=y\), \(c=-1/2\), \(a=\mu\), \(b=2\bar k\), \(u^2=4D_\kappa/\mu\), \(v^2=D_x/\bar k\), and \(D_0=D_x/2\), where \(\bar k,\mu,D_\kappa,D_x>0\). The ordinary Brownian displacement noise is independent of the active drift process. The theorem does not apply unchanged to correlated stiffness sum/difference, finite steric interactions, nonstationary initial OU states, or a non-OU hidden environment.

## Proof
**Second- and third-order obstruction.** Independence and stationarity give \(\mathbb E[H_0H_t]=c^2u^2v^2e^{-(a+b)|t|}\). Changing the sign of the entire Gaussian path \(U\) preserves the joint law but reverses every \(H_t\); hence every odd joint moment, in particular every third-order joint moment, is zero. The covariance of \(X\) for any two observation times is obtained by integrating that of \(H\) and adding the independent Brownian covariance. Therefore no statistical information of moment orders at most three distinguishes parameter pairs with identical \(a+b,c^2Q,D_0\).

**Fourth-order recovery.** For \(t>0\), Isserlis' pairing identity gives \(\mathbb E[U_0^2U_t^2]=u^4(1+2e^{-2at})\), and similarly for \(V\) with rate \(b\). Multiplying by independence and subtracting the three second-moment pairings yields
\[
\operatorname{cum}(H_0,H_0,H_t,H_t)
=2c^4u^4v^4\bigl(e^{-2at}+e^{-2bt}+e^{-2(a+b)t}\bigr).
\]
Writing \(x=e^{-2at}\) and \(y=e^{-2bt}\) gives \(x+y=S\) and \(xy=R(t)^2\), proving the quadratic reconstruction. Since \(x+y=2e^{-st}\cosh((a-b)t)\), the equality and strict monotonicity assertions follow. Permuting \(U,V\), along with their variances and \(a,b\), leaves the observed product unchanged in law, so unordered identification is optimal.

**Finite-time non-Gaussianity.** Conditional on the entire \(U\) trajectory, \(X_T\) is centered Gaussian with random conditional variance \(2D_0T+S_T\), where
\[
S_T=c^2v^2\int_0^T\!\int_0^T U_rU_q e^{-b|r-q|}\,dr\,dq.
\]
Gaussian mixture moments imply \(\kappa_4(X_T)=3\operatorname{Var}(S_T)\). For \(T>0\), the positive, nonzero covariance kernel of \(V\) makes this quadratic form of a nondegenerate Gaussian path nonconstant, so the variance is strictly positive.

**Sharp asymptotic coefficient.** On \(L^2([0,T])\) write \(K_a,K_b\) for the covariance operators with kernels \(u^2e^{-a|r-q|}\) and \(v^2e^{-b|r-q|}\). Wick's identity for centered Gaussian quadratic forms gives
\[
\operatorname{Var}(X_T)=2D_0T+c^2\operatorname{tr}(K_aK_b),\qquad
\kappa_4(X_T)=6c^4\operatorname{tr}\bigl[(K_aK_b)^2\bigr].
\]
Stationarity and an elementary one-dimensional integral yield
\[
\lim_{T\to\infty}\frac{\operatorname{tr}(K_aK_b)}T=\frac{2Q}{a+b}.
\]
All kernels decay exponentially, so after fixing one integration time and translating the other three, dominated convergence establishes the fourfold trace-per-time limit. With the Fourier transform \(\widehat{e^{-a|\cdot|}}(\omega)=2a/(a^2+\omega^2)\), it equals
\[
\begin{aligned}
\lim_{T\to\infty}\frac{\operatorname{tr}[(K_aK_b)^2]}T
&=\frac{Q^2}{2\pi}\int_{-\infty}^\infty
\frac{16a^2b^2\,d\omega}{(a^2+\omega^2)^2(b^2+\omega^2)^2}\\
&=\frac{4Q^2(a^2+3ab+b^2)}{ab(a+b)^3}.
\end{aligned}
\]
For the last identity, differentiate with respect to both positive parameters the basic integral \(\int_{-\infty}^\infty[(a^2+\omega^2)(b^2+\omega^2)]^{-1}d\omega=\pi/[ab(a+b)]\). The two trace limits establish the formula for \(L\). Finally \(a^2+3ab+b^2=(a+b)^2+ab\), and \(ab\le(a+b)^2/4\), with equality only at matching rates. Rearrangement gives both the sharp lower bound and the reconstruction from \(L\).

## Verification
The standalone Python checker `verify_fourth_order.py` runs symbolic Wick and generating-function derivatives, 225 positive-rate single-lag reconstruction/inequality checks, independent numerical Fourier quadrature, and finite-interval covariance-operator matrix traces. It passed 243 assertions on the packaged source version. These finite checks support but do not replace the analytic proof above. A transparent exact example: \((a,b)=(1,3)\) and \((2,2)\), with the same \(Q,c,D_0\), have identical second- and third-order statistics but at lag \(t=\log2\) have \(F(t)=69/256\) and \(33/256\), respectively.

## Relationship to prior work
Cocconi, Alston, and Bertrand, *Active Bound States Arise From Transiently Nonreciprocal Pair Interactions*, arXiv:2304.07738 (first publicly submitted 2023-04-16), derive the underlying two-particle model, product-OU reduction at maximally anticorrelated stiffness fluctuations, its instantaneous Bessel-type propulsion distribution, mean-square displacement, and entropy production; see main-text equations (2), (7), (10)–(13) and the supplemental derivation. Those model and second-order results are not claimed as new. The new assertion is the **sharp moment-order-four identifiability of the two hidden relaxation rates**, together with the exact integrated fourth-cumulant rate and its sharp constrained minimum. The computation uses standard Gaussian pairings, but the parameter-reconstruction statement is not the general Gaussian moment theorem or the published MSD calculation. General Gaussian quadratic-form large-deviation results, such as Bercu–Gamboa–Rouault (1997), cover broader tilted-integral methods; no independent new large-deviation principle is asserted here.

## Limitations
The recovery equations assume exact population correlations of the drift-only active force; measuring position alone does not automatically give noise-free measurements of that force. With positive independent thermal Brownian noise, the asymptotic displacement kurtosis formula is valid, but reconstructing rates from it additionally requires knowing the active variance fraction and summed relaxation rate. Exchange of the two independent OU factors is fundamentally unobservable. No statistical estimator, variance guarantee, general finite-data inference rate, or result for non-Gaussian hidden drivers is claimed. General Gaussian fourth-moment identities underlie the calculation; priority of this model-specific inverse interpretation remains open to independent review.

## References
1. L. Cocconi, H. Alston, T. Bertrand, *Active Bound States Arise From Transiently Nonreciprocal Pair Interactions*, arXiv:2304.07738v1, 2023-04-16; published as *Active bound states arising from transiently nonreciprocal pair interactions*, Physical Review Research **5**, 043032 (2023), DOI: 10.1103/PhysRevResearch.5.043032.
2. B. Bercu, F. Gamboa, A. Rouault, *Large deviations for quadratic forms of stationary Gaussian processes*, Stochastic Processes and their Applications **71**, 75–90 (1997), DOI: 10.1016/S0304-4149(97)00071-9. Cited only as broad prior Gaussian quadratic-form theory, not as a source of a new large-deviation claim.
3. D. Martin et al., *Statistical mechanics of active Ornstein–Uhlenbeck particles*, Physical Review E **103**, 032607 (2021). A Gaussian active-force comparator is fully characterized by second-order statistics; this is background contrast rather than a novelty claim.
