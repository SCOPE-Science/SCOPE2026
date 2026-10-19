# Sharp rank-band amplification in small-sample quantile Kaczmarz

## Finding

Consider the small-sample, rank-selected quantile randomized Kaczmarz rule: at a fixed iterate, sample \(k\) distinct rows uniformly without replacement and project onto the row with the \(p=k/2\)-th smallest absolute residual, for even \(k\). This is the rank-selection variant of subsampled quantile Kaczmarz, not the separate rule that tests an independently selected row against a quantile threshold.

For \(m\ge k\), with distinct residuals sorted in increasing order and \(p=k/2\), the exact probability of selecting population residual rank \(i\) is
\[
w_i=\frac{\binom{i-1}{p-1}\binom{m-i}{k-p}}{\binom{m}{k}},\qquad 1\le i\le m,
\]
where out-of-range binomial coefficients are zero. If an adversary can corrupt any \(c\) ranked rows, the *sharp* maximum one-step probability of selecting a corrupt row is
\[
W_{m,k,c}=\max_{0\le s\le m-c}\sum_{i=s+1}^{s+c}w_i.
\]
Thus a worst corrupt set may always be chosen as \(c\) consecutive *residual ranks*, not necessarily the largest residuals.

Let even \(k\to\infty\), \(m=k^3\), and let \(0\le c=c_k\le m-2\) be even, with \(c/m\to0\) and \(c\sqrt{k}/m\to\theta\in[0,\infty]\) (extended endpoint allowed). Then
\[
W_{m,k,c}\longrightarrow 2\Phi(\theta)-1,
\]
where \(\Phi\) is the standard normal distribution function and the value at \(\theta=\infty\) is \(1\). The profile is sharp in the class of full-column-rank, row-normalized real two-column linear systems with exactly \(c\) corrupted right-hand sides.

Indeed, there is an explicit such system, with true solution \(x^\star=0\) and initial \(x_0=(1,0)^\top\), whose first full Kaczmarz update \(x_1\) satisfies
\[
\lim_{k\to\infty}\mathbb E\|x_1-x^\star\|_2^2
=\frac34+\frac32[2\Phi(\theta)-1].
\]
The limiting expected squared error *increases* above its starting value \(1\) precisely when \(\theta>\Phi^{-1}(7/12)\approx0.2104283942\). In particular, one may take a vanishing corruption fraction \(c/m\asymp k^{-1/4}\), for which the probability of selecting a corrupt row tends to \(1\) and the expected squared error tends to \(9/4\).

## Assumptions and scope

All residuals are evaluated at the same fixed iterate and are pairwise distinct. Sampling is a uniform simple random subset of \(k\) of the \(m\) rows, with even \(k\), and the selected row is the lower sample median (rank \(k/2\) in ascending order). The corresponding quantile convention is \(q=1/2\) with rank \(\lfloor qk\rfloor\). A selected row is updated by its *ordinary*, unit-row Kaczmarz projection, without damping or rejection. The bound \(W_{m,k,c}\) is an exact one-step, fixed-residual-ranking statement. The asymptotic construction has \(m=k^3\), is deterministic apart from row sampling, and contains exactly \(c\) corrupted right-hand sides.

## Proof

**1. Exact finite selection law and extremality.** The sample median is rank \(i\) precisely if the sample contains row \(i\), exactly \(p-1\) rows of smaller rank, and exactly \(k-p\) rows of larger rank. Counting size-\(k\) subsets gives \(w_i\). These nonnegative weights sum to one. For supported neighboring ranks,
\[
\frac{w_{i+1}}{w_i}=
\frac{i(m-i-k+p)}{(i-p+1)(m-i)}.
\]
The ratio exceeds one exactly when \((p-1)(m-i)>i(k-p)\). Hence the weights first rise and then fall (allowing equality). The \(c\) largest weights can consequently be taken on an interval of \(c\) consecutive ranks. Any corruption set has selection probability equal to the sum of its \(c\) weights, proving the exact maximum \(W_{m,k,c}\).

**2. Gaussian rank-window limit.** Let \(J\) be the selected population rank. Couple the sample without replacement to \(k\) independent uniform draws from \(\{1,\ldots,m\}\); the probability of a collision in the latter is at most \(k(k-1)/(2m)=O(k^{-1})\) for \(m=k^3\). Under independent draws, the central order statistic obeys
\[
Y_k:=\sqrt{k}\left(\frac Jm-\frac12\right)
\ \Longrightarrow\ N(0,1/4).
\]
To see this directly, for fixed \(z\), the event \(Y_k\le z\) says that at least \(k/2\) draws lie below \(m/2+zm/\sqrt{k}\). The success probability is \(1/2+z/\sqrt{k}+O(1/m)\), and the binomial central limit theorem yields limiting distribution function \(\Phi(2z)\). The collision coupling transfers the limit to sampling without replacement.

Every block of \(c\) consecutive ranks represents a real interval of length \(c\sqrt{k}/m\) in the \(Y_k\) scale. Since the limiting normal CDF is continuous, convergence of the distribution functions is uniform. For finite \(\theta\), the maximal probability of any interval of length tending to \(\theta\) therefore tends to the maximum normal mass of an interval of length \(\theta\), attained when centered at zero:
\[
\sup_{a\in\mathbb R}\Pr\{a\le N(0,1/4)\le a+\theta\}
=2\Phi(\theta)-1.
\]
For \(\theta=0\), uniform continuity makes the maximum vanish; for \(\theta=\infty\), a centered block captures probability tending to one by tightness. This proves the envelope in all three regimes.

**3. Exact linear-system realization.** Set \(r_i=i/(m+1)\) and choose the *central* \(c=2h\) population ranks
\[
C=\{m/2-h+1,\ldots,m/2+h\},
\]
with \(C=\varnothing\) when \(c=0\). Define a unit row \(a_i\) and observed right-hand side \(b_i\) by
\[
(a_i,b_i)=\begin{cases}
((r_i,\sqrt{1-r_i^2}),0),&i\notin C,\\
((1,0),1+r_i),&i\in C.
\end{cases}
\]
The uncorrupted system has the exact solution \(x^\star=(0,0)^\top\), and \(b_i\ne0\) exactly on \(C\). As \(c\le m-2\), two distinct good rows exist and are not parallel; hence \(A\) has full column rank. At \(x_0=(1,0)^\top\), *every* absolute residual is exactly \(r_i\), increasing with \(i\). Therefore the selected row is indexed by \(J\) and the probability of a bad selection is \(\sum_{i\in C}w_i\). The symmetric central block captures asymptotically the maximum in step 2.

For any unit row, the projection update is \(x_1=x_0+(b_i-a_i^\top x_0)a_i\). An uncorrupted selection has
\[
\|x_1\|_2^2=1-r_i^2,
\]
whereas a corrupted selection has \(x_1=(1+r_i,0)^\top\) and
\[
\|x_1\|_2^2=(1+r_i)^2.
\]
The unconditional exact finite expectation is thus
\[
\sum_{i\notin C}w_i(1-r_i^2)
+\sum_{i\in C}w_i(1+r_i)^2
=1-\mathbb E[r_J^2]+\sum_{i\in C}w_i(2r_i+2r_i^2).
\]
The median rank satisfies \(r_J\to1/2\) in probability; boundedness gives \(\mathbb E[r_J^2]\to1/4\). On the central corrupted block \(\max_{i\in C}|r_i-1/2|\to0\), so its premium tends to \((3/2)[2\Phi(\theta)-1]\). This gives the stated error limit and the exact critical threshold. For instance \(c/m\asymp k^{-1/4}\) yields \(c\sqrt{k}/m\to\infty\) while \(c/m\to0\).

## Verification

Run `python verify.py` with Python 3 standard library only. The script enumerates simple random subsets, checks the exact weight formula, verifies the sample-rank mean and variance formulas, exhaustively compares the interval maximizer against all marked rank sets in small finite cases, and checks the exact Kaczmarz error decomposition with rational arithmetic. It also evaluates finite-population hypergeometric probabilities for increasing even sample sizes against the predicted Gaussian profile. The enumeration is finite diagnostic evidence, not the proof of the asymptotic statement; that proof is in the preceding section.

## Relationship to prior work

Haddock, Ma and Rebrova [1], Section V-D and Algorithm 2, propose selecting the sampled quantile row for small sample size and discuss its behavior heuristically. Their Theorem 1 instead treats a subset of size proportional to the entire equation count. The present theorem gives the exact one-step worst-case contamination envelope for the small-sample rank-selection variant and a sharp vanishing-corruption asymptotic, rather than a global convergence guarantee.

Haddock, Needell, Rebrova and Swartworth [2] and Steinerberger [3] study quantile *thresholding* with different update-row selection, and their convergence guarantees impose additional matrix and sampling conditions. Cai, Chen, Ma and Wu [4] later prove finite-horizon subsampling guarantees, but their Algorithm 1.1 tests an independently drawn update row against the subsampled quantile; it is not the rank-selected update analyzed here. Its random-matrix hypotheses also exclude the constructed adversarial row geometry. The binomial central limit theorem and finite-population order-statistic counting used in the proof are classical; novelty is not claimed for those tools themselves.

## Limitations

The instability is a *one-step* counterexample from a deliberately chosen iterate and matrix, not a proof of almost-sure or long-run divergence. It does not contradict positive convergence results under isotropic random-row assumptions or different quantile-thresholding rules. It assumes distinct residuals, uniform subset sampling without replacement, even sample size, and unit rows. The Gaussian phase limit uses the specified joint size scaling; its finite-count probability formula holds for arbitrary admissible finite dimensions. Independent mathematical validation has not been performed, and equivalent formulations outside the searched literature remain a possible originality risk.

## References

[1] J. Haddock, A. Ma, E. Rebrova, *On Subsampled Quantile Randomized Kaczmarz*, arXiv:2308.07987v1, first posted 2023-08-15, Sections III and V-D. https://arxiv.org/abs/2308.07987

[2] J. Haddock, D. Needell, E. Rebrova, W. Swartworth, *Quantile-based Iterative Methods for Corrupted Systems of Linear Equations*, arXiv:2009.08089, first posted 2020-09-17. https://arxiv.org/abs/2009.08089

[3] S. Steinerberger, *Quantile-Based Random Kaczmarz for corrupted linear systems of equations*, arXiv:2107.05554, first posted 2021-07-12. https://arxiv.org/abs/2107.05554

[4] J.-F. Cai, J. Chen, A. Ma, T. Wu, *On the Subsample Size of Quantile-Based Randomized Kaczmarz*, arXiv:2507.15185v2, first posted 2025-07-21. https://arxiv.org/abs/2507.15185
