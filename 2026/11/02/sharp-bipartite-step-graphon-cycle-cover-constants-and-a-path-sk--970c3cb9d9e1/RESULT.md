# Sharp bipartite step-graphon cycle-cover constants and a path-skeleton law

## Finding

Let \(W\) be a fixed finite symmetric step-graphon whose block masses \(x_i^*>0\) sum to one, and whose support skeleton \(S\) is a connected, loopless, bipartite graph with colour classes \(U,V\). Every supported inter-block edge probability is fixed and strictly positive, and all unsupported probabilities are zero. Let
\[
\mathcal C_S=\operatorname{cone}\{(e_i+e_j)/2:ij\in E(S)\}.
\]
Assume \(x^*\in\mathcal C_S\). For the simple random graph \(G_n\) sampled from \(W\), let \(P_n(W)\) be the probability of a spanning undirected \(2\)-regular subgraph (a vertex-disjoint cycle cover). The same conclusion holds for the symmetric-directed cycle-cover convention that permits opposite-arc \(2\)-cycles.

The balance condition \(\sum_{i\in U}x_i^*=\sum_{j\in V}x_j^*=1/2\) is automatic. Put \(p^U=(2x_i^*)_{i\in U}\), \(p^V=(2x_j^*)_{j\in V}\), and take an independent, centered Gaussian pair \(Z=(Z_U,Z_V)\) with
\[
\operatorname{Cov}(Z_U)=\tfrac12(\operatorname{diag}(p^U)-p^U(p^U)^\top),\qquad
\operatorname{Cov}(Z_V)=\tfrac12(\operatorname{diag}(p^V)-p^V(p^V)^\top).
\]
Let \(T\) be the tangent cone to \(\mathcal C_S\) at \(x^*\), intersected with the balance-direction space \(\{z:\sum_Uz_i=\sum_Vz_j=0\}\). Set \(\theta(S,x^*)=\Pr(Z\in T)\); equivalently, impose the nonnegative inequalities of all **relative** edge-cone facets active at \(x^*\), working in the linear balance hyperplane. Then \(0<\theta(S,x^*)\le1\) and
\[
P_{2m+1}(W)=0,\qquad
\lim_{m\to\infty}\sqrt{2m}\,P_{2m}(W)=\sqrt{2/\pi}\,\theta(S,x^*).
\]
In particular, if \(S=P_{2r}\) is the path on \(2r\) blocks, all block masses equal \(1/(2r)\), and arbitrary fixed positive probabilities are assigned along path edges, then for every fixed integer \(r\ge1\),
\[
\boxed{\lim_{m\to\infty}\sqrt{2m}\,P_{2m}(W)=\frac1r\sqrt{\frac2\pi}.}
\]
Thus the exact leading constant can be any \(1/r\) fraction of the balanced two-block benchmark while the decay exponent stays \(1/2\).

## Assumptions and scope

All graphons and their block counts are fixed as \(n\to\infty\); no supported edge probability tends to zero. The colour classes \(U,V\) are the unique bipartition up to reversal because \(S\) is connected. A spanning undirected \(2\)-regular subgraph means a disjoint union of simple cycles of length at least three; all its cycles are even under bipartiteness. The symmetric-directed convention mentioned above allows directed length-two cycles. For block sizes linear in \(n\), both events have the displayed leading constant. For a cone \(C\) and \(x\in C\), the tangent cone is \(T_C(x)=\overline{\{t(y-x):t\ge0,\ y\in C\}}\); it is polyhedral here. The Gaussian is supported on the \((q-2)\)-dimensional balance-direction subspace (under the convention \(q=2\), this space is zero-dimensional and \(\theta=1\)).

## Proof

**1. Reduction to random class counts with exponentially small error.** Let \(Y=(Y_i)\sim\operatorname{Multinomial}(n,x^*)\), so \(Y_i\) is the number of sampled graph vertices in block \(i\). The cited edge-cone necessity statement implies that every cycle cover forces \(Y\in\mathcal C_S\). Here the cone membership condition is invariant under positive rescaling. Conversely, fix a small compact neighbourhood \(B\) of \(x^*\) contained in the positive probability simplex. For every integer vector \(Y\in\mathcal C_S\) with \(Y/n\in B\), all \(Y_i\ge3\) for sufficiently large \(n\). The deterministic complete-\(S\)-partite cycle-cover theorem therefore supplies a spanning degree-two subgraph of the complete blow-up with these class sizes. The fixed-skeleton blow-up embedding lemma puts that bounded-degree subgraph into any appropriately super-regular supported inter-block graph.

We verify rather than assume the necessary high-probability regularity. Write \(p_*=\min_{ij\in E(S)}W_{ij}>0\), and choose \(\delta=p_*/4\) and the associated sufficiently small fixed regularity parameter \(\varepsilon>0\). Conditional on any \(Y/n\in B\), every supported pair comprises two classes of at least \(bn\) vertices, for fixed \(b>0\). Each vertex's cross-degree exceeds \(\delta\) times the partner size except with probability \(e^{-c_1 n}\) by a binomial Chernoff estimate. Every pair of subsets each occupying an \(\varepsilon\)-fraction of its parent class has cross-density exceeding \(\delta\), except with probability \(e^{-c_2 n^2}\), again by Chernoff. There are at most \(4^n\) pairs of such subsets. A union bound over the fixed supported pairs and all vertices yields a uniform \(O(e^{-cn})\) exceptional probability. Independently, multinomial Hoeffding bounds yield \(\Pr(Y/n\notin B)=O(e^{-cn})\). Therefore, for either permitted cycle-cover convention,
\[
0\le \Pr(Y\in\mathcal C_S)-P_n(W)\le C e^{-cn}.
\]
The proof of this reduction does not assume that every empirical concentration lies in the cone; it applies uniformly to those inside it.

**2. Exact balance and the local central limit factor.** Since every edge of \(S\) joins \(U\) to \(V\), every vector in the edge cone has equal total mass on the two sides. Consequently \(x^*\in\mathcal C_S\) forces mass \(1/2\) on each side. Writing \(B_n=\sum_{i\in U}Y_i\), the binomial law gives \(B_n\sim\operatorname{Binomial}(n,1/2)\). For odd \(n\) equality of the side cardinalities is impossible, proving the zero statement. For \(n=2m\),
\[
\Pr(B_{2m}=m)=\frac{\binom{2m}{m}}{4^m}=\sqrt{\frac{2}{\pi(2m)}}(1+O(m^{-1})).
\]
Conditional on \(B_{2m}=m\), the two families of class counts are independent multinomials with \(m\) trials and vectors \(p^U,p^V\). Thus \(Z_m=(Y-2mx^*)/\sqrt{2m}\) converges jointly to the specified centered Gaussian, whose covariance is exactly one-half the usual within-side multinomial covariance. Its support is the balance-direction space and, because all \(x_i^*>0\), it is nondegenerate within that space.

**3. Tangent-cone conditional probability.** Inside its linear span (here the bipartite balance hyperplane), the polyhedral cone has finitely many relative linear facet inequalities. For every inequality strictly positive at \(x^*\), that inequality is automatically positive at \(x^*+z/\sqrt{2m}\) for all bounded \(z\) and sufficiently large \(m\). The remaining, active, inequalities reduce exactly to their corresponding homogeneous inequalities in \(z\). Thus, uniformly on bounded subsets of the balance-direction space, the indicator of \(Y/(2m)\in\mathcal C_S\) agrees eventually with the indicator of \(Z_m\in T\). The Gaussian assigns zero mass to the boundary of each nontrivial active inequality; inequalities vanishing identically on the balance-direction space are redundant. Tightness and the conditional multinomial central limit theorem give
\[
\Pr(Y\in\mathcal C_S\mid B_{2m}=m)\longrightarrow\Pr(Z\in T)=\theta(S,x^*).
\]
There is strictly positive Gaussian mass in the relative interior of \(T\): because \(x^*\) has strictly positive coordinates and \(\mathcal C_S\) has a nonempty relative interior inside the balance hyperplane, there is a relative-interior point \(y\in\mathcal C_S\) and the direction \(y-x^*\) satisfies all nonredundant active inequalities strictly. Hence \(\theta>0\). Multiplying the last display by the balanced-binomial probability and applying step 1 proves the general leading-constant law.

**4. Exact path constant.** Number the path vertices \(1,\ldots,2r\) and set \(A_j=Y_{2j-1}\), \(B_j=Y_{2j}\), for \(1\le j\le r\). Conditional on the balanced event, \((A_j)_j\) and \((B_j)_j\) are independent \(\operatorname{Multinomial}(m;(1/r,\ldots,1/r))\) vectors. The edge-cone equations \(Y_i=s_{i-1}+s_i\), with \(s_0=s_{2r}=0\) and \(s_i\ge0\), have the unique solution
\[
s_{2j}=\sum_{a=1}^j(B_a-A_a),\qquad
s_{2j-1}=A_j-\sum_{a=1}^{j-1}(B_a-A_a),
\]
with the balance condition ensuring the final boundary equation. For fixed \(r\), the odd-indexed \(s_{2j-1}\) are \(m/r+O_{\Pr}(\sqrt m)\), hence all strictly positive with conditional probability tending to one. The active constraints are therefore the partial-sum inequalities
\[
\sum_{a=1}^j(B_a-A_a)\ge0\qquad(1\le j<r).
\]
After scaling by \(\sqrt{2m}\), the increments converge to a centered exchangeable nondegenerate Gaussian bridge \((D_1,\ldots,D_r)\) with total zero. For \(r\ge2\), its partial sums at the \(r\) cyclic starting positions have a unique global minimum almost surely, since any nontrivial subinterval sum is a nondegenerate Gaussian. Exactly one of the \(r\) cyclic shifts has every proper partial sum nonnegative. Cyclic exchangeability therefore makes the probability of the specified shift equal to \(1/r\). When \(r=1\) the condition is empty and the same value is one. Consequently \(\theta(P_{2r},x^*)=1/r\), completing the proof.

## Verification

The standalone standard-library Python program `checks.py` constructs exact rational multinomial probabilities for balanced path occupancies. For fixed path sizes \(2r\), it independently compares the exact edge-cone recursion with an integral maximum-flow test of a block-level bipartite matching and checks the necessary prefix inequalities. It then enumerates small occupancy configurations and prints conditional cone probabilities and scaled balance contributions. Its saved output `checks.txt` reports `PASS: 4382 exact and numerical assertions`; the matched cone/matching and prefix comparisons account for \(4336\) of those assertions. The finite tests are not invoked as proof of the asymptotic coefficient, Gaussian convergence, embedding theorem, or uniform exponential bound; those are established in the argument above.

Reproduction: execute `python3 checks.py` from a directory containing the extracted file, and compare standard output with `checks.txt`. Python 3 standard library is the only dependency.

## Relationship to prior work

Gao, Hu, and Chen (2026), arXiv:2604.05138v1, Theorem 1(3) prove an \(O(n^{-1/2})\) upper bound in the connected bipartite-skeleton, in-cone regime; their Section 2 provides the required necessary-cone and blow-up ingredients. That work does not compute the leading constant. Gao and Chen (2025), arXiv:2502.14853, give a Gaussian-cone limit in the different nonbipartite residual regime, where the probability tends to a nonzero number rather than zero. Jiang and Chen (2026), arXiv:2603.27424v3, supply deterministic complete-blow-up \(2\)-regular-subgraph optimization but not random sampling coefficients. Chen (2025), arXiv:2510.02074, establishes zero-one results for **directed** step-graphons with independently sampled arcs, but does not provide the undirected bipartite leading coefficient derived here. The present claim is the combination of the bipartite lattice balance factor with a lower-dimensional conditional Gaussian tangent angle, plus the explicit exchangeable-bridge factor \(1/r\) for a path family. Classical local central limit and ballot/cycle-lemma methods are acknowledged as proof ingredients, not themselves new results.

## Limitations

The result is for a fixed number of blocks, strictly positive fixed supported probabilities, connected loopless bipartite skeleton, and an in-cone population vector. No uniformity in growing path length \(r\), vanishing edge probabilities, or nonbipartite skeletons is claimed. The theorem does not give a second-order expansion or a convergence rate for the conditional cone probability. The finite checker is not an exhaustive argument for arbitrary \(n\) or \(r\). Historical priority remains conditional on external literature inspection; no independent audit has been performed.

## References

1. W. Gao, H. Hu, and X. Chen, *Convergence rate of H-property for step-graphons*, arXiv:2604.05138v1 (first public version 2026-04-06), https://arxiv.org/html/2604.05138v1 .
2. W. Gao and X. Chen, *On the H-property for Step-graphons: The Residual Case*, arXiv:2502.14853 (first public 2025-02-20), https://arxiv.org/abs/2502.14853 .
3. Y. Jiang and X. Chen, *Largest 2-regular Subgraphs in Complete S-partite Graphs*, arXiv:2603.27424v3, https://arxiv.org/html/2603.27424v3 .
4. J. Komlós, G. N. Sárközy, and E. Szemerédi, *Blow-up Lemma*, Combinatorica 17 (1997), 109–123, referenced for the fixed-skeleton bounded-degree embedding used in [1].
5. X. Chen, *Hamiltonicity of Step-graphons*, arXiv:2510.02074 (first public 2025-10-02), https://arxiv.org/html/2510.02074 .
