# Sharp convex-order bounds for Brownian motion with randomized partial resetting

## Finding
Consider one-dimensional freely diffusing Brownian motion punctuated by independent Poisson events \(X\mapsto AX\), with independent reset multipliers \(0\le A\le1\). Suppose the event rate \(r>0\), diffusion constant \(D>0\), and *mean-squared multiplier* \(u=\mathbb E[A^2]\in(0,1)\) are fixed. All these protocols have the same stationary position variance, but not the same fluctuations.

**Sharp protocol theorem.** If two squared multipliers are ordered in convex order, \(A_1^2\le_{\mathrm{cx}}A_2^2\), then their stationary squared positions obey \(X_1^2\le_{\mathrm{cx}}X_2^2\). In particular, the deterministic reset \(A\equiv\sqrt u\) is the unique sharp *least-variable* protocol, and the all-or-nothing reset \(\Pr(A=0)=1-u\), \(\Pr(A=1)=u\) is the unique sharp *most-variable* protocol, where uniqueness of these endpoints follows from the fourth moment. In the convex-order statements, \(Y\le_{\mathrm{cx}}Z\) means equal means and \(\mathbb E\varphi(Y)\le\mathbb E\varphi(Z)\) for every convex \(\varphi\) for which both expectations exist.

For arbitrary reset-factor laws within the specified class, letting \(v=\mathbb E[A^4]\),
\[
\mathbb E[X^2]=\frac{2D}{r(1-u)},\qquad
\frac{\mathbb E[X^4]}{(\mathbb E[X^2])^2}=\frac{6(1-u)}{1-v},\qquad
\frac6{1+u}\le\frac{\mathbb E[X^4]}{(\mathbb E[X^2])^2}\le6.
\]
The lower equality forces \(A=\sqrt u\) almost surely; the upper equality forces \(A\in\{0,1\}\) almost surely with the specified probabilities. At the upper endpoint, events with \(A=1\) are ineffective, so thinning the Poisson process yields an ordinary full-reset process with effective rate \(r(1-u)\); its stationary density is
\[
p_{\mathrm{upper}}(x)=\frac12\sqrt{\frac{r(1-u)}D}\exp\left(-\sqrt{\frac{r(1-u)}D}|x|\right).
\]

For every \(p\in(0,2)\), deterministic partial resetting gives the greatest value of \(\mathbb E|X|^p\) and all-or-nothing resetting the smallest; for every \(p>2\), their roles reverse. The second absolute moment is fixed. Their stationary densities at zero satisfy the opposite convex-risk order: deterministic resetting minimizes the central density, and all-or-nothing resetting maximizes it.

## Assumptions and scope
There is no confining drift. Between events, \(dX_t=\sqrt{2D}\,dB_t\). Events occur at a Poisson rate \(r\), and each instantaneous jump replaces \(X_{t-}\) by \(A X_{t-}\). Factors and Brownian increments are independent of each other and of all event times. Factors take values in the entire closed interval \([0,1]\), including zero (complete reset) and one (no-op). The prescribed number \(u\) lies strictly between zero and one. There is a unique stationary law with finite second moment. Only exact population distributions are considered; no noisy-data inference or thermodynamic implementation of the jump is asserted.

## Proof
**1. Construction and stationarity.** Extend the marked Poisson process backward from observation time zero. Its successive backward spacings \(E_0,E_1,\ldots\) are iid exponential with rate \(r\). Put \(U_j=A_j^2\), so the \(U_j\) are iid in \([0,1]\) with mean \(u<1\), independent of the spacings. Conditional on this resetting history, the stationary position is centered normal with random variance
\[
V=2D\sum_{j=0}^{\infty}E_j\prod_{i=1}^{j}U_i,
\qquad X\ \overset{d}=\ \sqrt V Z,
\]
where \(Z\) is an independent standard normal and the empty product is one. The series converges almost surely and in mean since \(\mathbb EV=2D\sum_{j\ge0}r^{-1}u^j=2D/[r(1-u)]\). The same common-clock/common-Brownian coupling contracts the expected squared distance of any two initial positions by \(e^{-r(1-u)t}\), proving uniqueness among finite-second-moment invariant laws. Splitting the first backward time interval gives the perpetuity \(V\overset d=2DE+UV'\), with the terms independent and \(V'\) an independent copy.

**2. Convex-order transfer.** Truncate the variance after \(n\) terms:
\[
V^{(n)}=2D\sum_{j=0}^{n-1}E_j\prod_{i=1}^j U_i.
\]
For each fixed index \(i\), holding every other coordinate fixed, \(V^{(n)}\) is an affine function of \(U_i\), with nonnegative slope. Consequently, for any convex function of \(V^{(n)}\), replacing one independent coordinate \(U_i\) by a larger one in convex order cannot decrease its expectation. Replace all \(n-1\) coordinates in succession. Since \(V^{(n)}\to V\) in \(L^1\), the call-option criteria \(\mathbb E(V^{(n)}-t)_+\), which are one-Lipschitz, pass to the limit for every \(t\ge0\). Means are equal because \(u\) is fixed. Hence \(V_1\le_{\mathrm{cx}}V_2\). For an independent nonnegative random variable \(W\), conditioning on \(W\) shows that multiplication \(V\mapsto WV\) preserves convex order whenever integrability permits. With \(W=Z^2\), this proves \(X_1^2\le_{\mathrm{cx}}X_2^2\).

**3. Sharp extremes.** Any probability law supported on \([0,1]\) with mean \(u\) lies between the point mass at \(u\) and the Bernoulli law with masses \(1-u,u\) at zero and one, respectively, in convex order: Jensen gives the first inequality; the chord inequality \(\varphi(s)\le(1-s)\varphi(0)+s\varphi(1)\) gives the second. Applying Step 2 proves the two universal extremizers for every convex squared-position risk, including variance of \(X^2\) and all stop-loss risks.

**4. Sharp equality and physical diagnostics.** Stationarity of \(x^{2j}\) under the generator \(\mathcal Lf(x)=Df''(x)+r(\mathbb E f(Ax)-f(x))\) yields the recurrence
\[
\mathbb E[X^{2j}]=\frac{D(2j)(2j-1)}{r(1-\mathbb E U^j)}\,\mathbb E[X^{2j-2}],\qquad j\ge1.
\]
The first two cases yield the variance and kurtosis in the finding. Since \(u^2\le v=\mathbb E U^2\le u\), with equality at the left endpoint iff \(U=u\) almost surely and at the right endpoint iff \(U\in\{0,1\}\) almost surely, both extrema are sharp and each is unique. Note the known deterministic fixed-multiplier kurtosis \(6/(1+u)\) is not claimed as new.

**5. Other position diagnostics.** Given \(V\), \(\mathbb E(|X|^p\mid V)=m_p V^{p/2}\), with \(m_p=\mathbb E|Z|^p>0\). The power \(v^{p/2}\) is concave for \(0<p<2\) and convex for \(p>2\); the claims follow by the opposite/ordinary directions of Step 3. All these moments are finite by the recurrence in Step 4 (for even moments) and interpolation. The density at zero is \(p_X(0)=\mathbb E[(2\pi V)^{-1/2}]\): the expectation is finite because \(V\ge2DE_0\), and \(v\mapsto v^{-1/2}\) is convex. Its order again follows from Step 3 using bounded convex approximations and monotone convergence. Bernoulli thinning gives the stated Laplace density.

## Verification
The standalone `verify.py` implements two independent rational moment recursions (the generator and the perpetuity), tests exact kurtosis/variance identities at several protocols with identical mean squared multiplier, tests moment orders through order seven, integrates the fixed-contraction characteristic function to compare central densities, and uses seeded Monte Carlo to corroborate their direction. Running `python verify.py` with NumPy and SciPy completed 365 checks successfully. These finite checks corroborate normalizations only; the infinite convex-order theorem rests on the proof above.

## Relationship to prior work
Tal-Friedman, Roichman and Reuveni's *Diffusion with Partial Resetting* (arXiv:2205.03363, first posted 2022-05-06) establishes the fixed-multiplier Brownian stationary distribution, its Fourier product, and specifically the deterministic kurtosis \(6/(1+a^2)\). Olsen and Gupta's *Thermodynamic work of partial resetting* (arXiv:2401.11919, first posted 2024-01-22) investigates deterministic partial resetting and thermodynamic work under explicitly finite-time resetting protocols. Dahlenburg, Chechkin, Schumer and Metzler's *Stochastic resetting by a random amplitude* (arXiv:2104.14866, first posted 2021-04-30) develops more general resetting amplitudes, particularly for ballistic growth. The claim here is neither the known deterministic formula nor a claim about physically implemented reset work: it is the sharp *distribution-wide comparison among iid random multipliers with the same squared mean*, including unique extremizers and opposite orders for subquadratic and superquadratic observables. The possible implication by a broad general perpetuity convex-order theorem remains a publication-priority risk.

## Limitations
Only one-dimensional free Brownian diffusion, Poisson event times, independent state-independent nonnegative multipliers, finite-second-moment stationarity, and exact laws are covered. The conclusions need not extend to signed multipliers with state-dependent correlation, non-Poisson clocks, non-Gaussian driving noise, finite-time work implementations, or arbitrary unbounded multipliers. Stochastic dominance in the ordinary first-order sense is NOT claimed; only convex order of squared positions. Numerical checks are not infinite proofs. Independent audit and publication-priority certification have not been performed.

## References
1. K. Stølevik Olsen and D. Gupta, *Thermodynamic work of partial resetting*, arXiv:2401.11919 (first posted 2024-01-22), https://arxiv.org/abs/2401.11919 .
2. O. Tal-Friedman, Y. Roichman and S. Reuveni, *Diffusion with Partial Resetting*, arXiv:2205.03363 (first posted 2022-05-06), https://arxiv.org/abs/2205.03363 .
3. M. Dahlenburg, A. V. Chechkin, R. Schumer and R. Metzler, *Stochastic resetting by a random amplitude*, arXiv:2104.14866 (first posted 2021-04-30), https://arxiv.org/abs/2104.14866 .
