# Sharp stationary-risk envelope and order-phase switches for two-sample reshuffling

## Finding

For a scalar finite-sum quadratic with two individually strongly convex components, **every stationary balanced coupling of the two epoch orders** has a limiting squared optimization error in an explicit sharp interval. Its two endpoints are achieved, and—apart from a degenerate step-size case—uniquely achieved, by choosing the epoch order once and retaining it forever, or by reversing the order at every epoch. Which policy is optimal changes with the sign of the two-step deterministic multiplier.

Precisely, fix \(a,b>0\), \(c\ne0\), and \(\eta>0\), and define
\[
 f_1(x)=\tfrac12 ax^2+cx,\qquad
 f_2(x)=\tfrac12 bx^2-cx,\qquad
 F(x)=\tfrac12(f_1(x)+f_2(x))=\tfrac14(a+b)x^2.
\]
The minimizer is \(x_*=0\). Let \(X_k\) be the iterate at the beginning of epoch \(k\). Each epoch makes exactly one constant-step stochastic-gradient update using each component, in one of the two possible orders. The order process is stationary and each order has marginal probability one half; correlations of orders between epochs are unrestricted. Define
\[
 g=(1-\eta a)(1-\eta b),\qquad
 m=\tfrac12\eta^2c(b-a),\qquad
 d=\tfrac12\eta^2c(a+b).
\]
Assume \(|g|<1\). For every deterministic initial \(X_0\) and every such order process, the limiting risk \(R=\lim_{k\to\infty}\mathbb E[X_k^2]\) exists, and the **best and worst possible values over all stationary balanced order processes** are exactly
\[
 \boxed{\frac{m^2}{(1-g)^2}+\frac{d^2}{(1+|g|)^2}
 \ \le\ R\ \le\
 \frac{m^2}{(1-g)^2}+\frac{d^2}{(1-|g|)^2}.}
\]
For \(g>0\), the lower endpoint requires order reversal at *every* epoch and the upper endpoint requires a fixed order chosen by one fair initial coin. For \(g<0\), these requirements reverse. For \(g=0\), every stationary balanced order process has the same limiting risk \(m^2+d^2\). These are all the equality cases in the nondegenerate regimes, up to null events and relabeling of the initial fair coin. The limiting expected objective gap is \((a+b)R/4\).

In the concrete fixed problem \(a=2,b=1,c=1\), the entire epoch-stable stepsize interval is \(0<\eta<3/2\). Alternation is uniquely risk-optimal for \(0<\eta<1/2\) and \(1<\eta<3/2\); persistence is uniquely optimal for \(1/2<\eta<1\). At \(\eta=1/2\) and \(\eta=1\), temporal coupling cannot change the limiting risk. The first two regimes already occur with both individual component-step multipliers strictly inside \((-1,1)\).

For the stationary symmetric Markov family with probability \((1+\rho)/2\) of repeating the previous order, \(-1\le\rho\le1\), the exact interpolation is
\[
 \boxed{R(\rho)=\frac{m^2}{(1-g)^2}
 +\frac{d^2(1+g\rho)}{(1-g^2)(1-g\rho)}.}
\]
It is strictly increasing in \(\rho\) for \(g>0\), strictly decreasing for \(g<0\), and constant for \(g=0\). The independent-uniform-reshuffling case is \(\rho=0\), strictly interior to the sharp range whenever \(g\ne0\).

**Unbounded benefit despite individually stable steps.** Set \(a=N\), \(b=c=1\), and \(\eta=(2N-1)/N^2\) for any integer \(N\ge3\). The two individual gradient multipliers are \(-(1-1/N)\) and \((1-1/N)^2\); both lie strictly between \(-1\) and \(1\). Yet \(g=-(1-1/N)^3\), so **keeping one random fixed order is optimal**, while alternation is worst. The ratio of the stationary objective gaps of alternation to persistence tends to infinity, with precise asymptotic \(2N^2/9\). The two strategies have identical uniform per-epoch order marginals and identical gradient-computation costs.

## Assumptions and scope

The components have positive curvatures \(a,b\), not necessarily equal, and nonzero opposing linear terms \(c,-c\). Every epoch uses both components exactly once with the same constant step \(\eta\). Order is selected exogenously: a \(\{-1,+1\}\)-valued strictly stationary process \((S_k)_{k\in\mathbb Z}\) with \(\mathbb P(S_k=+1)=\mathbb P(S_k=-1)=1/2\). Sign \(+1\) means apply component 1 then component 2, and sign \(-1\) means the reverse. No independence, mixing, ergodicity, or Markov assumption is imposed. The initial value \(X_0\in\mathbb R\) is deterministic. The only stability hypothesis is \(|g|<1\), the exact contraction condition for the homogeneous epoch map. All statements refer to epoch-boundary iterates and exact arithmetic.

## Proof

**1. Exact epoch map.** One component step is \(x\mapsto(1-\eta a)x-\eta c\) for the first component and \(x\mapsto(1-\eta b)x+\eta c\) for the second. Their compositions, in the two orders, are
\[
 T_{12}(x)=gx+\eta^2bc,\qquad
 T_{21}(x)=gx-\eta^2ac.
\]
Consequently the actual epoch sequence obeys \(X_{k+1}=gX_k+m+dS_k\). Here \(\mathbb E S_k=0\), \(\mathbb E S_k^2=1\), and \(d\ne0\). Iteration gives
\[
 X_k=g^kX_0+m\frac{1-g^k}{1-g}
       +d\sum_{j=0}^{k-1}g^{k-1-j}S_j.
\]
Therefore \(\mathbb E X_k\to m/(1-g)\), and the centered second moment equals
\[
 d^2\sum_{i,j=0}^{k-1}g^{i+j}\,r_{i-j},
 \qquad r_h=\mathbb E[S_0S_h].
\]
The series converges absolutely as \(k\to\infty\), since \(|r_h|\le1\) and \(|g|<1\). This proves existence of the limiting second moment for every allowed stationary order law, including periodic and nonergodic laws.

**2. A sharp universal spectral envelope.** Stationarity makes \((r_h)_{h\in\mathbb Z}\) a positive-definite sequence with \(r_0=1\). By the classical Herglotz representation, there is a probability measure \(\nu\) on the circle such that \(r_h=\int e^{ih\theta}\,d\nu(\theta)\). Absolute convergence permits exchanging the sums and the integral. The limiting variance is exactly
\[
 \operatorname{Var}_\infty(X)=
 d^2\int\frac{d\nu(\theta)}{1-2g\cos\theta+g^2}.
\]
For every real \(g\) with \(|g|<1\), the denominator belongs to \([(1-|g|)^2,(1+|g|)^2]\). Integration against a probability measure gives the asserted two sharp variance bounds; the bias square \(m^2/(1-g)^2\) is independent of the order law.

For \(0<|g|<1\), each denominator extremum has a unique frequency: \(0\) or \(\pi\). Equality requires \(\nu\) to be a unit point mass at the corresponding frequency. In that case \(r_1=+1\) or \(r_1=-1\), respectively. Since each \(S_k\) takes values \(\pm1\), \(r_1=\pm1\) implies \(S_{k+1}=\pm S_k\) almost surely; stationarity extends this to every integer \(k\). Conversely a single fair random sign held fixed forever has spectral measure concentrated at frequency \(0\), while its deterministic alternation has spectral measure concentrated at \(\pi\). Thus both extrema are attainable and the equality processes are completely classified. If \(g=0\), the integrand is constant and all laws tie.

**3. Markov interpolation.** For a stationary symmetric two-state Markov order law with order-persistence parameter \(\rho\), one has \(r_h=\rho^{|h|}\), including \(\rho=\pm1\). Splitting the covariance double sum by index difference yields
\[
 \sum_{i,j\ge0}g^{i+j}\rho^{|i-j|}
 =\frac{1}{1-g^2}\left(1+2\sum_{h\ge1}(g\rho)^h\right)
 =\frac{1+g\rho}{(1-g^2)(1-g\rho)}.
\]
This is the displayed \(R(\rho)\). Differentiating gives \(R'(\rho)=2d^2g/[(1-g^2)(1-g\rho)^2]\), proving its strict monotonicity with the sign of \(g\).

**4. Arbitrarily large policy gap within the component-stable regime.** For \(N\ge3\), the parameters in the finding have \(1-\eta a=-(1-1/N)\) and \(1-\eta b=(1-1/N)^2\), hence \(g=-r_N\) with \(r_N=(1-1/N)^3\). Writing \(h_N=(N-1)/(N+1)\), we have \((m/d)^2=h_N^2\). Therefore the precise ratio between the worst and best limiting objective gaps is
\[
 Q_N=\frac{h_N^2+\left(\frac{1+r_N}{1-r_N}\right)^2}{1+h_N^2}.
\]
Since \(h_N\to1\) and \(N(1-r_N)\to3\), it follows that \(Q_N/N^2\to2/9\). Both component multipliers have modulus below one, so this is not a one-component divergence artifact.

**5. Explicit double switch.** For \(a=2,b=1\), \(g=(1-2\eta)(1-\eta)=1-3\eta+2\eta^2\). Throughout \(0<\eta<3/2\), \(g<1\), while \(g+1=2(\eta-3/4)^2+7/8>0\); hence the interval is exactly epoch-stable. The signs of its two factors give \(g>0\) on \((0,1/2)\cup(1,3/2)\), \(g<0\) on \((1/2,1)\), and \(g=0\) at the two intervening steps. The optimal policy descriptions follow from step 2. For example, \(\eta=1/4\) gives \(g=3/8>0\), while \(\eta=3/4\) gives \(g=-1/8<0\); both have individually contractive component maps.

## Verification

The accompanying standard-library-only `verify.py` independently constructs every update by applying the two component gradients, enumerates every two-order Markov history through eight epochs with exact rational probabilities, and compares the directly computed first and second moments to the closed finite-horizon formula. It checks three rational stepsizes, two signed noise amplitudes, two deterministic starts, and five Markov correlations; **728 exact-rational checks passed**. It also checks the sharp limiting formulas on the Markov subfamily, the explicit sign-switch examples, and five exact-rational instances of the unbounded-gap family. The program uses finite enumeration only to test identities; the infinite-horizon theorem, unrestricted-stationary-law optimality, and unbounded stable-step policy gap are proved above analytically.

## Relationship to prior work

Ying, Yuan, Vlaski, and Sayed (2018) analyze constant-step random reshuffling, including epoch-boundary mean-square performance for randomly redrawn permutations. Mohtashami, Stich, and Jaggi (2022) analyze convergence bounds sensitive to chosen data orders. Domingo-Enrich (2022) supplies a general LTI spectral formula for **approximated** constant-curvature gradient noise, while Hu, Doshi, and Eun (2022) compare efficiency ordering primarily via diminishing-step CLT and time-averaged constant-step covariance. Neither gives a finite-step exact heterogeneous-curvature gradient composition or the coupling-specific optimality switches here. Kühn and Rosenow (2023; later revised) study anti-correlated gradient noise and variance in epoch-based SGD. Nguyen, Phan, and Kalagnanam (2026) analyze an *averaged epoch-map* paired-reversal operator and higher-order order sensitivity. These results motivate temporal order design but do not supply the sharp stationary-risk envelope over arbitrary balanced inter-epoch couplings, its complete equality classification, or the sign-dependent optimal policy reversal proved here. The LTI variance-transfer representation and Herglotz theorem are prior tools; the claimed contribution is the *exact heterogeneous-component-gradient* recurrence, complete sharp classification of stationary order-coupling policies, step-dependent reversals, and the unbounded stable-step gap, not a new spectral representation theorem.

## Limitations

The stationary balanced marginal assumption is essential: state-feedback policies, unequal order probabilities, nonstationary schedules, and within-epoch output risks are not classified. The result does not assert a general-dimensional nonlinear guarantee or algorithmic running-time savings. It concerns the limiting expected squared error under a fixed step, not convergence of the iterates to the exact minimizer. Sharpness is relative to coupling the two ordinary epoch orders, not relative to methods that average both order outcomes or alter component steps. Priority relative to unindexed specialized analyses of temporally dependent shuffling remains uncertain.

## References

1. B. Ying, K. Yuan, S. Vlaski, and A. H. Sayed, *Stochastic Learning under Random Reshuffling with Constant Step-sizes*, first submitted 2018-03-21, arXiv:1803.07964, https://arxiv.org/abs/1803.07964 (especially the epoch recursion and Theorem 2).
2. A. Mohtashami, S. Stich, and M. Jaggi, *Characterizing & Finding Good Data Orderings for Fast Convergence of Sequential Gradient Methods*, first submitted 2022-02-03, arXiv:2202.01838, https://arxiv.org/abs/2202.01838.
3. M. Kühn and B. Rosenow, *Anti-Correlated Noise in Epoch-Based Stochastic Gradient Descent: Implications for Weight Variances in Flat Directions*, first submitted 2023-06-08, arXiv:2306.05300, https://arxiv.org/abs/2306.05300.
4. L. M. Nguyen, D. T. Phan, and J. Kalagnanam, *Learning to Shuffle: Block Reshuffling and Reversal Schemes for Stochastic Optimization*, first submitted 2026-03-31, arXiv:2604.00260, https://arxiv.org/abs/2604.00260.
5. C. Domingo-Enrich, *Computing the Variance of Shuffling Stochastic Gradient Algorithms via Power Spectral Density Analysis*, first submitted 2022-06-01, arXiv:2206.00632, https://arxiv.org/abs/2206.00632 (especially Sections 2, 4, 5).
6. J. Hu, V. Doshi, and D. Y. Eun, *Efficiency Ordering of Stochastic Gradient Descent*, first submitted 2022-09-15, arXiv:2209.07446, https://arxiv.org/abs/2209.07446 (especially Section 3 and Appendix E).
7. Classical Herglotz representation for positive-definite sequences (used as a standard harmonic-analysis identity in the proof).
