# A universally maximal stability region for convex two-memory fixed-point iteration

## Finding

For every finite complex square matrix \(A\), consider the homogeneous error iteration
\[
 e_{k+1}=A\big((1-q)e_k+qe_{k-1}\big),\qquad 0\le q\le1,
\]
with one *constant* convex-memory weight \(q\). Call a weight stable for \(A\) when every pair of initial error vectors produces an exponentially decaying error sequence. **The unique weight whose stability region contains that of every other convex-memory weight is \(q_*=1/3\)**. Thus weighting the current iterate by \(2/3\) and the preceding iterate by \(1/3\) preserves every finite-dimensional linear stability guarantee attainable by any constant convex combination of the two.

For the scalar multiplier \(a\in\mathbb C\), its exact region is
\[
 \mathcal S_* = \big\{a\in\mathbb C:\ |a|^2<9,\quad |a|^4+(18+8\operatorname{Re}a)|a|^2<27\big\}.
\]
The first inequality is also implied by the second, but it displays the root-product constraint directly. The family of scalar regions obeys \(\mathcal S_q\subseteq\mathcal S_*\) for every \(q\in[0,1]\), strictly for \(q\ne1/3\). The exact stable negative-real interval at \(q_*\) is \((-3,0)\) when parametrized by \(a=-t\), \(t>0\), and the full real-axis intersection is \((-3,1)\). Its exact imaginary-axis intersection is \((-i\eta_*,i\eta_*)\), where
\[
 \eta_* = \sqrt{6\sqrt3-9}=1.179959679570986\ldots.
\]
At the boundary \(a=-3\), the characteristic polynomial becomes \((z+1)^2\), so the endpoint is not exponentially stable.

## Assumptions and scope

The dimension \(d\ge1\) is arbitrary but finite, \(A\in\mathbb C^{d\times d}\) is arbitrary (possibly nonnormal or defective), and \(q\in[0,1]\) is constant in the iteration. All statements concern exact arithmetic and the asymptotic spectral stability of the augmented two-step recurrence. For an affine fixed-point problem \(x=Ax+b\) with a fixed point, the stated homogeneous recurrence is its error propagation. The theorem is *not* a claim that \(q_*\) minimizes the convergence factor for each individual \(A\), nor that it minimizes transient norms.

Write \(\mathcal S_q\) for the scalar set for which the two roots of
\[
 p_{a,q}(z)=z^2-a\big((1-q)z+q\big)
\]
lie strictly inside the unit circle. The block companion for \(A\) has characteristic determinant
\[
 \det\big(z^2I-((1-q)z+q)A\big)
 =\prod_{a\in\sigma(A)}p_{a,q}(z),
\]
counting algebraic multiplicities, by triangularizing \(A\). Hence stability for every initial pair is equivalent to \(\sigma(A)\subset\mathcal S_q\), without a diagonalizability assumption.

## Proof

**1. Exact quadratic root criterion.** Set \(R=|a|^2\) and \(x=\operatorname{Re}a\). The degree-two Schur–Cohn criterion for \(z^2+bz+c\) is
\[
 |c|<1,\qquad |b-\overline b c|<1-|c|^2.
\]
With \(b=-(1-q)a\) and \(c=-qa\), it becomes
\[
 q^2R<1,\qquad F(q;a)>0,
\]
where
\[
 \begin{aligned}
 F(q;a)&=(1-q^2R)^2-(1-q)^2|a+qR|^2\\
 &=1-(1-2q+3q^2)R-2q(1-q)^2Rx+q^2(2q-1)R^2.
 \end{aligned}
\]
In particular,
\[
 27F(1/3;a)=27-18R-8Rx-R^2.
\]

**2. Universal region inclusion.** If \(R<1\), every weight is stable: a hypothetical root \(|z|\ge1\) would satisfy
\[
 |z|^2=|a|\,|(1-q)z+q|\le |a|\,|z|<|z|,
\]
a contradiction. If \(R=1\), any stable scalar has \(a\ne1\) because \(p_{1,q}(1)=0\), and then \(F(1/3;a)=8(1-x)/27>0\) while \(R/9<1\).

Suppose next that \(R>1\) and some \(q\) is stable. Necessarily \(q\in[0,R^{-1/2})\). Both endpoints of \(F\) on the closed interval \([0,R^{-1/2}]\) are nonpositive:
\[
 F(0;a)=1-R<0,
 \qquad F(R^{-1/2};a)=-(1-R^{-1/2})^2|a+\sqrt R|^2\le0.
\]
Because \(F\) is positive at the stable weight, it has a **positive interior maximum**. Differentiating gives the factorization
\[
 \frac{\partial F}{\partial q}
 =2R(3q-1)\big[x-1+q(R-x)\big].
\]
For \(R>1\), we have \(R-x>0\). The only possible stationary points are \(q=1/3\) and \(q_0=(1-x)/(R-x)\). At the latter,
\[
 F(q_0;a)
 =-\frac{(R-x^2)(R-1)^2}{(R-x)^2}\le0,
\]
so the positive maximum must occur at \(q=1/3\). In particular \(1/3<R^{-1/2}\) and \(F(1/3;a)>0\). The Schur–Cohn conditions are therefore satisfied at \(q_*\), proving \(\mathcal S_q\subseteq\mathcal S_*\) for all complex scalar multipliers and hence for all finite matrices. Moreover, for \(t=\sqrt R\ge3\) and \(x\ge-t\), one has \(27F(1/3;a)\le27-18t^2+8t^3-t^4=-(t-3)^3(t+1)\le0\); hence the second displayed inequality in the region definition already forces \(R<9\).

**3. Exact region and sharpness.** Substituting \(q=1/3\) into the two strict Schur–Cohn inequalities gives the displayed semi-algebraic region. For real negative \(a=-t\), \(t>0\), the real quadratic Jury conditions simplify to
\[
 tq<1,\qquad 1-t(1-2q)>0
\]
(the third condition \(1+t>0\) is automatic). Thus the negative-real stability ceiling is \(T(q)=\min\{U(q),V(q)\}\), where
\[
 U(q)=\begin{cases}1/q,&q>0,\\+\infty,&q=0,\end{cases}
 \qquad
 V(q)=\begin{cases}1/(1-2q),&q<1/2,\\+\infty,&q\ge1/2.\end{cases}
\]
It equals \(3\) at \(q=1/3\), is strictly below \(3\) at every other \(q\in[0,1]\), and supplies a real scalar in \(\mathcal S_*\setminus\mathcal S_q\) for each \(q\ne1/3\). For positive real \(a\), nonnegative weights give stability exactly for \(0\le a<1\); on the negative real axis the sharp endpoint is \(-3\). Indeed at \(a=-t\),
\[
 27F(1/3;-t)=-(t-3)^3(t+1).
\]
On the imaginary axis \(a=i\eta\), letting \(R=\eta^2\), the boundary equation is \(R^2+18R-27=0\), so the positive solution is \(R=6\sqrt3-9\). This proves the stated imaginary margin and completes the uniqueness proof.

## Verification

Run `python3 check.py` using Python's standard library. The program compares the exact Schur–Cohn inequalities with independently evaluated roots of the quadratic, checks the global inclusion on a complex grid and random complex parameters, verifies the derivative factorization and the competing critical-point value over exact rational inputs, and tests explicit strictness witnesses and real/imaginary endpoints. One execution produced `PASS 97272 checks; imaginary-axis boundary 1.179959679570986`. These computations are independent consistency checks; the analytic proof above establishes the statement for every complex multiplier and all finite dimensions.

## Relationship to prior work

Epperlein and Wirth's September 2026 *Moving-Average Iteration of Linear Maps* studies the stability regions of **equal-weight** moving averages of variable window length. Here the window is fixed at two but its convex weights vary; the conclusion is a universal **set-inclusion optimum among all constant weights** for *complex* spectra and arbitrary finite matrix dimension. The equal-weight two-memory member is \(q=1/2\), and its real negative stability endpoint is \(-2\), compared with \(-3\) here. The existence and geometry of the equal-weight regions alone do not imply the asserted cross-weight optimality or strictness.

Chebyshev inertial fixed-point schemes instead vary relaxation parameters across iterations and typically use real-spectrum design information; that framework does not yield this single-weight complex-spectrum set-inclusion result. The polynomial root tests used in this proof are classical and not claimed as new. A complete full-text comparison with the motivating preprint was unavailable: the bibliographic assessment is based on its publicly indexed abstract and an independent detailed technical synopsis, so overlap in inaccessible sections remains possible.

## Limitations

The result is about a specific two-lag convex memory placement and **asymptotic** stability, not the optimal iteration count, fastest contraction for a given spectrum, uniform transient bounds, switching weights, nonlinear mappings, floating-point effects, or longer memories. It makes no assertion of a globally optimal convex-memory rule when three or more past iterates are allowed. No independent mathematical audit has been performed. Bibliographic uniqueness is not certified; unindexed or inaccessible work may contain an equivalent formulation.

## References

1. J. Epperlein and F. Wirth, *Moving-Average Iteration of Linear Maps*, arXiv:2609.21442v1 (first public September 18, 2026), https://arxiv.org/abs/2609.21442 .
2. T. Wadayama and S. Takabe, *Chebyshev Inertial Iteration for Accelerating Fixed-Point Iterations*, arXiv:2001.03280v1 (2020), https://arxiv.org/abs/2001.03280 .
3. Classical Schur–Cohn stability criterion for monic quadratic polynomials, https://en.wikipedia.org/wiki/Lehmer%E2%80%93Schur_algorithm .
