# Dilogarithmic large deviations of stationary Brownian positions under weak partial resetting

## Finding
For a Brownian searcher whose position is multiplied by a factor approaching unit magnitude at Poisson times, a parameter-free large-deviation rate quantifies the rare stationary excursions that survive beyond the Gaussian core. Its cumulant limit is a dilogarithm; its rate function crosses over from quadratic behavior at small scaled displacement to a linear law with an explicit universal intercept.

Fix \(D,r>0\), let \(0<|a|<1\), and write
\[
\varepsilon=-\log(a^2),\qquad U_\varepsilon=\sqrt{r/D}\,X^{(a)},\qquad Y_\varepsilon=\varepsilon U_\varepsilon,
\]
where \(X^{(a)}\) is the stationary position. For every Borel set \(A\subset\mathbb R\), the family \(Y_\varepsilon\), as \(\varepsilon\downarrow0\), satisfies the full large-deviation bounds
\[
-\inf_{y\in A^\circ}I(y)\le\liminf_{\varepsilon\downarrow0}\varepsilon\log\mathbb P(Y_\varepsilon\in A)
\le\limsup_{\varepsilon\downarrow0}\varepsilon\log\mathbb P(Y_\varepsilon\in A)
\le-\inf_{y\in\overline A}I(y),
\]
where
\[
I(y)=\sup_{|\theta|<1}\{\theta y-\operatorname{Li}_2(\theta^2)\},\qquad
\operatorname{Li}_2(z)=\sum_{m=1}^{\infty}\frac{z^m}{m^2}.
\]
The rate is even, strictly convex, smooth, and good, with its unique zero at \(y=0\). The optimizer is uniquely determined by
\[
y=-\frac{2\log(1-\theta^2)}{\theta},\qquad |\theta|<1,
\]
with the continuous value \(\theta=0\) at \(y=0\). Its two decisive limiting laws are
\[
I(y)=\frac{y^2}{4}-\frac{y^4}{64}+O(y^6)\quad(y\to0),\qquad
I(y)=|y|-\frac{\pi^2}{6}+O(e^{-|y|/2})\quad(|y|\to\infty).
\]
The result is identical for positive and negative rescaling factors of the same magnitude.

## Assumptions and scope
Let \(B\) be standard Brownian motion and \(N\) an independent Poisson process of rate \(r>0\). Between jumps, the position evolves as \(dX_t=\sqrt{2D}\,dB_t\), where \(D>0\); at each jump time \(T\), it satisfies \(X_T=aX_{T-}\), where \(-1<a<1\). The large-deviation family uses \(0<|a|<1\) tending to \(1\) in magnitude, with \(\varepsilon=-\log(a^2)\). All statements concern the stationary spatial distribution and the limit \(\varepsilon\downarrow0\), not large observation-time deviations of trajectories or time-averaged functionals. For the distributional construction, a symmetric unit-scale Laplace variable \(L\) has density \(e^{-|x|}/2\).

## Proof
**1. Stationary perpetuity and normalization.** Independent Poisson interarrival times have law \(\operatorname{Exp}(r)\). A Brownian increment over such an interval has characteristic function \(r/(r+Dk^2)\), hence is symmetric Laplace with spatial scale \(\sqrt{D/r}\). By independence and the memoryless stationary-age property, the dimensionless stationary position has the exact convergent representation
\[
U_\varepsilon\;\stackrel{\mathrm d}=\;\sum_{j=0}^{\infty}a^jL_j,
\]
where the \(L_j\) are independent unit Laplace variables. The series converges in \(L^2\) since \(\sum_j a^{2j}<\infty\). Stationarity also follows by the renewal construction; uniqueness follows by coupling two trajectories with the same Brownian path and Poisson times, since their difference is multiplied by \(a^{N_t}\to0\) almost surely.

For every \(|\theta|<1\), the Laplace moment generating function is finite and equals
\[
M_\varepsilon(\theta)=\mathbb E e^{\theta U_\varepsilon}
=\prod_{j=0}^{\infty}(1-\theta^2 e^{-\varepsilon j})^{-1}.
\]
For \(|\theta|\ge1\), it is infinite because its first Laplace summand has no such moment. This sharp domain boundary is used below.

**2. Dilogarithmic scaled cumulants.** Put \(\Lambda_\varepsilon(\theta)=\log M_\varepsilon(\theta)\). The integrable function \(f_\theta(t)=-\log(1-\theta^2e^{-t})\) gives a Riemann sum
\[
\lim_{\varepsilon\downarrow0}\varepsilon\Lambda_\varepsilon(\theta)
=\int_0^\infty-\log(1-\theta^2e^{-t})\,dt
=\sum_{m=1}^\infty\frac{\theta^{2m}}{m^2}
=:\Lambda(\theta)=\operatorname{Li}_2(\theta^2).
\]
The convergence also holds for the first and second derivatives uniformly on compact subintervals of \((-1,1)\), because the differentiated integrands are bounded there by integrable exponential tails. The same expression gives the logarithmic transform of \(Y_\varepsilon/\varepsilon\), since \(Y_\varepsilon/\varepsilon=U_\varepsilon\).

For \(\theta\ne0\),
\[
\Lambda'(\theta)=-\frac{2\log(1-\theta^2)}{\theta}.
\]
Its continuous value at zero is zero. From the positive coefficients in \(\Lambda(\theta)=\sum_{m\ge1}\theta^{2m}/m^2\), \(\Lambda''(\theta)>0\) for \(|\theta|<1\). Moreover \(\Lambda'(\theta)\to\pm\infty\) at the two respective endpoints. Thus for each real \(y\) there is exactly one \(\theta_y\in(-1,1)\) satisfying \(\Lambda'(\theta_y)=y\), and \(I(y)=\theta_yy-\Lambda(\theta_y)\) is finite, smooth and strictly convex. As \(I(y)\ge \theta_0|y|-\Lambda(\theta_0)\) for each \(0<\theta_0<1\), its sublevel sets are compact.

**3. Full large-deviation upper bound.** For each \(0<\theta_0<1\), Chernoff bounds applied at \(\pm\theta_0\) give
\[
\mathbb P(|Y_\varepsilon|>R)
\le2\exp\!\left(\Lambda_\varepsilon(\theta_0)-\frac{\theta_0R}{\varepsilon}\right).
\]
Consequently \(Y_\varepsilon\) is exponentially tight at speed \(1/\varepsilon\). For each fixed \(y\), choose its optimizing \(\theta_y\). The corresponding exponential Markov inequality bounds probabilities in a sufficiently small neighborhood of \(y\) with rate arbitrarily close to \(I(y)\). A finite cover of a compact closed set, followed by exponential tightness to remove its complement, yields the claimed upper bound for all closed sets.

**4. Full large-deviation lower bound.** Fix any \(y\in\mathbb R\), set \(\theta=\theta_y\), and exponentially tilt the distribution by \(e^{\theta U_\varepsilon-\Lambda_\varepsilon(\theta)}\). Under this tilted law, derivative convergence yields
\[
\mathbb E_\theta Y_\varepsilon
=\varepsilon\Lambda_\varepsilon'(\theta)\longrightarrow y,
\qquad
\operatorname{Var}_\theta(Y_\varepsilon)
=\varepsilon^2\Lambda_\varepsilon''(\theta)=O(\varepsilon).
\]
Therefore the tilted probability of every fixed neighborhood of \(y\) tends to one. Undoing the tilt on a neighborhood of radius \(\delta\) gives the lower exponential bound \(-I(y)-|\theta|\delta\). Allowing \(\delta\downarrow0\) and taking an arbitrary point in an open set proves the lower bound. This direct tilt proof does not incorrectly assume differentiability of an extended limiting cumulant function at its finite-domain endpoints.

**5. Quadratic-to-linear shape and Gaussian core.** Expansion gives \(\Lambda(\theta)=\theta^2+\theta^4/4+O(\theta^6)\); inversion of \(y=\Lambda'(\theta)\) gives \(\theta_y=y/2-y^3/16+O(y^5)\) and the stated central expansion of \(I\). For large \(y>0\), \(\theta_y\uparrow1\), and \(\delta=1-\theta_y^2\) obeys \(\delta=e^{-y/2}(1+O(ye^{-y/2}))\). Combining \(\operatorname{Li}_2(1-\delta)=\pi^2/6+\delta\log\delta-\delta+O(\delta^2|\log\delta|)\) with the Legendre formula proves \(I(y)=y-\pi^2/6+O(e^{-y/2})\). Evenness supplies the negative tail.

Separately, the characteristic function of \(\sqrt\varepsilon U_\varepsilon\) is \(\prod_{j\ge0}(1+\varepsilon k^2e^{-\varepsilon j})^{-1}\), whose logarithm tends to \(-k^2\); hence \(\sqrt\varepsilon U_\varepsilon\Rightarrow N(0,2)\). This central Gaussian limit was known before this result.

## Verification
The independent, standard-library-only program `verify_ldp.py` tests the exact product-to-integral limit at four tilt parameters, the Legendre stationary equation and evenness at six displacements, the central quartic and remote linear expansions, and the rescaled Gaussian variance formula. It reports 19 successful checks when executed using Python 3. These finite computations check numerical consistency only; the proofs above establish all real parameters and the infinite-family limit.

## Relationship to prior work
Di Bello and collaborators (2023) derived the exact partial-reset stationary Fourier product for positive rescaling, and Biroli and collaborators (2024) treated the stationary density for both positive and negative rescaling, including fixed-parameter Gaussian-shaped centers and exponential tails. Olsen and Gupta (2024) established weak-reset Gaussian behavior and thermodynamic work results. Olsen and Löwen (2024) treated partial resetting with refractory periods and derived exact cumulant formulas. Those prior stationary-product, cumulant, fixed-rescaling-tail and Gaussian-limit results are not claimed as new. The contribution here is the full weak-contraction stationary-position large-deviation principle, its dilogarithmic rate, and the evaluated quadratic-to-linear rate geometry. General large-deviation and analytic \(q\)-product machinery supplies methods; no exclusive claim to those methods is made.

## Limitations
The theorem requires independent exponential resetting times, ordinary one-dimensional Brownian diffusion, deterministic multiplicative factors with \(0<|a|<1\), stationary initialization and the weak-contraction limit. It does not address refractory periods, resetting costs, first-passage times, multiplicative factors sampled randomly, or correlated resetting intervals. The rate concerns deviations of order \(\varepsilon^{-1}\) in the dimensionless stationary position; it does not supply uniform pointwise density asymptotics, precise probabilities at finite \(\varepsilon\), or an independent publication-priority certificate. Existing general weighted-sum large-deviation theorems could imply the result as a specialization; this remains a residual literature risk.

## References
1. M. Biroli, Y. Feld, A. K. Hartmann, S. N. Majumdar, and G. Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension*, arXiv:2406.08387v1 (first public 12 June 2024), https://arxiv.org/html/2406.08387v1 .
2. C. Di Bello, A. V. Chechkin, A. K. Hartmann, Z. Palmowski, and R. Metzler, *Time-dependent probability density function for partial resetting dynamics*, arXiv:2305.13722 (2023), https://arxiv.org/abs/2305.13722 .
3. K. Stølevik Olsen and D. Gupta, *Thermodynamic work of partial resetting*, arXiv:2401.11919 (2024), https://arxiv.org/abs/2401.11919 .
4. K. Stølevik Olsen and H. Löwen, *Partial stochastic resetting with refractory periods*, arXiv:2406.10039v1 (2024), https://arxiv.org/html/2406.10039v1 .
