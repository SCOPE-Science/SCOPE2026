# Shattered comparison forests and maximum supports for linear extensions

## Finding
Let \(P=(V,<_{P})\) be an arbitrary nonempty finite strict partially ordered set, with \(n=|V|\) and height \(h\) (maximum number of vertices in a chain). A hypothesis is a linear extension of \(P\); each query is an unordered pair of distinct vertices, answered according to which vertex precedes the other in the linear extension. Let \(\mathcal L(P)\) denote this Boolean comparison concept class.

**Complete support criterion.** For a set \(S\subseteq\binom V2\), form the graph \((V,S)\). When this graph is a forest, contract each of its connected components to one vertex, and put an arc from component \(C\) to component \(D\) for every comparability \(x<_{P}y\) with \(x\in C\), \(y\in D\). Loops count as cycles. Then
\[
S\text{ is VC-shattered by }\mathcal L(P)
\quad\Longleftrightarrow\quad
(V,S)\text{ is a forest and the contracted comparison digraph is acyclic}.
\]
In particular, for **every** such poset,
\[
\boxed{\operatorname{VCdim}(\mathcal L(P))=n-h.}
\]

**Complete maximum-support classification.** A support \(S\) of size \(n-h\) is shattered exactly when there is a surjective map \(f:V\to[h]\) satisfying \(x<_{P}y\Rightarrow f(x)<f(y)\), such that \(S\) consists of a spanning tree on each fiber \(f^{-1}(i)\), with no edges between fibers. The map \(f\) is **uniquely determined** by \(S\). Consequently the number \(N(P)\) of labeled shattered supports of maximum size is
\[
\boxed{N(P)=\sum_{\substack{f:V\twoheadrightarrow[h]\\x<_{P}y\Rightarrow f(x)<f(y)}}\ \prod_{i=1}^{h}\tau\bigl(|f^{-1}(i)|\bigr),\qquad
\tau(1)=1,\quad\tau(t)=t^{t-2}\ (t\ge2).}
\]
The formula counts **query supports**, not linear extensions or their orientations.

## Assumptions and scope
The ground set is fixed and labeled; \(P\) is finite, antisymmetric, and transitive; all total orders extending \(P\) are allowed. The concept domain is the complete set of **unordered** pairs of distinct elements, each with one fixed reference orientation for encoding a Boolean answer. VC shattering requires *every* one of the \(2^{|S|}\) assignments on the selected queries to be realized by some extension, and does not mean online/Littlestone shattering. The empty support is allowed, and the singleton case \(n=h=1\) has dimension zero and one maximum support. Cayley's counting convention for a one-vertex tree is \(\tau(1)=1\).

## Proof
**1. Cycles and contractions.** If \((V,S)\) has a cycle, orient the queries on that cycle cyclically; no linear order realizes that labeling. Hence a shattered support must be a forest. Suppose from now on that \((V,S)\) is a forest, so every pair of vertices in the same component has a unique undirected \(S\)-path.

If the contracted comparison digraph has a loop, say \(x<_{P}y\) with both vertices in one component, orient the unique \(S\)-path from \(y\) to \(x\); the resulting comparisons contradict \(x<_{P}y\). If the contracted digraph has a directed simple cycle on distinct components, select a witness of each comparability arc along the cycle. Inside every component on the cycle, orient the unique \(S\)-path from its incoming witness to its outgoing witness. These paths lie in different trees, so their orientations are compatible. Together with the chosen comparabilities they create a directed cycle. Thus any contracted directed cycle forbids at least one query labeling.

Conversely, suppose the contracted digraph is acyclic. Give the edges of \(S\) *any* directions. Their directions form an acyclic digraph inside each forest component. There is no comparability within a component because that would give a loop. A directed cycle in the union of the prescribed relations \(<_{P}\) and the chosen query directions would either stay inside one tree (impossible) or project to a nontrivial directed closed walk in the contracted comparison digraph (also impossible). The union is therefore acyclic and admits a topological order extending \(P\). Every query labeling is realizable. This proves the support criterion.

**2. Sharp VC dimension.** Let \(x_1<_{P}\cdots<_{P}x_h\) be a longest chain. In a shattered forest, no two vertices of this chain can lie in the same component; otherwise their comparability gives a contracted loop. Thus the forest has at least \(h\) components and at most \(n-h\) edges.

For the reverse inequality, define \(r(v)\) to be the maximum size of a chain of \(P\) ending at \(v\). Then \(r:V\to[h]\) is surjective and every strict comparability increases \(r\). Choose any spanning tree on each nonempty rank level. The resulting forest has \(n-h\) edges, and its contracted comparison digraph has arcs only from lower to higher ranks. It is therefore shattered by Step 1, proving equality.

**3. Every extremizer.** Any shattered support with \(n-h\) edges has exactly \(h\) forest components. A longest chain has \(h\) vertices; by Step 2 each belongs to a different component. Comparabilities along the chain induce a directed path through all \(h\) contracted components in chain order. Since the contracted digraph is acyclic, every remaining comparability must go in the same direction in this component order. Assigning each component its position from \(1\) to \(h\) gives a surjective strict order-preserving map \(f\). This order is unique because the longest chain forces it. Within each component the support is a spanning tree, so the classification follows. Conversely, every strict surjective \(f\) and choice of fiberwise trees yield an acyclic contracted digraph, hence a maximum shattered support. Distinct maps cannot produce the same support by uniqueness. Cayley's tree formula gives the displayed exact count.

## Verification
The standalone file `verify_linear_extensions_vc.py` uses only the Python standard library. Run `python3 verify_linear_extensions_vc.py 5` from the directory containing the file. It independently constructs every strict labeled poset on up to five vertices by checking transitivity of all ternary pair-state assignments, enumerates all its linear extensions as permutations, tests every query support by direct realized-label counts, and compares the results to the forest/contraction characterization, the formula \(n-h\), and the maximum-support count. It checked \(4{,}332{,}544\) pair-support instances at five vertices, encompassing all \(4{,}231\) labeled five-point posets. The file `verification_output.txt` records the actual output. These finite checks corroborate but do not replace the unrestricted proof.

## Relationship to prior work
Finite-poset order dimension, defined using *sets of linear extensions that reverse incomparable pairs*, is different from the VC dimension of the **family of all extensions considered as Boolean functions on pair queries**. Kozik, Micek and Trotter (2019, arXiv:1907.00380, especially Sections 1–2) analyze poset height, order dimension and alternating-cycle obstructions to jointly reversible pairs; their cited reversibility obstruction is related in spirit, but does not state this shattering criterion or its extremizer formula.

Bandelt, Chepoi and Knauer (2015, arXiv:1507.06111, Section 10) construct the ranking complex of oriented matroids whose topes are all linear extensions, and characterize several geometric properties. Their ranking-complex construction supplies the same **underlying concept class**, but Section 10 does not give the height-only VC formula or classify all maximally shattered coordinate supports. Chepoi, Knauer and Philibert (2021, arXiv:2110.15168, Sections 1.3 and 4) give proper labeled sample-compression schemes of size equal to the *already given* VC dimension for general complexes of oriented matroids; that does not compute the dimension for this instance.

Duan, Ouyang and Wang (arXiv:2412.06402, Sections 1–2) study a different incidence system: total orders or posets are **points** and compatibility with another order gives the **ranges**. Their bounds do not cover fixed-poset linear extensions evaluated on individual pair comparisons. For the antichain special case, the formula specializes to the elementary forest characterization for arbitrary total orders; the contribution is the fixed-poset contraction criterion and all-height/extremizer classification. No exhaustive historical-priority claim is made.

## Limitations
The theorem is about static VC dimension, not the optimal online mistake bound or Littlestone dimension. It assumes unrestricted access to every linear extension of the specified finite poset, and ordinary binary comparisons. The count of maximum supports may be expensive to evaluate directly from the rank-map sum for large instances. General COM sample compression and alternative incidence definitions are not subsumed. External literature searches cannot rule out an unindexed earlier equivalent formulation; independent mathematical and publication-priority assessment remains outstanding.

## References
1. Jakub Kozik, Piotr Micek, William T. Trotter, *Dimension is Polynomial in Height for Posets with Planar Cover Graphs*, arXiv:1907.00380, first version 2019, https://arxiv.org/abs/1907.00380.
2. Victor Chepoi, Kolja Knauer, Manon Philibert, *Labeled Sample Compression Schemes for Complexes of Oriented Matroids*, arXiv:2110.15168, first version 2021, https://arxiv.org/abs/2110.15168.
3. Hans-Jürgen Bandelt, Victor Chepoi, Kolja Knauer, *COMs: Complexes of Oriented Matroids*, arXiv:1507.06111, first version 2015, https://arxiv.org/abs/1507.06111.
4. Boyan Duan, Minghui Ouyang, Zheng Wang, *VC-dimensions Between Partially Ordered Sets and Totally Ordered Sets*, arXiv:2412.06402, https://arxiv.org/abs/2412.06402.
5. Leon Mirsky, *A dual of Dilworth's decomposition theorem*, American Mathematical Monthly 78 (1971), 876–877.
6. Arthur Cayley, *A theorem on trees*, Quarterly Journal of Mathematics 23 (1889), 376–378.
