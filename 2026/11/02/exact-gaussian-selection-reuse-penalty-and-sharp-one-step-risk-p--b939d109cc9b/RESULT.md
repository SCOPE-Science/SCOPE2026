# Exact Gaussian selection-reuse penalty and sharp one-step risk phase diagram for two-row Kaczmarz

## Finding

Let \(\sigma>0\) and \(x=(a,b)^{\mathsf T}\in\mathbb R^2\) be an arbitrary deterministic current error in the consistent system \(I_2 z=0\). The fresh noisy residual readings are \(R_i=x_i+\varepsilon_i\), with independent \(\varepsilon_i\sim N(0,\sigma^2)\). The greedy index \(I\) maximizes \(|R_i|\), with probability-zero ties broken arbitrarily. Compare the following **one-step**, unrelaxed row projections:

- **Reuse:** evaluate both readings, select \(I\), and update \(G=x-(x_I+\varepsilon_I)e_I\) using the *same* noise as in selection.
- **Split:** select \(I\) using the two readings, independently draw \(\xi\sim N(0,\sigma^2)\), and update \(F=x-(x_I+\xi)e_I\).
- **Uniform:** independently choose \(J\) uniformly from the two indices, draw \(\zeta\sim N(0,\sigma^2)\), and update \(U=x-(x_J+\zeta)e_J\).

Write \(r^2=a^2+b^2\), and define

\[
Q_\pm=\operatorname{erf}\!\left(\frac{a\pm b}{2\sigma}\right),\qquad
H(a,b)=\frac{a^2-b^2}{2}Q_+Q_-,\qquad
C(r)=\frac{2\sigma^2}{\pi}e^{-r^2/(2\sigma^2)}.
\]

All expectations below are over the explicitly stated independent Gaussian readings. The **exact expected squared solution errors** satisfy

\[
\boxed{\begin{aligned}
\mathbb E\|U\|_2^2&=\frac{r^2}{2}+\sigma^2,\\
\mathbb E\|F\|_2^2-\mathbb E\|U\|_2^2&=-H(a,b),\\
\mathbb E\|G\|_2^2-\mathbb E\|U\|_2^2&=C(r)-H(a,b),\\
\mathbb E\|G\|_2^2-\mathbb E\|F\|_2^2&=C(r)>0.
\end{aligned}}
\]

For every \(r>0\), the **sharp, all-orientation range** is

\[
0\le H(a,b)\le\frac{r^2}{2}\operatorname{erf}\!\left(\frac{r}{2\sigma}\right)^2,
\]

with equality on the left exactly when \(|a|=|b|\), and equality on the right exactly when \(ab=0\). Thus fresh-update (split) greed is never worse than uniform; it is strictly better unless the true coordinate residual magnitudes coincide. In contrast, reuse greed is strictly worse than uniform at every equal-magnitude start, regardless of signal-to-noise ratio.

Define \(z_*>0\) as the unique solution of

\[
\frac2\pi e^{-z_*^2/2}=\frac{z_*^2}{2}\operatorname{erf}(z_*/2)^2,
\qquad z_*=1.2401252666271909909\ldots.
\]

If \(0\le r<\sigma z_*\), reuse greed is **strictly worse than uniform at every starting orientation**. At equality, it ties uniform only on coordinate axes and is worse elsewhere. If \(r>\sigma z_*\), it is strictly better at coordinate-axis starts, but still strictly worse at equal-magnitude starts. These conclusions are exact one-update mean-square comparisons; they make no claim about multiple iterations.

## Assumptions and scope

The true system has two orthonormal rows, exact right-hand side zero and deterministic pre-update error \(x\). Each residual observation contains additive, independent, centered Gaussian noise of a *known common variance* \(\sigma^2>0\). Noise used to choose the greedy index is independent across rows; split-update noise is independent of both selection readings. All updates use unit relaxation (the noisy orthogonal row projection), and performance is squared Euclidean error after precisely one update. The uniform comparator requires one new reading, reuse greed requires two, and split greed requires three. The result does not normalize by oracle-query cost.

## Proof

**1. Greedy index probability.** Set

\[
V_+=\frac{R_1+R_2}{\sqrt2},\qquad
V_-=\frac{R_1-R_2}{\sqrt2},\qquad
\mu_\pm=\frac{a\pm b}{\sqrt2}.
\]

The variables \(V_+\) and \(V_-\) are independent \(N(\mu_\pm,\sigma^2)\), since the underlying Gaussian noises are independent with equal variance. The condition \(|R_1|>|R_2|\) is equivalent to \(V_+V_->0\). For a Gaussian \(W\sim N(\mu,\sigma^2)\), \(\mathbb E\operatorname{sgn}W=\operatorname{erf}(\mu/(\sqrt2\sigma))\). Hence

\[
\Pr(I=1)=\frac{1+Q_+Q_-}{2}.
\]

**2. Uniform and split risks.** A coordinate-row update replaces the chosen coordinate by the negative of its update noise and leaves the other coordinate untouched. For uniform selection, the displayed formula \(\mathbb E\|U\|_2^2=r^2/2+\sigma^2\) is immediate. For split selection, update noise is independent of \(I\), and

\[
\mathbb E\|F\|_2^2
=r^2+\sigma^2-\left[a^2\Pr(I=1)+b^2\Pr(I=2)\right]
=\frac{r^2}{2}+\sigma^2-H(a,b).
\]

Since \(\operatorname{erf}\) is odd and has the sign of its argument, \((a^2-b^2)Q_+Q_-\ge0\). It vanishes exactly when \(a=b\) or \(a=-b\).

**3. A direction-independent selection-reuse penalty.** Define independent centered noises \(E_\pm=V_\pm-\mu_\pm=(\varepsilon_1\pm\varepsilon_2)/\sqrt2\) and \(S=\operatorname{sgn}(V_+)\operatorname{sgn}(V_-)\). Then \(\mathbf1_{I=1}=(1+S)/2\), and \(\varepsilon_1^2-\varepsilon_2^2=2E_+E_-\). Therefore

\[
\begin{aligned}
\mathbb E\varepsilon_I^2-\sigma^2
&=\frac12\mathbb E[(\varepsilon_1^2-\varepsilon_2^2)S]\\
&=\mathbb E[E_+\operatorname{sgn}V_+]\,\mathbb E[E_-\operatorname{sgn}V_-].
\end{aligned}
\]

Directly integrating the centered Gaussian density on both sides of its threshold gives

\[
\mathbb E[(W-\mu)\operatorname{sgn}W]
=\frac{2\sigma}{\sqrt{2\pi}}e^{-\mu^2/(2\sigma^2)},
\qquad W\sim N(\mu,\sigma^2).
\]

Multiplying with \(\mu_+^2+\mu_-^2=r^2\) proves \(\mathbb E\varepsilon_I^2=\sigma^2+C(r)\). The residual-coordinate contribution \(r^2-\mathbb E x_I^2\) is identical for reuse and split, establishing all four exact risk identities.

**4. Sharp orientation envelope.** Put \(w=\mu_+^2\in[0,r^2]\) and \(r^2-w=\mu_-^2\). By oddness of \(\operatorname{erf}\),

\[
H(a,b)=g(w)g(r^2-w),\qquad
 g(w)=\sqrt w\operatorname{erf}\!\left(\frac{\sqrt w}{\sqrt2\sigma}\right),\quad g(0)=0.
\]

For \(w>0\), set \(s=\sqrt w/(\sqrt2\sigma)\) and

\[
T(s)=\frac{s e^{-s^2}}{\int_0^s e^{-t^2}\,dt}
=\left(\int_0^1e^{s^2(1-v^2)}\,dv\right)^{-1}.
\]

The function \(T\) is positive and strictly decreasing on \((0,\infty)\). Differentiation gives

\[
\frac{d}{dw}\log g(w)=\frac{1+T(s)}{2w},
\]

which is strictly decreasing in \(w>0\). Thus \(\log g\) is strictly concave, so \(g(w)g(r^2-w)\) is uniquely maximized at \(w=r^2/2\), i.e. \(ab=0\). The product is zero only at either endpoint \(w\in\{0,r^2\}\), i.e. \(|a|=|b|\). Substitution yields the sharp bounds.

**5. Sharp radial crossover.** The minimum possible reuse-minus-uniform risk at radius \(r\) is

\[
C(r)-\frac{r^2}{2}\operatorname{erf}\!\left(\frac r{2\sigma}\right)^2.
\]

After dividing by \(\sigma^2\), its first term is strictly decreasing in \(z=r/\sigma\) from \(2/\pi\) to zero, whereas its subtracted second term is strictly increasing from zero to infinity. There is exactly one positive crossing \(z_*\); the asserted sign diagram, including both equality cases, follows.

## Verification

The standalone `verify.py` uses only the Python standard library. It independently evaluates the one-step algorithm through conditional one-dimensional Gaussian quadrature for seven sign-and-scale configurations, tests risk identities and sharp orientation bounds on multiple radii and noise levels, and bisects the scalar crossover. Running `python3 verify.py` passed 10,893 deterministic checks, with crossover \(1.240125266627191\). The analytical proof above, not numerical integration or angular sampling, establishes the universal and unique statements.

## Relationship to prior work

Greedy maximum-residual Kaczmarz and randomized/partially greedy row rules are established methods. Haddock and Ma (2019) analyze sampling Kaczmarz–Motzkin on consistent systems; Zhang, Li and Tang (2022) analyze maximum-residual and maximum-distance greedy nonlinear Kaczmarz, with the linear rule as a special case. Yuan, Zhang and Wang (2021) treat noisy observations in sparse sampled Kaczmarz under a fixed perturbed right-hand side, while Zhang, Zeng and Zhang (2026) investigate doubly noisy greedy systems and measurement averaging. These works motivate the question but do not, in the inspected material, give the exact **fresh Gaussian two-row, same-sample-versus-split risk identity**, its orientation envelope or the sharp \(1.240125\ldots\) boundary. This is a best-knowledge specialized comparison, not a claim that selection bias or general noisy Kaczmarz is new; related specialized publication priority cannot be exhaustively excluded.

## Limitations

The analysis is exact for one update only, not a multi-iteration convergence theorem. It uses a square identity system, equal independent Gaussian observation variances, unrelaxed projection and squared Euclidean error. The split rule uses one more noisy evaluation than reuse; no claim is made about total oracle-budget optimality, correlated/non-Gaussian errors, overdetermined matrices, arbitrary row geometry or long-run stability. No independent mathematical audit has been performed.

## References

1. Y. Zhang, H. Li and L. Tang, *Greedy randomized sampling nonlinear Kaczmarz methods*, arXiv:2209.06082 (first public version 13 September 2022), https://arxiv.org/abs/2209.06082.
2. J. Haddock and A. Ma, *Greed Works: An Improved Analysis of Sampling Kaczmarz–Motzkin*, arXiv:1912.03544 (2019), https://arxiv.org/abs/1912.03544.
3. Z. Yuan, H. Zhang and H. Wang, *Sparse Sampling Kaczmarz-Motzkin Method with Linear Convergence*, arXiv:2101.04807 (2021), https://arxiv.org/abs/2101.04807.
4. L. Zhang, J. Zeng and H. Zhang, *Relaxed Greedy Randomized Kaczmarz with Signal Averaging for Solving Doubly-Noisy Linear Systems*, arXiv:2603.29372 (2026), https://arxiv.org/abs/2603.29372.
5. J. Haddock, A. Ma and E. Rebrova, *On Subsampled Quantile Randomized Kaczmarz*, arXiv:2308.07987 (2023), https://arxiv.org/abs/2308.07987.
