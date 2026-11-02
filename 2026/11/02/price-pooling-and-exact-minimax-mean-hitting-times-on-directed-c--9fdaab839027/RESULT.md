# Price pooling and exact minimax mean hitting times on directed cycles

## Finding

For every integer \(n\ge3\), every vector of strictly positive prices \(p_1,\ldots,p_n\), and every budget \(B>0\), the unique globally optimal allocation of transition rates on a one-way continuous-time Markov cycle, minimizing the **largest mean first-hitting time between distinct states**, is explicit.

Let \((u)_+=\max\{u,0\}\). Define \(c\) as the unique positive solution of
\[
\sum_{i=1}^n\left(1-\frac{p_i}{c}\right)_+=1,
\qquad
M=\sum_{i=1}^n\frac{p_i}{\sqrt{\max\{p_i,c\}}}.
\]
Then the unique minimizing rates and optimal worst mean first-hitting time are
\[
\boxed{r_i^*=\frac{B}{M\sqrt{\max\{p_i,c\}}}},
\qquad
\boxed{T_* = \frac{M^2}{B}}.
\]
The positive-rate optimum **always exists and is unique**, even at every price tie. All edges with \(p_i\le c\) have the same optimal rate; edges with \(p_i>c\) have optimal rates inversely proportional to the square roots of their prices. This is an endogenous price-pooling transition, not an imposed equality constraint.

For the three-state family with prices \((1,1,Q)\), the critical price is \(Q=2\):
\[
T_*=\frac{1}{B}\begin{cases}
2(2+Q),&0<Q\le2,\\
(\sqrt2+\sqrt Q)^2,&Q\ge2.
\end{cases}
\]
The corresponding rates are all equal for \(Q\le2\); when \(Q>2\), the two unit-price transitions remain equal while the expensive transition follows the square-root rule.

## Assumptions and scope

The states are the vertices \(1,\ldots,n\) of a directed cycle. From state \(i\), the chain jumps only to \(i+1\pmod n\) at freely selected rate \(r_i>0\). Holding times are exponential with means \(h_i=1/r_i\). Each rate has independent linear price \(p_i>0\), and admissible allocations satisfy \(\sum_i p_i r_i\le B\). For distinct states \(i,j\), \(\tau_j\) is the first hitting time of \(j\), starting at \(i\); no return time with \(i=j\) is included. The criterion is the maximum of these expectations over **all ordered distinct pairs**. No stationary initial distribution is assumed.

The theorem is for a single directed cycle, not reversible chains, chains with extra arcs, or any fixed stationary-target averaging criterion. Rates must remain strictly positive, and all asserted optima lie within that domain.

## Proof

**1. Reduction of first-hitting times.** Starting at \(i\), reaching \(j\ne i\) requires one clockwise traversal of each edge on the unique forward arc of length between \(1\) and \(n-1\). By linearity of expectation and the exponential holding law,
\[
\mathbb E_i\tau_j=\sum_{k\in\mathrm{arc}(i,j)}h_k.
\]
Since all \(h_k>0\), any such arc may be extended to a clockwise arc of length \(n-1\) without decreasing its total. The latter arcs are exactly those omitting one edge. Therefore
\[
T(r):=\max_{i\ne j}\mathbb E_i\tau_j
=\max_{1\le i\le n}\sum_{j\ne i}h_j
=\sum_{j=1}^n h_j-\min_j h_j.
\]
Writing the cost in holding times gives \(\sum_i p_i/h_i\le B\). As rates are scaled up uniformly, every mean hitting time decreases; hence every optimum saturates this budget.

**2. A unique price level.** Consider \(F(c)=\sum_i(1-p_i/c)_+\) for \(c>0\). It is continuous, vanishes through \(c=\min_i p_i\), and increases strictly thereafter until its limit \(n>1\). Thus exactly one \(c>\min_i p_i\) satisfies \(F(c)=1\). In particular, at least two prices are strictly below \(c\). Define
\[
\lambda_i=\left(1-\frac{p_i}{c}\right)_+,
\qquad a_i=1-\lambda_i=\min\left\{1,\frac{p_i}{c}\right\}>0.
\]
The nonnegative numbers \(\lambda_i\) sum to one, while \(a_i p_i=p_i^2/\max\{p_i,c\}\).

**3. Sharp global lower bound.** For any positive holding times, the worst omitted-edge sum is at least its convex average with weights \(\lambda_i\). Consequently,
\[
T(r)\ge\sum_i\lambda_i\sum_{j\ne i}h_j
=\sum_j a_j h_j.
\]
Cauchy--Schwarz and the budget now yield
\[
T(r)\ge\sum_i a_i h_i
\ge\frac{\big(\sum_i\sqrt{a_i p_i}\big)^2}{\sum_i p_i/h_i}
\ge\frac{M^2}{B},
\]
where \(\sum_i\sqrt{a_i p_i}=\sum_i p_i/\sqrt{\max\{p_i,c\}}=M\).

**4. Attainment.** Set \(h_i^*=(M/B)\sqrt{\max\{p_i,c\}}\), so \(r_i^*=1/h_i^*\). Its cost is exactly \(B\). Whenever \(\lambda_i>0\), we have \(p_i<c\), so \(h_i^*=(M/B)\sqrt c\), the common minimum holding time. Hence every omitted-edge sum bearing positive \(\lambda_i\) equals \(T(r^*)\), and the convex-average inequality in step 3 is an equality. Moreover \(h_i^*\) realizes equality in Cauchy--Schwarz, so \(T(r^*)=M^2/B\).

**5. Global uniqueness and boundary prices.** Every globally optimal \(h\) must realize equality throughout step 3. Because each \(a_i,p_i,h_i\) is strictly positive, equality in Cauchy--Schwarz forces \(h_i=K\sqrt{p_i/a_i}=K\sqrt{\max\{p_i,c\}}\) with the same \(K>0\) for all \(i\). Budget equality then forces \(K=M/B\). This proves the *unrestricted* uniqueness of \(r^*\), including for \(p_i=c\), where \(\lambda_i=0\) but Cauchy--Schwarz still constrains that edge.

**6. Explicit price breakpoints.** Sort the prices \(p_{(1)}\le\cdots\le p_{(n)}\). If precisely \(k\) prices are strictly below \(c\), then \(k\ge2\) and
\[
c=\frac{\sum_{i=1}^{k}p_{(i)}}{k-1},
\quad p_{(k)}<c\le p_{(k+1)},
\]
with the final upper inequality omitted when \(k=n\). At a tie \(p_i=c\), one may instead include the tied index in the formula without changing \(c\). This gives a finite sorting-and-threshold algorithm and resolves every tie without arbitrary convention.

**7. A sharply priced single edge.** If the prices are \((1,1,Q)\), then all three lie at or below \(c=(2+Q)/2\) exactly when \(Q\le2\), giving \(M^2=2(2+Q)\). For \(Q\ge2\), \(c=2\), \(M=\sqrt2+\sqrt Q\), proving the stated crossover. More generally, when one price \(Q\) exceeds the price level determined by all remaining edges (assuming at least two others), that price level is fixed, and the optimum is a perfect square \(T_*=(\sqrt Q+M_0)^2/B\), with \(M_0\) determined by the other prices. The expensive edge's fraction of the purchased-rate budget is \(\sqrt Q/(\sqrt Q+M_0)\), which tends to one as \(Q\to\infty\), despite its own rate tending to zero.

## Verification

The included standalone `verify.py` reconstructs the root and allocation, checks budget and dual equality numerically, compares against thousands of independently generated feasible allocations, and conducts optional independently initialized nonlinear optimization comparisons. It passed **6,393 deterministic assertions** and **33 of 36 successful SLSQP optimizer comparisons**; the other three optimizer runs returned non-success flags and are not treated as impossibility or contradiction. These finite tests only corroborate the formulas: steps 1--7 prove the claims for all positive parameters.

Run `python3 verify.py` in a working directory containing that file. NumPy is not required. If SciPy is installed, the optional SLSQP block is also run; otherwise deterministic verification remains available. Expected deterministic result in the tested environment is `PASS 6393 deterministic checks`.

## Relationship to prior work

Classical Markov-chain hitting-time identities, including Aldous--Fill's general treatment, supply the probabilistic framework, not the price-allocation classification. Roch's 2004 *Bounding Fastest Mixing* treats reversible, discrete-time spectral mixing under graph transition restrictions; its semidefinite and variational results concern a different performance objective and a different admissible chain class.

Berman's 1964 continuous activity time--cost resource-allocation framework for PERT networks is a serious broad ancestor. Encoding the forward arcs as project paths connects the present problem to this general class of minimax resource allocation, but the accessible abstract does not provide the explicit price-pooling level, all-price optimizer, or this directed-cycle hitting-time identification. Best--Chakravarti--Ubhaya's separable convex chain-constraint algorithms treat prespecified coordinate order constraints, rather than the present cyclic omitted-edge family with *endogenous* price pooling. These general frameworks may furnish alternative solution methods; the assessed exact formulas and boundary classification are not claimed as a new generic convexity principle.

A separate stationary-target Kemeny optimization has a different averaging objective and price transition; it does not imply the worst-ordered-pair minimax formula above. Search and material access limitations are stated below rather than counted as proof of novelty.

## Limitations

The theorem does not cover multiple outgoing arcs, reversible or bidirectional transitions, fixed target-stationary laws, expected maximum random hitting times, return times, or the variance or tail distribution of hitting delays. Finite code checks are not independent formal proof. Specialist priority remains uncertain: only abstracts of the 1964 PERT and 2000 isotonic papers could be inspected, and the former's full paper remained inaccessible after arXiv/open-access searches and an authorized full-text access attempt. The general PERT method could potentially yield this special case after additional calculations, which limits the strength of any unconditional originality claim. Independent mathematical audit has not been performed.

## References

1. S. Roch, *Bounding Fastest Mixing*, first arXiv version September 22, 2004, https://arxiv.org/abs/math/0409429 (accessible full HTML, §§1--3 and later sections).
2. D. Aldous and J. Fill, *Reversible Markov Chains and Random Walks on Graphs*, Chapter 2, §2.2, https://www.stat.berkeley.edu/users/aldous/RWG/Book_Ralph/Ch2.S2.html (accessible full chapter section).
3. E. B. Berman, *Resource Allocation in a PERT Network Under Continuous Activity Time-Cost Functions*, *Management Science* 10(4), 734--745 (1964), https://doi.org/10.1287/mnsc.10.4.734 (abstract accessible; full text not inspected).
4. M. J. Best, N. Chakravarti and V. A. Ubhaya, *Minimizing Separable Convex Functions Subject to Simple Chain Constraints*, *SIAM Journal on Optimization* 10(3), 658--672 (2000), https://doi.org/10.1137/S1052623497314970 (abstract accessible; full text not inspected).
