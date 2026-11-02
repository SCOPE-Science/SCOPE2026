# Sharp mean-exit envelopes for randomized proportional resetting at fixed stationary variance

## Finding

A Brownian searcher undergoing Poisson multiplicative resets can use reset factors of varying magnitude without changing its stationary positional variance. Nevertheless, the mean time to leave a symmetric interval admits two **sharp and uniquely characterized protocol envelopes**. At a fixed quadratic retention \(q\), all-or-nothing resetting gives the shortest mean exit time, while resetting by a constant absolute factor gives the longest. The gap grows exponentially in the square root of the reset rate.

Let \(D,r,L>0\). At rate \(r\), multiply the particle's current position by a fresh factor \(A\in[-1,1]\); between resets it is Brownian with generator \(D\partial_{xx}\). Assume the factors are independent and identically distributed, independent of the Brownian increments and clock, with
\[
q=\mathbb E[A^2]\in(0,1),\qquad m_j=\mathbb E[A^{2j}],\qquad s=\frac{rL^2}{D}.
\]
For \(\tau_L=\inf\{t\ge0:|X_t|\ge L\}\), started at \(X_0=x\in(-L,L)\), define \(T_A(x)=\mathbb E_x\tau_L\). Then
\[
\boxed{T_A(x)=\frac{L^2}{D}\sum_{n=1}^{\infty}\frac{s^{n-1}}{(2n)!}\left[\prod_{j=1}^{n-1}(1-m_j)\right]\left[1-\left(\frac{x}{L}\right)^{2n}\right].}\tag{1}
\]
Empty products equal one; the series converges absolutely for every finite \(r\).

Let \(T_{\rm onoff}\) correspond to \(\Pr(|A|=1)=q\), \(\Pr(A=0)=1-q\); let \(T_{\rm fixed}\) correspond to \(|A|=\sqrt q\) almost surely. For every \(|x|<L\),
\[
\boxed{\frac{\cosh(\kappa L)-\cosh(\kappa x)}{r(1-q)}=T_{\rm onoff}(x)\le T_A(x)\le T_{\rm fixed}(x),}\qquad \kappa=\sqrt{\frac{r(1-q)}D}.
\tag{2}
\]
The upper envelope is (1) with \(m_j=q^j\). Equality on the left occurs exactly when \(|A|\in\{0,1\}\) almost surely with \(\Pr(|A|=1)=q\); equality on the right occurs exactly when \(|A|=\sqrt q\) almost surely. In all other cases the respective inequality is strict at every interior starting position. The signs of the reset factors do not affect the mean symmetric exit time.

All these reset protocols satisfy the same unbounded-system stationary variance \(\mathbb E_{\rm stat}[X^2]=2D/[r(1-q)]\), even though their exit times differ. At \(x=0\), as \(r\downarrow0\) with \(D,L,q\) and the factor law fixed,
\[
T_{\rm fixed}(0)-T_A(0)=\frac{L^2}{D}\frac{s^2(1-q)}{720}\operatorname{Var}(A^2)+O(s^3).
\tag{3}
\]
Writing \((q;q)_\infty=\prod_{j=1}^{\infty}(1-q^j)>0\), for any fixed \(q\in(0,1)\), as \(r\to\infty\),
\[
\boxed{\frac{T_{\rm fixed}(0)}{T_{\rm onoff}(0)}\sim (1-q)(q;q)_\infty\exp\left[(1-\sqrt{1-q})L\sqrt{r/D}\right].}
\tag{4}
\]

## Assumptions and scope

The process is a one-dimensional Brownian diffusion with \(\mathbb E[(X_{t+h}-X_t)^2]=2Dh\) between independent rate-\(r\) Poisson events. Each event instantaneously applies \(X\mapsto AX\), with a fresh random factor supported on \([-1,1]\). The factor law may have atoms, including at zero and both endpoints; only \(0<q=\mathbb E A^2<1\) is imposed. Absorption occurs on the first visit to either \(-L\) or \(+L\), starting from any \(|x|<L\). No jump can cross the absorbing boundary because \(|A|\le1\). The stationary-variance statement refers to the same dynamics on the entire real line, without absorbing boundaries.

## Proof

**1. Well-posedness and finite mean exit.** On any fixed time interval of length \(h>0\), the probability of no reset is \(e^{-rh}\). Irrespective of the current interior position, a free Brownian displacement of magnitude at least \(2L\) by time \(h\) forces an exit before \(h\). Thus there is a uniform positive lower bound on the conditional probability of exit during each such interval. By the strong Markov property the survival probability has a geometric upper bound at integer multiples of \(h\), so \(T_A(x)<\infty\) uniformly in the starting position.

**2. Backward equation.** The killed process has generator
\[
\mathcal Lf(x)=D f''(x)+r\left(\mathbb E[f(Ax)]-f(x)\right).
\]
Its mean exit time satisfies \(\mathcal LT=-1\) for \(|x|<L\), with \(T(\pm L)=0\). Reflection symmetry implies \(T(x)=T(-x)\). Put \(T(x)=c_0+\sum_{n\ge1}c_nx^{2n}\). Equating coefficients gives
\[
2Dc_1=-1,\qquad c_{n+1}=\frac{r(1-m_n)}{D(2n+2)(2n+1)}c_n,\quad n\ge1.
\]
Therefore \(c_n=-D^{-1}(r/D)^{n-1}\prod_{j=1}^{n-1}(1-m_j)/(2n)!\). The two boundary conditions fix \(c_0=-\sum_{n\ge1}c_nL^{2n}\), proving (1). Since \(0\le m_j\le1\), the factorial denominator ensures uniform convergence of the series and its twice-differentiated counterpart on the closed interval, justifying termwise calculation. The bounded Dirichlet solution is unique: the stopped-generator martingale and finite exit imply any bounded homogeneous solution with zero boundary values vanishes.

**3. Sharp ordering.** Set \(U=A^2\in[0,1]\). Since \(\mathbb EU=q\), Jensen's inequality and \(U^j\le U\) give, for each integer \(j\ge1\),
\[
q^j\le m_j\le q.
\]
Thus \((1-q)^{n-1}\le\prod_{j=1}^{n-1}(1-m_j)\le\prod_{j=1}^{n-1}(1-q^j)\). Every multiplier in (1) is strictly positive for \(|x|<L\), yielding both inequalities in (2). At \(j=2\), equality in the upper Jensen inequality \(m_2\ge q^2\) forces \(U=q\) almost surely; equality in \(m_2\le q\) forces \(U\in\{0,1\}\) almost surely. With \(r>0\), the \(n=3\) coefficient has positive weight, proving the necessity, strictness, and uniqueness characterizations. The lower series resums to the hyperbolic-cosine expression in (2).

**4. Same stationary quadratic statistic.** For the unabsorbed process, apply its generator to \(f(x)=x^2\):
\[
\mathcal L(x^2)=2D-r(1-q)x^2.
\]
The second moment converges to \(2D/[r(1-q)]\), independent of all higher even moments of the reset factor. A stationary law exists because the quadratic drift has strictly negative coefficient; for example, the standard Markov Lyapunov argument applies to this nonexplosive jump diffusion. Thus (2) compares protocols having identical stationary position variance.

**5. Weak-reset sensitivity.** In (1), the terms \(n=1\) and \(n=2\) are independent of the factor distribution once \(q\) is fixed. The \(n=3\) coefficients differ by \((1-q)(m_2-q^2)/6!\). Higher terms are \(O(s^3)\) at fixed factor law, establishing (3). The corresponding gap above the lower envelope replaces \(m_2-q^2\) with \(q-m_2\).

**6. Fast-reset separation.** For the deterministic magnitude, \(m_j=q^j\), the product in (1) decreases to the positive infinite product \((q;q)_\infty\). Comparing the weighted cosh series with its unweighted version and splitting into a finite initial segment and a long-index tail gives
\[
T_{\rm fixed}(0)\sim (q;q)_\infty\frac{\cosh(\sqrt s)-1}{r}\sim\frac{(q;q)_\infty}{2r}e^{\sqrt s}.
\]
For all-or-nothing resetting, \(T_{\rm onoff}(0)=[\cosh(\sqrt{s(1-q)})-1]/[r(1-q)]\sim e^{\sqrt{s(1-q)}}/[2r(1-q)]\). Division proves (4).

## Verification

An included Python verifier computes (1) and separately solves the nonlocal backward equation using a finite-difference boundary-value discretization. The verifier passed 93 checks covering four reset laws, 30 parameter combinations with both envelopes, independent hyperbolic-cosine limits, factor-sign invariance, weak-reset gaps and fast-reset asymptotics. The analytic proof above, not this finite numerical exercise, establishes the universal inequalities. Run `python verify.py` with the documented numerical packages.

## Relationship to prior work

Biroli, Feld, Hartmann, Majumdar and Schehr (2024) derive the one-sided target mean first-passage equation and its power-series solution for a **fixed** rescaling multiplier; the present backward recurrence is related, but the new theorem addresses **random multipliers, two absorbing endpoints, a fixed quadratic-retention constraint, and both globally sharp factor-law optimizers**. Pal and Prasad (2018/2019) analyze exit from a bounded interval under resets to a **fixed initial location**, rather than a random multiple of the current position. Méndez, Flaquer-Galmés and Campos (2024) treat independent random reset locations, not state-dependent multiplier laws. Pierce (2022) treats fixed-proportion resets and stationary moments. The sharp distributional optimization and its exponential separation are not established by those formulas without the additional moment comparison and boundary argument.

## Limitations

The comparison controls the **mean** symmetric exit time, not stochastic order of its complete distribution. The signs of factors cease to be invisible for a single directional target. The result requires independent identically distributed multipliers and a bounded symmetric interval; it does not assert the same extremizers for asymmetric targets, non-Poisson clocks, or factors of magnitude exceeding one. General theorems not identified in the checked literature might imply portions of this exact classification; independent priority verification remains open.

## References

1. M. Biroli, Y. Feld, A. K. Hartmann, S. N. Majumdar and G. Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension*, arXiv:2406.08387 (first submitted 2024-06-12), https://arxiv.org/html/2406.08387v1; Phys. Rev. E 110, 044142 (2024).
2. A. Pal and V. V. Prasad, *First passage under stochastic resetting in an interval*, arXiv:1812.03009 (2018), https://arxiv.org/html/1812.03009v2; Phys. Rev. E 99, 032123 (2019).
3. V. Méndez, R. Flaquer-Galmés and D. Campos, *First-passage time of a Brownian searcher with stochastic resetting to random positions*, arXiv:2401.01125 (2024), https://arxiv.org/abs/2401.01125.
4. J. K. Pierce, *An advection-diffusion process with proportional resetting*, arXiv:2204.07215 (2022), https://arxiv.org/abs/2204.07215.
