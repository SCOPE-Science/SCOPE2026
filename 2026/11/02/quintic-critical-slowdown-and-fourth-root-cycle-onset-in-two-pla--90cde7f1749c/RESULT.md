# Quintic critical slowdown and fourth-root cycle onset in two-player lottery contests

## Finding
For a two-player Tullock lottery contest with unit prize, linear effort costs \(x\) and \(cy\), and alternating exact best responses, put
\[
c_* = 3-2\sqrt2,\qquad K=50688-35840\sqrt2>0,\qquad
\alpha=8+6\sqrt2,\qquad A=\left(\frac{\alpha}{K}\right)^{1/4}.
\]
The positive equilibrium efforts are \(x_*(c)=c/(1+c)^2\) and \(y_*(c)=1/(1+c)^2\). There exists a neighborhood of this equilibrium on which all best responses are positive and the following statements hold.

1. **Critical relaxation.** At \(c=c_*\), every sufficiently close non-equilibrium initial response coordinate \(y_0\) has the universal asymptotic
\[
\lim_{k\to\infty}k^{1/4}\big(F_{c_*}^{\,2k}(y_0)-y_*(c_*)\big)
=\operatorname{sgn}(y_0-y_*(c_*))(4K)^{-1/4},
\]
where \(F_c\) is one full round of two best responses. Thus the equilibrium is locally attracting at the critical cost ratio, but with algebraic rather than geometric relaxation along the subsequence of two-round iterations.

2. **Degenerate cycle onset.** For every sufficiently small \(\delta>0\), at \(c=c_*-\delta\) there is exactly one primitive positive two-cycle of \(F_c\) sufficiently near \(y_*(c)\), with points \(y_-(\delta)<y_+(\delta)\) satisfying
\[
y_\pm(\delta)=y_*(c)\pm A\delta^{1/4}+O(\delta^{1/2}),
\qquad
(F_c^2)'(y_\pm(\delta))=1-4\alpha\delta+o(\delta).
\]
The two-cycle is locally attracting, whereas the equilibrium is locally repelling for \(c<c_*\) sufficiently close to \(c_*\). For \(c>c_*\) sufficiently close, the equilibrium is locally geometrically attracting and there is no nearby primitive two-cycle. The exact amplitude satisfies \(A^4=(816+577\sqrt2)/256\).

The distinctive feature is the cancellation of the usual cubic flip coefficient: the first nonzero term of the critical two-round return map is quintic, producing fourth-root onset and a quarter-power relaxation law.

## Assumptions and scope
Both agents choose nonnegative efforts; utilities at positive total effort are \(u_1(x,y)=x/(x+y)-x\) and \(u_2(x,y)=y/(x+y)-cy\), with \(c>0\). The player with cost one responds first and the other responds second in each round. Only strictly positive responses in a neighborhood of the unique positive Nash equilibrium are considered. This avoids the convention-dependent best response when the opponent has zero effort. The theorem is local in initial condition and in the deviation of \(c\) from \(c_*\); it does not classify remote orbits, their basins, or every global cycle.

For \(0<y<1\), player one's positive best response is \(f(y)=\sqrt y-y\). When \(0<f(y)<1/c\), player two's positive best response is \(g_c(f(y))=\sqrt{f(y)/c}-f(y)\). Hence the two-move return map on the second player's effort is
\[
F_c(y)=\sqrt{\frac{\sqrt y-y}{c}}-(\sqrt y-y).
\]
At \(c=c_*\), \(x_*=1/8\) and \(y_*=(3+2\sqrt2)/8\), which lie strictly inside this positive-response region. All local assertions refer to a sufficiently small neighborhood where the displayed map is real analytic.

## Proof
**1. Return map and fixed-point multiplier.** Maximizing the strictly concave payoff \(z/(z+s)-a z\) for \(s>0\) gives the unique positive best response \(\sqrt{s/a}-s\) whenever \(s<1/a\). Substitution yields \(F_c\) above. Solving the two first-order conditions gives \((x_*,y_*)\). Differentiating at \(y_*(c)\) yields
\[
\lambda(c)=F'_c(y_*(c))=-\frac{(c-1)^2}{4c},\quad
\lambda(c_*)=-1,\quad \lambda'(c_*)=4+3\sqrt2.
\]
Thus \((F_c^2)'(y_*)-1=\alpha(c_*-c)+O((c-c_*)^2)\), with \(\alpha=8+6\sqrt2\). This multiplier alone does not determine the critical dynamics or cycle amplitude.

**2. An exact fifth-order return coefficient.** Let \(z=y-y_*(c_*)\) and write \(F_{c_*}(y_*+z)-y_* =\sum_{j=1}^5 a_jz^j+O(z^6)\). Direct Taylor expansion using the positive square-root branches gives
\[
(a_1,a_2,a_3,a_4,a_5)=
\big(-1,\,4-4\sqrt2,\,-48+32\sqrt2,\,16-16\sqrt2,\,33472-23680\sqrt2\big).
\]
Composing this polynomial with itself and retaining terms through degree five gives exactly
\[
F_{c_*}^{\,2}(y_*+z)-y_*=z-Kz^5+O(z^6),
\qquad K=50688-35840\sqrt2>0.
\]
The coefficients of degrees two, three and four vanish **exactly**, not approximately. For positivity, rationalization gives \(1/K=(99+70\sqrt2)/512>0\). A standalone exact-arithmetic derivation is included in `verification/check.py`.

**3. Critical attraction and its sharp rate.** On a sufficiently small real interval around zero, the map in step 2 preserves the sign of \(z\), strictly decreases its absolute value unless \(z=0\), and keeps it inside that interval. Therefore \(z_k=F_{c_*}^{\,2k}(y_0)-y_*\to0\). Since
\[
|z_{k+1}|=|z_k|\big(1-K|z_k|^4+O(|z_k|^5)\big),
\]
we have \(|z_{k+1}|^{-4}-|z_k|^{-4}\to4K\). Taking Cesàro averages yields \(|z_k|^{-4}/k\to4K\), and sign preservation gives the asserted signed limit.

**4. Unique nearby orbit and fourth-root amplitude.** Center the map at the moving equilibrium and define the analytic function
\[
H(\delta,z)=\frac{F_{c_*-\delta}^{\,2}(y_*(c_*-\delta)+z)-y_*(c_*-\delta)-z}{z},
\]
with its removable singularity filled at \(z=0\). Steps 1 and 2, together with analyticity in \((\delta,z)\), give
\[
H(\delta,z)=\alpha\delta-Kz^4+O(\delta^2+|\delta z|+|z|^5).
\]
At \(\delta=0\), \(H(0,z)\) has a zero of multiplicity four and no other zero in a sufficiently small complex disk. The analytic zero-counting principle preserves four zeros in that disk for all sufficiently small \(\delta\). With the scaling \(z=\delta^{1/4}w\) for \(\delta>0\), the zero equation tends uniformly on bounded sets to \(\alpha-Kw^4=0\). Its four simple roots are \(\pm A\) and \(\pm iA\). Consequently exactly two nearby roots are real, with \(z_\pm=\pm A\delta^{1/4}+O(\delta^{1/2})\); the other two are nonreal. The two real roots are exchanged by \(F_c\), because \(F_c'(y_*)\to-1\) and \(F_c\) permutes the fixed points of \(F_c^2\). Differentiating the local expansion at those roots gives \((F_c^2)'=1-4\alpha\delta+o(\delta)\), which lies strictly between zero and one for small positive \(\delta\). The moving equilibrium has multiplier \(\lambda(c)^2>1\) below the boundary and \(<1\) just above. For negative \(\delta\), the four rescaled roots tend to nonreal fourth roots of a negative number, so no nearby nonzero real fixed point of \(F_c^2\) exists. This completes the local classification.

## Verification
Running `python verification/check.py` with the standard Python 3 library proves the fifth-degree Taylor-composition identities in exact rational arithmetic over \(\mathbb Q(\sqrt2)\), verifies \(K\), \(\alpha\), and the amplitude identity, and separately checks the two-cycle roots at three shrinking positive parameter gaps using 70-digit Decimal arithmetic. The exact Taylor certificate is independent of the floating-point sampling. The analytic zero-counting and asymptotic arguments are mathematical deductions from the verified local coefficients, not assertions based on finite samples.

## Relationship to prior work
Ghosh and Goldberg (2023, arXiv:2305.10881v1) give the lottery-contest best-response rule, homogeneous fast convergence, and examples of nonconvergence under asymmetric costs, but do not report a fifth-order critical expansion, a critical algebraic relaxation exponent, or a fourth-root cycle amplitude. Ghosh (2023, arXiv:2310.03528v2) generalizes convergence results for homogeneous convex-cost contests and gives an asymmetric periodic example, without resolving this local critical scaling in the linear-cost contest. Milchtaich and Zahojay (2023) give a general linearized condition for alternating-response stability; linearization is inconclusive at multiplier \(-1\).

A previously recorded result on precisely this lottery return map establishes the sharp global convergence/period-two-existence boundary \(c_*\) in a restricted parameter interval. That statement covers the location of the threshold and the existence or absence of period-two orbits; it **does not imply** the present exact fifth-order degeneracy, \(k^{-1/4}\) critical relaxation, \(\delta^{1/4}\) amplitude, or the leading orbit multiplier. The current claim is restricted to those additional nonlinear facts; it makes no new claim to the previously established global threshold or cycle existence alone. General interval-dynamics results about convergence without two-cycles likewise do not determine these exponents or constants.

## Limitations
The theorem is local near the positive equilibrium and near the lower asymmetric-cost boundary. Its algebraic rate counts applications of \(F_c^2\), each equal to two complete rounds or four single-agent moves. The exact normal-form coefficients apply to the unit-prize, linear-cost Tullock model; different cost curvature or response protocols may give different orders. No global basin estimate, full-period spectrum away from the boundary, or independent specialist priority review is asserted.

## References
- A. Ghosh and P. W. Goldberg, *Best-Response Dynamics in Lottery Contests*, arXiv:2305.10881v1 (first released 2023-05-18), https://arxiv.org/abs/2305.10881 . Sections 2–4, 7.
- A. Ghosh, *Best-Response Dynamics in Tullock Contests with Convex Costs*, arXiv:2310.03528v2 (2023), https://arxiv.org/abs/2310.03528 . Sections 1–3 and Appendix A.
- I. Milchtaich and O. Zahojay, *Altruism and Spite in Tullock Contest*, June 2023 manuscript, https://econ.biu.ac.il/sites/econ/files/shared/staff/u36/papers/Tullock.pdf . Appendix: discrete alternating-response stability criterion.
