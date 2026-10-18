# Quenched invariance principle for independent-cardinality bootstrap random walks

## Finding

**Theorem (quenched functional limit for the one-factor inclusion-induced model).** Fix \(0<\varepsilon<1/2\). Suppose the random binary coefficients \((\beta_{n,k})_{n\ge1,0\le k\le n}\) are mutually independent, with \(\mathbb P(\beta_{n,k}=1)=p_{n,k}\in[\varepsilon,1-\varepsilon]\), and are independent of a fair independent sign sequence \((\xi_j)_{j\ge1}\). In the one-factor inclusion-induced bootstrap construction defined below, **for almost every realization of the coefficients**, the processes
\[
\left(n^{-1/2}X_{\lfloor nt\rfloor},\ n^{-1/2}Y_{\lfloor nt\rfloor}\right)_{t\ge0}
\]
converge in distribution under the conditional sign-sequence law to a standard two-dimensional Brownian motion with independent coordinates, in \(D([0,\infty),\mathbb R^2)\). Moreover, for almost every coefficient environment, the normalized predictable cross variation converges to zero almost surely under the conditional sign-sequence law:
\[
\frac1N\sum_{j=0}^{N-1}\zeta_j\longrightarrow0.
\]
No homogeneity in \(n\) or \(k\) is required of the coefficient success probabilities.

## Assumptions and scope

Let \(\xi_1,\xi_2,\ldots\) be independent fair signs. Define the count of negative increments and the recursive sign multiplier by
\[
S_0=0,\qquad S_n=\sum_{j=1}^n\mathbf 1_{\{\xi_j=-1\}},\qquad
\zeta_0=1,\qquad
\zeta_n=(-1)^{\sum_{k=0}^{S_n}\binom{S_n}{k}\beta_{n,k}}\quad(n\ge1).
\]
The exponent is interpreted modulo two. The two random walks are
\[
X_0=Y_0=0,\qquad X_n=\sum_{j=1}^n\xi_j,\qquad
Y_n=\sum_{j=1}^n\zeta_{j-1}\xi_j.
\]
Equivalently, the binary coefficient shared by all subsets of cardinality \(k\) at time \(n\) is \(\beta_{n,k}\). This is precisely the inclusion-induced, one-factor Markov, independent-in-time specialization in the motivating paper. The environment law is a product law on a countable collection of binary variables; the quenched law fixes the entire environment and randomizes only \((\xi_j)\). The conclusion is for every fixed ellipticity parameter \(\varepsilon\), not uniformly over its approach to zero.

## Proof

**1. Odd-binomial factors.** Define \(b(s)\) as the number of ones in the binary expansion of a nonnegative integer \(s\), and set \(\rho=1-2\varepsilon\in(0,1)\). Lucas's theorem modulo two says that \(\binom{s}{k}\) is odd precisely when the one-bit set of \(k\) is contained in that of \(s\); there are \(2^{b(s)}\) such indices \(k\). Conditional on the complete sign path, coefficient independence gives
\[
m_n(\xi):=\mathbb E_{\beta}(\zeta_n\mid\xi)
=\prod_{0\le k\le S_n:\,\binom{S_n}{k}\ \mathrm{odd}}(1-2p_{n,k}),
\qquad
|m_n(\xi)|\le\rho^{2^{b(S_n)}}\le\rho^{b(S_n)}.
\]
The last inequality uses \(2^{\ell}\ge\ell\) for every integer \(\ell\ge0\) and \(0<\rho<1\). The simpler envelope \(f(s)=\rho^{b(s)}\) is enough.

**2. Deterministic binary-digit Cesàro decay.** For every integer \(d\ge0\), all binary strings of length \(d\) occur once between \(0\) and \(2^d-1\); thus
\[
\sum_{s=0}^{2^d-1}f(s)=(1+\rho)^d.
\]
If \(2^{d-1}<M\le2^d\), positivity yields
\[
0\le\frac1M\sum_{s=0}^{M-1}f(s)
\le2\left(\frac{1+\rho}{2}\right)^d\longrightarrow0.
\]
This is a deterministic averaging result and does not assume that the bits of any fixed \(S_n\) are approximately uniform.

**3. Occupation-weighted Cesàro decay along the walk.** For the fair counting process \((S_n)\), let \(T_M=\inf\{n:S_n=M\}\) and \(W_s=T_{s+1}-T_s\). The \(W_s\) are independent geometric random variables with success parameter \(1/2\), supported on \(1,2,\ldots\), with mean \(2\), variance \(2\); moreover \(T_M/M\to2\) almost surely. Since \(0\le f(s)\le1\),
\[
\sum_{s\ge0}\frac{\operatorname{Var}((W_s-2)f(s))}{(s+1)^2}
\le2\sum_{s\ge0}(s+1)^{-2}<\infty.
\]
Kolmogorov's convergence theorem and Kronecker's lemma therefore imply
\[
\frac1M\sum_{s=0}^{M-1}(W_s-2)f(s)\longrightarrow0
\quad\text{almost surely}.
\]
Combining this with Step 2 gives \(\sum_{s<M}W_sf(s)=o(M)\) almost surely. The times \(n\) with \(S_n=s\) are exactly \(T_s,\ldots,T_{s+1}-1\), whence
\[
\sum_{n=0}^{T_M-1}f(S_n)=\sum_{s<M}W_sf(s)=o(M).
\]
For arbitrary \(N\) choose \(M\) with \(T_M\le N<T_{M+1}\). By positivity, \(\sum_{n<N}f(S_n)\le\sum_{s\le M}W_sf(s)=o(M)\); since \(N\ge T_M\sim2M\),
\[
\frac1N\sum_{n=0}^{N-1}f(S_n)\longrightarrow0
\quad\text{for almost every sign path}.
\]
Consequently \(N^{-1}\sum_{n=1}^N|m_n(\xi)|\to0\) for almost every sign path, uniformly in the permitted array of success probabilities.

**4. Conditional strong law over environments.** Fix any sign path from the probability-one event of Step 3. The random variables \((\zeta_n)_{n\ge1}\) depend on disjoint coefficient rows indexed by \(n\) and hence are independent under the environment law. The variables \(\zeta_n-m_n(\xi)\) are centered, bounded by \(2\), and have variance at most \(1\). Therefore
\[
\sum_{n\ge1}\frac{\operatorname{Var}_{\beta}(\zeta_n-m_n(\xi))}{n^2}<\infty,
\]
and the independent-variable strong law gives \(N^{-1}\sum_{n=1}^N(\zeta_n-m_n(\xi))\to0\) almost surely in the environment. Together with Step 3, \(N^{-1}\sum_{n=0}^{N-1}\zeta_n\to0\) for joint-almost every \((\beta,\xi)\). Fubini's theorem then provides one environment-measure-one set on which the same convergence holds with conditional sign-path probability one. This is a pathwise, not merely annealed, statement.

**5. Quenched functional martingale limit.** Fix an environment in the preceding measure-one set. For the natural sign filtration, the process \((X_n,Y_n)\) is a square-integrable two-dimensional martingale with increments \(\Delta M_j=(\xi_j,\zeta_{j-1}\xi_j)\) and conditional covariance
\[
\mathbb E_\xi(\Delta M_j\Delta M_j^{\mathsf T}\mid\mathcal F_{j-1})
=\begin{pmatrix}1&\zeta_{j-1}\\\zeta_{j-1}&1\end{pmatrix}.
\]
Step 4 gives \(N^{-1}\sum_{j=1}^N\zeta_{j-1}\to0\) almost surely. The associated rescaled predictable covariance processes converge uniformly on each compact time interval to \(tI_2\): for the off-diagonal term this follows from the Cesàro limit and the elementary bound \(\sup_{0\le k\le nT}|\sum_{j<k}\zeta_j|/n\to0\); the diagonal terms are deterministic. Every increment has Euclidean norm \(\sqrt2\), so the conditional Lindeberg condition holds automatically. The multivariate martingale functional central limit theorem yields a Brownian limit with covariance \(tI_2\), i.e. independent standard coordinate Brownian motions. This proves both assertions. \(\square\)

## Verification

The argument reduces the problem to a conditional independent-variable strong law and a deterministic binary-digit Cesàro lemma; it does not require numerical or finite-size asymptotics. The accompanying `verify_quenched.py` performs exact checks of the odd-binomial parity count, the dyadic sum identity, the stated coefficient-expectation identity for heterogeneous rational Bernoulli parameters, and finite conditional covariance identities. It uses only the Python standard library. Execute `python verify_quenched.py` after extracting the file from this package. Passing finite tests is diagnostic only; the infinite theorem follows from the foregoing proof and the standard strong-law and martingale-limit theorems.

## Relationship to prior work

Hamza and Tournier, *Are random random walks normal?* (arXiv:2610.01658v1, first public October 1, 2026), introduced this exact inclusion-induced one-factor representation and proved in Corollary 9 a two-coordinate **annealed** Brownian limit under independence across time and cardinalities. Their discussion immediately after Corollary 9 explicitly states that the corresponding **quenched** conclusion was not obtained. The present theorem provides that conclusion under their same uniform-ellipticity and cross-time-independence hypotheses, by proving almost-sure cross-variation decay. Their Theorem 2 supplies a different quenched result under independence across subset-indexed coefficient blocks; it cannot be applied to this model because coefficients for distinct subsets of the same size are equal. Their Proposition 7(b) supplies only the first-moment condition, not the needed second-moment or pathwise cross-variation condition. Collevecchio–Hamza–Shi–Williams' earlier bootstrap-walk limit characterization supplies the standard martingale limit criterion, not the almost-sure verification for this randomized cardinality-coupled model. Lucas's theorem and both probabilistic limit tools are classical inputs, not claimed as new.

## Limitations

The environment coefficients must be independent across all distinct time-cardinality pairs; the argument does **not** establish the same quenched statement when the coefficients are time-invariant by cardinality (the different model of Corollary 12), or under arbitrary dependence across time. Uniform ellipticity is essential to the stated proof. The theorem identifies the functional Brownian limit and pathwise normalized cross variation but gives no optimal convergence rates, almost-sure coupling, or quenched large deviations. Novelty is assessed against accessible primary and mathematical-record literature; an unindexed equivalent theorem remains a residual priority risk. No independent external audit has been performed.

## References

1. Kais Hamza and Laurent Tournier, *Are random random walks normal?*, arXiv:2610.01658v1, October 1, 2026; Sections 2–4, especially Theorem 2, Proposition 7(b), Proposition 8, Corollary 9 and its subsequent remark. https://arxiv.org/html/2610.01658v1
2. Andrea Collevecchio, Kais Hamza, Yulin Shi and Andrew R. Williams, *Limit theorems and ergodicity for general bootstrap random walks*, arXiv:2010.16000 (earlier version 2020; published account referenced in [1]); the general martingale convergence criterion. https://arxiv.org/abs/2010.16000
3. Édouard Lucas's binomial congruence theorem modulo two, used as a standard binary parity identity; and the classical Kolmogorov convergence theorem, Kronecker lemma and bounded-increment martingale functional central limit theorem.
