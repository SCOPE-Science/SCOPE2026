# A sharp dispersion transition for finite-tumble first-exit times

## Finding

Consider the unbiased finite-duration run-and-tumble process defined below. Write \(x=\gamma L/v>0\), \(p=\varphi/\gamma>0\), and \(\tau=\gamma T\). Its first-exit-time coefficient of variation squared, \(Q(x,p)=\operatorname{Var}(\tau)/(\mathbb E\tau)^2\), exhibits an **exact change of geometry at \(p=1/2\)**:

- If \(0<p\leq 1/2\), then \(Q(x,p)\) is strictly decreasing in interval half-width \(x>0\), always lies strictly above \(2/3\), and tends to \(2/3\) as \(x\to\infty\).
- If \(p>1/2\), then \(Q(x,p)\) decreases to exactly one strict minimum, then increases to \(2/3\) from below. It crosses \(2/3\) at exactly
\[
 x_c(p)=\frac{\sqrt{(3p+1)/(2p-1)}-1}{p+2}>0.
\]
Thus, sufficiently fast tumble completion creates an interval-size range with escape-time dispersion **below** the Brownian first-exit benchmark, whereas slower tumble completion keeps it **above** that benchmark for every finite interval size.

This classification follows from an exact positive-Laplace-parameter transform of the complete first-exit-time law and explicit first two moments; the threshold and unique-minimum statements are not numerical conjectures.

## Assumptions and scope

Fix \(L,v,\gamma,\varphi>0\). On the open interval \((-L,L)\), a piecewise deterministic particle has internal velocity \(V_t\in\{-v,0,+v\}\) and position \(\dot X_t=V_t\). Each running state \(\pm v\) changes to state \(0\) at independent exponential rate \(\gamma\). State \(0\) lasts for an exponential time of rate \(\varphi\), after which the particle chooses \(+v\) or \(-v\) with equal probability, independently of its past. There is no translational Brownian noise or imposed drift. Start at \((X_0,V_0)=(0,0)\). Set \(T=\inf\{t\geq0:|X_t|=L\}\); the particle is absorbed at the first boundary hit. The \(0\) state is a finite-duration physical tumble, not an instantaneous flip. All limits vary only parameters explicitly named.

For every \(z\geq0\), define \(K(z)\geq0\) by
\[
 K(z)^2=\frac{z(z+1)(z+p+1)}{z+p}.
\]
Then the exact Laplace transform is
\[
 \boxed{\mathbb E[e^{-z\tau}]=
 \frac{p}{p+z}\left(\cosh(xK(z))+
 \frac{K(z)}{1+z}\sinh(xK(z))\right)^{-1}.}
\]
The formula is defined continuously at \(z=0\) and equals one there.

Put \(M=(p+1)(x^2+2x)+2\) and \(N=(p+1)^2(x^4+4x^3)+(12+6p)x^2+12x+6\). Then
\[
 \boxed{\mathbb E\tau=\frac{M}{2p},\qquad
 \operatorname{Var}(\tau)=\frac{N}{6p^2},\qquad
 Q(x,p)=\frac{2N}{3M^2}.}
\]
These formulas apply for every \(x,p>0\); the dimensional mean and variance of \(T\) are obtained by dividing respectively by \(\gamma\) and \(\gamma^2\).

## Proof

**Almost-sure exit and moment existence.** The internal chain visits the tumble state repeatedly. Every time it begins a run, either direction has probability \(1/2\), and its independent exponential run duration exceeds \(2L/v\) with probability \(e^{-2\gamma L/v}\). A run of this length exits from any interior point. The waiting times to successive runs are sums of independent exponentials of rates \(\gamma,\varphi\). Geometric domination consequently gives an exponential moment for \(T\) in a neighborhood of zero, ensuring the legitimate Laplace differentiation below.

**Backward equations.** For \(s\geq0\) let \(f_+(y),f_-(y),f_0(y)\) be the Laplace transforms \(\mathbb E_{y,\pm v,0}[e^{-sT}]\) from the three initial velocity states. In \((-L,L)\), their generator equations are
\[
 vf_+'=(s+\gamma)f_+-\gamma f_0,\qquad
 -vf_-'=(s+\gamma)f_--\gamma f_0,\qquad
 (s+\varphi)f_0=\frac\varphi2(f_++f_-).
\]
The two outgoing absorbing boundary conditions are \(f_+(L)=f_-(-L)=1\). There is no artificial incoming boundary condition for the zero-speed state. By reflection symmetry, \(S=(f_++f_-)/2\) is even and \(D=(f_+-f_-)/2\) is odd. The equations give
\[
 S'=\frac{s+\gamma}{v}D,\quad
 D'=\frac{s(s+\gamma+\varphi)}{v(s+\varphi)}S,\quad
 f_0=\frac\varphi{s+\varphi}S.
\]
Therefore \(S(y)=A\cosh(\kappa y)\), \(D(y)=Av\kappa\sinh(\kappa y)/(s+\gamma)\), where \(\kappa^2=s(s+\gamma)(s+\gamma+\varphi)/[v^2(s+\varphi)]\). The outward boundary condition determines
\[
 A^{-1}=\cosh(\kappa L)+\frac{v\kappa}{s+\gamma}\sinh(\kappa L).
\]
The initial tumble transform is \(f_0(0)=\varphi A/(s+\varphi)\). Setting \(s=\gamma z\) yields the asserted formula. The Markov stopping representation, or uniqueness of the nonnegative bounded solution, justifies identifying the ODE solution with the transform.

**Moments.** Around \(z=0\), the even entire combinations \(\cosh(xK)\) and \(K\sinh(xK)\) possess ordinary Taylor series in \(z\), despite the square-root presentation. Differentiation of the transform at zero gives the displayed \(M,N\). Explicit expansions and independent numerical checks are reproducible with `verify.py`; they are not substitutes for the finite Taylor algebra.

**Sharp transition.** Direct polynomial simplification yields
\[
 Q(x,p)-\frac23 =
 -\frac{4[(2p-1)((p+2)x^2+2x)-1]}{3M^2}
\]
and
\[
 \partial_xQ(x,p)=\frac{8P_p(x)}{3M^3},
\]
where
\[
 P_p(x)=(2p^3+5p^2+p-2)x^3
 +(6p^2+3p-3)x^2-6px-6p.
\]
Both leading coefficients are strictly increasing as functions of \(p>0\) and vanish at \(p=1/2\). If \(p\leq1/2\), all coefficients of \(P_p\) are nonpositive with strictly negative lower coefficients, so \(\partial_xQ<0\) throughout \(x>0\). The difference formula yields \(Q>2/3\).

If \(p>1/2\), the cubic and quadratic coefficients of \(P_p\) are positive, and the linear and constant coefficients are negative. Descartes' rule of signs yields exactly one positive root (existence follows from \(P_p(0)<0\) and \(P_p(x)\to+\infty\)). The derivative changes from negative to positive at that root, giving a unique strict minimum. The difference formula shows a unique crossing of \(2/3\), determined by \((2p-1)((p+2)x^2+2x)=1\). Solving the quadratic gives \(x_c(p)\) as stated. Finally, the degree-four leading coefficients give \(Q(x,p)\to2/3\) for every fixed \(p>0\) as \(x\to\infty\). As \(x\downarrow0\), \(Q(x,p)\to1\). This completes all parameter cases, including equality at \(p=1/2\).

## Verification

`verify.py` verifies the exact second-order Laplace expansion and the two polynomial identities symbolically using SymPy, then independently differentiates the unexpanded Laplace transform at 30 parameter points using high-precision mpmath. It also simulates 150,000 complete finite-state trajectories over five parameter choices from the stipulated initial tumble state and compares sample means and variances to the exact formulas. Randomness is seeded. Running `python verify.py` requires SymPy and mpmath; no external data or third-party paper is required. These finite numerical checks neither prove the all-parameter algebra nor establish publication priority.

## Relationship to prior work

Grange and Yuan (arXiv:2509.11308v1, first posted September 14, 2025) introduced exactly the finite-duration three-velocity run-and-tumble model with a constant drift. They solved the boundary exit probabilities and conditional first moments in drifted configurations, and their conclusion explicitly names first-passage variance as a further extension. The present result removes the imposed drift, keeps a finite symmetric absorbing interval, starts specifically in the tumble state at its center, evaluates the **entire exit-time Laplace transform and variance**, and classifies the strict dispersion geometry with a sharp \(\varphi/\gamma=1/2\) threshold. The published backward equations supply the natural starting point, not the resulting variance phase diagram.

Li, Xu, Metzler, Wang and Suleiman (J. Phys. A 58 (2025) 265002) analyze transition-path coefficient of variation for a two-state dichotomous velocity \(\pm v\) with instantaneous switching. Their model has no independent positive-duration \(0\) state and their transition-path conditioning differs from the full center-to-either-boundary exit considered here. Sun, Ye and Podgornik (arXiv:2409.00578v2) study moments of a finite-tumble particle under harmonic confinement, not first absorption at an interval boundary. Classical two-state telegraph first-passage formulas arise only as the \(\varphi\to\infty\) limit and do not supply the finite-\(\varphi\) threshold.

## Limitations

The result is for a single unbiased one-dimensional particle, a symmetric interval, an initial center position **in the zero-speed state**, independent exponential run and tumble durations, and perfectly absorbing endpoints. It does not classify other initial velocity mixtures, nonzero drift, spatially dependent rates, boundary reactivity, or higher moments. For \(p>1/2\), the unique minimum is characterized as a polynomial root but is not expressed in radicals. Literature comparisons cannot exclude unidentified implicit coverage in the general Markov-additive/fluid-queue literature; the new sharp dispersion classification is therefore offered with this residual originality risk. No independent scientific audit is claimed.

## References

1. P. Grange and L. Yuan, *Mean first-passage time of a run-and-tumble particle with exponentially-distributed tumble duration in the presence of a drift*, arXiv:2509.11308v1 (2025), https://arxiv.org/abs/2509.11308 .
2. H. Li, Y. Xu, R. Metzler, Z. Wang and K. Suleiman, *Transition path properties of a run and tumble particle subjected to an external potential*, Journal of Physics A 58, 265002 (2025), DOI:10.1088/1751-8121/ade5db .
3. A. Sun, F. Ye and R. Podgornik, *Exact moments for a run and tumble particle in a harmonic trap with a finite tumble time*, arXiv:2409.00578v2 (2025), https://arxiv.org/abs/2409.00578 .
4. L. Angelani, R. Di Leonardo and M. Paoluzzi, *First-passage time of run-and-tumble particles*, arXiv:1506.08046v1 (2015), https://arxiv.org/abs/1506.08046 .
