# Exact memory amplification of edge-count fluctuations in Pólya threshold graphs

## Finding
For every fixed integer memory length \(M\ge1\) and positive urn parameters \(a,b\), the edge count \(E_n\) of the stationary finite-memory Pólya threshold graph on \(n\) vertices satisfies
\[
\frac{E_n-\rho n(n-1)/2}{n^{3/2}}
\;\Longrightarrow\;
N\!\left(0,\frac{\rho(1-\rho)}3
\frac{(M+\kappa)(M+\kappa+1)}{\kappa(\kappa+1)}\right),
\quad\rho=\frac a{a+b},\quad \kappa=a+b.
\]
Furthermore,
\[
\lim_{n\to\infty}\frac{\operatorname{Var}(E_n)}{n^3}
=\frac{\rho(1-\rho)}3\frac{(M+\kappa)(M+\kappa+1)}{\kappa(\kappa+1)}.
\]
Thus the exact integrated-correlation multiplier is \(\tau_M=(M+\kappa)(M+\kappa+1)/(\kappa(\kappa+1))\). It grows quadratically, not linearly, with memory length. This growth concerns the *fixed-memory asymptotic variance coefficient*, with the graph-size limit taken first; it does not assert a central limit theorem uniform in growing \(M\).

For each fixed \(M\), \(E_n/n^2\to\rho/2\) almost surely. In the corresponding infinite-memory Pólya construction, \(E_n/n^2\to\Theta/2\) almost surely, where \(\Theta\) has the \(\operatorname{Beta}(a,b)\) law. The latter is random when \(a,b>0\), distinguishing the limiting fluctuation scales. If the last graph vertex is forced to be universal to ensure connectivity, the same displayed central limit theorem and variance coefficient hold.

## Assumptions and scope
The initial two-color urn has \(R>0\) red balls, \(B>0\) black balls, and adds \(\Delta>0\) balls matching a draw, removing those added exactly \(M\) draws afterward. Put \(a=R/\Delta\) and \(b=B/\Delta\), allowing any positive real parameters. Its binary outputs \(Z_j\) satisfy
\[
\Pr(Z_j=1\mid Z_1,\ldots,Z_{j-1})
=\begin{cases}
\dfrac{a+\sum_{i<j}Z_i}{a+b+j-1},&j\le M,\\[4pt]
\dfrac{a+\sum_{i=j-M}^{j-1} Z_i}{a+b+M},&j>M.
\end{cases}
\]
The finite-memory process begins with the ordinary \(M\)-draw Pólya law, not a deterministic atypical initial window. A threshold graph is built by giving every vertex \(j\in\{2,\ldots,n\}\) edges to all \(j-1\) previous vertices if and only if \(Z_j=1\); hence \(E_n=\sum_{j=2}^n(j-1)Z_j\). All limits in the Gaussian statement hold as \(n\to\infty\) with \(M,a,b\) fixed.

## Proof
**Stationarity.** Write \((u)_r=u(u+1)\cdots(u+r-1)\). The initial window distribution is
\[
\pi(z_1,\ldots,z_M)
=\frac{(a)_{s}(b)_{M-s}}{(a+b)_M},\qquad s=\sum_{i=1}^M z_i.
\]
It is the marginal of an exchangeable Bernoulli mixture with \(\Theta\sim\operatorname{Beta}(a,b)\). Appending a draw according to the displayed \(M\)-step predictive probability yields the same joint law as the first \(M+1\) members of this mixture. Removing the oldest of these \(M+1\) coordinates therefore preserves \(\pi\). Thus the shift-register chain on \(\{0,1\}^M\) is stationary. Since every binary output has strictly positive conditional probability, every state communicates with every other in at most \(M\) shifts; the all-zero state has a self-loop. The finite chain is consequently irreducible and aperiodic, hence exponentially mixing and ergodic.

**Exact integrated covariance.** Put \(v=\rho(1-\rho)\) and \(c_h=\operatorname{Cov}(Z_1,Z_{1+h})\). Stationarity and the length-\((M+1)\) beta-mixture representation give
\[
c_0=v,\qquad c_h=\frac{v}{\kappa+1}\quad(1\le h\le M).
\]
The conditional expectation for the most recent window and the Markov property imply, for all \(h\ge M+1\),
\[
c_h=\frac1{M+\kappa}\sum_{j=1}^M c_{h-j}.
\]
Exponential mixing implies absolute convergence of \(S=\sum_{h=1}^\infty c_h/v\). Summing the last recurrence over \(h\ge M+1\), and subtracting the \(M(M-1)/2\) missing low-lag terms, gives
\[
S-\frac{M}{\kappa+1}
=\frac{MS-M(M-1)/(2(\kappa+1))}{M+\kappa}.
\]
Solving,
\[
S=\frac{M(M+2\kappa+1)}{2\kappa(\kappa+1)},\qquad
\frac{c_0+2\sum_{h\ge1}c_h}{v}
=1+2S=\tau_M
=\frac{(M+\kappa)(M+\kappa+1)}{\kappa(\kappa+1)}.
\]
Every coefficient is finite and strictly positive.

**Weighted Markov central limit theorem.** The stationary irreducible aperiodic finite-state shift chain, observed through its newest binary coordinate, obeys the functional central limit theorem
\[
n^{-1/2}\sum_{j=1}^{\lfloor nt\rfloor}(Z_j-\rho)
\;\Longrightarrow\;\sqrt{v\tau_M}\,B(t),\qquad0\le t\le1,
\]
where \(B\) is standard Brownian motion. The variance coefficient is the absolutely summable covariance series just evaluated. Summation by parts applied to \(E_n-\mathbb EE_n=\sum_{j=2}^n(j-1)(Z_j-\rho)\) gives convergence of its \(n^{-3/2}\)-normalization to \(\sqrt{v\tau_M}\int_0^1t\,dB(t)\). The Gaussian stochastic integral has variance \(v\tau_M\int_0^1t^2\,dt=v\tau_M/3\), proving the asserted weak limit.

To establish the separate variance limit, expand the variance as
\[
\operatorname{Var}(E_n)
=c_0\sum_{j=1}^{n-1}j^2
+2\sum_{h=1}^{n-2}c_h\sum_{j=1}^{n-h-1}j(j+h).
\]
For each fixed \(h\), the inner sum divided by \(n^3\) tends to \(1/3\), and its absolute value is uniformly bounded by a constant times \(n^3\). Dominated convergence using \(\sum_h|c_h|<\infty\) yields \(n^{-3}\operatorname{Var}(E_n)\to(c_0+2\sum_{h\ge1}c_h)/3=v\tau_M/3\).

**Limits and connectivity.** Ergodicity and weighted summation imply \(E_n/n^2\to\rho/2\) almost surely for fixed \(M\). In the infinite-memory construction, de Finetti's beta mixing and the conditional strong law imply \(E_n/n^2\to\Theta/2\). Finally, replacing \(Z_n\) by \(1\) changes the edge count by \((n-1)(1-Z_n)\), bounded deterministically by \(n-1\). This perturbation is negligible on the \(n^{3/2}\) scale and changes the variance by \(o(n^3)\): its variance is \(O(n^2)\), while Cauchy–Schwarz bounds the cross term by \(O(n^{5/2})\) using the already established \(O(n^3)\) original variance. These observations prove the connected-graph extension.

## Verification
The standalone `verify.py` evaluates the finite-state shift-register Markov chain with exact rational arithmetic, checks its beta-binomial invariant law, solves its Poisson equation, and compares the exact long-run variance with \(v\tau_M\) for eight parameter sets. It also exhaustively enumerates binary histories and compares their exact finite-graph means and variances with the covariance formula in 34 cases. All 42 checks pass. The finite computations are corroboration only; the infinite statements follow from the displayed covariance-summation proof and the finite-state functional central limit theorem. Run `python -m pip install -r requirements.txt` and `python verify.py`.

## Relationship to prior work
Yu, Alajaji and Gharesifard introduce Pólya threshold graphs (arXiv:2603.18452, first available March 19, 2026), including the finite-memory urn variant and simulations of its effect on consensus. Their inspected finite-memory section does not give this edge-count central limit theorem or an explicit quadratic memory amplification factor. The stationary finite-memory Pólya/contagion mechanism was previously studied by Alajaji and Fuja, and by Zhong, Alajaji and Takahara. Mori, Hisakado and Nakayama (arXiv:2105.10653) also explicitly include finite rectangular memory kernels and a general autocorrelation self-consistency recursion. In particular, the latter's equivalent uniform-queue model provides an autocorrelation *recurrence*, so neither that recurrence nor the stationarity of the finite-memory urn is claimed as new. Here the recurrence is summed to an exact integrated-covariance closed form and transferred to a weighted graph statistic, yielding its explicit Gaussian limit, variance asymptotic, and distinction from the infinite-memory law.

## Limitations
The central limit theorem treats each fixed finite \(M\), not a triangular array with \(M=M_n\) growing. The exact quadratic growth of the variance coefficient after the \(n\)-limit does not establish an intervening joint crossover law. The proof covers undirected unweighted threshold-graph edge count under the specified stationary urn initialization; it does not establish new vertex-degree or spectral limit theorems. The general finite-state Markov central limit theorem and stationary beta-mixture facts are used as established tools. Although comparisons did not locate prior published coverage of the combined graph-statistic result, equivalent formulations in older queue or communication-channel work remain a priority risk.

## References
1. J. Yu, F. Alajaji and B. Gharesifard, *Pólya Threshold Graphs*, arXiv:2603.18452 (public March 19, 2026). https://arxiv.org/abs/2603.18452
2. F. Alajaji and T. Fuja, *A Communication Channel Modeled on Contagion*, IEEE Transactions on Information Theory (1994), finite-memory Pólya contagion model.
3. Y. Zhong, F. Alajaji and G. Takahara, *A Binary Communication Channel with Memory Based on a Finite Queue*, IEEE Transactions on Information Theory (2007). https://mast.queensu.ca/~communications/Papers/it-qbc.pdf
4. S. Mori, M. Hisakado and K. Nakayama, *Pólya urn with memory kernel and asymptotic behaviours of autocorrelation function*, arXiv:2105.10653. https://arxiv.org/abs/2105.10653
5. A. Singh, F. Alajaji and B. Gharesifard, *A Finite Memory Interacting Pólya Contagion Network and Its Approximating Dynamical Systems*, arXiv:2010.00463. https://arxiv.org/abs/2010.00463
