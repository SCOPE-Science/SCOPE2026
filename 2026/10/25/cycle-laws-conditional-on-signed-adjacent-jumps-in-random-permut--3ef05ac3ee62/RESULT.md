# Cycle laws conditional on signed adjacent jumps in random permutations

## Finding
Let \(\Pi\) be uniform on the permutations of \([n]\), \(n\ge2\), and \(C\) its number of disjoint cycles. Independently choose \(I\) uniformly from \(\{1,\ldots,n-1\}\). For every nonzero integer \(d\) with \(|d|<n\), condition on the *signed positional jump* event
\[
E_d=\{\Pi(I+1)-\Pi(I)=d\}.
\]
Let \(B\) have the number-of-cycles law of a uniform permutation on \(n-2\) symbols, with \(B=0\) for \(n=2\). Then \(C\mid E_d\) has the law of the sum of independent \(B\) and \(W_d\), where
\[
\begin{array}{c|c}
\text{jump}&\text{law of }W_d\\ \hline
 d=1&2\operatorname{Bernoulli}(1/(n-1))\\
 2\le d<n&\operatorname{Bernoulli}(2/(n-1))\\
 d=-1&\operatorname{Bernoulli}((3n-5)/(n-1)^2)\\
 d=-h,\ 2\le h<n&\operatorname{Bernoulli}(2(n-h-1)/((n-1)(n-h))).
\end{array}
\]
Here \(2\operatorname{Bernoulli}(p)\) takes values \(0\) and \(2\), rather than being binomial with two trials. For every positive \(d\), \(\mathbb E[C\mid E_d]=H_n+1/(n(n-1))\). Nevertheless, when \(n\ge3\) and \(2\le d<n\), the law at \(d=1\) is strictly *larger in convex order* than at \(d\), with conditional variance higher by exactly \(2/(n-1)\).

For each signed \(d\), define the count \(K_d=\sum_{i=1}^{n-1}\mathbf1\{\Pi(i+1)-\Pi(i)=d\}\). Then
\[
\operatorname{Cov}(C,K_d)=
\begin{cases}
 (n-d)/(n^2(n-1)), &1\le d<n,\\
 (n^2-2n-1)/(n^2(n-1)),&d=-1,\\
 -(n+h)/(n^2(n-1)),&d=-h,\ 2\le h<n.
\end{cases}
\]
Thus positive jumps always correlate positively with cycles; jumps of size at most \(-2\) correlate negatively; the \(-1\) correlation is positive for \\(n\\ge3\\) and negative at \(n=2\).

## Assumptions and scope
The permutation is uniform on \(S_n\), interpreted as the function from positions to values. All \(n!\) permutations are equally likely. The position \(I\) is sampled **independently and uniformly** before conditioning. The conditioning event has probability \((n-|d|)/(n(n-1))\). Conditioning on \(E_d\) is *not* the same as conditioning on \(K_d>0\): it reweights permutations in proportion to their number of matching jumps. The harmonic number is \(H_n=\sum_{j=1}^{n}1/j\), with \(H_0=0\). A Bernoulli parameter equal to zero or one denotes a degenerate distribution.

## Proof
**1. Forced-edge contraction.** Fix a position \(i\) and a value \(v\) for which both \(v\) and \(v+d\) lie in \([n]\). The jump imposes two arrows in the functional digraph of \(\Pi\): \(i\to v\) and \(i+1\to v+d\). Both tails and heads are distinct, so the prescribed arrows form vertex-disjoint directed paths and possibly closed directed cycles. If exactly \(r\) cycles are closed by these two arrows, contract all prescribed paths and delete the closed cycles. There are \(n-2\) remaining supervertices; arbitrary permutations on these supervertices biject with the \((n-2)!\) completions, preserving the number of non-forced cycles. Therefore, conditional on the given \((i,v,d)\), the cycle count has the law \(B+r\). Its counting polynomial is \(t^r\prod_{j=0}^{n-3}(t+j)\), with an empty product for \(n=2\).

**2. Classifying closures.** Write \(m=n-|d|\), the number of allowed values of \(v\). Every pair \((i,v)\) is equiprobable given \(E_d\), among \((n-1)m\) pairs. If \(d=1\), the condition \(v=i\) occurs at each of the \(n-1\) sites and creates **two distinct one-cycles**; all other pairs close no cycles. If \(d>1\), exactly one cycle closes for each eligible pair with either \(v=i\) or \(v=i+1-d\). There are respectively \(n-d\) eligible pairs of each kind, hence \(2(n-d)\) one-cycle closures.

If \(d=-h\) with \(h\ge2\), closures arise at \(v=i\) when \(i\ge h+1\), or at \(v=i+1+h\) when \(i\le n-h-1\). Thus there are \(2(n-h-1)\) one-cycle closures. If \(d=-1\), these two self-loop mechanisms give \(2(n-2)\) pairs, and the extra case \(v=i+1\) closes a directed two-cycle for each of the \(n-1\) sites, giving \(3n-5\) one-cycle closures. These cases are distinct. Dividing by \((n-1)m\) yields exactly the four displayed laws of \(W_d\). Since the residual law of \(B\) is the same for every allowed pair, it may be taken independent of \(W_d\).

**3. Means, convex order, covariance.** The mean of \(B\) is \(H_{n-2}\). For every positive jump, \(\mathbb E W_d=2/(n-1)\), so \(\mathbb E(C\mid E_d)=H_n+1/(n(n-1))\). Put \(p=1/(n-1)\). The laws \(2\operatorname{Bernoulli}(p)\) and \(\operatorname{Bernoulli}(2p)\) share mean \(2p\). For any strictly convex function \(\varphi\) on the relevant finite set, their expectation difference is \(p[\varphi(0)-2\varphi(1)+\varphi(2)]>0\); averaging after an independent shift by \(B\) preserves strictness. Their variance difference is \(2p\).

For \(d=-1\), subtracting \(H_n=H_{n-2}+1/(n-1)+1/n\) from the conditional mean gives \((n^2-2n-1)/(n(n-1)^2)\). For \(d=-h\), \(2\le h<n\), it gives \(-(n+h)/(n(n-1)(n-h))\). Finally, \(\mathbb EK_d=(n-|d|)/n\) and \(\mathbb E[CK_d]=\mathbb EK_d\,\mathbb E[C\mid E_d]\), because uniform sampling of \(I\) is equivalent to size-biasing by \(K_d\). Multiplication by \((n-|d|)/n\) yields the covariance cases. The signs follow directly: \(n^2-2n-1>0\) for integer \(n\ge3\).

## Verification
The companion Python program `signed_jump_cycle_verify.py` reconstructs the exact local cycle-count laws for every permissible site and signed jump for \(2\le n\le8\) using integer enumeration of every permutation. It separately compares the pooled conditional law and the covariance against the displayed formulas using exact rational arithmetic. Output includes \(2,8,18,32,50,72,98\) local-law comparisons as \(n\) ranges from \(2\) through \(8\). This finite check supports the proof but is not a proof for unbounded \(n\).

## Relationship to prior work
Diaconis–Evans–Graham (2013 preprint) establish equality in law between the *set* of ordinary one-line positive-one successions and a restricted fixed-point set; the present joint dependence on the cycles of the **same** permutation is additional information, not supplied by equality of those marginal sets. Mansour–Shattuck (2016) count **cycle-form** successions jointly with cycle count and generalize to cycle-form positive-\(d\) adjacencies. Their paper explicitly explains that the bijection to ordinary one-line successions transforms cycles into left-to-right minima, so the cycle-form joint law does not give this conditioning on the original permutation's cycle count. Ma–Qi–Yeh–Yeh (2024 preprint) investigate ordinary successions jointly with Eulerian, left-to-right-minimum, and related statistics; no formula for this exact signed-jump conditional cycle law was identified in the inspected treatment. The forced-edge contraction used here is standard permutation counting; the contribution is the explicit signed classification, a positive-jump convex-order contrast, and the resulting exact sign boundary for cycle covariance.

## Limitations
Only adjacent **positions** and exact signed **value differences** in a uniform random permutation are considered. Sampling the adjacency site independently is essential. The result does not assert any stochastic ordering for conditioning on existence of a jump, nonuniform permutation measures, multiple simultaneous prescribed jumps, or the entire joint distribution of \(C\) with the full jump-count vector. Exact original-priority claims are limited by the possibility of equivalent specializations of general constrained-cycle enumerators not identified in the inspected sources.

## References
1. P. Diaconis, S. N. Evans, R. L. Graham, *Unseparated pairs and fixed points in random permutations*, arXiv:1308.5459v1, first posted 2013-08-25. https://arxiv.org/abs/1308.5459
2. T. Mansour, M. Shattuck, *Counting permutations by the number of successions within cycles*, Discrete Mathematics 339 (2016), 1368–1376, DOI:10.1016/j.disc.2015.12.004. https://doi.org/10.1016/j.disc.2015.12.004
3. S.-M. Ma, H. Qi, J. Yeh, Y.-N. Yeh, *On the joint distributions of succession and Eulerian statistics*, arXiv:2401.01760v1, first posted 2024-01-03. https://arxiv.org/abs/2401.01760
