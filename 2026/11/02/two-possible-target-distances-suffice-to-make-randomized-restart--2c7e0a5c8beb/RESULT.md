# Two possible target distances suffice to make randomized restart strictly better than every fixed or Poisson clock

## Finding
Consider one-dimensional Brownian motion of generator \(\partial_{xx}\), started and restarted at the origin, searching for a single absorbing target. At the beginning of a search, its distance \(R\) is drawn once, with \(\mathbb P(R=1)=19/20\) and \(\mathbb P(R=5)=1/20\); its distance does not change at subsequent resets. The performance criterion is the unconditional mean detection time, averaging *after* computing the mean conditional on the initially drawn distance.

Use independently resampled reset intervals distributed according to
\[
\psi_\star=\frac{43}{50}\delta_{2/5}+\frac{7}{50}\delta_{10}.
\]
Then the exact strict, certified inequalities are
\[
\boxed{\quad \mathbb E[T_{\psi_\star}]<\frac{21}{5}
<\frac{17}{4}<\inf_{\tau>0}\mathbb E[T_{\delta_\tau}],\qquad
\frac{17}{4}<\inf_{r>0}\mathbb E[T_{\operatorname{Exp}(r)}].\quad}
\]
Thus a two-atom resetting *time* law beats every periodic deterministic clock and every Poisson reset clock, despite the target-distance distribution having bounded support of cardinality two. A target-distance support of cardinality one cannot exhibit this advantage against all deterministic clocks: for any single fixed distance, a deterministic duration attains (or approximates) the optimum over all iid reset-duration laws. Consequently the minimum number of possible fixed target distances needed for such a strict improvement is **exactly two**. No claim is made that the displayed mixed clock is globally optimal among randomized clocks.

## Assumptions and scope
Reset positions and the starting position are the same fixed origin; the diffusion coefficient in the standard generator convention \(D\partial_{xx}\) is \(D=1\), so the unreset process has variance \(2t\). The target is either \(+R\) or \(-R\); only distance matters. Target distance is drawn once per entire search, not at each reset. Reset times are independently sampled before each attempt, independent of all Brownian paths and the target. A reset is instantaneous, has zero cost, and redraws a fresh Brownian path. The search terminates at the first target hit. All random variables and clocks are strictly nonnegative and admissible clocks have positive detection probability per attempt. Comparisons are over every positive deterministic duration and every positive Poisson rate, not over all conceivable randomized or adaptive controls.

## Proof
For a fixed target distance \(R>0\), let \(H_R\) be the unreset first hitting time. The reflection principle gives
\[
S_R(t)=\mathbb P(H_R>t)=\operatorname{erf}\!\left(\frac{R}{2\sqrt t}\right),\qquad
F_R(t)=1-S_R(t)=\operatorname{erfc}\!\left(\frac{R}{2\sqrt t}\right).
\]
Write \(A_R(t)=\int_0^t S_R(s)\,ds\). Direct differentiation, with \(y=R^2/(4t)\), yields
\[
A_R(t)=\left(t+\frac{R^2}{2}\right)S_R(t)
+\frac{R\sqrt t}{\sqrt\pi}e^{-y}-\frac{R^2}{2}.
\]
For an independently redrawn clock \(Z\sim\psi\), the renewal equation applied **conditionally on the fixed target** gives
\[
M_R(\psi)=\frac{\mathbb E[A_R(Z)]}{\mathbb E[F_R(Z)]},
\qquad\overline M(\psi)=\frac{19}{20}M_1(\psi)+\frac1{20}M_5(\psi).
\]
In particular \(M_R(\delta_t)=A_R(t)/F_R(t)\). These are established forward identities; the contribution here is the certified global separation below.

**Certified mixed-clock upper bound.** Substitute the two displayed rational times and weights into the last formula. The standalone exact-rational interval verifier proves \(\overline M(\psi_\star)<21/5\), with numerical reference value \(4.19479906689790\ldots\). It does not use floating point for the inequalities.

**All deterministic clocks, short range.** The unreset hitting density is
\[
f_R(t)=\frac{R}{2\sqrt\pi\,t^{3/2}}e^{-R^2/(4t)}.
\]
For the unit-distance target, \(f_1(t)<2S_1(t)\) for every \(t>0\): when \(t\ge1/4\), the integral representation of the error function gives \(S_1(t)\ge e^{-1/(4t)}/\sqrt{\pi t}\), hence \(f_1/S_1\le1/(2t)\le2\). When \(t\le1/4\), \(S_1(t)\ge\operatorname{erf}(1)>1/2\) and \(f_1(t)\le f_1(1/6)<1\). The latter follows from \(\pi>3\) and \(e>8/3\). Integrating \(f_1<2S_1\) gives \(M_1(\delta_t)>1/2\).

For distance five, \(f_5'(t)>0\) if \(0<t<25/6\). Hence \(g_5=S_5/f_5\) is strictly decreasing there, because \(g_5'=-1-S_5f_5'/f_5^2<0\). Since \(A_5/F_5\) is a \(f_5\)-weighted mean of \(g_5\) on \((0,t)\), it is decreasing on this same interval. Thus for \(0<t\le29/10\),
\[
\overline M(\delta_t)>
\frac{19}{40}+\frac1{20}\frac{A_5(29/10)}{F_5(29/10)}
>4.2675>\frac{17}{4}.
\]
The strict rational comparison is included in the verifier.

**All deterministic clocks, middle range.** Split the *entire continuum* \([29/10,20]\) into the thirty-five consecutive closed intervals with endpoints
\[
a_j=\frac{29}{10}+\frac j2\quad(0\le j\le34),\qquad a_{35}=20.
\]
Both \(A_R\) and \(F_R\) are increasing. For every \(t\in[a_j,a_{j+1}]\), therefore,
\[
\overline M(\delta_t)\ge
\frac{19}{20}\frac{A_1(a_j)}{F_1(a_{j+1})}
+\frac1{20}\frac{A_5(a_j)}{F_5(a_{j+1})}.
\]
The exact rational certificate checks all thirty-five lower bounds exceed \(17/4\); their minimum is between \(4.3631\) and \(4.3632\), attained among these coarse bounds for the interval \([22/5,49/10]\). This finite partition covers *every* real duration in the stated continuum; it is not a finite grid sample masquerading as an infinite proof.

**All deterministic clocks, long range.** For \(t\ge20\), monotonicity of \(A_1\), the bound \(F_1\le1\), and positivity of the other target's contribution imply
\[
\overline M(\delta_t)\ge\frac{19}{20}A_1(20)>4.3389>\frac{17}{4}.
\]
Together the three ranges exhaust every \(t>0\).

**Every exponential (Poisson) clock.** With \(u=\sqrt r>0\), the standard Poisson-reset formula gives
\[
\overline M(\operatorname{Exp}(r))=
\frac{\frac{19}{20}(e^u-1)+\frac1{20}(e^{5u}-1)}{u^2}.
\]
Truncating both positive exponential power series after degree four gives the lower bound
\[
P_4(u)=\frac6{5u}+\frac{11}{10}+\frac65u+\frac{161}{120}u^2.
\]
The difference satisfies
\[
120u\left(P_4(u)-\frac{17}{4}\right)
=161u^3+144u^2-378u+144>0.
\]
On each of \([0,1/2]\), \([1/2,2/3]\), and \([2/3,1]\), every cubic Bernstein coefficient of this polynomial is strictly positive (the verifier computes them with rational arithmetic). For \(u\ge1\), its value at one is \(71\) and its derivative \(483u^2+288u-378\) is positive. This proves the inequality for *all* positive rates.

**Minimality of two target values.** If the target has one fixed distance \(R\), then for every clock \(\psi\) with finite mean completion time,
\[
M_R(\psi)=\frac{\int F_R(t)\,[A_R(t)/F_R(t)]\,\psi(dt)}{\int F_R(t)\,\psi(dt)}
\ge\inf_{t>0} M_R(\delta_t).
\]
The right side is the infimum of deterministic-clock performance, so randomizing cannot strictly outperform *every* deterministic duration. Our two-point example shows that exactly two possible target distances are sufficient.

## Verification
Run `python3 verify_two_target_restart.py` using only the Python standard library. It verifies all inequality claims with exact `fractions.Fraction` interval bounds. It brackets \(\pi\) using the alternating arctangent series and Machin's identity, brackets square roots using integer square root, and brackets exponential and error functions using explicit alternating-series tail bounds. The shortest-period, all thirty-five middle-period intervals, longest-period and Poisson polynomial certificates are all checked. Typical diagnostic values (not used as certificates) are mixed-clock \(4.1947990669\), short-range bound \(4.2675323058\), intermediate minimum bound \(4.3631715498\), and long-range bound \(4.3389016670\). Infinite duration/rate domains are covered by analytic inequalities plus certified finite interval coverage.

## Relationship to prior work
Evans and Ray, arXiv:2410.01941 (first publicly available October 2, 2024), formulated the quenched random-target problem, proved its renewal formula and studied stochastic resetting outperforming sharp restart for target laws with broad unbounded tails. The present narrow claim concerns the *minimum discrete target support size* and a rigorously certified **two-point, bounded-support** strict separation from every sharp clock and every Poisson clock. These results are not inferred solely from a failure to find a matching title.

Eliazar and Reuveni, arXiv:2003.14116, prove optimality properties of sharp restart for one fixed completion-time law. That theorem addresses iid attempts with the same unconditional completion-time distribution, not a hidden target parameter held fixed over successive attempts. Indeed, averaging conditional ratios is different from taking a ratio of averaged attempt quantities; interchanging them would be erroneous. Evans and Majumdar, arXiv:1107.4225, optimize resetting *positions* and rates against random target positions rather than distributions of iid reset *durations* of a fixed spatial reset point. The elementary one-target impossibility is proved here as well and is not asserted as new. A broader published finite-support restart optimization theorem, if found, could subsume the present certificate.

## Limitations
This is an explicit and sharp target-support-cardinality counterexample, not a full classification of optimal clock laws for binary target distributions. It gives strict comparison with all deterministic and exponential clock laws; it does not identify the global optimal randomized policy, consider adaptive clocks, or quantify finite-data estimation. The target is fixed through the entire search; redrawing it at each reset changes the optimization problem and removes the counterexample mechanism. External independent scientific validation and exhaustive priority verification have not been performed.

## References
1. M. R. Evans and S. Ray, *Stochastic resetting prevails over sharp restart for broad target distributions*, arXiv:2410.01941 (first public version 2024-10-02), https://arxiv.org/abs/2410.01941.
2. I. Eliazar and S. Reuveni, *Mean-performance of sharp restart I: Statistical roadmap*, arXiv:2003.14116 (2020), https://arxiv.org/abs/2003.14116.
3. M. R. Evans and S. N. Majumdar, *Diffusion with Optimal Resetting*, arXiv:1107.4225 (2011), https://arxiv.org/abs/1107.4225.
