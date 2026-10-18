# Logarithmic-time Dirichlet crossover in vanishing Pólya–Friedman urns

## Finding

A vanishing frequency of color-mixing replacements retains a quantitatively visible trace of the classical Pólya limit when the frequency is of order \(1/\log N\). For \(k\ge2\) colors and the urn specified below, put \(u=(1/k,\ldots,1/k)\). If \(p_N\to0\) and \(p_N\log N\to\lambda\in[0,\infty)\), then under one natural coupling there is a single Dirichlet vector
\[
B\sim\operatorname{Dirichlet}(r_1/c,\ldots,r_k/c)
\]
such that, for every \(\varepsilon\in(0,1)\),
\[
\mathbb E\left[\sup_{\varepsilon\le s\le1}
\left\|Z^{(N)}_{\lfloor N^s\rfloor}
-u-e^{-kb\lambda s/c}(B-u)\right\|_2^2\right]\longrightarrow0.
\]
When \(p_N\log N\to\infty\), provided \(p_N\to0\), the same assertion holds with deterministic limit \(u\):
\[
\mathbb E\left[\sup_{\varepsilon\le s\le1}
\left\|Z^{(N)}_{\lfloor N^s\rfloor}-u\right\|_2^2\right]\longrightarrow0.
\]
Thus the endpoint ranges from the pure Pólya Dirichlet law at \(\lambda=0\) through an affine contracted Dirichlet law for \(0<\lambda<\infty\) to a point mass at the uniform proportions when \(\lambda=\infty\). The limiting logarithmic-time profile is **not** a sequence of independent Dirichlet draws: all times share the same random vector \(B\).

## Assumptions and scope

Fix an integer \(k\ge2\); positive integer initial counts \(r_1,\ldots,r_k\); positive integers \(a,b\); set \(c=a+(k-1)b\), \(R=\sum_i r_i\) and \(\theta=R/c\). Each triangular row, indexed by integer \(N\ge1\), is run for \(N\) draws from the initial configuration \(r\). At draw \(j\), choose one ball uniformly. Independently use the symmetric Friedman addition with probability \(p_N\) (add \(a\) balls of the chosen color and \(b\) of each other color), or with probability \(1-p_N\) add \(c\) balls of the chosen color (Pólya rule). The replacement-choice indicators are independent across draws within each row. Both rules add exactly \(c\) balls in total per draw, so the denominator after \(t\) draws is the deterministic \(R+ct\). Write \(Z^{(N)}_t\) for the vector of ball proportions, \(0\le t\le N\). The parameter sequence satisfies \(0\le p_N\le1\) and \(p_N\to0\). All limits are as \(N\to\infty\) with \(k,r,a,b\) fixed; the logarithmic-time assertion is uniform only for \(s\in[\varepsilon,1]\) with fixed \(\varepsilon>0\).

## Proof

**1. Exact martingale renormalization.** Let \(\mathcal F_{j,N}\) denote the history in row \(N\), \(J_{j,N}\) the chosen color and \(\xi_{j,N}\) the indicator of Friedman replacement. The fraction of the \(c\) newly added balls in color \(i\) is
\[
Q_{j,N,i}=\frac bc\xi_{j,N}+
\left(1-\frac{kb}{c}\xi_{j,N}\right)\mathbf1_{\{J_{j,N}=i\}}.
\]
The formula remains valid when \(a<b\): the value for the drawn color is \(a/c\), and for every other color it is \(b/c\). Thus \(0\le Q_{j,N,i}\le1\), \(\sum_iQ_{j,N,i}=1\), and conditional on \(\mathcal F_{j-1,N}\),
\[
\mathbb E(Q_{j,N,i}\mid\mathcal F_{j-1,N})
=Z^{(N)}_{j-1,i}-\gamma_N(Z^{(N)}_{j-1,i}-1/k),
\qquad\gamma_N=\frac{kbp_N}{c}.
\]
Define the vector martingale difference \(\eta_{j,N}=Q_{j,N}-\mathbb E(Q_{j,N}\mid\mathcal F_{j-1,N})\). Since \(R+ct=c(\theta+t)\), exact subtraction gives
\[
Z^{(N)}_j-u
=\left(1-\frac{\gamma_N}{\theta+j}\right)(Z^{(N)}_{j-1}-u)
+\frac{\eta_{j,N}}{\theta+j}.
\]
For sufficiently large \(N\), \(\gamma_N\le1/4\), so all factors below are positive. Put
\[
A_{0,N}=1,\qquad
A_{t,N}=\prod_{j=1}^t\left(1-\frac{\gamma_N}{\theta+j}\right),\qquad
M_{t,N}=\frac{Z^{(N)}_t-u}{A_{t,N}}.
\]
The process \(M_{t,N}\) is a square-integrable vector martingale with differences
\[
M_{j,N}-M_{j-1,N}
=\frac{\eta_{j,N}}{(\theta+j)A_{j,N}}.
\]
Taking expectations before division proves the exact finite-row mean formula
\[
\mathbb EZ^{(N)}_t-u
=\left(\frac rR-u\right)A_{t,N},\qquad 0\le t\le N.
\]

**2. Uniformly summable fluctuations.** Because \(\gamma_N\le1/4\), Taylor's bound for the logarithm and \(\sum_j(\theta+j)^{-2}<\infty\) imply, uniformly in \(t\ge1\),
\[
\log A_{t,N}
=-\gamma_N\sum_{j=1}^t\frac1{\theta+j}+O_{\theta}(\gamma_N^2),
\qquad
A_{t,N}^{-2}\le C_{\theta}(t+1)^{2\gamma_N}
\le C_{\theta}(t+1)^{1/2}.
\]
The increments of each component of \(\eta\) have absolute value at most one. Orthogonality of martingale differences and Doob's \(L^2\) inequality, summed over the fixed \(k\) coordinates, give, for every \(1\le K<N\),
\[
\mathbb E\left[\max_{K\le t\le N}
\|M_{t,N}-M_{K,N}\|_2^2\right]
\le C_{k,\theta}\sum_{j>K}(\theta+j)^{-2}(j+1)^{1/2}
\le C'_{k,\theta}K^{-1/2}.
\]
The same computation bounds \(\mathbb E\max_{0\le t\le N}\|M_{t,N}\|_2^2\) uniformly in all sufficiently large \(N\).

**3. Identification with one Pólya limit.** On one probability space take independent sequences of \(\operatorname{Uniform}(0,1)\) variables to drive the inverse-cumulative color selection and the Friedman/Pólya rule choice in every row. Use the same color uniforms to construct the classical pure Pólya urn with increment \(c\). For every fixed \(K\), the first \(K\) Friedman indicators are zero for all sufficiently large \(N\), almost surely: \(p_N\to0\) and finitely many rule-choice uniforms are strictly positive. The first \(K\) updates therefore eventually coincide exactly with the pure Pólya urn; moreover \(A_{K,N}\to1\). Consequently,
\[
M_{K,N}\longrightarrow Z^{(0)}_K-u
\quad\text{almost surely and in }L^2.
\]
The pure Pólya proportions form a bounded martingale and converge almost surely and in \(L^2\) to \(B\sim\operatorname{Dirichlet}(r_1/c,\ldots,r_k/c)\). This follows, for example, from the exact Dirichlet-multinomial predictive probabilities. Using the preceding maximal bound, then sending \(N\to\infty\) and \(K\to\infty\), proves for every fixed \(\varepsilon>0\)
\[
\mathbb E\sup_{N^\varepsilon\le t\le N}
\|M_{t,N}-(B-u)\|_2^2\longrightarrow0.
\]
Indeed for \(N^\varepsilon\ge K\) the supremum is bounded by the martingale tail after \(K\), the fixed-\(K\) comparison, and the pure Pólya tail; all three vanish in that order.

**4. Deterministic logarithmic clock and the regimes.** The harmonic sum obeys \(\sum_{j=1}^t(\theta+j)^{-1}=\log t+O_\theta(1)\), uniformly for \(t\ge1\). If \(p_N\log N\to\lambda<\infty\), then uniformly for \(\varepsilon\le s\le1\)
\[
A_{\lfloor N^s\rfloor,N}
=\exp\left[-\frac{kb}{c}p_Ns\log N+o(1)\right]
\longrightarrow e^{-kb\lambda s/c}.
\]
Since \(0<A_{t,N}\le1\), multiplying the martingale approximation from Step 3 by \(A_{t,N}\) proves the claimed uniform mean-square path limit. If \(p_N\log N\to\infty\), then \(\sup_{s\in[\varepsilon,1]}A_{\lfloor N^s\rfloor,N}=A_{\lfloor N^\varepsilon\rfloor,N}\to0\); the uniformly bounded martingale maximal second moment from Step 2 yields the uniform mean-square deterministic limit. Both statements follow without interchanging the fixed-\(p\) and large-\(N\) limits.

## Verification

The accompanying standalone \(\texttt{verify.py}\) enumerates finite-state distributions with exact rational arithmetic for two- and three-color balanced urns. It checks every conditional drift identity, exact total mass and finite-time expectation formula across varied initial states and reinforcement parameters. It also checks illustrative deterministic contraction coefficients in finite triangular rows. On Python 3 its current run completed **280,206 checks**. These finite calculations corroborate the formulas; the path-level and infinite-horizon conclusions come from the martingale proof in Steps 1–4.

## Relationship to prior work

Shi, Yin and Miao [1] introduce the two-color mixed Pólya–Friedman urn with a *fixed*, nonzero mixing probability and study its central limit theorem. The present theorem instead treats an \(N\)-dependent probability tending to zero; the critical \(1/\log N\) scale, joint logarithmic-time profile, multicolor extension and contracted-Dirichlet endpoint law are not statements of [1]. Alves and Rosales [2] prove eventual equalization with fixed positive mixing probability, which does not determine this singular finite-horizon crossover. Zhang [3] develops general randomized and time-inhomogeneous urn convergence, but the inspected results do not identify the explicit triangular-array Dirichlet contraction at a finite accumulated drift; [4] gives the classical pure Pólya Dirichlet limit as prior knowledge. Interacting Pólya urn synchronization [5] concerns a different multi-urn geometry rather than symmetric replacements of one urn. The claims here are limited to this explicitly defined balanced mixture, and no assertion of historical uniqueness is made.

## Limitations

The reinforcement amounts and initial composition are fixed positive integers, the Friedman matrix is fully symmetric with one color drawn per step, both replacement rules are exactly balanced, and the replacement choices are independent within each row. The coupling limit requires \(p_N\to0\); neither fixed positive mixing nor rates depending on the current urn state are included. The logarithmic-time profile is stated only away from the initial exponent \(s=0\). The theorem gives no explicit convergence rate in \(N\) or joint CLT on top of the critical profile. A possible older general triangular-array stochastic-approximation theorem that implies the stated special case is a remaining originality risk.

## References

1. J. Shi, Q. Yin and Y. Miao, *Central Limit Theorem for a Pólya-Friedman Mixed Urn Model* (first public version 2026-05-26), arXiv:2605.26669.
2. R. Alves and R. A. Rosales, *Friedman vs Pólya* (2025 preprint), arXiv:2502.16768.
3. L.-X. Zhang, *Convergence of randomized urn models with irreducible and reducible replacement policy* (2022 preprint), arXiv:2204.04810.
4. S. Janson, *Rate of convergence for traditional Pólya urns*, arXiv:1911.09569.
5. I. Crimaldi, P. Dai Pra and I. G. Minelli, *Fluctuation Theorems for Synchronization of Interacting Pólya’s urns*, arXiv:1407.5043.
