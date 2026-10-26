# A sharp endpoint alignment law for bounded-noise stochastic gradient clipping

## Finding

For any dimension \(d\ge 1\), clipping radius \(q>0\), true gradient \(g\in\mathbb R^d\), and random error \(\xi\in\mathbb R^d\) with \(\mathbb E\xi=0\) and \(\|\xi\|_2\le q\) almost surely, the Euclidean clipped stochastic gradient satisfies the **uniform, dimension-free and sharp** inequality

\[
\left\langle g,\mathbb E\operatorname{clip}_q(g+\xi)\right\rangle
\ge \frac12\min\{\|g\|_2^2,q\|g\|_2\}.
\]

The coefficient \(1/2\) cannot be increased uniformly: when \(0<\|g\|_2\le q\), take \(\xi=\pm qg/\|g\|_2\) with equal probabilities. Then the left side equals \(\|g\|_2^2/2\). The noise distribution need not be symmetric for the inequality.

This closes the **equality case** of the clipping-radius/noise-radius threshold: if an oracle error is bounded by \(\sigma\), the inequality holds whenever \(q\ge\sigma\). Conversely, for each \(0<q<\sigma\), a centered, bounded two-point stochastic gradient oracle for the strongly convex quadratic \(f(x)=x^2/2\) has zero expected clipped drift at every \(x\in[-(\sigma-q),\sigma-q]\), even though the true gradient is \(x\). Thus the threshold \(q\ge\sigma\) is sharp for universal positive alignment.

Furthermore, with independent positive-variance Gaussian noise *added after clipping* and with the decaying stepsizes used in the motivating paper, sufficiently small step amplitude leaves a positive probability of convergence to a nonoptimal random point inside this zero-drift interval. The zero-drift interval itself was exhibited in an equivalent two-component example by Chen, Wu and Hong (2020); the new quantitative contribution here is the arbitrary-dimensional sharp endpoint alignment inequality and the matching all-centered-oracle threshold, with the stated Gaussian pathwise consequence.

## Assumptions and scope

Euclidean ball clipping is \(\operatorname{clip}_q(v)=v\min\{1,q/\|v\|_2\}\) for nonzero \(v\), with \(\operatorname{clip}_q(0)=0\). All expectations exist since clipping is bounded. No density, symmetry, independence across coordinates, differentiability of the oracle, or upper bound on dimension is assumed. The error is conditionally centered at each fixed optimization state; the result is pointwise in that state.

For the negative example choose dimension one, \(f(x)=x^2/2\), \(\xi_t\) independent and equally likely \(+\sigma\) or \(-\sigma\), and independent \(\zeta_t\sim\mathcal N(0,s^2)\), where \(s>0\). The iterates start at \(x_0=0\) and obey

\[
x_{t+1}=x_t-\alpha_t\bigl(\operatorname{clip}_q(x_t+\xi_t)+q\zeta_t\bigr),\qquad
\alpha_t=\frac{c}{(t+1)^{1-\theta}},\quad 0<\theta<\tfrac12,
\]

for sufficiently small \(c>0\). The Gaussian perturbation is outside the clipping function, as in the cited SGD-CN construction; no privacy guarantee is inferred.

## Proof

**1. Normalization and pointwise affine minorant.** It suffices to prove the bound when \(q=1\), since \(\operatorname{clip}_q(v)=q\operatorname{clip}_1(v/q)\). For \(g\ne0\), put \(r=\|g\|_2\) and \(e=g/r\). First suppose \(0<r\le1\). For a fixed noise vector \(\xi\) with \(\|\xi\|_2\le1\), set \(s=\langle e,\xi\rangle\in[-1,1]\). We prove the stronger *pointwise* inequality

\[
\langle e,\operatorname{clip}_1(re+\xi)\rangle
\ge\frac r2+\left(1-\frac r2\right)s. \tag{1}
\]

If \(\|re+\xi\|_2\le1\), its left side equals \(r+s\); subtracting the right side gives \(r(1+s)/2\ge0\). Otherwise, \(\|re+\xi\|_2>1\) and \(\|\xi\|_2\le1\) imply \(r^2+2rs>0\), hence \(s>-r/2\). In particular \(r+s>0\), and

\[
\langle e,\operatorname{clip}_1(re+\xi)\rangle
=\frac{r+s}{\|re+\xi\|_2}
\ge F_r(s):=\frac{r+s}{\sqrt{1+r^2+2rs}}.
\]

For \(-r/2\le s\le1\), direct differentiation gives

\[
F_r''(s)=\frac{r(r^2-2-rs)}{(1+r^2+2rs)^{5/2}}<0,
\]

because \(r\le1\) and \(s\ge-r/2\). Thus \(F_r\) is concave on this interval. At its endpoints,

\[
F_r(-r/2)=r/2\ge r^2/4,
\qquad F_r(1)=1.
\]

The affine right side of (1) takes values \(r^2/4\) and \(1\) at these endpoints. Concavity places \(F_r\) above the chord joining its endpoint values, and that chord dominates the claimed affine minorant. This proves (1).

**2. Centering, large gradients, and the optimal constant.** Taking expectations of (1) and using \(\mathbb E\langle e,\xi\rangle=0\) gives \(\mathbb E\langle e,\operatorname{clip}_1(re+\xi)\rangle\ge r/2\) for \(r\le1\). Multiplication by \(r\) proves the first branch. For fixed \(\xi\), the map \(r\mapsto\langle e,\operatorname{clip}_1(re+\xi)\rangle\) is nondecreasing: Euclidean projection onto a closed ball is monotone, and its monotonicity inequality for the arguments \(ae+\xi\) and \(be+\xi\), \(0\le a<b\), implies the assertion. Consequently for every \(r\ge1\), the expected projected component is at least its value at \(r=1\), hence at least \(1/2\). Multiplying by \(r\) establishes the second branch. The case \(g=0\) is immediate. Scaling proves the displayed inequality for general \(q\). For sharpness, for \(0<r\le q\) the two outputs from \(g\pm qg/r\) are \(qg/r\) and \((r-q)g/r\), so their average is \(g/2\).

**3. Subthreshold obstruction.** Fix \(0<q<\sigma\). With equal-probability errors \(\xi=\pm\sigma\), for every \(|x|\le\delta:=\sigma-q\), the two clipped gradients are exactly \(+q\) and \(-q\). Hence the conditional clipped expectation is zero throughout that whole interval, including at nonstationary \(x\ne0\). Therefore no universal strictly positive multiple of \(\min\{x^2,q|x|\}\) can hold below the threshold.

**4. Nonoptimal almost-sure limit with Gaussian post-clipping noise.** Couple the SGD-CN iteration to the independent-increment martingale

\[
S_n=-q\sum_{t=0}^{n-1}\alpha_t(\varepsilon_t+\zeta_t),
\quad\varepsilon_t\in\{-1,+1\}\text{ iid equiprobable}.
\]

Until the process exits \([-\delta,\delta]\), the actual iterate equals \(S_n\). Its terminal variance is finite:

\[
V=q^2(1+s^2)c^2\sum_{t=0}^{\infty}(t+1)^{-2(1-\theta)}<\infty.
\]

Choose \(c>0\) with \(V<\delta^2\). By Doob's \(L^2\) maximal inequality and monotone limits, \(\mathbb P(\sup_{n\ge0}|S_n|\ge\delta)\le V/\delta^2<1\). On the complementary positive-probability event the entire SGD-CN trajectory stays inside the flat-drift interval, agrees with \(S_n\), and converges to \(S_\infty\) almost surely by square-integrable martingale convergence. The terminal martingale is non-atomic: it has a nondegenerate Gaussian component (indeed the first \(\zeta_0\) term alone has positive variance), independent of the remaining increments and the Rademacher terms. Thus \(\mathbb P(S_\infty=0)=0\). The intersection is a positive-probability event on which the iterates converge to a point other than the unique minimizer \(0\). For a reproducible rational variance certificate, take \(q=1\), \(\sigma=2\), \(s=1\), \(\theta=1/4\), \(c=1/100\): using \(\sum_{n=1}^{\infty}n^{-3/2}\le3\), we obtain \(V\le3/5000\) and non-exit probability at least \(4997/5000\).

## Verification

The accompanying standard-library Python checker reproduces the equality cases exactly with rational arithmetic, verifies zero drift for rational states strictly inside three subthreshold intervals, checks the rational maximal-probability certificate, and samples 96,000 normalized noise vectors to stress-test the pointwise affine inequality (1) in dimensions \(1,2,3,8,19\). It outputs `CHECK_OK` when successful. These finite samples do **not** prove (1); the proof is the explicit inside-ball case and the concavity argument above. The nonexit and nonzero-limit assertions follow from the cited martingale inequalities and Gaussian non-atomicity, not from simulation.

## Relationship to prior work

Mukherjee and Liu (2026), Proposition 2, gives the lower alignment coefficient \(1-\sigma_g/q\) when \(q>\sigma_g\) and explicitly states the \(1/2\) bound when \(q\ge2\sigma_g\); its coefficient degenerates at \(q=\sigma_g\). The new inequality establishes the same \(1/2\) bound already at \(q=\sigma_g\), without distributional symmetry, and is sharp. Their stochastic-convergence argument can use this sharper alignment input, but a new independent convergence theorem for their momentum algorithms is not claimed here.

Chen, Wu and Hong (2020), Example 2, explicitly demonstrates the pre-existing subthreshold zero-drift interval on a symmetric two-component quadratic. This example is acknowledged, not represented as a newly discovered obstruction. Their Theorem 2 treats symmetric distributions with a lower bound involving noise mass at small radii, whereas the new endpoint inequality treats every centered distribution supported in the noise ball with a fixed universal coefficient. Koloskova, Hendrikx and Stich (2023) analyze threshold and bias under the weaker bounded-*variance* hypothesis and discuss uniform-noise clipping radii at or above the noise bound; these statements do not supply the all-centered sharp endpoint constant. Qian et al. (2021) give angle/norm-dependent conditions for incremental clipped gradients rather than the present bound from centering and support alone.

## Limitations

The universal positive-alignment claim concerns a centered stochastic oracle with **almost-sure bounded vector error**, a stronger assumption than finite variance. The coefficient \(1/2\) is sharp uniformly over all \(q\ge\sigma\), but no optimal coefficient is claimed for each fixed ratio \(\sigma/q<1\). The negative construction is specific to a one-dimensional quadratic and a two-point stochastic oracle; it proves failure of *universal* alignment and an existence result for pathwise nonconvergence, not failure for every distribution or every initialization. The Gaussian post-clipping noise has positive variance but is not asserted to confer privacy. Older equivalent statements may exist outside the inspected primary sources; no independent validation has been performed.

## References

1. Amartya Mukherjee and Jun Liu, *Almost Sure Convergence Analysis of Stochastic Gradient Methods with Clipping and Additive Noise*, arXiv:2609.12119v1, publicly submitted 2026-09-10. https://arxiv.org/abs/2609.12119
2. Xiangyi Chen, Zhiwei Steven Wu and Mingyi Hong, *Understanding Gradient Clipping in Private SGD: A Geometric Perspective*, NeurIPS 33, 2020. https://papers.neurips.cc/paper_files/paper/2020/file/9ecff5455677b38d19f49ce658ef0608-Paper.pdf
3. Anastasia Koloskova, Hadrien Hendrikx and Sebastian U. Stich, *Revisiting Gradient Clipping: Stochastic bias and tight convergence guarantees*, ICML/PMLR 202, 2023. https://proceedings.mlr.press/v202/koloskova23a/koloskova23a.pdf
4. Jiang Qian et al., *Understanding Gradient Clipping In Incremental Gradient Methods*, AISTATS/PMLR 130, 2021. https://proceedings.mlr.press/v130/qian21a/qian21a.pdf
