# Exact two-atom residual law and sharp pivoting reversal on common-factor matrices

## Finding

Consider the real positive-definite matrix
\[
 A=b\mathbf 1\mathbf 1^{\mathsf T}+\operatorname{diag}(a,1,\ldots,1)
 \quad(n\ge3,\ a>1,\ b>0).
\]
Let \(1\le k\le n-1\). Run exact randomly pivoted partial Cholesky for \(k\) steps, sampling each remaining pivot with probability proportional to the **current residual diagonal**, and let \(T_k\) be the trace of the final positive-semidefinite residual. Put
\[
 x=b^{-1}+k-1,\quad
 T_0=a+n-k-1+\frac{n-k}{b^{-1}+k},\quad
 T_1=(n-k)\left(1+\frac{1}{b^{-1}+k-1+a^{-1}}\right),
\]
and
\[
 p_0=\prod_{j=0}^{k-1}
 \frac{(n-1-j)(1+(b^{-1}+j)^{-1})}
 {(n-1-j)(1+(b^{-1}+j)^{-1})+a+(b^{-1}+j)^{-1}}.
\]
Let \(E_k\) be the event that the exceptional column is not selected. Then \(\Pr(E_k)=p_0\), the residual trace equals \(T_0\) on \(E_k\) and equals \(T_1\) on its complement. Thus this is a law supported on **at most two values**: when \(T_0\ne T_1\) its atom probabilities are \(p_0\) and \(1-p_0\); when the values coincide the law has a single atom. Consequently,
\[
 \mathbb E T_k=p_0T_0+(1-p_0)T_1,
 \qquad T_0-T_1=(a-1)\left[1-\frac{n-k}{(ax+1)(x+1)}\right].
\]
Greedy largest-residual-diagonal pivoting always includes the exceptional column, attaining \(T_1\). The globally optimal \(k\)-column Nyström subset instead omits that column, and randomly pivoted Cholesky has **strictly smaller expected residual trace than greedy**, precisely when
\[
 \boxed{(ax+1)(x+1)<n-k.}
\]
At equality every \(k\)-column subset has the same trace error. Beyond this boundary the exceptional-column subsets are optimal and greedy is optimal. Since the right side decreases and the left side increases with \(k\), the strict reversal region, if nonempty, is an initial interval of integer pivot counts.

The reversal can be arbitrarily severe even for an asymptotically perfectly correlated matrix with almost equal diagonal entries. For integers \(t\to\infty\), choose
\[
 n=t^3,\qquad a=t,\qquad b=t^2,\qquad k=1.
\]
Then, writing \(G_t\) for greedy residual trace and \(R_t\) for the expected randomly pivoted residual trace,
\[
 G_t\sim t^4,\quad R_t\sim2t^3,\quad
 \boxed{G_t/R_t\sim t/2\longrightarrow\infty.}
\]
Yet the ratio of the largest to smallest diagonal of \(A\) tends to one, and **every pairwise correlation** \(A_{ij}/\sqrt{A_{ii}A_{jj}}\), \(i\ne j\), tends uniformly to one. Thus neither near-uniform diagonal magnitudes nor almost-perfect correlations protect the trace objective against greedy pivot choice.

## Assumptions and scope

The matrix and calculations are real and in exact arithmetic; the diagonal values \(a,1\) are positive and the rank-one strength \(b\) is strictly positive. The exceptional coordinate is index 1. A \(k\)-pivot Nyström approximation means \(A(:,S)A(S,S)^{-1}A(S,:)\) for a set \(S\) of \(k\) distinct indices. Its residual is a positive-semidefinite Schur complement padded with zeros at selected indices. The trace error is the trace of that residual, not a spectral- or Frobenius-norm error. No numerical-tolerance stopping rule is used.

## Proof

**1. Schur-complement closure.** For any selected set \(S\), let \(d_1=a\) and \(d_i=1\) otherwise. The selected principal matrix is \(D_S+b\mathbf1_S\mathbf1_S^{\mathsf T}\), with \(D_S=\operatorname{diag}(d_i:i\in S)\). Writing \(s=\sum_{i\in S}d_i^{-1}\), the rank-one inverse identity yields
\[
 \mathbf1_S^{\mathsf T}(D_S+b\mathbf1_S\mathbf1_S^{\mathsf T})^{-1}\mathbf1_S
 =\frac{s}{1+bs}.
\]
The remaining Schur complement is therefore exactly
\[
 D_{S^c}+\left(b-\frac{b^2s}{1+bs}\right)
 \mathbf1_{S^c}\mathbf1_{S^c}^{\mathsf T}
 =D_{S^c}+(b^{-1}+s)^{-1}\mathbf1_{S^c}\mathbf1_{S^c}^{\mathsf T}.
\]
The formula is independent of the order of elimination. If index 1 has not been selected, \(s=k\); otherwise \(s=k-1+a^{-1}\). Taking the traces of the remaining \(n-k\) coordinates produces exactly \(T_0\) and \(T_1\), respectively. In particular, the event partition alone fixes the entire residual-trace distribution.

**2. Exact inclusion probability.** If the exceptional index is still unchosen after \(j\) normal pivots, set \(u_j=(b^{-1}+j)^{-1}\). The current residual has \(n-1-j\) normal diagonal entries \(1+u_j\) and one exceptional diagonal entry \(a+u_j\). The conditional probability of avoiding the exceptional pivot at the next step is
\[
 \frac{(n-1-j)(1+u_j)}{(n-1-j)(1+u_j)+a+u_j}.
\]
Multiplying these \(k\) conditional probabilities proves the stated \(p_0\). For \(1\le k\le n-1\), both inclusion and avoidance have strictly positive probabilities.

**3. Sharp pivoting comparison.** Because \(a>1\), index 1 has a strictly larger residual diagonal than every normal index at the beginning. Greedy therefore picks it first; all later columns are exchangeable, giving trace \(T_1\). A direct common-denominator calculation with \(x=b^{-1}+k-1\) gives
\[
 T_0-T_1=(a-1)\left(1-\frac{n-k}{(ax+1)(x+1)}\right).
\]
Every \(k\)-column subset contains or omits index 1, so the better of these two values is the globally optimal column-subset trace. Furthermore,
\[
 \mathbb ET_k-T_1=p_0(T_0-T_1).
\]
The exact strict criterion follows from \(p_0>0\). The monotonicity of \((ax+1)(x+1)\) in \(k\), and the decrease of \(n-k\), establish the initial-interval assertion.

**4. Near-perfect-correlation separation.** For \(n=t^3,a=t,b=t^2,k=1\), the greedy pivot is exceptional, so
\[
 G_t=(t^3-1)\left(1+\frac{t^3}{t+t^2}\right)=t^4(1+o(1)).
\]
A normal pivot gives
\[
 T_0=t+t^3-2+(t^3-1)\frac{t^2}{t^2+1}
 =2t^3(1+o(1)).
\]
The chance of the exceptional pivot under residual-diagonal sampling is
\[
 q_t=\frac{t^2+t}{(t^3-1)(t^2+1)+(t^2+t)}
 =O(t^{-3}).
\]
Thus \(R_t=(1-q_t)T_0+q_tG_t=2t^3(1+o(1))\), proving the unbounded ratio. The diagonal ratio is \((t^2+t)/(t^2+1)\to1\). Normal-normal correlations are \(t^2/(t^2+1)\to1\); exceptional-normal correlations are
\[
 \frac{t^2}{\sqrt{(t^2+t)(t^2+1)}}\longrightarrow1.
\]
These are all possible off-diagonal correlation types, completing the uniform-correlation claim.

## Verification

Run `python3 verify.py` using the supplied Python 3 standard-library checker. It reconstructs exact Schur complements from independent rational matrix operations and checks every \(k\)-subset for \(3\le n\le7\), three exceptional variances and three common-factor strengths. It additionally enumerates randomized elimination orders for small dimensions and verifies survival probabilities, the two-value law and mean trace against direct Markov-path probabilities. A final diagnostic compares finite \(t\) against the rigorously derived asymptotics. At preparation time it passed 9,345 grouped checks. These finite computations do **not** certify the quantified infinite-dimensional family; the proof above supplies that argument.

## Relationship to prior work

Chen, Epperly, Tropp and Webber (first public preprint July 13, 2022) introduce and analyze residual-diagonal-sampled RPCholesky. Their Appendix on greedy pivoting proves broad worst-case failure using a block-diagonal matrix of identity and all-ones blocks, and their analysis of constant-diagonal blocks gives related Schur-complement algebra. The present theorem does **not** claim that arbitrary greedy failure or the Schur identity is new. Its distinguishing combination is a complete finite-step random residual-trace law, a necessary and sufficient comparison against greedy on a one-defect *common-factor* family, and an unbounded separation while all correlations and diagonal ratios tend to one. The block-diagonal witness does not have that correlation property.

Steinerberger (first public preprint April 17, 2024) studies alternate pivot-weight exponents and explains why large diagonal entries need not identify informative columns; the exact two-event distribution and the near-perfect-correlation boundary are not among the results inspected. Epperly (2026) proves general expected trace and spectral guarantees; these bounds provide context, not the family-specific sharp equality and optimizer threshold.

## Limitations

The classification concerns only this positive-definite diagonal-plus-common-factor family, exact trace-error Nyström approximations and distinct column pivots. It does not show that RPCholesky always beats greedy, nor does it assert unbounded separation for pivot counts growing arbitrarily with dimension. The counterexample is one-pivot and the exact comparison handles all \(1\le k\le n-1\). Historical publication priority is not independently certified: specialized earlier work could contain an equivalent formula or a reduction not identified in the inspected sources.

## References

1. Y. Chen, E. N. Epperly, J. A. Tropp, R. J. Webber, *Randomly pivoted Cholesky: Practical approximation of a kernel matrix with few entry evaluations*, arXiv:2207.06503 (initial posting July 13, 2022), https://arxiv.org/abs/2207.06503.
2. S. Steinerberger, *Randomly Pivoted Partial Cholesky: Random How?*, arXiv:2404.11487 (initial posting April 17, 2024), https://arxiv.org/abs/2404.11487.
3. E. N. W. Epperly, *A new analysis of the randomly pivoted Cholesky algorithm*, arXiv:2608.20633 (initial posting August 21, 2026), https://arxiv.org/abs/2608.20633.
