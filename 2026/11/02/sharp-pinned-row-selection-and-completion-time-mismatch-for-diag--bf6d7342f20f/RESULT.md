# Sharp pinned-row selection and completion-time mismatch for diagonal randomized Kaczmarz

## Finding

For exact subspace-constrained randomized Kaczmarz applied to a positive diagonal system, the optimal fixed row constraints for the **sharp worst-case expected squared-error rate** can be selected by a consecutive-window scan of the ordered squared row magnitudes. A row-interpolative-decomposition/Frobenius-norm selection rule may have arbitrarily poorer rate, and the set that minimizes the sharp error rate need not minimize the expected time until the complete solution is reached.

More precisely, fix integers \(n\ge3\) and \(2\le k\le n-1\), positive real weights \(0<w_1\le\cdots\le w_n\), and the system \(A x=b\) with \(A=\operatorname{diag}(\sqrt{w_1},\ldots,\sqrt{w_n})\). Choose any set \(R\subseteq\{1,\ldots,n\}\) of \(k\) unpinned rows and pin the remaining rows to their exact solution values. Set \(S_R=\sum_{i\in R}w_i\). Independently at each step, draw one \(i\in R\) with probability \(p_i=w_i/S_R\) and carry out the exact projected Kaczmarz correction on that row. For every integer \(t\ge0\) and every initial error \(e^0\) vanishing on the pinned coordinates,

\[
\mathbb E\|e^t\|_2^2=\sum_{i\in R}|e_i^0|^2(1-p_i)^t.
\]

For every integer \(t\ge1\), the sharp worst-case factor is \(\rho_R^t\), where

\[
\rho_R=1-\frac{\min_{i\in R}w_i}{S_R}.
\]

The optimal value over all fixed sets of size \(k\) is exactly

\[
\boxed{\rho_*=1-\max_{1\le j\le n-k+1}\frac{w_j}{w_j+w_{j+1}+\cdots+w_{j+k-1}}.}
\]

A block \(R=\{j,j+1,\ldots,j+k-1\}\) attaining the displayed maximum is optimal. If all weights are strictly increasing, **every** optimal set is such a consecutive block. This is a worst-case error criterion, not an assertion about every particular initial error.

For any choice of \(R\), let \(T_R\) be the first step by which every unpinned row has been sampled at least once. If every unpinned initial error is nonzero, this is exactly the first finite step at which the algorithm reaches the solution. For each nonnegative integer \(t\),

\[
\mathbb P(T_R\le t)=\sum_{J\subseteq R}(-1)^{|J|}\left(1-\frac{\sum_{i\in J}w_i}{S_R}\right)^t,
\]

and

\[
\boxed{\mathbb E T_R=\sum_{\varnothing\ne J\subseteq R}(-1)^{|J|+1}\frac{S_R}{\sum_{i\in J}w_i}.}
\]

The two natural selection criteria differ already for \(n=4\), \(k=3\), and the squared row magnitudes \((2,3,6,8)\). Rate minimization uniquely retains weights \((2,3,6)\), with \(\rho=9/11\) and \(\mathbb E T=2593/360\). Expected completion-time minimization uniquely retains \((3,6,8)\), with \(\rho=14/17\) and \(\mathbb E T=38677/5544\). In particular, the better worst-case contraction factor gives the **larger** expected number of steps to full finite completion.

Finally, for \(n=3\), \(k=2\), and weights \((\varepsilon^2,1,4)\) with \(0<\varepsilon<1/2\), the unique rate-optimal choice pins the \(\varepsilon\)-magnitude row, yielding \(\rho_*=4/5\). The row-interpolative/Frobenius rule, including its exact largest-row CPQR implementation on this diagonal matrix, instead pins the row of magnitude \(2\), yielding \(\rho_{\rm ID}=1/(1+\varepsilon^2)\). The ratio of their sharp one-step improvement fractions is

\[
\boxed{\frac{1-\rho_*}{1-\rho_{\rm ID}}=\frac{1+\varepsilon^2}{5\varepsilon^2}\longrightarrow\infty\quad(\varepsilon\downarrow0).}
\]

Thus the Frobenius surrogate has no uniform multiplicative approximation guarantee for this specific convergence-rate objective, even on invertible diagonal systems.

## Assumptions and scope

All quantities are real and all diagonal entries are strictly positive. Computations are in exact arithmetic, with exact pinned equations and a consistent system. The constraint set is chosen once, before independent fixed-probability sampling begins. The scheme is the classical *unconditional* fixed-probability, nonaccelerated, exact-projection subspace-constrained randomized Kaczmarz update (as in Lok--Rebrova Algorithm 1): a draw of an already satisfied row counts as a null step. In contrast, Sun et al. Algorithm 1 explicitly rejects zero-residual draws, so this theorem does **not** describe its number of accepted updates, which on a diagonal system is at most \(k\). It also does not describe an orthogonalized Krylov variant or adaptive residual-weighted sampling. Row-selection setup cost, noise sensitivity and pseudoinverse conditioning are excluded from the convergence-rate objective. For the finite-completion interpretation of \(T_R\), each unpinned initial coordinate error must be nonzero; the coupon-collection identity itself holds without that assumption.

## Proof

**Exact error law.** For a diagonal matrix, the orthogonal projector onto the nullspace of the pinned rows is the coordinate projector supported on \(R\). When row \(i\in R\) is drawn, exact Kaczmarz projection replaces the \(i\)-th coordinate by its exact solution value and leaves every other coordinate unchanged. If \(N_i(t)\) denotes the event that row \(i\) has not been drawn in the first \(t\) steps, then \(e_i^t=e_i^0\mathbf1_{N_i(t)}\) on \(R\), while all pinned errors vanish. Independence of the draws gives \(\mathbb P(N_i(t))=(1-p_i)^t\). Summing the coordinate squares proves the exact expectation formula. The expression is diagonal in the initial squared errors, so its supremum over unit initial errors is exactly the largest survival probability, \((1-\min_i p_i)^t\), achieved by an initial error supported on a least-weight unpinned coordinate. In particular, the rate is not merely a non-sharp upper bound.

**Complete minimax selection.** Let \(R=\{i_1<\cdots<i_k\}\) and write \(j=i_1\). Because the sorted weights satisfy \(w_{i_r}\ge w_{j+r-1}\) for all \(r\),

\[
\frac{\min_{i\in R}w_i}{S_R}=\frac{w_j}{\sum_{r=1}^k w_{i_r}}\le
\frac{w_j}{\sum_{r=0}^{k-1}w_{j+r}}.
\]

The right side is attained by the consecutive indices \(j,\ldots,j+k-1\); necessarily \(j\le n-k+1\). Maximizing over \(j\) proves the exact global formula. If the weights are strictly increasing and any \(i_r>j+r-1\), its inequality is strict, so nonconsecutive choices cannot be optimal. With equal weights, nonconsecutive ties may also attain the optimum, which explains the weaker existence statement in that case.

**Exact finite completion.** The event \(T_R>t\) is the union over \(i\in R\) of \(N_i(t)\). For a subset \(J\subseteq R\), the probability that no index in \(J\) has been sampled is \((1-\sum_{i\in J}p_i)^t\). Inclusion-exclusion gives the cumulative distribution. Summing \(\mathbb P(T_R>t)\) over \(t\ge0\), interchanging only finitely many subset terms with geometric series, yields the stated exact expectation. Positivity of all \(p_i\) ensures finite expectation.

**Exact separation of objectives.** For squared weights \((2,3,6,8)\), the four possible retained triples, their sharp factors and their exact expected completion times are:

| Retained weights | \(\rho_R\) | \(\mathbb E T_R\) |
|---|---|---|
| \((2,3,6)\) | \(9/11\) | \(2593/360\) |
| \((2,3,8)\) | \(11/13\) | \(11057/1320\) |
| \((2,6,8)\) | \(7/8\) | \(937/105\) |
| \((3,6,8)\) | \(14/17\) | \(38677/5544\) |

Direct comparison of these exact rational numbers gives different unique minimizers. The exact checker also recomputes all four values from the defining finite subset sum; no simulation is needed.

**Unbounded surrogate loss.** For \(0<\varepsilon<1/2\), the retained pair \((1,4)\) has improvement fraction \(1/5\), whereas pairs \((\varepsilon^2,1)\) and \((\varepsilon^2,4)\) have fractions \(\varepsilon^2/(1+\varepsilon^2)\) and \(\varepsilon^2/(4+\varepsilon^2)\), both strictly smaller. Thus pinning the smallest row is the unique rate minimizer. Minimizing the remaining Frobenius norm for a single pinned diagonal row pins the largest squared row magnitude \(4\), as does exact row CPQR. The resulting improvement fraction is \(\varepsilon^2/(1+\varepsilon^2)\). Their ratio is the displayed divergent expression. For any fixed target fractional worst-case squared error \(r\in(0,1)\), the surrogate needs \(\lceil\log(r)/\log(1/(1+\varepsilon^2))\rceil=\Theta(\varepsilon^{-2})\) samples, whereas the optimal pinning needs \(\lceil\log(r)/\log(4/5)\rceil\) samples, independent of \(\varepsilon\).

## Verification

The independent-of-the-proof standalone exact-rational checker `verify.py` uses finite exhaustive subsets, all nondecreasing integer weight profiles up to seven dimensions, explicit enumeration of independent sampling sequences for short horizons, and direct exact rational calculations for the two distinguishing examples. Command: `python verify.py`. It reported **15,133 exact-rational assertions passed**. These checks corroborate the formulas and boundary comparisons; the arbitrary-dimension and all-time statements follow from the preceding proof rather than finite enumeration.

## Relationship to prior work

Sun, Qi, Han and Xie (2026), Section 3.2 and Lemma 3.5, motivate optimizing a reduced singular-value convergence factor but propose a Frobenius residual / row interpolative decomposition surrogate for feasible selection. The theorem uses the same fixed-row, squared-projected-row-norm sampling distribution, but counts all iid draws, including those selecting already solved equations. Sun et al. Algorithm 1 rejects zero-residual samples, so the unbounded-iteration comparison applies to the *unconditional* SCRK convention and to the general geometric rate-surrogate objective, **not** to the count of Sun et al. accepted updates. It **does not contradict** the source convergence results, which make no universal surrogate approximation claim. Lok and Rebrova (2023), Algorithm 1 and Section 3.3, formulate the constrained Kaczmarz update and explain why chosen rows can improve convergence. Strohmer and Vershynin (2007) establish the classical randomized Kaczmarz exponential bound. Anceaume, Busnel and Sericola (2014), together with Anceaume, Busnel, Schulte-Geers and Sericola (2015), give more general unequal-probability coupon-collector distribution and optimization results, including that freely chosen uniform probabilities optimize collection time. Our inclusion-exclusion formula is classical and is not a novelty claim; the new selection comparison fixes probabilities through the retained row magnitudes and varies the set of pinned equations.

The all-dimension consecutive-window formula and the exact disagreement between asymptotic-rate and finite-completion objectives are not asserted to be independent of all existing order-statistic or coupon-collector literature. A more general prior result on normalized-weight subset optimization could subsume the simple consecutive-window argument; historical priority is not independently established.

## Limitations

The result is confined to exact diagonal systems with one-coordinate independent norm-squared sampling, including null draws, and exact fixed constraints. Conditional resampling of only unsolved rows removes the diagonal waiting-time phenomenon; in that different iteration-count convention all \(k\) unpinned equations are solved in exactly \(k\) accepted updates. Pinning a very small row may amplify data noise and incur an unfavorable setup cost; the divergent rate advantage is **not** a complete wall-clock or noisy inverse-problem comparison. The exact coupon-completion expectation applies when all unpinned coordinate errors initially are nonzero. The theorem does not address general nondiagonal matrices, nonuniform adaptive sampling, numerical roundoff, blocked or accelerated methods, nor claims about empirical time-to-accuracy across those settings.

## References

1. Y. Sun, H.-D. Qi, D. Han and J. Xie, *On subspace-constrained preconditioning for randomized iterative methods*, arXiv:2605.29304v1, first public 2026-05-28. https://arxiv.org/html/2605.29304v1
2. J. Lok and E. Rebrova, *A subspace constrained randomized Kaczmarz method for structure or external knowledge exploitation*, arXiv:2309.04889, first public 2023-09-09; revised 2024-06-07. https://arxiv.org/html/2309.04889v2
3. T. Strohmer and R. Vershynin, *A randomized Kaczmarz algorithm with exponential convergence*, arXiv:math/0702226, first public 2007-02-08. https://arxiv.org/abs/math/0702226
4. S. Steinerberger, *Randomized Kaczmarz converges along small singular vectors*, arXiv:2006.16978, first public 2020-06-30. https://arxiv.org/abs/2006.16978
5. E. Anceaume, Y. Busnel and B. Sericola, *New results on a generalized coupon collector problem using Markov chains*, arXiv:1402.5245, 2014. https://arxiv.org/abs/1402.5245
6. E. Anceaume, Y. Busnel, E. Schulte-Geers and B. Sericola, *Optimization results for a generalized coupon collector problem*, arXiv:1504.03878, 2015. https://arxiv.org/abs/1504.03878
