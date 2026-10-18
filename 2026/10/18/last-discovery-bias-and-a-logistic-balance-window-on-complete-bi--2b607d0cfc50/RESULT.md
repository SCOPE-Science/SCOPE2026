# Last-discovery bias and a logistic balance window on complete bipartite graphs

## Finding

Let \(K_{a,b}\) be the complete bipartite graph with parts \(A\) and \(B\) of sizes \(a,b\geq1\). A simple discrete-time random walk starts from one specified vertex of \(A\) and stops the first time all vertices have been visited. Write \(L\) for its last newly visited vertex and \(p_{a,b}=\Pr(L\in B)\). For \(m\geq1\), let \(C_m\) denote the number of independent uniform draws from \(m\) coupon types needed to observe all types, including the first draw. All coupon collectors in a joint comparison below are independent.

**Exact law.** For every \(a,b\geq1\),
\[
p_{a,b}=\Pr(C_b\geq C_a)
=\sum_{j=1}^{b}(-1)^{j+1}\binom bj
\prod_{k=1}^{a-1}\frac{(k/a)(1-j/b)}{1-(1-k/a)(1-j/b)}.
\]
The empty product is \(1\). Each of the \(b\) vertices in \(B\) is last with probability \(p_{a,b}/b\); each of the \(a-1\) vertices of \(A\) other than the start is last with probability \((1-p_{a,b})/(a-1)\) when \(a\geq2\). The starting vertex is never last unless the graph consists of one vertex, which is excluded here.

**Sharp finite majority boundary.** For every positive integer pair,
\[
p_{a,b}>\tfrac12\ \Longleftrightarrow\ b\geq a,
\qquad p_{a,b}<\tfrac12\ \Longleftrightarrow\ b<a.
\]
In particular, equality with \(1/2\) never occurs. On the balanced graph \(K_{n,n}\), \(n\geq2\),
\[
p_{n,n}=\tfrac12+\tfrac12\Pr(C_n=C_n'),
\]
where \(C_n'\) is an independent copy of \(C_n\). The parity of the last visit gives the opposite part a strict advantage even when the parts have equal size.

**Logistic balance window.** Suppose \(a=n\to\infty\), \(b=b_n\) is an integer, \(b_n/n\to1\), and
\[
\frac{(b_n-n)\log n}{n}\longrightarrow c\in\mathbb R.
\]
Then
\[
p_{n,b_n}\longrightarrow\frac1{1+e^{-c}}.
\]
If the displayed scaled imbalance tends to \(+\infty\) or \(-\infty\) while \(b_n/n\to1\), the limit is respectively \(1\) or \(0\). Thus the nontrivial competition window has part-size difference of order \(n/\log n\).

**Quantitative near-uniformity in balance.** Let \(\nu_n\) be the law of \(L\) on the \(2n-1\) vertices other than the start, and let \(u_n\) be uniform on those vertices. Then
\[
\Pr(C_n=C_n')\sim\frac1{4n},\qquad
p_{n,n}=\frac12+\frac1{8n}+o(n^{-1}),\qquad
\|\nu_n-u_n\|_{\rm TV}\sim\frac1{8n}.
\]
The exact last-vertex distribution is nonuniform for \(n\geq3\), but it approaches uniformity with this sharp total-variation constant. For \(n=2\), \(K_{2,2}\) is a cycle and the distribution is exactly uniform.

## Assumptions and scope

The graph is finite, simple, connected, and complete bipartite, with both part sizes positive. The walk is the non-lazy nearest-neighbour walk choosing uniformly among all neighbours. Every vertex of the opposite part is chosen uniformly and independently of the past, so successive visits to the same part form an iid uniform sample. Time counts graph edges traversed; the initially occupied vertex is already visited at time zero. Logarithms are natural. The limiting statements are for deterministic integer sequences of part sizes satisfying the displayed hypotheses; no independence between graph sizes is needed. The formula concerns the side and identity of the *last first-visit*, not the vertex at a fixed observation time nor the location after an additional move.

## Proof

**1. Reduction to two independent collectors.** Visits to \(B\) occur at times \(1,3,5,\ldots\), while subsequent visits to \(A\) occur at times \(2,4,6,\ldots\). Their vertex labels form two independent iid uniform streams. Let \(T_A\) be the number of even-time visits required to see the \(a-1\) vertices of \(A\) other than the starting vertex, and \(T_B\) the number of odd-time visits required to see all \(b\) vertices of \(B\). Then \(T_A,T_B\) are independent. Since the first draw of a standard collector always sees a new type, exchangeability gives \(T_A\stackrel d=C_a-1\), while \(T_B\stackrel d=C_b\). Their graph completion times are \(2T_A\) and \(2T_B-1\). Consequently \(L\in B\) precisely when \(T_B>T_A\), proving \(p_{a,b}=\Pr(C_b\geq C_a)\). The identity of the last vertex, conditional on its part, is uniform by permutation symmetry.

**2. Rational formula.** The standard coupon collector has the independent geometric-stage decomposition
\[
C_m\stackrel d=\sum_{k=1}^{m}G_{k,m},
\qquad \Pr(G_{k,m}=r)=\frac{k}{m}\left(1-\frac{k}{m}\right)^{r-1},\quad r=1,2,\ldots.
\]
Thus \(T_A\) has probability-generating function
\[
Q_a(z)=\mathbb E[z^{T_A}]
=\prod_{k=1}^{a-1}\frac{(k/a)z}{1-(1-k/a)z}
\quad(0\leq z\leq1).
\]
Inclusion-exclusion for the coupons absent after \(t\) draws yields
\[
\Pr(T_B>t)=\sum_{j=1}^{b}(-1)^{j+1}\binom bj(1-j/b)^t,
\qquad t=0,1,\ldots.
\]
Taking the expectation at \(t=T_A\) proves the displayed rational formula, including the boundary cases \(a=1\) or \(b=1\).

**3. Exact majority boundary.** Independent geometric variables can be coupled monotonically in their success probabilities. If \(b\geq a\geq2\), comparison term-by-term in the geometric-stage decomposition (adding the extra stages when \(b>a\)) shows \(C_b\) stochastically dominates \(C_a\). For \(b=a\), iid symmetry gives
\[
\Pr(C_a'\geq C_a)=\tfrac12\bigl(1+\Pr(C_a'=C_a)\bigr)>\tfrac12.
\]
Therefore \(p_{a,b}>1/2\) for \(b\geq a\). The case \(a=1\) has \(p_{1,b}=1\).

If \(b\leq a-1\), the variable \(T_A=\sum_{k=1}^{a-1}G_{k,a}\) stochastically dominates a full \(b\)-coupon collection \(C_b'\), because for \(k\leq b\) its geometric stage has success probability \(k/a\leq k/b\), with extra nonnegative stages. Take \(C_b'\) independently of \(C_b\), preserving independence from \(T_A\). Then
\[
p_{a,b}=\Pr(C_b>T_A)
\leq\Pr(C_b>C_b')
=\tfrac12\bigl(1-\Pr(C_b=C_b')\bigr)<\tfrac12.
\]
Every inequality is strict as stated, completing the finite classification.

**4. Gumbel-to-logistic crossover.** For the standard collector, inclusion-exclusion gives
\[
\Pr(C_m\leq t)=\sum_{j=0}^m(-1)^j\binom mj(1-j/m)^t.
\]
At \(t=\lfloor m\log m+mx\rfloor\), the fixed-\(j\) terms converge to \((-1)^j e^{-jx}/j!\). Bonferroni bounds and then arbitrarily long fixed truncations prove
\[
(C_m-m\log m)/m\ \xrightarrow{\rm d}\ G,
\qquad\Pr(G\leq x)=e^{-e^{-x}}.
\]
Independent collectors have independent limiting Gumbels. With \(b_n/n\to1\) and \((b_n-n)\log n/n\to c\), expansion of \(b_n\log b_n\) gives
\[
\frac{C_{b_n}-C_n}{n}\ \xrightarrow{\rm d}\ c+G_B-G_A.
\]
The difference of two independent standard Gumbels has continuous logistic distribution, with cumulative distribution function \(x\mapsto(1+e^{-x})^{-1}\), as follows directly by integrating their densities. The event \(C_{b_n}\geq C_n\) therefore has the asserted limit. For scaled imbalance tending to either infinity, the centered collector times remain tight while the deterministic displacement diverges, giving the corresponding zero-one limits.

**5. Sharp balanced tie constant.** Let \(\phi_n(\theta)=\mathbb E[e^{i\theta C_n}]\). Fourier inversion on the integers and independence give
\[
q_n:=\Pr(C_n=C_n')=\frac1{2\pi}\int_{-\pi}^{\pi}|\phi_n(\theta)|^2\,d\theta.
\]
Use \(t=n\theta\). One geometric factor in \(C_n\), with success probability \(1/n\), gives for \(n\geq2\), \(|t|\leq\pi n\),
\[
|\phi_n(t/n)|^2\leq
\frac1{1+2n(n-1)(1-\cos(t/n))}
\leq\frac1{1+2t^2/\pi^2}.
\]
The other geometric factors have characteristic-function modulus at most one. The Gumbel limit in step 4 implies pointwise convergence \(|\phi_n(t/n)|^2\to|\phi_G(t)|^2\). Dominated convergence and Plancherel, applied to the standard Gumbel density \(g(x)=e^{-x-e^{-x}}\), now give
\[
\lim_{n\to\infty}nq_n
=\frac1{2\pi}\int_{\mathbb R}|\phi_G(t)|^2dt
=\int_{\mathbb R}g(x)^2dx
=\int_0^\infty y e^{-2y}dy=\frac14.
\]
Thus \(p_{n,n}=1/2+q_n/2=1/2+1/(8n)+o(n^{-1})\). By within-part exchangeability, the two measures \(\nu_n\) and \(u_n\) have constant masses within each of the two unvisited vertex orbits, whence
\[
\|\nu_n-u_n\|_{\rm TV}
=\left|p_{n,n}-\frac{n}{2n-1}\right|
=\frac1{8n}+o(n^{-1}).
\]
This proves all assertions.

## Verification

The standalone Python 3 program `verify.py` implements the finite product/inclusion-exclusion formula using rational arithmetic and separately solves the exact Markov first-step equations on visited-count states. It compares the two methods for all \(1\leq a,b\leq10\), checks the strict majority dichotomy, and checks exact small cases. Running `python3 verify.py` produces `PASS: 314 independent exact-rational assertions`. The independent numerical occupancy calculation, not needed for the proof, found the scaled balanced tie probabilities \(n\Pr(C_n=C_n')\) decreasing toward \(1/4\) and scaled uniform total-variation distances increasing toward \(1/8\). The proof of the asymptotic constants is the analytic Fourier argument above; no finite computation is used as an infinite certificate.

## Relationship to prior work

Lovász and Winkler (1993) characterize graphs whose last newly visited vertex is exactly uniform from every start. Buchanan, Horn and Rombach (2022) extend the characterization to directed graphs, with a structural inequality comparing neighbours and non-neighbours. Ohwa and Shirai (2008) give a general inclusion-exclusion expression for the joint distribution of a finite Markov chain's cover time and last visited point; this general tool is fully credited and is not claimed as new. Classical coupon-collector theory supplies the geometric-stage representation and Gumbel limit, and the logistic difference of two Gumbels is standard.

The result here is the explicit complete-bipartite last-visit law together with its strict all-size majority boundary, sharp \(n/\log n\) logistic competition window and exact \(1/(8n)\) total-variation asymptotic against uniform last-vertex selection. The general formulas and qualitative classification in the inspected primary texts do not themselves state these graph-specific quantitative conclusions. The finite law can also be recovered by specializing general Markov-chain formulas; the nontrivial new comparison is its sharp finite and asymptotic behavior.

## Limitations

Only complete bipartite, unweighted, non-lazy simple random walks are treated. The logistic window requires both part sizes to grow comparably; the theorem makes no claim for arbitrary sparse bipartite graphs, varying transition weights, or dependent visit subsequences. The finite rational formula may suffer cancellation if evaluated in floating point and should be evaluated with exact rational arithmetic or stable recurrences. The \(1/(8n)\) asymptotic is not an exact equality at finite \(n\). A 1993 publisher article was not available in full text through attempted accessible routes; its published qualitative theorem is credited and residual historical-priority uncertainty remains. Same-paper overlap against other historical graph-cover literature cannot be ruled out independently.

## References

1. C. Buchanan, P. Horn and P. Rombach, *On the Last New Vertex Visited by a Random Walk in a Directed Graph*, arXiv:2209.08079 (first posted 2022-09-16), subsequently Discrete Mathematics Letters **11** (2023), 96–98. https://arxiv.org/abs/2209.08079
2. T. Ohwa and T. Shirai, *Joint Distribution of the Cover Time and the Last Visited Point of Finite Markov Chains*, Kyushu Journal of Mathematics **62** (2008), 281–292. https://doi.org/10.2206/kyushujm.62.281
3. L. Lovász and P. Winkler, *A Note on the Last New Vertex Visited by a Random Walk*, Journal of Graph Theory **17** (1993), 593–596. https://doi.org/10.1002/jgt.3190170505
4. A. Pósfai, *Approximation Theorems Related to the Coupon Collector's Problem*, arXiv:1006.3531 (2010). https://arxiv.org/abs/1006.3531
