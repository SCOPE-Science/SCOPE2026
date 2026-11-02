# Exact stationary rank diagram for two-level small-sample quantile Kaczmarz

## Finding

Consider the small-sample, order-statistic version of randomized Kaczmarz on a scalar system with \(g\) uncorrupted unit rows whose observed right-hand sides are \(0\), and \(c\) corrupted unit rows whose observed right-hand sides are the same \(h>0\). Assume integers \(1\le c<g\), let \(m=g+c\), and choose a batch size \(1\le s\le g\). Each step independently samples a uniform \(s\)-element subset of the \(m\) rows **without replacement within a batch**, then projects onto a row attaining the \(j\)-th smallest absolute residual for a fixed integer rank \(1\le j\le s\). Within-type ties may be resolved arbitrarily.

Put
\[
 w_k=\frac{\binom{c}{k}\binom{g}{s-k}}{\binom{m}{s}},\qquad
 A_j=\sum_{k=s-j+1}^{s}w_k,\qquad B_j=\sum_{k=0}^{j-1}w_k,
\]
where binomial coefficients outside their natural range are zero. The iterates enter \(\{0,h\}\) after one update and remain there. In state order \((0,h)\), their exact transition matrix is
\[
 P_j=\begin{pmatrix}1-A_j&A_j\\B_j&1-B_j\end{pmatrix}.
\]
Their unique invariant law is
\[
 \mu_j=(1-\pi_j)\delta_0+\pi_j\delta_h,
 \qquad \pi_j=\frac{A_j}{A_j+B_j}.
\]
The stationary mean squared error from the unique uncorrupted solution \(0\) is precisely \(h^2\pi_j\). The only nonconstant eigenvalue is \(\xi_j=1-A_j-B_j\), and for a chain already in \(\{0,h\}\) with \(\Pr(X_0=h)=z\),
\[
 \Pr(X_t=h)=\pi_j+(z-\pi_j)\xi_j^t,\quad
 \operatorname{Cov}_{\mu_j}(X_0,X_t)=h^2\pi_j(1-\pi_j)\xi_j^t.
\]

The complete rank, batch-size, and correlation classification is as follows.

1. When \(s\le c\), \(\pi_1<\pi_2<\cdots<\pi_s\). The uniquely optimal residual rank is \(j=1\), with
\[
 \pi_1=\frac{\binom{c}{s}}{\binom{c}{s}+\binom{g}{s}}>0.
\]
Every fixed-rank chain is irreducible and aperiodic; the corrupt state is visited infinitely often almost surely. At \(s=1\), the one available rank is of course the unique optimum.

2. When \(c<s\le g\), \(\pi_j=0\) exactly for \(1\le j\le s-c\), while \(\pi_j>0\) at all larger ranks. Thus \(s=c+1\) is the **sharp finite-population batch-size threshold** for the existence of a rank that almost surely reaches and permanently retains the uncorrupted solution. For \(j=1\) in this regime, the expected number of steps to first reach \(0\) starting at \(h\) is
\[
 \mathbb E_h[T_0]=\frac{\binom{m}{s}}{\binom{g}{s}}.
\]

3. The sign of the lag-one eigenvalue is decided exactly by the sample rank:
\[
 \xi_j=\begin{cases}
 \displaystyle\sum_{k=j}^{s-j}w_k,&2j\le s,\\[4pt]
 0,&2j=s+1,\\[4pt]
 \displaystyle-\sum_{k=s-j+1}^{j-1}w_k,&2j\ge s+2.
 \end{cases}
\]
In particular, the median order statistic on every **odd** batch size makes the states from the **second update onward** independent draws from \(\mu_j\), regardless of the corruption fraction. For \(s=2r\), the two central ranks have eigenvalues \(w_r\) and \(-w_r\), respectively. Empty interval sums equal zero, so statements also cover support-degenerate batches.

4. If the batches instead consist of \(s\) independent draws **with replacement**, while still choosing the update row from those same draws, all formulas remain valid after replacing \(w_k\) with \(\binom{s}{k}(c/m)^k(g/m)^{s-k}\). For every finite positive \(s\), the rank \(j=1\) is uniquely optimal but has
\[
 \pi_1=\frac{c^s}{c^s+g^s}>0.
\]
Consequently, no finite batch size gives the exact-absorption property under replacement. This is a comparison of the specified within-batch-update algorithms, not of an independently sampled update-row variant.

## Assumptions and scope

The unknown is one real coordinate. All row coefficients are exactly \(1\); hence the uncorrupted system has the unique solution \(0\). All corrupted right-hand sides share the fixed positive value \(h\). Corruption multiplicities \(c,g\), batch size \(s\), and order rank \(j\) are fixed over time, and batches are independent from step to step. For a uniform fixed-size subset the count of corrupt rows is hypergeometric. A row of the selected residual rank is used for the complete, unrelaxed Kaczmarz projection. Rank, rather than a convention-dependent quantile fraction, is specified to resolve finite-sample rounding. At a generic initial point outside \(\{0,h\}\) the first update may have a different selection law; all transition, invariant, and convergence formulas apply thereafter. No claim applies to the distinct scheme that estimates a quantile on one batch but draws the update row independently from the entire data set.

## Proof

**Exact two-state reduction.** Projecting \(x\) onto the equation \(x=b_i\) replaces \(x\) by \(b_i\), either \(0\) or \(h\). Denote by \(K\) the number of corrupt rows in a uniformly chosen batch. Counting subsets yields \(\Pr(K=k)=w_k\). At state \(0\), every clean row has residual \(0\), every corrupt row residual \(h\); hence the rank-\(j\) row is corrupted if and only if \(K\ge s-j+1\). At state \(h\) the order reverses, and the chosen row is clean precisely when \(K<j\). These conditions give \(P_j\). Because \(s\le g\), \(w_0>0\), so \(B_j>0\) for every rank; \(A_j\ge0\) and \(A_j<1\). Solving \(\mu P=\mu\) gives the unique invariant distribution even if \(A_j=0\). Matrix diagonalization (or the scalar affine recurrence) yields \(\xi_j\), the transient formula and the stationary covariance. For \(s\le c\), \(w_s>0\), \(w_0>0\), both transitions and both self-transitions have positive probability, establishing irreducibility, aperiodicity, and almost-sure recurrent visits to both states.

**Sharp rank optimum.** For \(s\le c\), each \(w_u\) and \(w_{s-u}\) is positive. Write the stationary odds as a running weighted mean:
\[
 \frac{A_j}{B_j}=
 \frac{\sum_{u=0}^{j-1}w_u r_u}{\sum_{u=0}^{j-1}w_u},
 \qquad r_u=\frac{w_{s-u}}{w_u}.
\]
Direct cancellation of consecutive hypergeometric ratios gives
\[
 \frac{r_{u+1}}{r_u}=
 \frac{(g-u)(g-s+u+1)}{(c-u)(c-s+u+1)}>1
 \quad(0\le u<s),
\]
where the strict inequality follows from \(g>c\) and positivity of all factors. Adding a new larger number strictly raises the weighted mean, so \(A_j/B_j\), then \(\pi_j\), increases strictly with \(j\). The displayed formula for \(\pi_1\) follows by taking only \(K=0\) and \(K=s\). If \(s>c\), the event \(K\ge s-j+1\) is impossible exactly when \(j\le s-c\); for larger \(j\), this event has positive probability. That proves the zero-error rank classification and the sharp sample-size boundary. At rank one in the absorbing regime, the transition from \(h\) to \(0\) succeeds exactly when the sampled batch is all clean, with probability \(\binom gs/\binom ms\), so the hitting time is geometric with the stated mean.

**Correlation and replacement.** The events defining \(A_j\) and \(B_j\) are tail events of the same integer variable \(K\). If \(2j\le s\), the two tails are disjoint and their uncounted complement is \(j\le K\le s-j\), giving \(\xi_j\ge0\). If \(2j=s+1\), the tails partition the entire support, giving \(A_j+B_j=1\) and identical transition rows; the sequence is independent after the first update. If \(2j\ge s+2\), the tails overlap on \(s-j+1\le K\le j-1\), yielding the negative interval formula. The central even-batch identities follow immediately. With replacement, \(K\) is binomial; the same two-state argument holds, and the ratio in the weighted-mean proof is \((g/c)^2>1\), so every rank strictly raises the stationary error. Since both all-clean and all-corrupt outcomes have positive probability for every finite \(s\), no stationary corrupt mass vanishes.

## Verification

Run `python3 verify.py` with Python 3.9 or later (standard library only). It directly enumerates every row subset for \(3\le m\le10\) and all admissible clean/corrupt counts, sample sizes and ranks, and checks the exact rational transition probabilities against the formulas. It also verifies stationary rank ordering, the sharp absorbing classification, eigenvalue sign identities, seven-step transition laws, and the independent-with-replacement variant. A worked instance with \(g=6,c=3,s=3\) gives \(\pi_1=1/21\) and median \(\pi_2=19/84\); at \(s=4\), rank one is absorbing with mean recovery time \(42/5\) from the corrupted state. These finite checks are cross-checks; the proof above supplies the universal statements.

## Relationship to prior work

Haddock, Ma and Rebrova (2023), Section V-D and Algorithm 2, introduce a small-sample quantile randomized Kaczmarz variant selecting a row at the sampled residual quantile. They identify possible error spikes, discuss corruption-heavy batches, and explicitly leave mathematical guidance on optimal tiny-batch sizes and quantiles as a future direction. Their main theorem concerns a larger proportional-subsampling setting and does not imply this exact scalar stationary, rank, or lag-correlation classification.

Haddock, Needell, Rebrova and Swartworth (2020/2022) introduced and analyzed quantile-based iterative methods for corrupted systems, primarily with broad high-dimensional convergence guarantees rather than two-level finite-population invariant laws.

Cai, Chen, Ma and Wu (2025/2026) establish sharp-order finite-horizon high-probability sample-size bounds for a related but materially different method: it estimates the quantile from independent-with-replacement draws and samples the tentative update row from the entire system, accepting or rejecting that update. They explain the difference from the update-from-subset algorithm. Their high-probability bounds do not imply the present all-rank exact invariant distribution, the two-state median independence, or the without-versus-with-replacement absorption dichotomy. Neither their results nor the present scalar model can be used as a blanket replacement for the other.

The underlying hypergeometric and two-state Markov formulas are classical; the specific exact optimization and mixing classification for this small-sample row-selection mechanism is the claimed contribution, not any novelty in those classical tools.

## Limitations

The model uses identical normalized scalar rows and exactly two response values, with independent sampled batches and full Kaczmarz projections. In particular, the rank-one optimum cannot be extended without proof to multidimensional or noisy systems, where a very small quantile can markedly slow progress. The sharp finite-population cure depends on sampling without replacement within the batch and is not a guarantee for other quantile-randomized-Kaczmarz implementations. The stationary law does not imply a strong finite-time accuracy guarantee. Literature overlap with specialized two-point row-selection or order-statistic Markov models remains a possible publication-priority risk. No independent audit or general empirical performance study has been performed.

## References

1. J. Haddock, A. Ma, and E. Rebrova, *On Subsampled Quantile Randomized Kaczmarz*, arXiv:2308.07987 (first public version, 15 August 2023), Section V-D and Algorithm 2. https://arxiv.org/abs/2308.07987
2. J. Haddock, D. Needell, E. Rebrova, and W. Swartworth, *Quantile-based Iterative Methods for Corrupted Systems of Linear Equations*, arXiv:2009.08089 (2020). https://arxiv.org/abs/2009.08089
3. J.-F. Cai, J. Chen, A. Ma, and T. Wu, *On the Subsample Size of Quantile-Based Randomized Kaczmarz*, arXiv:2507.15185 (2025; later revised in 2026), particularly Introduction, Algorithm 1.1 and Section 3. https://arxiv.org/abs/2507.15185
