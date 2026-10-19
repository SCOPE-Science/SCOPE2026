# Sharp spectral-decay threshold for one-probe log-determinant estimation

## Finding

For the ideal spectral-deflation/Gaussian-trace model defined below, the following is a sharp *uniform allocation theorem*. Let \(c\geq1\) be an integer cost per exact trace probe, and suppose the ordered log-eigenvalues obey \(0\leq a_{j+1}\leq q a_j\) for a common \(0<q<1\). Subject to a fixed integer budget \(B\), allocating the budget to the largest possible ideal deflation rank and **one** Gaussian probe minimizes mean-square error for every finite positive-semidefinite input with this decay constraint whenever

\[
q\leq 2^{-1/(2c)}.
\]

This threshold is best possible uniformly over finite dimensions and spectra: for every larger \(q\), some finite geometric log-spectrum and a budget admitting two probes make the two-probe estimator strictly more accurate. In the infinite trace-class geometric model, the exact optimal number of probes is an explicit budget-truncated integer depending only on \(q\) and \(c\), while for polynomial log-spectrum \(a_j=L j^{-p}\) with \(p>1\), the asymptotically optimal probe count occupies the fraction \(1/(2pc)\) of the budget. These statements optimize *within the specified ideal estimator family*, not among arbitrary randomized trace algorithms.

## Assumptions and scope

Let \(d\geq2\), and let \(A\in\mathbb R^{d\times d}\) be real symmetric positive semidefinite with eigenvalues \(\lambda_1\geq\cdots\geq\lambda_d\geq0\), eigenvectors \(u_j\), and log-eigenvalues \(a_j=\log(1+\lambda_j)\). For \(0\leq k\leq d\), define the *ideal* spectral preconditioner and its transformed matrix by

\[
P_k=I+\sum_{j=1}^k\lambda_j u_ju_j^{\mathsf T},\qquad
M_k=P_k^{-1/2}(I+A)P_k^{-1/2}.
\]

For independent standard Gaussian vectors \(w_1,\ldots,w_N\in\mathbb R^d\), with \(N\geq1\) an integer, form

\[
\widehat L_{k,N}=\log\det P_k+
 \frac1N\sum_{i=1}^N w_i^{\mathsf T}(\log M_k)w_i.
\]

All logarithmic quadratic forms are computed *exactly*. The idealized cost is defined to be one unit per deflated eigenpair and \(c\geq1\) units per quadratic-form evaluation. For a budget \(B\geq c\) with \(B-c<d\), the admissible allocations are \(N=1,\ldots,\lfloor B/c\rfloor\), with \(k_N=B-cN\). Thus every allocation uses the entire assumed budget, and every \(k_N<d\). The cost convention is a model parameter, not a guarantee about real eigensolvers, Nyström preconditioners, or a fixed-step Lanczos approximation.

Write \(S(k)=\sum_{j=k+1}^d a_j^2\) and \(\mathcal V_N=\mathbb E(\widehat L_{k_N,N}-\log\det(I+A))^2\). In particular, if \(B=c\), there is only one admissible allocation. The nontrivial comparison assumes \(B\geq2c\).

For the separate infinite-spectrum examples, let the positive trace-class diagonal operator have eigenvalues \(\lambda_j=e^{a_j}-1\), and define the Gaussian quadratic form directly as the almost-sure convergent sum of independent \(a_jZ_{ij}^2\). An infinite-dimensional standard Gaussian vector in the Hilbert space is **not** assumed to exist.

## Proof

**1. Exact mean-square error.** Orthogonal diagonalization gives

\[
\log M_k=\sum_{j>k}a_j u_ju_j^{\mathsf T},\quad
\widehat L_{k,N}-\log\det(I+A)=\frac1N\sum_{i=1}^N\sum_{j>k}a_j(Z_{ij}^2-1),
\]

where the \(Z_{ij}\) are independent standard normal variables. Because \(\mathbb E(Z^2-1)=0\) and \(\mathbb E(Z^2-1)^2=2\), all cross terms vanish and

\[
\boxed{\mathcal V_N=\frac{2S(B-cN)}{N}.}
\]

The same identity holds for the two infinite trace-class examples by \(L^2\) convergence of the centered sums.

**2. Universal sharp one-probe threshold.** Suppose \(a_{j+1}\leq q a_j\) for every valid index. For each nonnegative integer \(h\) and any \(k\) with \(k+h<d\), termwise comparison after shifting by \(h\) gives

\[
S(k+h)=\sum_{j=k+h+1}^d a_j^2
\leq q^{2h}\sum_{j=k+1}^{d-h}a_j^2
\leq q^{2h}S(k).
\]

Taking \(h=c(N-1)\), \(k=B-cN\), and dividing the exact variances proves the sharp useful inequality

\[
\boxed{\frac{\mathcal V_1}{\mathcal V_N}\leq Nq^{2c(N-1)}}
\]

when \(\mathcal V_N>0\); when it is zero, both numerator and denominator vanish and the undivided inequality holds. If \(q^{2c}\leq1/2\), the elementary inequality \(N\leq2^{N-1}\) shows \(\mathcal V_1\leq\mathcal V_N\) for *every* admissible \(N\). For finite \(d\), the comparison is strict for all \(N>1\) if the one-probe residual is nonzero, even at equality of the decay threshold, because the final shifted sum omits at least one positive starting term.

To prove optimality of the threshold, fix any \(q>2^{-1/(2c)}\), take \(B=2c\) and finite \(d>c\), and set \(a_j=Lq^{j-1}\) with \(L>0\). This is realized by the finite PSD diagonal matrix \(\lambda_j=e^{a_j}-1\). Only \(N=1,2\) are feasible. Direct geometric summation yields

\[
\frac{\mathcal V_1}{\mathcal V_2}
=2q^{2c}\frac{1-q^{2(d-c)}}{1-q^{2d}}
\longrightarrow 2q^{2c}>1 \qquad(d\to\infty).
\]

Thus some sufficiently large but *finite* dimension makes two probes strictly better; there is no larger universal \(q\) threshold.

**3. Complete geometric allocation law.** For the infinite trace-class log-spectrum \(a_j=Lq^{j-1}\), the exact risk is

\[
\mathcal V_N=\frac{2L^2 q^{2(B-cN)}}{N(1-q^2)}.
\]

Set \(r=q^{2c}\in(0,1)\), \(H=r/(1-r)\), and \(N_{\max}=\lfloor B/c\rfloor\). Consecutive risks obey

\[
\frac{\mathcal V_{N+1}}{\mathcal V_N}=\frac{N}{r(N+1)}.
\]

They fall until \(N\) crosses \(H\), and thereafter rise. Consequently, a minimizing allocation is

\[
\boxed{N_*=\min\{N_{\max},\max\{1,\lceil H\rceil\}\}.}
\]

If \(H\) is a positive integer and \(H+1\leq N_{\max}\), then \(H+1\) is a second, equally good optimizer; otherwise the optimizer is unique. This is exact in the infinite trace-class example. Finite geometric matrices converge to this risk profile as their dimension grows with \(B\) fixed.

**4. Polynomial-tail allocation law.** For \(a_j=Lj^{-p}\), \(p>1\), let \(B\to\infty\) through integers and choose any exact-risk-minimizing feasible \(N_B\); put \(k_B=B-cN_B\). The integral test implies

\[
\sum_{j>k}j^{-2p}\sim\frac{k^{1-2p}}{2p-1}
\qquad(k\to\infty).
\]

For sequences with \(k/B\to x\in(0,1)\), the scaled risk converges uniformly on compact interior sets to

\[
B^{2p}\mathcal V_N\longrightarrow
\frac{2cL^2}{2p-1}\,\frac{x^{1-2p}}{1-x}.
\]

Near \(x=0\), the integral lower bound for the tail forces the scaled risk to diverge; near \(x=1\), the vanishing number of probes does the same. Thus minimizers stay in an interior compact interval. Differentiating the displayed positive function gives its unique minimum at \(x=(2p-1)/(2p)\), proving

\[
\boxed{\frac{k_B}{B}\longrightarrow\frac{2p-1}{2p},\qquad
\frac{N_B}{B}\longrightarrow\frac{1}{2pc}.}
\]

The resulting optimal risk has the exact leading asymptotic

\[
\boxed{\min_N\mathcal V_N\sim
 \frac{4pcL^2}{2p-1}\left(\frac{2p}{2p-1}\right)^{2p-1}B^{-2p}.}
\]

All limits are in the defined ideal model and do not assert a finite-step Lanczos quadrature error estimate.

## Verification

Run `python verify.py` using Python 3 and only the standard library. The program directly checks 6,125 exact rational finite-spectrum inequalities, 24 finite strict-threshold counterexamples, 1,020 infinite-geometric discrete optimizer identities, 32 large-budget power-law optimizer approximations, and four independent Gaussian-moment simulations (7,205 checks in total). It reports its counts when successful. Its polynomial quadrature is a high-order numerical approximation used solely for finite tests; the asymptotic theorem follows from the integral test. The script uses deterministic random seeds and includes all inputs and tolerances. Finite tests cannot prove the universal ratio bound, the sharp all-dimension threshold, or the infinite-budget laws; those statements are covered by the preceding arguments.

## Relationship to prior work

Cortinovis and Toni (arXiv:2601.05778v1, first public 2026-01-09) develop one-sample preconditioned log-determinant estimation and analyze exactly the *idealized* residual Gaussian trace risk. Their equations (8) and (10) give the spectral risk formula for one and multiple probes, and equation (11) is a pairwise condition for choosing an allocation. Those identities are *prior work* and are not the novelty claimed here. The contribution is the sharp universal adjacent-log-spectrum threshold that resolves **all allocations simultaneously**, its finite-dimensional necessity witness, and the complete geometric/polynomial optimal-allocation regimes under explicit costs. The source's main practical method uses random Nyström subspaces rather than exact spectral deflation, so these idealized guarantees must not be transferred to that method without further analysis.

Epperly, Tropp, and Webber (arXiv:2301.07825) study exchangeable stochastic trace estimators such as XTrace and XNysTrace under fixed budgets; these are different estimators and may outperform the restricted family examined here. Saibaba, Alexanderian, and Ipsen (arXiv:1605.04893) analyze randomized matrix-free trace and log-determinant approximation using subspace iteration, with different approximation mechanisms and error criteria. Related general trace estimators do not by themselves give the sharp optimal allocation within the precisely defined ideal spectral-deflation family. No claim of global estimator optimality is made.

## Limitations

The cost model assigns one unit per *exactly known* spectral component and \(c\) units per *exact* Gaussian logarithmic quadratic form. In a real application spectral subspaces are unknown, randomized Nyström compression has additional error, and Lanczos quadrature introduces truncation and rounding errors. None of those effects is included. The sharp one-probe statement concerns only nonnegative ordered log-eigenvalues with a uniform adjacent-ratio envelope, and mean-square error; it is not a high-probability guarantee. The illustrative power-law and geometric infinite spectra are trace-class idealizations. No external independent scientific validation is asserted.

## References

1. A. Cortinovis and D. Toni, *Preconditioned log-determinant approximation: one Gaussian probe vector is almost always enough*, arXiv:2601.05778v1, first public January 9, 2026. https://arxiv.org/abs/2601.05778
2. E. N. Epperly, J. A. Tropp, and R. J. Webber, *XTrace: Making the most of every sample in stochastic trace estimation*, arXiv:2301.07825, 2023. https://arxiv.org/abs/2301.07825
3. A. K. Saibaba, A. Alexanderian, and I. C. F. Ipsen, *Randomized Matrix-free Trace and Log-Determinant Estimators*, arXiv:1605.04893, first public May 16, 2016. https://arxiv.org/abs/1605.04893
