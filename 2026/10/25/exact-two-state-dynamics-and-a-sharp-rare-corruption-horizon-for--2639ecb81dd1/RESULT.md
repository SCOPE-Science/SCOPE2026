# Exact two-state dynamics and a sharp rare-corruption horizon for small-sample quantile Kaczmarz

## Finding
For the quantile-at-the-sample-row variant of small-sample randomized Kaczmarz, a natural two-level corrupted, one-dimensional linear system admits an exact finite-population transition law. For odd sample sizes, the chosen quantile rank controls the *sign* of serial correlation: lower ranks give positive correlations, the median makes consecutive iterates independent, and higher ranks give negative correlations (when every subset corruption count is feasible). The median's rare wrong iterates have an exactly hypergeometric frequency, and an asymptotically sharp exponential observation horizon with a computable square-root prefactor. This is a theorem about the stated scalar model and the sampled-quantile *equality* selection rule, not a convergence theorem for general corrupted matrices.

## Assumptions and scope
Let \(m\ge 3\) and \(1\le c<m/2\) be integers. Let \(A\in\mathbb R^{m\times1}\) consist of entries equal to \(1\), and put \(b_i=\delta\ne0\) for the first \(c\) rows and \(b_i=0\) for the other \(m-c\) rows. The uncorrupted scalar solution is \(0\). Starting with \(X_0=0\), independently at each iteration draw a uniformly random size-\(s\) subset of the \(m\) labeled rows, without replacement, where \(1\le s\le m\). Order the absolute residuals \(|X_t-b_i|\) of these sampled rows. Choose a sampled row attaining the \(k\)-th *smallest* residual, \(1\le k\le s\), and make the exact normalized Kaczmarz projection to its equation. Any tie among rows with the same residual may be resolved arbitrarily: in this two-level model the resulting iterate is independent of the tie policy. The update is therefore \(X_{t+1}=b_i\). The method is the rank-\(k\) specialization of the sampled-quantile *equality* selection in Algorithm 2 of Haddock–Ma–Rebrova, not their distinct threshold-accepted Algorithm 1.

Write \(H\) for the number of corrupted rows in a fresh subset. Its distribution is
\[
\Pr(H=j)=\frac{\binom cj\binom{m-c}{s-j}}{\binom ms},\qquad \max(0,s-m+c)\le j\le\min(s,c).
\]
Use the convention that an out-of-range tail is zero. Define
\[
p_k=\Pr(H\ge s-k+1),\qquad q_k=\Pr(H\le k-1).
\]

## Proof
**Exact transition and correlations.** Every iterate is either \(0\) or \(\delta\). At \(0\), the \(s-H\) clean rows have residual zero and the \(H\) corrupt rows have nonzero residual; hence the rank-\(k\) projection is corrupt exactly when \(H\ge s-k+1\). At \(\delta\), the order is reversed, and the projection is *clean* exactly when \(H\le k-1\). Fresh independent sampling thus makes \((X_t)\) a Markov chain on \(\{0,\delta\}\), with the exact matrix
\[
P_k=\begin{pmatrix}1-p_k&p_k\\q_k&1-q_k\end{pmatrix}.
\]
Whenever \(p_k+q_k>0\), the stationary law is unique, has mass \(\pi_\delta=p_k/(p_k+q_k)\) at \(\delta\), and has nontrivial eigenvalue \(\ell_k=1-p_k-q_k\). In a stationary realization,
\[
\operatorname{Cov}(X_t,X_{t+j})=\delta^2\pi_\delta(1-\pi_\delta)\ell_k^j\quad(j\ge0).
\]
This follows directly by conditioning: \(\mathbb E[X_{t+1}\mid X_t]=\delta p_k+\ell_k X_t\), and iterating the centered regression. The covariance formula can be zero due to a degenerate stationary law even when \(\ell_k\ne0\).

**Rank phase transition.** Suppose that \(s=2r+1\le c\). Then \(H\) has strictly positive mass at every integer from \(0\) to \(s\), because \(m-c>c\ge s\). For \(k\le r\), the two events defining \(p_k\) and \(q_k\) are disjoint and exclude a nonempty middle interval, so \(p_k+q_k<1\) and \(\ell_k>0\). For \(k=r+1\), the events partition the sample space, so \(p_k+q_k=1\) and \(\ell_k=0\). For \(k\ge r+2\), the two events overlap on a nonempty interval, so \(p_k+q_k>1\) and \(\ell_k<0\). In this full-support regime both transition probabilities are positive, so these are strict positive, zero, and alternating-sign stationary correlations respectively. No strict-sign assertion is made when \(s>c\).

**Median independence, cutoff, and first wrong update.** Let \(s=2r+1\), \(k=r+1\), with no requirement that \(s\le c\). In either state \(0\) or \(\delta\), the median row has the label of the majority class of the sampled subset. Thus it is corrupt if and only if \(H\ge r+1\), *independently of the previous iterate*. Since the sampled subsets are independent, \(X_1,X_2,\ldots\) are independent and identically distributed with
\[
\Pr(X_t=\delta)=p_{m,c,s}:=\frac{\displaystyle\sum_{j=r+1}^{\min(c,s)}\binom cj\binom{m-c}{s-j}}{\binom ms}\quad(t\ge1).
\]
Because the clean population has strict majority, at least one size-\(s\) subset has clean sample majority; therefore \(p_{m,c,s}<1\) for every admissible sample size. If \(p_{m,c,s}>0\), the first wrong-update time \(\tau=\inf\{t\ge1:X_t=\delta\}\) is geometric: \(\Pr(\tau>T)=(1-p_{m,c,s})^T\), \(\mathbb E\tau=1/p_{m,c,s}\). Almost surely, both values occur infinitely often; therefore \(\liminf_{t\to\infty}|X_t|=0\), \(\limsup_{t\to\infty}|X_t|=|\delta|\), and the iterates do not converge. If \(p_{m,c,s}=0\), all iterates after the first are exactly correct. The hypergeometric tail vanishes if and only if \(r+1>c\), equivalently \(s\ge2c+1\). This is an *exact finite-population, one-step robust sample-size cutoff* for median selection, even when \(c/m<1/2\).

**Sharp growing-sample horizon.** Fix \(\beta\in(0,1/2)\). Consider any sequence of odd sizes \(s\to\infty\), integer populations \(m_s,c_s\) with \(c_s/m_s=\beta+o(1/s)\) and \(s^2/m_s\to0\). Define
\[
\kappa_\beta=-\tfrac12\log(4\beta(1-\beta)),\qquad
C_\beta=\frac{\sqrt{2\beta(1-\beta)}}{(1-2\beta)\sqrt\pi}.
\]
Then
\[
p_{m_s,c_s,s}\sim C_\beta s^{-1/2}e^{-\kappa_\beta s}.
\]
Indeed, the ratio of each hypergeometric point mass to the corresponding binomial \(\operatorname{Binomial}(s,\beta)\) mass is uniformly \(1+o(1)\) over all admissible \(j\): the falling-factorial formula yields a logarithmic error \(O(s^2/m_s+s|c_s/m_s-\beta|)=o(1)\). For \(s=2r+1\), the first binomial upper-tail mass is \(\binom{2r+1}{r+1}\beta^{r+1}(1-\beta)^r\). Stirling's formula gives its \(s^{-1/2}e^{-\kappa_\beta s}\) prefactor; successive upper-tail terms have ratios bounded by, and converging at fixed offsets to, \(\beta/(1-\beta)<1\). Summing by dominated convergence supplies the factor \((1-\beta)/(1-2\beta)\) and precisely the displayed constant \(C_\beta\). Consequently, for every fixed \(a>0\), with \(T_s=\lfloor a\sqrt{s}e^{\kappa_\beta s}\rfloor\),
\[
\Pr(X_1=\cdots=X_{T_s}=0)=(1-p_{m_s,c_s,s})^{T_s}\longrightarrow e^{-aC_\beta}.
\]
The threshold is sharp on exponential scales: if \(T_s=\lfloor e^{\eta s}\rfloor\), the probability of observing at least one corrupted iterate tends to zero when \(\eta<\kappa_\beta\), and to one when \(\eta>\kappa_\beta\). At equality the stated square-root correction is necessary.

## Verification
The accompanying standalone `verify.py` enumerates every sample subset for all \(3\le m\le12\), all strictly minority corruption counts, all sample sizes and all ranks, and compares the direct residual-order update with the exact hypergeometric transitions in both states. It checks the odd-sample sign phase, median independence condition, and exact zero-probability cutoff for those finite instances. It also checks representative large-size binomial asymptotics and the concrete finite-population benchmark. The verifier uses Python's standard library and integer/rational arithmetic for the finite combinatorial identities; numerical comparisons are supporting checks, not proofs of infinite assertions.

For \(m=50000\), \(c=1000\), and median size \(s=11\), the exact tail gives \(p_{m,c,s}\approx2.673785294\times10^{-8}\), hence \(\mathbb E\tau\approx3.7400161\times10^7\) updates. Short runs can appear perfectly robust although a sufficiently long run almost surely produces infinitely many corrupted outputs in this stylized model.

## Relationship to prior work
Haddock, Ma, and Rebrova (2023), Section V-D and Algorithm 2, introduce the sampled-quantile equality update and explicitly describe occasional small-sample spikes and the problem of choosing quantile rank and sample size. They supply a heuristic and experiments for constant-size sampling, not this exact two-state law, rank-controlled correlation classification, or hypergeometric rare-event scaling. Their distinct Algorithm 1 uses a threshold acceptance set; the result here must **not** be transferred to that algorithm. Haddock, Needell, Rebrova, and Swartworth (2020) develop quantile Kaczmarz theory and discuss sample-based variants, without this special-case calculation. The later Cai–Chen–Ma–Wu (2025) work gives general sample-size guarantees for a different update that selects a row from the full row set after estimating a quantile. The Battaglia–Ma (2025) error-horizon paper instead treats qRK/dqRK with general noise, global residual thresholds and expected-error bounds, not this size-\(s\) sampled-row equality rule or its exact two-state transitions. The known qualitative issue of occasional corrupted projections and logarithmic finite-horizon sample requirements is **not** claimed as novel; the contribution is the sharp model-specific distribution, rank sign phase, and constant-level horizon.

## Limitations
The theorem is only for one scalar unknown, identical unit-norm rows, two exact right-hand-side values, independent sampling each iteration, and projection to the sampled **order-statistic equality** row. It is not a convergence guarantee for general linear systems, an endorsement of a practical median rule, an assertion of behavior for arbitrary corrupted magnitudes, or an analysis of threshold-accepted sQRK / other QRK variants. The original median convention for odd sample sizes can be implemented by rank \(r+1\) (not by a prescribed interpolated quantile). The cutoff \(s\ge2c+1\) may require a sample much larger than a fixed constant. The sharp asymptotics require fixed \(\beta<1/2\), vanishing finite-population sampling fraction, and the stated population-approximation rates; no uniform assertion is made as \(\beta\uparrow1/2\). Publication priority against unexamined specialist literature remains uncertain; no independent review has been performed.

## References
1. J. Haddock, A. Ma, E. Rebrova, *On Subsampled Quantile Randomized Kaczmarz*, arXiv:2308.07987 (first posted 2023-08-15), especially Algorithm 2 and Section V-D. https://arxiv.org/abs/2308.07987
2. J. Haddock, D. Needell, E. Rebrova, W. Swartworth, *Quantile-based Iterative Methods for Corrupted Systems of Linear Equations*, arXiv:2009.08089 (first posted 2020-09-17). https://arxiv.org/abs/2009.08089
3. Z. Cai, J. Chen, A. Ma, Y. Wu, *On the Subsample Size of Quantile-Based Randomized Kaczmarz*, arXiv:2507.15185 (first posted 2025-07-21), especially its algorithm and sample-size results. https://arxiv.org/abs/2507.15185
4. E. Battaglia, A. Ma, *Quantile-RK and Double Quantile-RK Error Horizon Analysis*, arXiv:2505.00258 (first posted 2025-05-01), especially Sections 4.2 and 6. https://arxiv.org/abs/2505.00258
