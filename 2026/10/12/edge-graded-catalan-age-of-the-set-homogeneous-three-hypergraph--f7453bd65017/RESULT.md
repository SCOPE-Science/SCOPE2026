# Edge-graded Catalan age of the set-homogeneous three-hypergraph

## Finding

Let \(M_3\) be the countable, set-homogeneous but nonhomogeneous 3-uniform hypergraph defined by Assari, Hosseinzadeh and Macpherson from the unique strongly dense ordered 2-regular \(C\)-set. For \(n\geq1\), let \(a_{n,e}\) count isomorphism types of induced \(n\)-vertex subhypergraphs of \(M_3\) with exactly \(e\) hyperedges, and define \(P_n(q)=\sum_e a_{n,e}q^e\).

**Theorem.** The complete edge-graded age has the exact recursive description
\[
P_1(q)=1,\qquad P_n(q)=\sum_{a=1}^{n-1}q^{a\binom{n-a}{2}}P_a(q)P_{n-a}(q)\quad(n\geq2).
\]
In particular, \(P_n(1)=C_{n-1}=\frac1n\binom{2n-2}{n-1}\) (the Catalan number), and
\[
q^{\binom n3}P_n(q^{-1})=P_n(q).
\]
For five vertices this specializes to
\[
P_5(q)=1+q+q^2+2q^3+2q^4+2q^6+2q^7+q^8+q^9+q^{10}.
\]
Thus there are precisely **14** five-vertex induced isomorphism types and **none has exactly five edges**, although every other edge count between zero and ten occurs. For six vertices there are precisely \(42\) types, including four ten-edge types. More generally, for **every \(n\ge6\)** and **every integer \(0\le e\le\binom n3\)**, at least one induced \(n\)-vertex type has exactly \(e\) edges. Thus **the lone missing intermediate edge count at any positive order is \(n=5,e=5\)**.

The induced action on injective ordered \(n\)-tuples has exactly \(n!C_{n-1}\) orbits. Allowing repeated coordinates, its orbit number is
\[
\sum_{r=1}^{n}\left\{\begin{matrix}n\\r\end{matrix}\right\}r!C_{r-1},
\]
where braces denote Stirling numbers of the second kind. This ungraded sequence begins \(1,3,19,207,3211,64383\) for \(n=1,\ldots,6\) and coincides numerically with OEIS A052886; only its interpretation for this hypergraph and the edge-graded recurrence are claimed here.

## Assumptions and scope

Fix the ordered 2-regular \(C\)-set \((M,C,<)\) from Theorem 3.1.1 of the cited paper. Its finite distinct-point configurations are restrictions of a planar binary branching geometry: the finite minimal subtree spanning \(n\) selected maximal chains is, after suppressing nonbranching vertices, a rooted plane full binary tree with \(n\) leaves in increasing order. Such configurations of every finite plane full binary shape occur, and two restrictions are isomorphic as ordered \(C\)-sets precisely when their reduced plane trees have the same shape. Put a symmetric hyperedge on three distinct points exactly when the **least** point \(x\) satisfies \(C(x;y,z)\) for the other two, as in Section 3.1 of the source.

The enumeration concerns induced finite subhypergraphs **up to ordinary hypergraph isomorphism**, not labeled hypergraphs and not arbitrary 3-uniform hypergraphs. The automorphism-orbit statements refer to the full countable \(M_3\), not the internal automorphism groups of its finite restrictions.

## Proof

**Finite-shape classification.** For a finite collection of maximal chains, truncate the underlying semilinear 2-branching tree just above their pairwise splits and suppress every unary vertex. Each internal branching vertex then has two ordered children and the chosen points form its leaves. The \(C\)-relation determines which two of any three leaves remain together below their first common branch, and the inherited order determines the left and right children. Conversely these ternary decisions reconstruct all clusters: a subset forms a cluster exactly when all its leaves coalesce below some branch before merging with an outside leaf. Thus the ordered \(C\)-structure and the reduced plane full binary tree determine one another. Strong density of the ambient countable ordered \(C\)-set provides arbitrarily deep ordered splits, so each plane full binary shape is realized. Homogeneity identifies exactly the configurations with equal reduced shapes.

The cited Proposition 3.1.2 proves both set-homogeneity of \(M_3\) and
\[\operatorname{Aut}(M_3)=\operatorname{Aut}(M,C,<).\]
Therefore two finite induced **hypergraphs** are isomorphic if and only if they lie in one set-orbit of this automorphism group, if and only if their reduced plane full binary trees agree. This uses set-homogeneity essentially: definability of the order in the ambient structure does not assert that every finite hypergraph isomorphism preserves the restricted order. Rather, the source proves existence of some ambient automorphism carrying the two underlying finite sets.

**Edge statistic.** Let \(T\) be such a plane tree, with left and right root subtrees \(L,R\) containing \(a,b\) leaves, respectively. An increasing triple entirely in one root subtree has the edge status prescribed by that subtree. Among triples meeting both sides, one with a leaf in \(L\) and two in \(R\) is a hyperedge: its least leaf separates from the other two at the root. A triple with two leaves in \(L\) and one in \(R\) is not a hyperedge. Hence
\[e(T)=e(L)+e(R)+a\binom b2.\]
Every rooted plane full binary tree has a unique root split. Multiplying the edge-count generating polynomials of the two subtrees and summing over \(a+b=n\) yields the stated recurrence. Specializing \(q=1\) gives the Catalan recurrence and its closed form.

**Complement symmetry.** Mirror the tree, exchanging left and right at every internal node. On each increasing triple the least-point \(C\)-decision is reversed, so the corresponding hyperedge status is complemented. The mirror involution maps a tree of edge count \(e\) to one of edge count \(\binom n3-e\), proving palindromicity.

**No further edge-count gaps.** The coefficient vector of \(P_6(q)\), indexed by degrees zero through twenty, is \( (1,1,1,2,3,1,3,3,2,2,4,2,2,3,3,1,3,2,1,1,1)\), with every entry positive. Suppose at some \(n\ge7\) all degrees from zero through \(\binom{n-1}{3}\) occur on \(n-1\) leaves. Attach a new rightmost leaf to the root as a singleton right child; the edge count is unchanged, so every degree in \([0,\binom{n-1}{3}]\) occurs. Attaching instead a new leftmost singleton leaf adds \(\binom{n-1}{2}\) edges, so every degree in \([\binom{n-1}{2},\binom n3]\) occurs. These two integer intervals overlap for \(n\ge7\), since \(\binom{n-1}{3}\ge\binom{n-1}{2}-1\). This proves the all-order full-support claim by induction and isolates the five-point exception.

**Tuple orbit formula.** The exact order of any \(r\) pairwise distinct points can be chosen in \(r!\) ways for an ordered tuple, and the reduced plane tree has \(C_{r-1}\) possible shapes. For a tuple with repetitions, first partition the \(n\) coordinate positions into \(r\) nonempty equal-value blocks in \(\left\{\begin{smallmatrix}n\\r\end{smallmatrix}\right\}\) ways. The displayed expression follows. No identification by finite internal automorphisms is made, since the ambient group preserves \(<\).

## Verification

Run `python3 artifacts/verify.py` with Python 3's standard library. The program independently constructs all plane full binary shapes through nine leaves, calculates the hyperedge relation from the ternary root-split rule, and independently computes the weighted polynomial recursion through eleven leaves. It checks equality of the two distributions, Catalan totals, palindromicity, the five-vertex missing middle count, and the six-vertex full-support base used in the induction.

For all \(1\le n\le6\), it also enumerates **every** permutation of the vertices for each tree's induced hypergraph and computes a canonical bit representation, verifying that different plane shapes are never hypergraph-isomorphic. The replay yields `VERIFY_OK 73 exact assertions; exhaustive plane-tree shapes through n=9; permutation-isomorphism classification through n=6`. These finite tests support but do not replace the all-arity combinatorial proof or the cited homogeneous-model theorems.

## Relationship to prior work

Assari–Hosseinzadeh–Macpherson prove the construction, the ambient automorphism-group identification, and set-homogeneity (Theorem 3.1.1 and Proposition 3.1.2); their proof explicitly analyzes left and right root cones. Their Figure 3 records the five four-vertex configurations with zero through four edges. The **new object of calculation** here is the entire edge-graded finite age for every cardinality, including the weighted Catalan recurrence, the unique five-vertex forbidden edge-count, and the full-support theorem in every larger arity, not the construction or set-homogeneity themselves.

The count \(C_{n-1}\) for plane full binary trees is classical. Moreover, OEIS A052886 already records the Stirling–Catalan formula for the ungraded ordered-tuple sequence. Accordingly neither Catalan numbers nor that numeric sequence are independently asserted to be new. The separate claimed contribution is their exact interpretation in \(M_3\) together with its hyperedge-graded age polynomial. Targeted literature and mathematical-index searches found no formulation of that polynomial for \(M_3\); an unindexed prior derivation remains possible.

## Limitations

This is a derived classification of one explicitly defined countable hypergraph, not a classification of arbitrary set-homogeneous hypergraphs. It inherits the ambient structure and group-identification results from the primary paper. It does not characterize which arbitrary finite 3-hypergraphs embed into \(M_3\) without reference to the tree encoding, nor compute general automorphism groups of finite members. The verification is finite, and an independent mathematical audit has not been performed.

## References

1. A. Assari, N. Hosseinzadeh, D. Macpherson, *Set-homogeneous hypergraphs*, arXiv:2202.09613v1, first public 19 February 2022; J. London Math. Soc. 108 (2023), 1852–1885, DOI:10.1112/jlms.12796. Theorem 3.1.1 and Proposition 3.1.2. https://arxiv.org/abs/2202.09613 ; https://doi.org/10.1112/jlms.12796
2. OEIS A000108, Catalan numbers. https://oeis.org/A000108
3. OEIS A052886, exponential generating function and Stirling–Catalan convolution. https://oeis.org/A052886
