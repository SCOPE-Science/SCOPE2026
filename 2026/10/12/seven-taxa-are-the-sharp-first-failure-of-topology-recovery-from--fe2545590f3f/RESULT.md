# Seven taxa are the sharp first failure of topology recovery from complete mean phylogenetic-diversity rarefaction

## Finding
For any integer \(2\le n\le6\), the complete expected **rooted** phylogenetic-diversity rarefaction curve of a rooted, fully binary, positive-edge-length tree on \(n\) tips determines its **unlabeled rooted tree topology**. The same holds within the strictly ultrametric subclass. The conclusion fails at the sharp threshold \(n=7\), even for two different strictly binary, ultrametric seven-tip trees with positive **integer** branch lengths and the same root-to-tip height. Their mean curves agree at every sample size, but their two-tip rooted-PD distributions and variances differ. Such pairs exist for every integer \(n\ge7\).

The mean-formula ingredient is established in earlier phylogenetic-rarefaction work [1,2]. The contribution here is the sharp topology-identifiability cutoff, the exact ultrametric witness, and the distributional separation of two trees with identical complete expected curves.

## Assumptions and scope
Let \(T\) be a finite rooted full binary tree whose \(n\ge2\) leaves each represent one distinct species, with a strictly positive real length \(\ell_e\) on every edge. A rooted ultrametric tree has equal root-to-tip path lengths. The root is fixed, and leaf relabelings and swaps of sibling order do not alter the tree's unlabeled topology. For each \(k=0,\ldots,n\), draw uniformly a \(k\)-subset \(K\) of its leaves, without replacement. The rooted phylogenetic diversity \(\mathrm{PD}_T(K)\) is the sum of the lengths of edges lying on a root-to-leaf path for at least one selected leaf; set \(\mathrm{PD}_T(\varnothing)=0\). Write \(m_T(k)=\mathbb E[\mathrm{PD}_T(K)]\).

For an edge \(e\), let \(s_e\in\{1,\ldots,n-1\}\) be the number of leaf descendants of the edge. Define the **length-weighted descendant-clade-size spectrum** \(c_s(T)=\sum_{e:s_e=s}\ell_e\) for \(1\le s\le n-1\). We use \(\binom{u}{v}=0\) when \(v>u\), for nonnegative integer \(u,v\). Here the terminal edges have size one, while every nonroot internal node corresponds to a proper internal clade of size between two and \(n-1\).

## Proof
**(1) The entire mean curve determines exactly the weighted spectrum.** A fixed edge with \(s\) descendants is absent precisely if all sampled leaves lie among the other \(n-s\) tips. Thus the standard rooted-PD rarefaction calculation [1,2] gives
\[
m_T(k)=\sum_{s=1}^{n-1}c_s(T)\left(1-\frac{\binom{n-s}{k}}{\binom nk}\right),\qquad k=0,\ldots,n.
\]
In particular \(m_T(n)=\sum_s c_s(T)\). For \(k=n-j\) with \(1\le j\le n-1\), multiplying the difference by \(\binom nk\) yields
\[
\binom nk\bigl(m_T(n)-m_T(k)\bigr)=\sum_{s=1}^{j}c_s(T)\binom{n-s}{k}.
\]
The term newly appearing at step \(j\) is \(c_j(T)\binom{n-j}{n-j}=c_j(T)\), with coefficient one. Increasing \(j=1,2,\ldots,n-1\) therefore recovers all \(c_s(T)\) by exact triangular elimination. Conversely the displayed mean formula immediately recovers the curve from \(c_s\). Hence
\[
\bigl(m_T(0),\ldots,m_T(n)\bigr)=\bigl(m_U(0),\ldots,m_U(n)\bigr)
\quad\Longleftrightarrow\quad
c_s(T)=c_s(U)\ \text{for every }s.
\]
This triangular inversion is elementary; no claim that the general mean formula itself is new is made.

**(2) The sharp lower bound.** Because **every edge length is positive**, the support \(\{s:2\le s\le n-1,\ c_s(T)>0\}\) is exactly the set of sizes of proper nontrivial clades of the unlabeled rooted topology, with multiplicities forgotten. Exhausting rooted unordered full binary shapes by the unique recursion \(T=(T_1,T_2)\), in which the children are an unordered pair of smaller full binary shapes and their leaf counts add to \(n\), gives the following complete list of supports for \(2\le n\le6\):

| \(n\) | All nontrivial clade-size supports, one per shape |
|---|---|
| 2 | \(\varnothing\) |
| 3 | \(\{2\}\) |
| 4 | \(\{2\},\ \{2,3\}\) |
| 5 | \(\{2,3\},\ \{2,4\},\ \{2,3,4\}\) |
| 6 | \(\{2,3\},\ \{2,4\},\ \{2,3,4\},\ \{2,3,5\},\ \{2,4,5\},\ \{2,3,4,5\}\) |

These lists contain respectively \(1,1,2,3,6\) distinct supports, equal to the exhaustive shape counts. They can also be regenerated from scratch by the included independent unordered-shape enumerator, which confirms all eleven shapes on seven tips. Thus all topology-support maps are injective for \(n\le6\). Equal complete mean curves force equal supports by (1), and therefore the same unlabeled rooted topology. This argument needs neither clocklike edge lengths nor any genericity assumptions.

**(3) Two positive ultrametric seven-tip counterexamples.** For compact exact specification, let \([P,Q]_h\) denote a binary ancestor at height \(h\), measured upwards from leaves at height zero; the edge to each child has length \(h-h_{\rm child}\). Distinct symbols \(a,b,c,d,e,f,g\) denote leaves (at height zero). Construct
\[
\begin{aligned}
T_A&=\bigl[[a,[b,c]_1]_2,\ [[d,e]_2,[f,g]_2]_3\bigr]_4,\\
T_B&=\bigl[[a,[b,c]_1]_3,\ [d,[e,[f,g]_1]_2]_3\bigr]_4.
\end{aligned}
\]
Every parent height is strictly greater than its children's heights, so all edge lengths are positive integers, and every root-to-leaf distance is four. Both have root split sizes \(3+4\), but the four-leaf clade of \(T_A\) is balanced while that of \(T_B\) is a caterpillar; they are not isomorphic as rooted unlabeled shapes. Direct edge accounting gives, in order \(s=1,2,3,4,5,6\),
\[
\bigl(c_s(T_A)\bigr)=\bigl(c_s(T_B)\bigr)=(12,3,2,1,0,0).
\]
For transparency, the size-two contributions in \(T_A\) have lengths \(1,1,1\), while in \(T_B\) they have lengths \(2,1\); the size-three contributions in \(T_A\) come from one length-two edge and in \(T_B\) from two length-one edges. In both cases the four-leaf root-child edge has length one, and the terminal lengths sum to twelve. Part (1) proves equality of *every* expected rarefaction point. The exact curve at \(k=0,\ldots,7\) is
\[
\left(0,4,\frac{51}{7},\frac{351}{35},\frac{433}{35},\frac{101}{7},\frac{114}{7},18\right).
\]
The curves nevertheless discard distributional information. Exhaustive direct edge accounting over all \(\binom72=21\) unordered two-tip samples yields:

| Rooted PD for two tips | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|
| \(T_A\), number of tip pairs | 1 | 4 | 4 | 12 |
| \(T_B\), number of tip pairs | 2 | 2 | 5 | 12 |

Both two-tip means equal \(51/7\), but their population variances, with denominator \(21\) (not \(20\)), are \(128/147\) and \(142/147\), respectively. The variance gap is therefore \(2/21\).

**(4) Every larger size.** From an ultrametric counterexample on \(n\ge7\) leaves of common root-to-tip height \(H\), attach its root as one child of a new binary root of height \(H+1\), and a new leaf as the other child. Keep all old edge lengths; the edge to the old root has length one and descendant size \(n\), and the edge to the new leaf has length \(H+1\) and descendant size one. Apply exactly the same graft to both trees. It adds the same amount to every corresponding \(c_s\), retains positive edge lengths and ultrametricity, and preserves nonisomorphism: the large child can be recovered uniquely from the root's \(1+n\) split. Inductively, counterexamples exist for every \(n\ge7\). The lower-bound argument above completes sharpness.

## Verification
Run `python3 verify_pd.py` using Python's standard library. Its executable assertions: generate the full unordered binary shape set at every tip count through seven; confirm complete support collision absence through six and the unique collision at seven; test both trees' positive edge lengths, ultrametric height, and weighted clade vectors; calculate the rooted PD of **every** tip subset at every sample size in exact rational arithmetic and match the closed mean formula; invert the exact mean curve; and compute both 21-outcome two-tip distributions and their variances. The successful run ends with `VERIFY_OK`. This finite shape enumeration proves the *finite base case* because all unordered binary shapes are generated; the infinite-size assertion instead follows from the explicit grafting proof above.

## Relationship to prior work
Nipperess and Matsen [1] already establish exact general formulas for the rooted and unrooted **mean and variance** of phylogenetic diversity under uniform rarefaction. Nipperess [2] explicitly specializes and applies the rooted expectation formula. Chao and colleagues [3] develop rarefaction and extrapolation of phylogenetic diversity under related ecological data models. These do **not** become new here by rewriting them as weighted-clade sums. The question answered here is different: whether the *complete mean curve alone* identifies the **unlabeled topology**, and what is the smallest positive-edge ultrametric counterexample.

Fischer, Hamann and Wicke [4] compare clade-size **multiset** sequences of rooted trees and report first distinct trees having identical full clade-size sequences at nine tips. A multiplicity-retaining multiset is a **stronger invariant** than the support of positive length sums, and is not the weighted-length rarefaction invariant. Our seven-tip examples have different clade-size multiplicities but the same **total branch length at each size**, made possible by their explicit positive clocklike lengths. Thus [4] neither asserts the seven-tip mean-rarefaction collision nor proves its impossibility; its nine-tip count is not being contradicted or renamed. The published tree-shape count [5] helps cross-check the finite enumeration, not establish the rarefaction theorem.

## Limitations
The invariant here is the entire **exact expectation curve** at all discrete sample sizes on a complete census with exactly one observation per tip. We do not claim identifiability of species labels, divergence times or individual edge lengths, even below seven tips; only unlabeled rooted topology is identified. The equality and counterexample do not imply equivalence of distributions or variances—indeed the witness shows a variance difference. Partial/noisy sampling curves, species abundances, nonbinary or zero-length trees, phylogenetic networks, unrooted PD, and other sampling schemes are outside the theorem. The finite enumeration alone is not a proof for every size; the induction is essential. Novelty is relative to the specific inspected literature and can be superseded by an unindexed stronger topology-recovery result.

## References
1. Nipperess, D. A. and Matsen, F. A. IV, *The mean and variance of phylogenetic diversity under rarefaction*, arXiv:1208.6552 (first posted 2012-08-31); Methods in Ecology and Evolution (2013), DOI 10.1111/2041-210X.12042. Full open preprint: https://arxiv.org/html/1208.6552v2 .
2. Nipperess, D. A., *The Rarefaction of Phylogenetic Diversity: Formulation, Extension and Application*, 2015, DOI 10.1007/978-3-319-22461-9_10; open chapter: https://link.springer.com/chapter/10.1007/978-3-319-22461-9_10 .
3. Chao, A., Chiu, C.-H., Hsieh, T. C., Davis, T., Nipperess, D. A. and Faith, D. P., *Rarefaction and extrapolation of phylogenetic diversity*, Methods in Ecology and Evolution (2015), DOI 10.1111/2041-210X.12247.
4. Fischer, M., Hamann, T. N. and Wicke, K., *Metaconcepts of Rooted Tree Balance*, Bulletin of Mathematical Biology (2025), DOI 10.1007/s11538-025-01509-y; open full article: https://link.springer.com/article/10.1007/s11538-025-01509-y .
5. OEIS A001190, *Number of unlabeled rooted trees with n leaves and all non-end nodes having degree 3*: https://oeis.org/A001190 .
