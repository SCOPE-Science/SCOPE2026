# Eight habitat patches are the sharp threshold for a degree-matched largest-fragment reversal

## Finding

Consider an unweighted habitat-corridor tree whose vertices represent equal-sized habitat patches. Retain vertices independently with common probability \(p\), and let \(L_T(p)\) be the order of the largest connected component in the surviving induced subgraph, setting it to zero when no patch survives. A comparison is **degree-matched** if the trees have the same order and degree multiset. For every two degree-matched trees on at most seven vertices, the expected largest-fragment functions are ordered in the same direction for every \(p\in[0,1]\). More strongly, their expected largest fragment conditional on *exactly* \(k\) surviving patches is ordered in one common direction for every integer \(k\) from zero through the number of patches.

Eight vertices are the sharp threshold at which the comparison can reverse. Let \(A\) and \(B\) be three-armed trees with branch lengths \((3,3,1)\) and \((4,2,1)\), respectively, measured in edges from their unique degree-three vertex. Both have eight vertices and degree multiset \((1,1,1,2,2,2,2,3)\), but they are not isomorphic. Their expected largest-surviving-component difference is exactly

\[
\mathbb E L_A(p)-\mathbb E L_B(p)=p^5(1-p)^2(2p-1).
\]

In particular, \(B\) is better for \(0<p<1/2\), whereas \(A\) is better for \(1/2<p<1\). There is exactly one *unordered nonisomorphic degree-matched pair* on eight vertices whose conditional largest-component expectations are not comparable in a single direction across all fixed survivor counts: this pair.

## Assumptions and scope

The underlying habitat network \(T=(V,E)\) is a finite, connected, simple, undirected tree with \(n=|V|\) equal-sized vertices. The network is fixed in advance. Each vertex independently survives with probability \(p\in[0,1]\); failed vertices and incident edges are removed. The largest remaining induced connected component is measured by vertex count, not geographic area, abundance, or total remaining connectivity. For any subset \(U\subseteq V\), write \(\ell_T(U)\) for the maximum component order of \(T[U]\), with \(\ell_T(\varnothing)=0\). Define the integer fixed-size totals

\[
S_T(k)=\sum_{\substack{U\subseteq V\\|U|=k}}\ell_T(U),\qquad 0\leq k\leq n.
\]

Conditional on exactly \(k\) surviving vertices, the expected largest fragment is \(S_T(k)/\binom nk\). The independent-retention expectation is the Bernstein-form polynomial

\[
F_T(p)=\mathbb E L_T(p)=\sum_{k=0}^{n}S_T(k)p^k(1-p)^{n-k}.
\]

The lower-bound classification is exhaustive only for \(n\leq7\); uniqueness of the incomparable degree-matched pair is asserted only for \(n=8\). No conclusion is asserted for general graphs, unequal patch sizes, or dependent failures.

## Proof

**Exact conditional-to-unconditional identity.** Every survivor subset \(U\) of size \(k\) has probability \(p^k(1-p)^{n-k}\), yielding the displayed formula. If \(S_T(k)-S_{T'}(k)\) has the same weak sign for all \(k\), then both the entire conditional expectation profile and the independent-retention expectation are ordered in that sign for every \(p\in[0,1]\), because each Bernstein weight is nonnegative.

**Complete lower-bound classification.** Every tree with at least two vertices contains a leaf. Removing a leaf produces a smaller tree, and conversely every tree of order \(n\) occurs, up to isomorphism, by attaching a new leaf to some vertex of a tree of order \(n-1\). Generate all such leaf attachments recursively, and keep one representative per isomorphism class. A canonical rooted word is defined by recursively sorting the rooted child words between parentheses; the lexicographically least such word over all possible roots is a complete invariant of unrooted tree isomorphism. Two trees with the same canonical word are isomorphic, and nonisomorphic trees have different words.

Using that exhaustive generation, the numbers of tree classes for orders one through eight are

\[
(1,1,1,2,3,6,11,23).
\]

For each generated tree, enumerate *every* subset \(U\subseteq V\), find the connected components of \(T[U]\), and accumulate the exact integer \(S_T(|U|)\). Group trees by their sorted degree sequence. Across orders one through eight, the numbers of unordered pairs of nonisomorphic trees with identical degree multiset are

\[
(0,0,0,0,0,1,5,23).
\]

The single degree-matched comparison at order six has, after choosing the orientation with nonnegative differences, the coefficientwise difference \((0,0,0,0,1,0,0)\). The five order-seven comparisons have corresponding difference triples at survivor counts \(k=4,5,6\) equal to

\[
(1,0,1),\quad(2,0,1),\quad(1,0,0),\quad(2,1,0),\quad(2,1,1),
\]

and differences are zero at every other survivor count. Thus no two degree-matched trees of order at most seven have an incomparable conditional-largest-fragment profile. This is a finite complete argument: the leaf-extension enumeration covers every class, the canonical word resolves isomorphism, and all subsets within each class are evaluated. The accompanying executable verification exposes each step and checks the asserted counts with exact integers.

**The eight-vertex witness.** The two specified three-arm trees are nonisomorphic, since their unordered branch-length multisets differ. Their exact fixed-survivor totals, listed in order \(k=0,1,\ldots,8\), are

\[
S_A=(0,8,35,98,167,177,119,46,8),
\]
\[
S_B=(0,8,35,98,167,178,118,46,8).
\]

Consequently \(S_A-S_B\) is zero except for a value \(-1\) at \(k=5\) and \(+1\) at \(k=6\). Substitution into the Bernstein representation gives

\[
F_A(p)-F_B(p)=-p^5(1-p)^3+p^6(1-p)^2
=p^5(1-p)^2(2p-1).
\]

Its sign has precisely the asserted interior change at \(p=1/2\). Conditional on five surviving patches, \(A\) is worse by \(1/56\); conditional on six surviving patches, \(A\) is better by \(1/28\).

**Uniqueness at order eight.** The same complete tree-isomorphism enumeration yields 23 unordered degree-matched pairs at order eight. Exactly one pair has both a negative and positive coordinate in the integer vector \(S_T-S_{T'}\). Comparing the canonical tree words of that exceptional pair with the two explicit three-arm trees proves that they are the same unordered isomorphism pair. This uniqueness claim is about profile incomparability, not uniqueness of every imaginable performance measure or behavior on larger trees.

## Verification

The included `verify.py` uses only the Python standard library. It exhausts all unrooted tree classes through eight vertices by recursive leaf attachment and a complete canonical rooted-tree word; it enumerates all survivor subsets, groups trees by degree multiset, and checks all coordinatewise comparisons. For the witness, an independent union-find implementation recomputes all 512 survivor subsets for each tree and reproduces both nine-entry totals. Every quantity is integer exact; there is no floating-point fitting or stochastic simulation. Execute `python3 verify.py`; its single-line canonical JSON output should equal the included `certificate.json` (ignoring its final newline). Exhaustiveness applies only through eight vertices and the independently verified identities imply the all-parameter polynomial statement for the displayed witness.

## Relationship to prior work

Rayfield, Fortin, and Fall (2011) motivate habitat-network assessment based on connected habitat area and network components, rather than only local degree. The new claim is a precise degree-controlled comparison under independently surviving patches: a sharp smallest tree order at which the optimal network changes with patch survival probability.

Andriantiana, Razanajatovo Misanantenaina, and Wagner (2021) develop broad fixed-degree-sequence tree extremal theorems for several different graph invariants, including subtree counts and related graph statistics. Such an extremality claim about a different invariant does not, by itself, imply the pairwise sign reversal and sharp fixed-survivor largest-fragment classification proved here.

Gu and Yuan (arXiv:2408.12515, first public version 2024) analyze site-percolation clusters and largest-cluster asymptotics in an ensemble of random recursive trees. Their random-tree large-size limit is a different object from the present deterministic, fixed-degree, small-order ranking. These works establish the ecological and mathematical context; the standard use of independent site survival is not claimed as novel.

## Limitations

The classification is finite, with lower bound through seven vertices and a unique incomparable eight-vertex pair. It is not a classification for all larger trees. Independently retained equal-sized patches and tree-shaped corridors are stylized ecological assumptions. Correlated disturbances, unequal habitat values, weighted/directed corridors, imperfect observations, and non-tree networks are outside the theorem. The verification is a transparent exhaustive computation for small trees plus a symbolic exact two-tree identity; it is not a claim of independent external certification. Although the inspected sources and mathematical-record searches did not exhibit an earlier equivalent statement, previously unlocated literature on network reliability, vulnerability, or graph polynomials may contain related or stronger results.

## References

1. B. Rayfield, M.-J. Fortin, and A. Fall, “Connectivity for conservation: a framework to classify network measures,” *Ecology* 92 (2011), 847–858. First online 2011-04-01. https://doi.org/10.1890/09-2190.1
2. E. O. D. Andriantiana, V. Razanajatovo Misanantenaina, and S. Wagner, “Extremal trees with fixed degree sequence,” *Electronic Journal of Combinatorics* 28 (2021), #P1.1. https://doi.org/10.37236/9770
3. C. Gu and L. Yuan, “Size distribution of clusters in site-percolation on random recursive tree,” arXiv:2408.12515, initial version 2024-08-22. https://arxiv.org/abs/2408.12515
