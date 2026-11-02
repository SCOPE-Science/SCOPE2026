# Matrix-block decomposition and an Euler spectrum for path partial-automorphism algebras

## Finding
For every integer \(n\ge0\), let \(P_n\) be the simple undirected path on \([n]\) (the empty graph for \(n=0\)), and let \(S_n=\operatorname{PAut}(P_n)\) be the inverse monoid of isomorphisms between vertex-induced subgraphs, including the empty partial map. Let \(K\) be an arbitrary commutative ring with identity, and take the **noncontracted** semigroup algebra \(K[S_n]\), in which the empty partial map is a basis element.

For each finite sequence \(\mathbf a=(a_1,a_2,\ldots)\) of nonnegative integers with finite support, define \(\ell(\mathbf a)=\sum_{j\ge1}ja_j\), \(k(\mathbf a)=\sum_{j\ge1}a_j\), and, for nonempty \(\mathbf a\),
\[
m_n(\mathbf a)=
\begin{cases}
\displaystyle\frac{k(\mathbf a)!}{\prod_{j\ge1}a_j!}
\binom{n-\ell(\mathbf a)+1}{k(\mathbf a)},&\ell(\mathbf a)+k(\mathbf a)-1\le n,\\
0,&\text{otherwise}.
\end{cases}
\]
Here the binomial coefficient counts sets, and no factor with zero degree is included. Put
\[
G_{\mathbf a}=\mathfrak S_{a_1}\times\prod_{j\ge2}(C_2\wr\mathfrak S_{a_j}),
\]
with trivial factors omitted and \(\mathfrak S_0\) understood to be trivial. There is an isomorphism of unital \(K\)-algebras
\[
\boxed{K[S_n]\cong K\times\prod_{\substack{\mathbf a\ne\mathbf 0\\m_n(\mathbf a)>0}}
M_{m_n(\mathbf a)}(K[G_{\mathbf a}]).}
\]
For \(n=0\) the product over nonempty types is empty and the algebra is \(K\).

Write \(p(r)\) for the number of integer partitions of \(r\), with \(p(0)=1\), and let \(p_2(r)=\sum_{i=0}^rp(i)p(r-i)\). Over \(\mathbb C\), the number \(D_n\) of isomorphism classes of simple \(\mathbb C[S_n]\)-modules (equivalently, the center dimension) is
\[
\boxed{D_n=1+\sum_{\substack{\mathbf a\ne\mathbf0\\\ell(\mathbf a)+k(\mathbf a)-1\le n}}
p(a_1)\prod_{j\ge2}p_2(a_j).}
\]
Let \(P(z)=\prod_{h\ge1}(1-z^h)^{-1}\) and \(\Phi(z)=P(z^2)\prod_{r\ge3}P(z^r)^2\). Then, as a formal power-series identity in \(\mathbb Z[[z]]\),
\[
\boxed{\sum_{n\ge0}D_nz^n=\frac1{1-z}+\frac{\Phi(z)-1}{z(1-z)}.}
\]
The first values, starting at \(n=0\), are \(1,2,4,8,12,24,36,63,99,162,244\).

## Assumptions and scope
Partial automorphisms must preserve both adjacency and nonadjacency on their domains. The monoid product is composition of partial maps. For an induced subgraph on a vertex subset \(U\), its maximal path components are runs of consecutive integers. The integer \(a_j\) counts runs of size \(j\). The empty map has its own singleton component in the noncontracted algebra; the *contracted* semigroup algebra, in which the empty map is set equal to zero, is obtained by deleting the first \(K\) factor. No semisimplicity over positive-characteristic coefficients is asserted. The simple-module formula applies over \(\mathbb C\), not indiscriminately over arbitrary coefficient fields.

## Proof
**1. Induced-subgraph types.** Every induced subgraph of \(P_n\) is a disjoint union of paths, and two such subgraphs are isomorphic if and only if their run-length multiplicities \(\mathbf a\) agree. Fix a nonempty type with \(k\) runs and \(\ell\) occupied vertices. The multiset of run lengths has \(k!/\prod_j a_j!\) distinct left-to-right arrangements. Between consecutive runs place at least one vacant vertex; after accounting for these \(k-1\) mandatory vacancies, distribute the remaining \(n-\ell-(k-1)\) vacant vertices among the \(k+1\) gaps before, between, and after runs. Stars and bars gives \(\binom{n-\ell+1}{k}\) distributions. This proves the expression for \(m_n\) and the feasibility inequality. Each path component with at least two vertices has a reflection of order two; a singleton does not. Equal-length components can be permuted, so the automorphism group is exactly \(G_{\mathbf a}\).

**2. An integral groupoid basis.** Consider the finite groupoid whose objects are all subsets \(U\subseteq[n]\), and whose arrows are the induced-subgraph isomorphisms \(s:U\to V\). Its algebra over \(K\) has arrow basis \([s]\), with \([s][t]=[st]\) if \(\operatorname{dom}(s)=\operatorname{ran}(t)\), and zero otherwise. Define a linear map from the ordinary partial-map basis of \(K[S_n]\) to this groupoid algebra by
\[
\rho(s)=\sum_{A\subseteq\operatorname{dom}(s)}[s|_A].
\]
For \(s,t\in S_n\), pairs of restrictions multiply nontrivially precisely when \(A=t(B)\), where \(B\subseteq\operatorname{dom}(t)\) and \(t(B)\subseteq\operatorname{dom}(s)\). Thus their sum equals \(\rho(st)\), establishing multiplicativity. Ordering all arrows by domain size makes \(\rho\) unitriangular with diagonal entries one; hence it is invertible over every unital commutative ring. Explicitly the inverse transforms an arrow into its Möbius restriction combination \(\sum_{A\subseteq\operatorname{dom}(s)}(-1)^{|\operatorname{dom}(s)|-|A|}s|_A\). This is the standard finite inverse-semigroup/groupoid algebra mechanism, included to fix the zero convention and coefficient scope.

**3. Matrix blocks.** Arrows connect exactly subsets of the same run-length type. For a nonempty type \(\mathbf a\), choose a reference induced subgraph \(R\) and an isomorphism \(\theta_U:R\to U\) for each of its \(m_n(\mathbf a)\) realizations. The arrow \(f:U\to V\) becomes the matrix unit \(E_{V,U}\) labeled by \(\theta_V^{-1}f\theta_U\in\operatorname{Aut}(R)=G_{\mathbf a}\). Composable arrows multiply exactly as matrix units with group coefficients. Noncomposable arrows have product zero. The empty subset contributes one arrow with trivial isotropy, hence the displayed factor \(K\). This proves the full algebra decomposition over \(K\).

**4. Counting complex simple modules.** Matrix factors do not change the number of simple modules of a semisimple complex group algebra. The group \(\mathfrak S_r\) has \(p(r)\) conjugacy classes. Each conjugacy class of \(C_2\wr\mathfrak S_r\) is specified by two partitions, recording cycle lengths whose cycle-products have sign \(+1\) or \(-1\); hence it has \(p_2(r)\) classes. By Maschke's theorem and character theory, these are the counts of simple modules of the respective complex group algebras. Conjugacy class counts multiply across direct products. Summing over feasible run types and including the empty type yields \(D_n\).

**5. Euler product.** A run of size \(j\) uses \(j\) occupied vertices and incurs one slot for a compulsory separator in the bookkeeping, except that the final run saves one separator. Thus \(\mathbf a\) is feasible precisely when \(\sum_{j\ge1}(j+1)a_j\le n+1\). Using \(\sum_{r\ge0}p(r)u^r=P(u)\) and \(\sum_{r\ge0}p_2(r)u^r=P(u)^2\), the generating function for the weights of all types indexed by \(m=\sum(j+1)a_j\) is \(\Phi(z)\). Its constant term represents the empty type; every nonempty type has \(m\ge2\). A nonempty type of weight \(m\) contributes for precisely the values \(n\ge m-1\). Summing the geometric tail gives \((\Phi(z)-1)/(z(1-z))\), and the empty type contributes \(1/(1-z)\). This proves the formal identity.

## Verification
The included standalone program `verify_path_reps.py` independently enumerates all subsets of \([n]\), confirms each run-type multiplicity through \(n=10\), computes group orders and the resulting monoid cardinalities, and checks the Euler-product coefficients against independent sums of complex simple-module counts. For \(n\le6\), it separately enumerates all domain–range pairs and all bijections, retaining exactly induced-subgraph isomorphisms, and checks the full cardinalities. For \(n\le4\), it enumerates the complete monoid and tests all pairwise products of the restriction-Möbius basis against the groupoid multiplication law. The outcomes include \(\lvert S_n\rvert=1,2,7,22,71,252,935\) for \(n=0,\ldots,6\), and \(D_n=1,2,4,8,12,24,36,63,99,162,244\) for \(n=0,\ldots,10\). All checks passed. These finite computations support but do not replace the all-\(n\) proof.

## Relationship to prior work
Jajcay, Jajcayova, Szakács, and Szendrei establish the general characterization of the \(\mathcal D\)-classes of graph partial-automorphism inverse monoids by induced-subgraph isomorphism types, with isotropy groups the automorphism groups of those subgraphs. Dimitrova, Fernandes, Koppitz, and Quinteiro study **this exact path monoid**: they determine Green's relations, generators, rank, and a formula for its cardinality. These structural and cardinality results are prior work; the cardinality of \(S_n\), the Green-class description, and the general groupoid-algebra mechanism are not novelty claims. Everitt explains the general Clifford–Munn correspondence for finite semigroups. The contribution here is the fully specified coefficient-ring matrix-block decomposition by run signatures and, in particular, the explicit multipartition/Euler-product census of all complex simple modules. The inspected publications do not state that census or the complete numerical matrix-degree spectrum for this particular path monoid.

## Limitations
The result gives neither a new general inverse-semigroup representation theorem nor a new enumeration of the underlying monoid's elements. The decomposition over positive-characteristic coefficient fields need not be semisimple, and its number of simples may differ from the complex count. No closed asymptotic formula for \(D_n\) is asserted. An equivalent path-specific representation count could exist under alternative notation; targeted searches and inspected primary texts do not establish exhaustive publication priority. No independent mathematical audit has been performed.

## References
1. R. Jajcay, T. Jajcayova, N. Szakács, and M. B. Szendrei, *Inverse monoids of partial graph automorphisms*, arXiv:1809.04422, first publicly posted 2018-09-12, https://arxiv.org/abs/1809.04422, especially Proposition 3.1 and preceding maximal-subgroup discussion.
2. I. Dimitrova, V. H. Fernandes, J. Koppitz, and T. M. Quinteiro, *Partial Automorphisms and Injective Partial Endomorphisms of a Finite Undirected Path*, arXiv:2101.12468, first publicly posted 2021-01-29, https://arxiv.org/abs/2101.12468, especially Corollary 1.6 and Theorem 2.1.
3. B. Everitt, *The sympathetic sceptic's guide to semigroup representations*, arXiv:1909.13279, first publicly posted 2019-09-29, https://arxiv.org/abs/1909.13279, especially §5 on the Clifford–Munn correspondence.
