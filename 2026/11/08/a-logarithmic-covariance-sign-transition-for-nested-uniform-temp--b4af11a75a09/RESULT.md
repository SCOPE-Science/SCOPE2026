# A logarithmic covariance sign transition for nested uniform temporal trees

## Finding

Consider a rooted infinite complete \(n\)-ary tree, where \(n\ge2\). Independently label every edge uniformly in \([0,1]\). For \(p\in[0,1]\), let \(T_n(p)\) count the root and all vertices reached by a strictly decreasing sequence of edge labels, each below \(p\). All values of \(p\) use **the same edge labels**, so \(T_n(p)\le T_n(q)\) whenever \(p\le q\).

**Theorem (exact covariance and its sign transition).** For all integers \(n\ge2\) and \(0<p\le q\le1\),
\[
\begin{aligned}
\mathbb E T_n(p)&=e^{np},\\
\operatorname{Cov}(T_n(p),T_n(q))
 &=\frac{e^{2np}(1-e^{-np})}{n}
 \left[n-1+\frac{2np}{e^{np}-1}-e^{n(q-p)}\right].
\end{aligned}
\]
Put
\[
q_*(n,p)=p+\frac1n\log\left(n-1+\frac{2np}{e^{np}-1}\right).
\]
For a fixed \(n,p\), the covariance is strictly positive when \(p\le q<q_*(n,p)\), vanishes at \(q=q_*(n,p)\), and is strictly negative when \(q>q_*(n,p)\), subject to \(q\le1\). If \(q_*(n,p)>1\), it remains positive throughout the available range. In particular, nesting does **not** imply nonnegative covariance. For example, \(q_*(2,0.4)=0.8176587522849861\ldots\).

**Theorem (sharp crossover).** For each fixed \(p\in(0,1)\) and \(x\in\mathbb R\), choose \(q_n=p+(\log n+x)/n\) for all sufficiently large \(n\). Then
\[
\frac{\operatorname{Cov}(T_n(p),T_n(q_n))}{e^{2np}}
 \longrightarrow 1-e^x,
\qquad
q_*(n,p)-p=\frac{\log n+o(1)}n.
\]
For any fixed \(t\ge0\), the microscopic correlation profile is
\[
\operatorname{Corr}(T_n(p),T_n(p+t/n))\longrightarrow e^{-t}.
\]
For any fixed \(p<q\), the correlation instead satisfies
\[
\operatorname{Corr}(T_n(p),T_n(q))=-\frac1n+o(n^{-1}).
\]
These assertions concern the same coupled trees at all thresholds, not independently sampled trees.

**Additional multithreshold consequence.** For any fixed \(0<p_1<\cdots<p_m\le1\),
\[
\big(e^{-np_1}T_n(p_1),\ldots,e^{-np_m}T_n(p_m)\big)
\ \Longrightarrow\ (E_1,\ldots,E_m),
\]
where the \(E_j\) are *independent* mean-one exponential random variables. This extends the published one-threshold exponential limit to the natural common-label coupling.

## Assumptions and scope

The infinite ambient tree is deterministic and each vertex has exactly \(n\) children. All edge labels are independent continuous uniform variables. There is no vertex-label at the root beyond the threshold \(p\), and all thresholded trees are defined from one shared set of edge labels. The size \(T_n(p)\) includes the root. Every such size is finite almost surely, since its expected value is finite. Parameters in the exact formula satisfy \(n\in\{2,3,\ldots\}\), \(0<p\le q\le1\); the \(p=0\) case is deterministic and has zero covariance. The crossover statements fix \(p\) strictly between zero and one before taking \(n\to\infty\). They do not assert a uniform limit when \(p=p_n\to0\) or \(1\).

## Proof

**Root decomposition.** If \(U_1,\ldots,U_n\) are the labels on the root's edges, let \(S_i(u)\) be the size of the descending-label subtree rooted at child \(i\) when that child's entering label is \(u\); conditionally on \(U_i=u\), this has the same law as \(T_n(u)\). Distinct child subtrees and labels are independent. For \(0\le p\le1\),
\[
T_n(p)=1+\sum_{i=1}^n \mathbf1_{\{U_i<p\}}S_i(U_i).
\]
Consequently, writing \(m(p)=\mathbb E T_n(p)\),
\[
m(p)=1+n\int_0^p m(u)\,du,
\qquad m(0)=1,
\]
so \(m(p)=e^{np}\). The integrations are valid by Tonelli, since the summands are nonnegative.

**Second moment.** Write \(f(p)=\mathbb E T_n(p)^2\). Independence of child terms gives
\[
f(p)=m(p)^2+n\int_0^p f(u)\,du-
 n\left(\int_0^p m(u)\,du\right)^2.
\]
Since \(\int_0^p m(u)\,du=(e^{np}-1)/n\), differentiation yields
\[
f'(p)=nf(p)+(2n-2)e^{2np}+2e^{np},
\qquad f(0)=1.
\]
Solving the linear equation gives
\[
f(p)=(2-2/n)e^{2np}+(2p-1+2/n)e^{np},
\]
which is finite and, after subtraction of \(m(p)^2\), gives the variance
\[
\operatorname{Var}T_n(p)=(1-2/n)e^{2np}+(2p-1+2/n)e^{np}.
\]
All identities can also be obtained first for depth-truncated trees and passed to the limit by monotone convergence; the displayed finite solution justifies all second moments.

**Disjoint root-label bins.** For \(p\le q\), the additional vertices in \(T_n(q)-T_n(p)\) originate precisely from children whose entering labels lie in \([p,q)\); a child's entire descending subtree then belongs to one bin. Hence, for each root child, the contributions to \(T_n(p)\) and to the increment are mutually exclusive. Their per-child product is zero, and their expectations are respectively \((e^{np}-1)/n\) and \((e^{nq}-e^{np})/n\). Cross-child terms have zero covariance. Therefore
\[
\operatorname{Cov}(T_n(p),T_n(q))
=\operatorname{Var}T_n(p)-\frac{(e^{np}-1)(e^{nq}-e^{np})}{n}.
\]
Insert the variance formula and factor to obtain the exact theorem. Since \(q\mapsto e^{n(q-p)}\) is strictly increasing and the prefactor is positive for \(p>0\), there is at most one crossing and its unique algebraic candidate is \(q_*\). For \(n\ge2\), the bracket at \(q=p\) is strictly positive, proving \(q_*>p\). The candidate lies within the permitted threshold interval exactly when \(q_*\le1\).

**Scaling.** For fixed \(p\in(0,1)\), \(e^{-np}\to0\) and
\[
R_n(p):=n-1+\frac{2np}{e^{np}-1}=n-1+o(1).
\]
Inserting \(n(q_n-p)=\log n+x\) into the factored covariance proves the limit \(1-e^x\). Taking logarithms of \(R_n(p)\) proves the location of \(q_*\). The normalized variance satisfies
\[
e^{-2np}\operatorname{Var}T_n(p)
=1-2/n+(2p-1+2/n)e^{-np}\longrightarrow1.
\]
Combining this expression at \(p\) and \(q\) with the exact covariance proves the microscopic correlation limit for \(q=p+t/n\). For fixed \(p<q\), normalized covariance equals
\[
\frac{\operatorname{Cov}(T_n(p),T_n(q))}{e^{n(p+q)}}
=\frac{1-e^{-np}}n\left[R_n(p)e^{-n(q-p)}-1\right]
=-\frac1n+o(n^{-1}),
\]
and normalized variances approach one, proving the final correlation claim.

**Joint exponential limit.** The cited one-threshold theorem of Atamanchuk–Devroye–Lugosi gives \(e^{-np}T_n(p)\Longrightarrow\operatorname{Exp}(1)\) for each fixed \(p>0\). Put \(p_0=0\) and \(I_{n,j}=T_n(p_j)-T_n(p_{j-1})\). Since \(\mathbb E T_n(p_{j-1})/e^{np_j}=e^{-n(p_j-p_{j-1})}\to0\), each \(e^{-np_j}I_{n,j}\) has the same limiting exponential law. For \(t_j\ge0\) define
\[
a_{n,j}(t_j)=\int_{p_{j-1}}^{p_j}
 \mathbb E\left[1-e^{-t_j e^{-np_j}T_n(u)}\right]du.
\]
The root-bin decomposition and independence across children imply the exact joint Laplace transform
\[
\mathbb E e^{-\sum_j t_j e^{-np_j}I_{n,j}}
=\left(1-\sum_j a_{n,j}(t_j)\right)^n,
\qquad
\mathbb E e^{-t_j e^{-np_j}I_{n,j}}=(1-a_{n,j}(t_j))^n.
\]
The inequality \(1-e^{-z}\le z\) and \(\mathbb E T_n(u)=e^{nu}\) give \(0\le a_{n,j}(t_j)\le t_j/n\). Thus the joint Laplace transform differs from the product of the marginal Laplace transforms by \(O_{m,\mathbf t}(n^{-1})\). The marginals converge to \((1+t_j)^{-1}\), so the joint Laplace transform tends to \(\prod_j(1+t_j)^{-1}\), the law of independent exponentials. Since \(e^{-np_j}(T_n(p_j)-I_{n,j})\to0\) in \(L^1\), the same joint limit holds for the normalized total sizes. This uses the one-threshold published result only, without assuming joint independence beforehand.

## Verification

The standalone standard-library script \(\texttt{verify.py}\) implements two algebraic forms of the exact covariance, the threshold crossing and its asymptotic normalizations. It also constructs moments of independently depth-truncated trees as *exact rational polynomials*, with truncation depths up to seventeen, and compares the resulting covariance against the infinite-tree formula. Independent direct tree simulations of four small-parameter cases check both positive and negative covariance. The script completed 301 finite assertions. These diagnostics are not proofs of the infinite statements; the proof above establishes their scope.

## Relationship to prior work

Atamanchuk, Devroye and Lugosi define the uniform temporal tree and prove the one-threshold mean and exponential size limit (arXiv:2501.13044, Theorem 2.1). They also study height, typical depth and expected degrees. Those results alone do not specify the covariance of **the same tree** at two distinct thresholds, its sign reversal, or the logarithmic crossover. The present derivation uses their model and their one-threshold theorem for the final joint exponential consequence, while the finite-parameter covariance and its sign classification are derived independently above.

Hu, Wu and Dong (2022) study accessible-vertex counts across **depth cutoffs** in an \(N\)-ary tree under a fixed root value and derive pair-accessibility probabilities. A depth cutoff is not a shared-label threshold, and its joint distribution does not by itself give the two-threshold covariance. Their pair-counting methods are closely related and constitute an important priority comparison. The search and material inspection do not establish definitive historical uniqueness.

## Limitations

The covariance theorem is for a complete deterministic branching tree with independent atomless uniform edge labels and a **shared** coupling across thresholds. It does not automatically extend to random branching factors, dependent timestamps, or graphs with cycles. The crossover assumes fixed interior \(p\); boundary regimes when \(p\) depends on \(n\) are not treated. The multi-threshold weak limit is not a functional limit in the entire threshold parameter. Historical priority has not been independently certified. The 2022 accessibility article's complete PDF was not inspected, so additional formulas there or in other literature remain a residual risk.

## References

1. C. Atamanchuk, L. Devroye, G. Lugosi, *Uniform temporal trees*, arXiv:2501.13044, first posted 22 January 2025, https://arxiv.org/html/2501.13044 ; journal version *Random Structures & Algorithms* 67 (2025), e70040, https://doi.org/10.1002/rsa.70040.
2. Z. Hu, J. Wu, L. Dong, *Accessibility percolation on N-ary trees*, *Journal of the University of Science and Technology of China* 52 (2022), https://doi.org/10.52396/JUSTC-2022-0059.
3. S. Nowak, J. Krug, *Accessibility percolation on n-trees*, *Europhysics Letters* 101 (2013), 66004, https://arxiv.org/abs/1302.1423.
