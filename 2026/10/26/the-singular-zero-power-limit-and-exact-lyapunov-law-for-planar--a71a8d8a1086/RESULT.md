# The singular zero-power limit and exact Lyapunov law for planar residual-weighted Kaczmarz

## Finding

**Theorem (exact planar pathwise rate and singular sampling limit).** Let \(m\ge2\) and let \(a_1,\ldots,a_m\in\mathbb R^2\) be unit vectors whose unoriented lines are pairwise distinct and never perpendicular. Let \(b\in\mathbb R^m\) make \(a_i^\mathsf T x=b_i\) consistent, and let \(x_*\) be its unique solution. For \(i<j\), put

\[
 s_{ij}=|\det(a_i,a_j)|\in(0,1),\qquad
 c_{ij}=|a_i^\mathsf Ta_j|\in(0,1),\qquad
 Z_p=\sum_{i<j}s_{ij}^p.
\]

Starting from an \(x_0\) with \(e_0=x_0-x_*\ne0\) not parallel to any \(a_i\), perform exact Kaczmarz row projections. When \(p>0\), choose the next row \(j\) with conditional probability proportional to \(|a_j^\mathsf T(x_k-x_*)|^p\). Then, for every finite \(p>0\), almost surely,

\[
 \lim_{k\to\infty}\frac{1}{k}\log\|x_k-x_*\|_2
 =\ell(p):=\frac{\sum_{i<j}s_{ij}^{p}\log c_{ij}}{Z_p}<0.
\]

The rate is nonincreasing in \(p\), and it is **strictly decreasing** unless all the \(c_{ij}\) coincide. Its greedy-exponent limit is

\[
 \lim_{p\to\infty}\ell(p)=\log\min_{i<j}c_{ij}.
\]

At \(p=0\), define the conventional unweighted Kaczmarz algorithm by choosing all \(m\) rows independently and uniformly, including the just-satisfied row. Its almost-sure logarithmic rate is

\[
 \ell_{\mathrm{iid}}=\frac{2}{m^2}\sum_{i<j}\log c_{ij}.
\]

**The exact-arithmetic zero-power limit is discontinuous:**

\[
 \boxed{\displaystyle
 \lim_{p\downarrow0}\ell(p)
 =\frac{2}{m(m-1)}\sum_{i<j}\log c_{ij}
 =\frac{m}{m-1}\ell_{\mathrm{iid}}\ne\ell_{\mathrm{iid}}.}
\]

Both numbers are negative, so any arbitrarily small positive residual exponent improves the asymptotic magnitude of the logarithmic contraction by the **exact factor \(m/(m-1)\)** over iid uniform row sampling. This does not assert a corresponding improvement at every finite iteration.

## Assumptions and scope

Rows are unit normalized and belong to the real plane. Pairwise distinct row lines guarantee \(s_{ij}>0\); absence of perpendicular pairs guarantees \(c_{ij}>0\). These assumptions ensure every post-initial projection is nonzero and every logarithm is finite. Consistency and two nonparallel rows give a unique solution. Random choices use fresh conditional draws with exactly the prescribed probabilities. The initial genericity condition prevents immediate exact termination; it is automatic for every starting error outside a finite union of one-dimensional subspaces. All claims are in exact arithmetic. The finite exponent \(p>0\) rule is not defined at the solution, where iteration stops.

## Proof

Write \(e_k=x_k-x_*\). Orthogonal projection onto the selected equation \(a_j^\mathsf T e=0\) is

\[
 e_{k+1}=(I-a_ja_j^\mathsf T)e_k.
\]

Choose for each row a unit perpendicular \(n_i\), with a consistent ninety-degree rotation of all \(a_i\). After the first projection, \(e_k=\alpha_k n_{I_k}\) for a nonzero scalar \(\alpha_k\), where \(I_k\) denotes the most recently selected row. For every \(j\),

\[
 |a_j^\mathsf T e_k|=|\alpha_k|s_{I_kj},\qquad
 (I-a_ja_j^\mathsf T)e_k=\alpha_k(a_j^\mathsf Ta_{I_k})n_j.
\]

The first identity cancels the common amplitude from row-selection probabilities, and the second gives the exact norm multiplier \(c_{I_kj}\) (with \(c_{ii}=1\)). Thus, for \(p>0\), the row-index process after the first projection is a finite Markov chain with

\[
 P_{ij}(p)=\frac{s_{ij}^p}{d_i(p)}\ (j\ne i),\qquad
 P_{ii}(p)=0,\qquad
 d_i(p)=\sum_{j\ne i}s_{ij}^p.
\]

The weights \(s_{ij}^p=s_{ji}^p\) are strictly positive off the diagonal. The chain is irreducible (possibly periodic when \(m=2\)); its stationary distribution is

\[
 \pi_i(p)=\frac{d_i(p)}{2Z_p},\qquad
 \pi_i(p)P_{ij}(p)=\frac{s_{ij}^p}{2Z_p}.
\]

These equalities follow directly by substitution and establish detailed balance. Along every trajectory after the first step,

\[
 \log\|e_k\|_2=\log\|e_1\|_2+
 \sum_{t=1}^{k-1}\log c_{I_tI_{t+1}}.
\]

The strong law for additive functionals of finite irreducible Markov chains applies even in the two-state periodic case. The stationary directed-edge average is

\[
 \sum_i\pi_i\sum_jP_{ij}\log c_{ij}
 =\frac{1}{Z_p}\sum_{i<j}s_{ij}^p\log c_{ij}=\ell(p).
\]

Every \(c_{ij}<1\), so \(\ell(p)<0\). The transition statement, the rate, and almost-sure exponential convergence follow.

For monotonicity, take the probability measure \(q_{ij}(p)=s_{ij}^p/Z_p\) on unordered pairs. Differentiation gives

\[
 \ell'(p)=\operatorname{Cov}_{q(p)}(\log s_{ij},\log c_{ij}).
\]

Because \(s_{ij}^2+c_{ij}^2=1\) with both coordinates in \((0,1)\), \(\log c_{ij}\) is strictly decreasing as a function of \(\log s_{ij}\). The pairwise covariance identity

\[
 2\ell'(p)=\sum_{e,f}q_e(p)q_f(p)
 (\log s_e-\log s_f)(\log c_e-\log c_f)
\]

is therefore nonpositive, and strictly negative when any two pairwise angles differ. The maximum \(s_{ij}\) corresponds exactly to the minimum \(c_{ij}\); concentration of the finite positive weights \(s_{ij}^p\) as \(p\to\infty\) proves the greedy-exponent limit.

Under conventional \(p=0\) iid uniform sampling, the row chain has \(P_{ij}=1/m\), including \(P_{ii}=1/m\), and stationary distribution \(\pi_i=1/m\). A repeated row leaves the current error unchanged (\(\log c_{ii}=0\)), hence its exact stationary average is \(2m^{-2}\sum_{i<j}\log c_{ij}\). In contrast, for every \(p>0\), the already-satisfied row has exactly zero probability. Since \(s_{ij}^p\to1\) for each distinct pair as \(p\downarrow0\), its stationary directed-edge average tends to \(2/[m(m-1)]\sum_{i<j}\log c_{ij}\). These expressions prove the strict jump and its universal factor. \(\square\)

## Verification

Run \(\texttt{python3 VERIFY.py}\) with the Python standard library. The checker uses the unit rows

\[
 a_1=(1,0),\qquad a_2=(3/5,4/5),\qquad a_3=(5/13,12/13).
\]

The unordered edge data \((c_{ij},s_{ij})\) are exactly

\[
 (3/5,4/5),\quad(5/13,12/13),\quad(63/65,16/65).
\]

The script checks these by exact rational arithmetic, verifies the projection and detailed-balance identities, compares stationary edge and row averages at several integer exponents, checks endpoint limits and monotonicity numerically, and compares five simulated long paths with the analytic rates. Its output starts with \(\texttt{VERIFY_OK}\). As a reproducible numerical illustration, the rates for the three-row system are approximately \(\ell_{\mathrm{iid}}=-0.33279769\), \(\ell(0+)=-0.49919654\), \(\ell(2)=-0.73614548\), and \(\ell(\infty)=\log(5/13)=-0.95551145\). Simulations and finite checks are not the proof of the infinite-step limits.

## Relationship to prior work

The residual-power sampling rule is classical: Steinerberger's 2020 preprint studies the weighted randomized Kaczmarz method and a monotone family of worst-case expected-error bounds, while Zhang, Yuan, Wang and Zhang's 2023 paper extends residual-power sampling to sparse Bregman Kaczmarz and proves expected Bregman-distance bounds. The present theorem concerns ordinary orthogonal row projections, not sparse Bregman projections, and computes the **actual almost-sure** asymptotic rate for every planar row arrangement under the stated genericity hypotheses. The monotonicity of the published *bounds* does not determine this pathwise rate or its exact zero-power limit.

Gower, Molitor, Moorman and Needell's adaptive sketch-and-project paper already observes that the most recently satisfied sketched equation has zero residual and uses this for improved expected-error guarantees. That observation is prior work, not claimed here as new. The additional assertion here is the reversible finite-state reduction, closed-form pairwise angular exponent, strict all-power ordering, and sharp universal \(p\downarrow0\) rate jump. Because generic probability limits and long-time limits need not commute, a statement that the rule approaches uniform sampling for the first step does not establish equality of its long-run rates.

## Limitations

The formula is specific to a consistent two-unknown system with pairwise nonparallel and nonorthogonal normalized row lines; it does not cover general dimensions, incompatible data, soft-thresholded sparse Bregman projections, or a row pair whose angle is exactly right. It describes typical-path norm decay, **not** the decay rate of expected squared error, high-probability finite-time bounds, or flop costs. Finite precision, tolerances and residual regularization may turn an exactly zero residual into a small positive one and eliminate the precise discontinuity. The generic starting-error restriction deliberately excludes positive-probability exact termination at the first step. No independence of external scientific review is asserted.

## References

1. L. Zhang, Z. Yuan, H. Wang, H. Zhang, *A Weighted Randomized Sparse Kaczmarz Method for Solving Linear Systems*, arXiv:2306.06813, first posted 2023-06-12. https://arxiv.org/abs/2306.06813
2. S. Steinerberger, *A Weighted Randomized Kaczmarz Method for Solving Linear Systems*, arXiv:2007.02910, first posted 2020-07-06. https://arxiv.org/abs/2007.02910
3. R. M. Gower, D. Molitor, J. Moorman, D. Needell, *Adaptive Sketch-and-Project Methods for Solving Linear Systems*, arXiv:1909.03604, first posted 2019-09-09. https://arxiv.org/abs/1909.03604
