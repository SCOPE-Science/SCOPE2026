# Exact shattering profiles and maximal online depth of binary-tree ancestor-incidence graphs

## Finding
For an integer \(h\ge1\), let \(T_h\) be the rooted full binary tree whose leaves have depth \(h\). Form a finite simple bipartite graph \(B_h\) with vertex classes the \(2^h\) leaves and the \(2^h-1\) internal nodes; an internal node \(u\) and a leaf \(a\) are adjacent exactly when \(u\) is an ancestor of \(a\). Let \(\mathscr N_h=\{N_{B_h}[v]:v\in V(B_h)\}\), the family of **closed** vertex neighborhoods. The ground set for membership queries is the entire graph vertex set. For \(S\subseteq V(B_h)\), say \(S\) is shattered when \(\{S\cap C:C\in\mathscr N_h\}=2^S\), and write \(\Phi_h(z)=\sum_{S\text{ shattered}}z^{|S|}\).

**Theorem.** For every \(h\ge2\), with \(L=2^h\),
\[
\boxed{\Phi_h(z)=1+(2L-1)z+\left(\binom{L}{2}+(2h-2)L+2\right)z^2+\left(\frac{3L^2}{4}-(h+1)L\right)z^3.}
\]
For \(h=1\), \(\Phi_1(z)=1+2z\). Hence the VC dimension is \(1\) for \(h=1\), \(2\) for \(h=2\), and \(3\) for all \(h\ge3\).

The Littlestone dimension, defined as the greatest depth of a complete adaptive binary membership-query tree realized by concepts in \(\mathscr N_h\), is exactly
\[
\boxed{\operatorname{Ldim}(\mathscr N_h)=h=\left\lfloor\log_2|V(B_h)|\right\rfloor.}
\]
Thus the adaptive-minus-static gap is \(h-3\) for \(h\ge3\). The graphs \(B_h\) are connected, chordal bipartite, and have diameter exactly four for \(h\ge2\).

## Assumptions and scope
Only finite, simple, undirected graphs are considered. The graph has an edge from each internal vertex to **all** of its descendant leaves, not merely its children. Every vertex supplies one closed neighborhood and is a permissible query point. The parameter \(h\) is an integer at least one; \(L=2^h\). A full binary rooted tree means every internal node has exactly two children and all leaves have depth \(h\). All online-query branches must have at least one consistent concept; no infinite or probabilistic claims are made.

## Proof
Write \(I\) for internal vertices and \(A\) for leaves. For \(a\in A\) let \(P(a)\subseteq I\) be the internal ancestors of \(a\); for \(u\in I\) let \(D(u)\subseteq A\) be the descendant leaves of \(u\). The complete neighborhood classification is
\[
N[a]=\{a\}\cup P(a),\qquad N[u]=\{u\}\cup D(u).
\]
In particular, a leaf-centered neighborhood contains exactly one leaf and a chain of internal vertices; an internal-centered neighborhood contains exactly one internal vertex and a laminar leaf cluster. These identities, not a sampling assumption, determine the entire concept family.

**Support sizes zero, one and two.** The empty support is shattered. When \(h\ge2\), all singletons are shattered: every vertex belongs to its own neighborhood, while another suitable neighborhood avoids it. For \(h=1\), the root belongs to all three neighborhoods, and exactly the two leaves are shattered singletons. For \(h\ge2\), the shattered two-point supports are exactly: (i) arbitrary pairs of leaves; (ii) pairs of comparable internal vertices (one an ancestor of the other); (iii) pairs \(\{a,u\}\) with leaf \(a\) descended from internal vertex \(u\). In each of these cases the four traces have witnesses among the two endpoint-centered neighborhoods, an appropriate ancestor or descendant neighborhood, and a neighborhood in a disjoint branch. In the remaining cases even the positive-positive trace is impossible: incomparable internal vertices never occur together in a closed neighborhood, nor does a leaf occur with a nonancestor internal vertex. Leaf pairs contribute \(\binom{L}{2}\); leaf/internal incidences contribute \(hL\); internal comparable pairs contribute \(\sum_{d=1}^{h-1}d2^d=(h-2)L+2\). The stated quadratic coefficient follows. For \(h=1\), no pair is shattered.

**Triples.** Any shattered three-point support has exactly two leaves \(a,b\) and one internal vertex \(u\). Indeed three leaves cannot realize all three positive-positive-negative pair traces because the sets \(D(v)\) are laminar; three internal vertices either have no common-positive witness (if not a chain) or, if they form a chain, cannot realize the positive trace on the highest and lowest vertices while excluding the middle one; and two internal vertices and one leaf cannot be shattered: when the all-positive trace is possible, the two internals are comparable ancestors of the leaf, and the lower internal cannot appear alone without either the upper internal or the leaf. For the remaining type, the all-positive trace forces \(u\) to be an ancestor of the lowest common ancestor \(v=\operatorname{lca}(a,b)\). The trace containing both leaves but not \(u\) forces \(v\) to have positive depth; the singleton leaf traces force \(v\) to lie strictly above the parents of \(a\) and \(b\), equivalently \(\operatorname{depth}(v)\le h-2\). These conditions are also sufficient. To realize the eight traces, use: an internal vertex in the root subtree opposite \(v\) for the empty trace; a third descendant leaf of \(u\) for \(\{u\}\); the two children of \(v\) for \(\{a\}\) and \(\{b\}\); an ancestor of both leaves different from \(u\) for \(\{a,b\}\) (namely \(v\) if \(u\ne v\), otherwise the parent of \(v\)); the leaf centers \(a,b\) for \(\{u,a\},\{u,b\}\); and center \(u\) for \(\{u,a,b\}\). Each such witness exists for \(1\le\operatorname{depth}(v)\le h-2\).

At depth \(d\), there are \(2^d\) possibilities for \(v\), \(2^{2(h-d-1)}\) unordered leaf pairs split between its two child subtrees, and \(d+1\) choices of \(u\) on the root-to-\(v\) path. Consequently the triple coefficient is
\[
\sum_{d=1}^{h-2}(d+1)2^{2h-d-2}
=3\cdot 2^{2h-2}-(h+1)2^h.
\]
The empty sum for \(h=2\) is zero, as is the closed expression.

**No larger support.** Every shattered support has all its subsets shattered. Every four-point support has a three-point subset of a type ruled out above: the only allowed triple type has exactly two leaves and one internal, and no four-point support can have all four of its triples of that type. Thus \(\Phi_h\) has degree at most three. The positive triple coefficient for \(h\ge3\) establishes the VC dimensions.

**Adaptive rank.** There are exactly \(2^{h+1}-1\) distinct neighborhoods: the unique vertex of its own bipartition contained in each concept identifies the center, and leaf/internal concepts cannot coincide (the \(h=1\) case is also directly distinct). A complete depth-\(d\) online query tree needs at least \(2^d\) distinct concepts, so \(\operatorname{Ldim}\le\lfloor\log_2(2^{h+1}-1)\rfloor=h\). For the matching lower bound restrict to the \(2^h\) leaf-centered hypotheses. At depth \(d=0,\dots,h-2\), given a prefix node of the tree, query its left child, an internal vertex; a leaf-centered neighborhood answers positive exactly when its leaf belongs to the left child subtree, thereby splitting the candidate leaves equally. At depth \(h-1\), query the left leaf of the remaining sibling pair, separating those two leaf-centered hypotheses. All \(2^h\) root-to-leaf answer sequences are realized; therefore \(\operatorname{Ldim}=h\).

**Graph class.** The graph is connected because every leaf is adjacent to the root, and every internal node has descendant leaves. Its diameter is at most four: internal vertices can connect through a descendant leaf, the root, and another descendant leaf, and all remaining types of pairs have shorter routes. Two distinct depth-one internal vertices have distance exactly four when \(h\ge2\), so the diameter is four. To show chordal bipartiteness, suppose an induced cycle has at least six edges. Select among its internal vertices a vertex \(u\) of maximum depth, with two adjacent cycle leaves \(a,b\). Let \(w\) be the other internal cycle neighbor of \(a\). Both \(u,w\) are ancestors of \(a\), hence comparable; maximality of \(u\) forces \(w\) to be a strict ancestor of \(u\). Therefore \(w\) is also adjacent to \(b\), yielding a chord in the purported induced cycle. Contradiction.

## Verification
The standalone script `verify_binary_ancestor_neighborhoods.py` constructs the graph from ancestor incidences and independently enumerates neighborhood traces for every support through size four at heights one to four, and through size three at height five. It checks each support against the structural criterion and against the coefficient formulas. A complete memoized version-space recursion independently computes Littlestone ranks for heights one through four. In the stated ranges the observed coefficients are \([1,2]\), \([1,7,16]\), \([1,15,62,16]\), \([1,31,218,112]\), and \([1,63,754,576]\). These finite calculations do not replace the proofs for arbitrary \(h\).

## Relationship to prior work
Coudert, Csikós, Ducoffe and Viennot (first public version May 13, 2024) explicitly study the closed-neighborhood concept family of arbitrary graphs, develop algorithms and bounds for its VC dimension, and provide the motivating definitions. Their general computations do not specify this ancestor-incidence construction, its coefficientwise shattering polynomial, or its exact Littlestone rank. Bousquet and Thomassé (2014/2015) study graph-neighborhood VC/distance complexity at a general structural level, rather than this exact online/static enumeration. Paszke and Pilipczuk (2020) address definable set-system VC density on tree-like graphs; such general bounds do not imply the displayed coefficientwise finite formulas or exact adaptive rank. The standard prefix-query phenomenon on binary trees explains the constructive online lower bound; it alone does not enumerate all traces of the *closed-neighborhood* set system on the entire graph. Priority under another incidence-graph or laminar-system description is unresolved.

## Limitations
This theorem concerns the specified ancestor-incidence graphs only; it does not classify arbitrary chordal bipartite graphs. The source inspection was finite and cannot establish historical uniqueness. The Littlestone lower-bound construction itself is a conventional tree prefix strategy; the exact full shattering enumeration and simultaneous restriction to the stated graph class form the assessed contribution. No independent mathematical audit has yet been performed.

## References
1. D. Coudert, M. Csikós, G. Ducoffe, L. Viennot, *Practical Computation of Graph VC-Dimension*, arXiv:2405.07588 (first submitted May 13, 2024); SEA 2024, DOI: 10.4230/LIPIcs.SEA.2024.8. https://arxiv.org/abs/2405.07588
2. N. Bousquet and S. Thomassé, *VC-dimension and Erdős–Pósa property*, arXiv:1412.1793 (2014). https://arxiv.org/abs/1412.1793
3. M. Paszke and M. Pilipczuk, *VC Density of Set Systems Definable in Tree-Like Graphs* (2020). https://arxiv.org/abs/2003.14177
4. H. Chase, J. Freitag, L. Reyzin, *Applications of Littlestone Dimension to Query Learning and to Compression*, MFCS 2024, DOI: 10.4230/LIPIcs.MFCS.2024.42.
