# Leaf-label complements give an exact biclique lower bound for Krajíček search-tree error
## Finding
Fix a prime \(p\) and integers \(2\le d\le n/2\). Let \(T'\) be a \((d,e)\)-tree with leaf labels in \([n+1]\times[n]\) in Krajíček's reduced pigeonhole-principle search problem, and let \(S\subseteq[n+1]\times[n]\) be the set of distinct labels occurring at leaves. Sample \(\omega=(\rho,L)\) as in \(\Omega(n,d)\), so \(n_\rho=2d\), and put \(E(T')=\Pr[T'(\omega)\notin D^\rho\times R^\rho]\). With \(N=n+1\), \(M=n\), \(a=2d+1\), and \(b=2d\), let \(B_{a,b}(\overline S)\) be the number of pairs \((D,R)\) with \(|D|=a\), \(|R|=b\), and \(D\times R\subseteq\overline S\), where the complement is taken in \([N]\times[M]\). Then
\[
E(T')\ge \frac{B_{a,b}(\overline S)}{\binom Na\binom Mb}.
\]
Consequently,
\[
E(T')\ge \max\!\left\{0,1-|S|\frac{ab}{NM}\right\}\ge \max\!\left\{0,1-p^e\frac{ab}{NM}\right\}.
\]
Hence \(E(T')<1/2\) forces \(|S|>NM/(2ab)=n(n+1)/(4d(2d+1))\) and \(e>\log_p(NM/(2ab))\). If \(E(T')=0\), then \(\overline S\) is \(K_{a,b}\)-free, so \(|S|\ge NM-z(N,M;a,b)\), where \(z(N,M;a,b)\) is the bipartite Zarankiewicz number. This is an exact output-support obstruction; it does not establish the paper's stronger path-sensitive probability bound or a new \(\mathrm{AC}^0[p]\)-Frege lower bound.

The first inequality identifies a purely combinatorial component of the reduced search-tree error: the probability that the residual pigeon-hole rectangle misses every label the tree can ever output. This component is exactly a complete-bipartite-subgraph density in the complement of the leaf-label graph.

## Assumptions and scope
Fix a prime \(p\), integers \(n,d,e\) with \(2\le d\le n/2\), and Krajíček's candidate family \(\Omega(n,d)\). A restriction \(\rho\) has \(n_\rho=2d\), so
\[
|D^\rho|=2d+1=a,\qquad |R^\rho|=2d=b.
\]
The tree \(T'\) is any finite \(p\)-ary \((d,e)\)-tree whose leaves are labelled by pairs in \([n+1]\times[n]\), exactly as in the reduced search problem. The probability \(E(T')\) is the error probability under the sampling used for \(\Omega(n,d)\): first a uniformly random admissible restriction and then a uniformly random design conditional on that restriction.

Let \(S\) be the set of distinct leaf labels, not the multiset of leaves. The complement \(\overline S\) is taken in the complete bipartite edge set \([N]\times[M]\), with \(N=n+1\) and \(M=n\).

## Proof
For a fixed admissible restriction \(\rho\), if
\[
S\cap(D^\rho\times R^\rho)=\varnothing,
\]
then every leaf label of \(T'\) lies outside \(D^\rho\times R^\rho\). Therefore \(T'\) errs for every design \(L\) compatible with \(\rho\). It follows immediately that
\[
E(T')\ge \Pr_\rho\!\left[S\cap(D^\rho\times R^\rho)=\varnothing\right].
\]

Write \(k=n-2d\). For every pair of sets \(D\subseteq[N]\), \(R\subseteq[M]\) with \(|D|=a\) and \(|R|=b\), the restrictions having \(D^\rho=D\) and \(R^\rho=R\) are precisely the bijections from \([N]\setminus D\) to \([M]\setminus R\). There are exactly \(k!\) of them. Thus under the uniform distribution on admissible restrictions, \(D^\rho\) and \(R^\rho\) are independent uniform subsets of their prescribed sizes. Hence
\[
\Pr_\rho\!\left[S\cap(D^\rho\times R^\rho)=\varnothing\right]
=
\frac{B_{a,b}(\overline S)}{\binom Na\binom Mb},
\]
because the event is exactly \(D^\rho\times R^\rho\subseteq\overline S\). This proves the first inequality.

For a fixed label \((i,j)\), independence and uniformity give
\[
\Pr_\rho[(i,j)\in D^\rho\times R^\rho]=\frac aN\frac bM=\frac{ab}{NM}.
\]
By the union bound,
\[
\Pr_\rho[S\cap(D^\rho\times R^\rho)\ne\varnothing]
\le |S|\frac{ab}{NM}.
\]
Taking complements gives the second displayed lower bound. A \(p\)-ary tree of height at most \(e\) has at most \(p^e\) leaves, so \(|S|\le p^e\), proving the third bound.

If \(E(T')<1/2\), the lower bound forces \(|S|ab/(NM)>1/2\), and therefore \(|S|>NM/(2ab)\). Since \(|S|\le p^e\), the stated logarithmic necessary condition follows. Finally, if \(E(T')=0\), then no admissible residual rectangle can avoid \(S\); equivalently, \(\overline S\) contains no \(K_{a,b}\). By the definition of the bipartite Zarankiewicz number, \(|\overline S|\le z(N,M;a,b)\), which is equivalent to \(|S|\ge NM-z(N,M;a,b)\).

## Verification
The proof uses only finite counting and the published definitions of the restriction family and tree error. For each prescribed pair \((D,R)\), both complements have size \(k=n-2d\), and exactly \(k!\) bijections give restrictions with those complements. Therefore every pair \((D,R)\) occurs equally often, establishing the required product-uniform distribution without an asymptotic approximation.

Boundary cases were checked symbolically. When \(S=\varnothing\), the biclique density is \(1\) and the tree necessarily errs. When \(S=[N]\times[M]\), the biclique density is \(0\). The union-bound estimate is explicitly truncated at \(0\), so it remains valid when \(|S|ab>NM\). The zero-error conclusion is a necessary condition only and makes no claim that every \(K_{a,b}\)-hitting label set is realizable by a successful search tree.

## Relationship to prior work
Krajíček's 2026 paper defines the restrictions \(D^\rho\) and \(R^\rho\), the candidate family \(\Omega(n,d)\), the reduced output tree, and its error probability. Sections 4--6 then analyze the stronger path-sensitive quantity involving feasibility of a path after restriction. The paper does not identify the leaf-label support with a bipartite graph, does not express the support-only error contribution as a \(K_{2d+1,2d}\) density, and does not state the Zarankiewicz consequence.

The 2024 predecessor already contains the restriction construction and the reduction from a conflict pair to a residual pair, but it does not define the 2026 tree-error functional and does not state the biclique-density or leaf-support bounds. The present result isolates a distinct, exact baseline obstruction that is complementary to the path-sensitive analysis: any argument based only on the possible output labels factors through the residual-rectangle hitting problem described here.

## Limitations
The bound depends only on the set of possible leaf labels and ignores the algebraic information in the queries, path feasibility, and the dimensions \(\dim^\rho(P)\). It can therefore become weak or vacuous once the output support is dense. In particular, it does not prove the lower bound on \(\Pr_{\rho,P}[\chi(P,\rho)=1]\) required by the 2026 reduction, does not prove that \(\Omega(n,d)\) is a pseudo-solution in the target parameter regime, and does not imply a new lower bound for \(\mathrm{AC}^0[p]\)-Frege systems.

An equivalent formulation may exist in the combinatorics literature under the language of rectangular hitting sets or covering arrays; the literature checks performed for this result did not locate an application of that formulation to Krajíček's search-tree error.

## References
1. Jan Krajíček, *Pseudo-solutions of polynomial systems and the lower bound problem for \(\mathrm{AC}^0[p]\)-Frege systems*, arXiv:2609.35927v2, 2026. See Definition 4.3, Lemma 4.4, Section 5, and Theorem 6.1.
2. Jan Krajíček, *Extended Nullstellensatz proof systems*, Proceedings of the American Mathematical Society 152 (2024), 4881--4892; arXiv:2301.10617v3. See Definition 4.2, Lemma 4.3, and Problem 4.4.
