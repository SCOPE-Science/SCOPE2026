# Signed seven-point symmetry on fourth homology of the triangular-graph neighborhood complex
## Finding
Let \(T_7=L(K_7)\) be the triangular graph on the twenty-one edges of the complete graph on seven labeled points. Its open Lovász neighborhood complex \(K=\mathcal N(T_7)\) satisfies
\[
H_4(K;\mathbb Z)\cong\mathbb Z^7,\qquad
H_4(K;\mathbb Q)\cong \operatorname{sgn}_{\mathfrak S_7}\otimes\mathbb Q^{[7]}
\cong S^{(1^7)}\oplus S^{(2,1^5)}.
\]
Here \(\mathbb Q^{[7]}\) is the natural permutation representation on seven points, \(\operatorname{sgn}\) is the sign character and the two Specht modules have dimensions one and six. Consequently, for every \(g\in\mathfrak S_7\),
\[
\operatorname{tr}\bigl(g\mid H_4(K;\mathbb Q)\bigr)=\operatorname{sgn}(g)\,|\operatorname{Fix}_{[7]}(g)|.
\]
In particular, there is no globally invariant rational fourth-homology class. A transposition has trace \(-5\), not \(+5\).

## Assumptions and scope
The vertices of \(T_7\) are unordered two-point subsets of \([7]\). Distinct vertices are adjacent exactly when their subsets meet. The open neighborhood \(N(e)\) of a vertex \(e\) excludes \(e\) itself, and \(K\) consists precisely of all subsets of at least one \(N(e)\), including the empty simplex in its augmented chain complex. The action of \(\mathfrak S_7\) permutes the seven labels, hence the twenty-one graph vertices and simplices. Integral homology here is ordinary simplicial homology; the representation identification is over \(\mathbb Q\), **not** an assertion about the integral group-ring lattice. No behavior for \(T_n\) with \(n\ne7\) is claimed.

## Proof
**Exact construction.** List the \(21\) edges in lexicographic order and encode any simplex by its twenty-one-bit indicator. Every open neighborhood has ten vertices. Enumerating the complete power set of each open neighborhood, with duplicates identified, yields exactly \(18{,}495\) augmented simplices. This step is exhaustive because every simplex of \(K\) has such a common neighbor by definition.

**Verified elementary collapses.** Starting from this full face set, keep for each face its live codimension-one cofaces. Repeatedly choose a face \(t\) with exactly one such coface \(s\), in decreasing face cardinality and then increasing bitmask order. The code verifies that \(s\) is maximal, that \(t\) is a codimension-one face of \(s\), and that the pair is removed. Each operation is therefore an elementary simplicial collapse, not merely an algebraic matching. Exactly \(7{,}962\) such pairs are removed. The remainder has augmented face numbers, in dimensions \(-1,0,1,2,3,4\), equal to \((1,21,210,881,1194,264)\). There are no cells in dimension at least five.

**Exact integral top homology.** Form the signed simplicial boundary \(\partial_4\) from the \(264\) remaining four-simplices to the \(1194\) three-simplices. Integral sparse-column elimination, always choosing the first available pivot row, yields \(257\) pivot columns, *each* having unit pivot \(\pm1\). The remaining seven columns yield seven integer cycles; they have identity coordinates at the seven free-column positions. All seven have exactly zero signed boundary. Unit-pivot elimination is invertible over \(\mathbb Z\); every integral kernel vector is determined uniquely by its seven free coordinates. Thus \(\ker\partial_4\cong\mathbb Z^7\). Since the collapsed complex has no five-cells, \(H_4(K;\mathbb Z)\cong\mathbb Z^7\).

**Exact symmetry matrices.** An underlying permutation \(g\) acts on an oriented simplex by reordering its permuted vertices into lexicographic order, multiplied by the resulting sign. To express the induced action in the seven-cycle basis, compose this simplicial chain map with the chain projection of every elementary collapse. If \(t\subset s\) is the collapsed free pair with \(\dim t=4\), the degree-four projection sends \(t\) to \(t-[t:s]^{-1}\partial s\); if \(\dim s=4\) it sends \(s\) to zero. These are integral chain-homotopy equivalences, so the calculated matrices represent the genuine induced homology action. Read the seven free coordinates of each image to obtain a \(7\)-by-\(7\) integer matrix. For each of the fifteen cycle types of \(\mathfrak S_7\), exact computation gives trace \(\operatorname{sgn}(g)|\operatorname{Fix}_{[7]}(g)|\). The six adjacent-transposition matrices additionally satisfy the involution, braid, and commuting Coxeter relations by exact integer multiplication.

The rational character is therefore identical to the sign twist of the natural seven-point permutation character. Since characteristic-zero representations of finite groups are semisimple and determined by characters, the asserted isomorphism follows. Splitting the natural permutation representation into its trivial line and six-dimensional standard module yields the displayed Specht decomposition after sign twist.

## Verification
Run `python3 verify.py` with Python 3.10 or later; it uses only the standard library and reconstructs the entire complex from its definition. All inputs, face orderings, signed boundaries, elementary-collapse rules, pivot selection, integral cycle representatives, permutation signs and conjugacy-class representatives are generated in the script. The verifier reports the complete face count, collapse count, surviving cells, unit-pivot rank, all fifteen character traces and Coxeter-relation checks; its assertions fail if any of these disagree. No finite sampling is used for \(\mathfrak S_7\), since a character is constant on conjugacy classes and all fifteen are checked.

## Relationship to prior work
The previously published mixed-dimensional neighborhood-homology computation for triangular graphs determines only mod-two ranks, including seven degree-four mod-two classes at \(T_7\); it explicitly does not determine integral torsion or the symmetry representation. Its result therefore does not imply the signed representation formula. Fröberg's 2026 primary study of Stanley–Reisner rings for neighborhood complexes treats families such as complete, bipartite and multipartite graphs rather than the line graph \(L(K_7)\); the full available article was checked for line-graph and triangular-graph treatments. The Kneser-graph symmetry calculation for \(KG(6,2)\) concerns a distinct graph with different symmetry group and degree, so its Specht decomposition does not imply this one. The new assertion distinguishes the sign-twisted and untwisted permutation representations, which collapse to the same representation in characteristic two.

## Limitations
The theorem determines **only** degree-four integral homology and its rational \(\mathfrak S_7\)-representation. It does not identify the integral \(\mathbb Z[\mathfrak S_7]\)-module, lower-degree integral torsion, attaching maps, or complete homotopy type. The exact computation is finite and reproducible for this specific twenty-one-vertex complex; it makes no extrapolation to larger triangular graphs. Unindexed or differently named equivalent results may exist; searching is not a proof of universal novelty. Independent scientific verification has not been performed.

## References
1. R. Fröberg, *Stanley–Reisner rings of neighborhood complexes and linear resolutions*, Journal of Algebraic Combinatorics **63** (2026), article 56, DOI 10.1007/s10801-026-01530-x, first public May 21, 2026.
2. *Mixed-dimensional mod-two neighborhood homology first appears at \(T_7\)*, public research record dated October 11, 2026, published-finding corpus 2026 collection, record `5026f3f1e8ec`.
3. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803 (2012), background on the neighborhood-complex construction.
