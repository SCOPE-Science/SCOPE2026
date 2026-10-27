# Exact sequential false-stop law for two-dimensional Gaussian matrix-free QB

## Finding

Let \(A\in\mathbb R^{2\times2}\) be nonsingular with singular values \(a\ge b>0\), and fix an absolute error tolerance \(0<\tau<b\). Let \(g_1,g_2,g_3\) be independent standard two-dimensional Gaussian columns. Consider the one-column-at-a-time, exact-arithmetic Gaussian QB look-ahead mechanism: inspect \(\|Ag_1\|\) and declare rank zero if it is at most \(\tau\); otherwise take \(q=Ag_1/\|Ag_1\|\) and inspect \(\|(I-qq^\top)Ag_2\|\), declaring rank one if this is at most \(\tau\); otherwise append the orthogonal second direction and declare rank two when its residual is zero. Let \(K\in\{0,1,2\}\) be the resulting stopping rank before any optional post-processing.

Write \(d(u)=b^2+(a^2-b^2)u\) and \(w(u)=1/(\pi\sqrt{u(1-u)})\), for \(0<u<1\). Then the complete law of \(K\) is

\[
\begin{aligned}
 p_0:=\Pr(K=0)&=\int_0^1\left(1-e^{-\tau^2/(2d(u))}\right)w(u)\,du,\\
 p_1:=\Pr(K=1)&=\int_0^1e^{-\tau^2/(2d(u))}\,\operatorname{erf}\left(\frac{\tau\sqrt{d(u)}}{\sqrt 2\,ab}\right)w(u)\,du,\\
 \Pr(K=2)&=1-p_0-p_1.
\end{aligned}
\]

Every outcome with \(K\le1\) **violates the Frobenius error tolerance**, because every rank-at-most-one approximation of \(A\) has Frobenius residual at least \(b>\tau\). Hence the exact probability of a false declaration of success is \(p_0+p_1\). This formula depends on \(A\) only through its singular values and applies to any real left and right singular vectors.

On reaching rank one, the actual Frobenius residual magnitude \(R=\|(I-qq^\top)A\|_F\), without conditioning on the first gate, has the following exact law. For \(a>b\), it is supported on \([b,a]\) and has CDF

\[
\Pr(R\le r)=\frac2\pi\arccos\sqrt{\frac{b^2(a^2-r^2)}{r^2(a^2-b^2)}}\quad(b\le r\le a)
\]

and density

\[
f_R(r)=\frac{2ab}{\pi r\sqrt{(a^2-r^2)(r^2-b^2)}}\quad(b<r<a).
\]

For \(a=b\), \(R=b\) deterministically. The rank-one residual distribution is unconditional; the first-gate pass event is correlated with it and is retained in the integral for \(p_1\).

Finally, write \(\kappa=a/b\) and \(c=\tau/b\in(0,1)\). For every fixed \(c\), the false-stop probability has the strictly positive high-condition-number limit

\[
\boxed{\lim_{\kappa\to\infty}\Pr(K\le1)
=J(c):=\frac2\pi\int_0^{\pi/2}\operatorname{erf}\left(\frac{c\cos\theta}{\sqrt2}\right)\,d\theta>0.}
\]

In particular, \(J(1/2)=0.247126056147589\ldots\). For \(a=4\), \(b=1\), \(\tau=1/2\), the exact integral values are \(p_0\approx0.0302435018200\) and \(p_1\approx0.2597894952034\), so roughly \(29.0\%\) of one-probe decision paths stop below the required rank two. These numerical evaluations illustrate the formulas; no approximation is used in the theorem.

## Assumptions and scope

All matrices are real and all arithmetic is exact. The Gaussian columns are fresh, mutually independent, and have independent \(N(0,1)\) coordinates (the source algorithm's Gaussian block normalization equals this when its block size is one). The tolerance satisfies \(0<\tau<b\) strictly. The initial empty approximation is taken to have rank zero. The statement classifies the **look-ahead decision events**, with a natural empty-output interpretation of stopping at the first gate; this is not a claim that any particular software implementation handles its empty-block rank-pruning branch. Rank-one pruning cannot discard the sole basis column when \(\tau<b\), since its coefficient row has norm at least \(b\). Thus the rank-one stopping event is also retained by the stated one-column pruning rule.

No claim is made for adaptive Gaussian reuse, non-Gaussian sketches, block sizes exceeding one, floating-point arithmetic, relative tolerance with an independently estimated normalization, or higher-rank matrices. Only the first two random probes are needed to determine \(K\); a third observes an exact zero residual after two independent directions are acquired.

## Proof

**1. Gaussian-angle decomposition.** Orthogonal invariance reduces \(A\) to \(\operatorname{diag}(a,b)\). Write \(g_1=(X,Y)^\top\), let \(T=X^2+Y^2\), and set \(U=X^2/(X^2+Y^2)\). The Gaussian polar decomposition gives \(T\sim\chi_2^2\), \(U\sim\operatorname{Beta}(1/2,1/2)\), and independence of \(T\) and \(U\). Consequently

\[
\|Ag_1\|^2=T\,d(U),\qquad
\Pr(\|Ag_1\|\le\tau\mid U=u)=1-e^{-\tau^2/(2d(u))}.
\]

Averaging against the arcsine density \(w\) proves the formula for \(p_0\).

**2. Exact rank-one residual and density.** Conditional on \(g_1\ne0\), let \(L=\sqrt{a^2X^2+b^2Y^2}\). The selected unit column is \(q=(aX,bY)^\top/L\), and an orthogonal unit column is \(q_\perp=(-bY,aX)^\top/L\). Hence

\[
(I-qq^\top)A=q_\perp(q_\perp^\top A),\quad
R^2=\|q_\perp^\top A\|^2
=\frac{a^2b^2(X^2+Y^2)}{a^2X^2+b^2Y^2}
=\frac{a^2b^2}{d(U)}.
\]

The map \(u\mapsto ab/\sqrt{d(u)}\) carries \([0,1]\) monotonically onto \([b,a]\) when \(a>b\). Its inverse at \(r\) is \(u(r)=b^2(a^2-r^2)/(r^2(a^2-b^2))\). Since \(\Pr(U\ge u)=(2/\pi)\arccos\sqrt u\), the displayed CDF follows. Differentiating in \(r\) gives the stated density, whose endpoint singularities are integrable. When \(a=b\) the formula for \(R\) is constant.

**3. Second look-ahead and correlation.** Because \(g_2\) is independent of \(g_1\), conditional on \(g_1\) the rank-one matrix \((I-qq^\top)A\) maps \(g_2\) to a vector of norm distributed as \(R|Z|\), with \(Z\sim N(0,1)\). Thus

\[
\Pr(\|(I-qq^\top)Ag_2\|\le\tau\mid U=u)
=\operatorname{erf}\left(\frac{\tau\sqrt{d(u)}}{\sqrt2\,ab}\right).
\]

The first gate passes with conditional probability \(e^{-\tau^2/(2d(u))}\) given \(U=u\). Independence of its radial variable and the second probe *conditional on* \(U\) permits multiplication of these two factors before integration, proving \(p_1\). Omitting the first factor would incorrectly treat the rank-one stopping event as unconditioned. The remaining probability yields \(K=2\): almost surely two independent projected Gaussian directions span \(\mathbb R^2\), after which the residual is zero.

**4. Actual error and the pruning boundary.** The Eckart–Young best-rank-one theorem gives \(\inf_{\operatorname{rank}(M)\le1}\|A-M\|_F=b\). Therefore both \(K=0\) and \(K=1\) fail \(\tau<b\), while \(K=2\) is exact. Moreover, for a retained rank-one basis \(q\), its QB coefficient row has squared norm \(\|q^\top A\|_2^2\ge b^2\). The one-column rank-pruning test of the motivating method cannot remove it when \(\tau<b\). At rank zero the empty-output convention avoids attributing any undefined empty-block pruning operation to the source's pseudocode.

**5. The nonvanishing anisotropic risk.** Substitute \(u=\cos^2\theta\) into the two integrals, so \(w(u)du\) becomes uniform \((2/\pi)d\theta\) on \([0,\pi/2]\). With \(a=\kappa b\) and \(\tau=cb\), the first integrand is \(1-e^{-c^2/(2[1+(\kappa^2-1)\cos^2\theta])}\), which tends to zero except at the measure-zero endpoint. The second is its complementary exponential factor times \(\operatorname{erf}(c\sqrt{1+(\kappa^2-1)\cos^2\theta}/(\sqrt2\kappa))\), which tends to \(\operatorname{erf}(c\cos\theta/\sqrt2)\) almost everywhere. Both are bounded by one, so dominated convergence proves the limit. Strict positivity follows because the integrand is positive on an interval of positive measure for each \(c>0\).

## Verification

Run `python verify.py` under Python 3, without external libraries. The script independently computes one- and two-gate decisions by direct matrix-vector algebra for \(400{,}000\) fixed-seed Gaussian pairs, verifies the determinant-based formula for \(R\) on non-stopping first gates, and checks the theoretical rank probabilities against direct frequencies for four spectra and tolerances. A separate \(100{,}000\)-draw test checks four CDF thresholds for the actual rank-one residual. Composite Simpson quadrature checks the isotropic closed case and the high-condition-number constant. The script completes with `PASS numerical suite: 500029 trial/analytic checks`. Its seeded frequencies have statistical tolerance and **are not** substitutes for the preceding universal proof.

## Relationship to prior work

Smith, Do, and Chen [1] introduce the Gaussian matrix-free Frobenius error indicator and the adaptive, rank-pruned QB algorithm; their Algorithm 2 uses each new Gaussian residual probe both for a norm stopping decision and, when needed, the next basis block. They state its norm estimate is unbiased for squared residual norm and study empirical accuracy. Neither unbiasedness nor a generic high-probability assertion specifies the distribution of the stopping rank after a data-dependent first basis update. The present result is a sharp finite-dimensional special-case *risk law for the coupled sequential decisions*, not a new norm estimator, basis construction, or general high-probability guarantee.

Gorman et al. [2], especially Section 2.5 and Appendix A, give generalized chi-square models and Chernoff probability bounds for Gaussian residual probes in adaptive HSS construction. Those models correctly describe the probe conditional on a fixed residual; they do not state the joint angular/radial two-probe law when the first sampled column is also used to select the QB basis. The angular CDF and coupled stopping formula require handling that induced dependence.

Pearce et al. [3] use randomized residual estimation for adaptive LU-based interpolative decompositions; the decomposition, update, and stopping decision differ from this exact orthogonal QB model. Epperly and Webber [4] give sharp minimax bounds for randomized low-rank approximation, not this exact absolute-tolerance sequential stopping distribution. Standard Gaussian polar decomposition, arcsine/Beta laws, and Eckart–Young are used as established tools, not claimed original.

## Limitations

This is a complete **two-by-two, block-one, exact-arithmetic** classification of the explicitly defined decision process, not a probabilistic theorem about every implementation or every matrix size. The source algorithm's empty-block pruning operation when the first gate succeeds is not defined here; the rank-zero case is the natural stopping-decision extension. The matrix-free algorithm's commonly used larger blocks and safety-tuned tolerances can have different risks; the numerical example is not a claim about the source paper's default experimental configuration. The result proves no impossibility of reliable randomized stopping with multiple validation probes. The comparisons with primary literature and mathematical record searches do not establish absolute historical priority; analogous formulas may occur in older specialized random-projection literature. No independent mathematical audit has been performed.

## References

[1] A. I. Smith, E. Do, and C. Chen, *Adaptive, Matrix-Free Low-Rank Approximation*, arXiv:2607.06758v1, first posted July 7, 2026. https://arxiv.org/html/2607.06758v1 . Especially Sections 2.3, 3.1–3.2, Algorithm 2, Algorithm 3, and the first-page MSC classification 65F55.

[2] C. Gorman, G. Chávez, P. Ghysels, T. Mary, F.-H. Rouet, and X. S. Li, *Matrix-free construction of HSS representation using adaptive randomized sampling*, arXiv:1810.04125v2, October 2018. https://arxiv.org/html/1810.04125v2 . Especially Section 2.5 and Appendix A.

[3] K. J. Pearce, C. Chen, Y. Dong, and P.-G. Martinsson, *Adaptive Parallelizable Algorithms for Interpolative Decompositions via Partially Pivoted LU*, arXiv:2310.09417, October 2023. https://arxiv.org/abs/2310.09417 .

[4] E. N. Epperly and R. J. Webber, *Sharp analysis of sketched least squares and randomized low-rank approximation*, arXiv:2605.19096, May 2026. https://arxiv.org/abs/2605.19096 .
