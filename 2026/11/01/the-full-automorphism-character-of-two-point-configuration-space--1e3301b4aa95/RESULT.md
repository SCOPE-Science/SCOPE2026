# The full automorphism character of two-point configuration spaces of finite trees

## Finding
Let \(T\) be any finite tree with at least one edge, and let \(G=\operatorname{Aut}(T)\) act on the unordered two-particle configuration space \(X_T=\operatorname{UConf}_2(|T|)\). Write \(D(v)\) for the incident directions at \(v\) and \(W_v=\ker(\mathbb Q^{D(v)}\xrightarrow{\sum}\mathbb Q)\). The full rational automorphism module is
\[
H_1(X_T;\mathbb Q)\cong\bigoplus_{v\in V(T)}\bigwedge^2 W_v,
\]
where an automorphism sends the \(v\)-summand to the corresponding summand at its image. This is an existence assertion of an isomorphism of rational representations, not a proposed canonical identification of homology generators.

For \(g\in G\), at each fixed vertex \(v\) let \(f_v(g)\) count fixed incident directions and let \(t_v(g)\) count the two-cycles in its permutation of incident directions. Then
\[
\operatorname{tr}\bigl(g\mid H_1(X_T;\mathbb Q)\bigr)
=\sum_{v:g(v)=v}\left(\frac{(f_v(g)-1)(f_v(g)-2)}2-t_v(g)\right).
\]
In particular, \(\dim H_1(X_T;\mathbb Q)=\sum_v\binom{\deg(v)-1}{2}\), and \(H_i(X_T;\mathbb Q)=0\) for all \(i\ge2\). The formula is uniform over all finite trees, including graphs whose automorphisms exchange distinct branching vertices.

## Assumptions and scope
An edge direction at \(v\) is an edge of \(T\) incident to \(v\). The term \(\frac{(f-1)(f-2)}2\) is evaluated as a polynomial for every integer \(f\ge0\), including \(f=0\). The tree need not be trivalent, rooted, or free of degree-two vertices. For the one-edge tree the representation is zero and the formula still holds. The action is the diagonal action of graph automorphisms on unordered distinct-particle configurations, not interchange of particle labels.

## Proof
**Step 1 (an equivariant cellular model).** Subdivide each edge once, obtaining \(T'\). Its graph automorphisms induced from \(G\) preserve old vertices and subdivision midpoints; in particular none reverses an oriented edge. The standard sufficiently subdivided cubical discrete-configuration model \(Y\subset X_T\) has zero-cells unordered pairs of distinct vertices, one-cells unordered pairs \(\{v,e\}\) with \(v\) not an endpoint of \(e\), and two-cells unordered pairs \(\{e,e'\}\) of vertex-disjoint edges. The model is homotopy equivalent to \(X_T\) by the graph-configuration subdivision/deleted-product theorem. Because its inclusion and the \(G\)-action commute, its cellular homology realizes the same \(G\)-representation. It suffices to calculate its signed cellular Lefschetz character. Farber's two-point tree configuration theorem (also the classical graph-braid Morse results) gives \(H_i(X_T;\mathbb Q)=0\) for \(i\ge2\); its connectedness gives \(H_0\cong\mathbb Q\).

**Step 2 (fixed cells and orientation signs).** Fix \(g\in G\). In \(T'\), let \(k\) and \(q\) be the respective numbers of individually fixed vertices and edges; let \(s_V\) and \(s_E\) count two-cycles of vertices and edges. A tree automorphism with no edge inversions fixes a nonempty connected subtree. Thus \(q=k-1\). For each fixed vertex \(v\), put \(f_v\) equal to its number of fixed incident edges, and \(t_v\) equal to its number of incident edge two-cycles.

Signed cellular traces in dimensions zero through two are, respectively,
\[
\begin{split}
L_0&=\binom{k}{2}+s_V,\\
L_1&=q(k-2),\\
L_2&=\binom{q}{2}-\sum_{g(v)=v}\binom{f_v}{2}-s_E+\sum_{g(v)=v}t_v.
\end{split}
\]
The first count separates two individually fixed vertices from a swapped pair. A fixed one-cell must consist of an individually fixed vertex and edge, and a fixed edge has two forbidden fixed endpoints. For a fixed two-cell, two individually fixed nonincident edges contribute \(+1\). Two swapped nonincident edges contribute \(-1\) because the two cellular coordinates are interchanged. Swapped edges that meet at a fixed vertex are forbidden and account for the correction \(\sum_v t_v\). A two-cycle of edges that meet has a fixed common vertex; hence this correction neither omits nor duplicates any such pair.

**Step 3 (the vertex–edge two-cycle identity).** The fixed subgraphs of \(g\) and \(g^2\) are both nonempty subtrees of \(T'\), because \(T'\) has no edge inversions. Thus their numbers of vertices minus edges both equal one. Their respective counts are \(k-q=1\) and \((k+2s_V)-(q+2s_E)=1\); subtracting yields \(s_V=s_E\). Also \(\sum_{g(v)=v}f_v=2q=2(k-1)\), counting ends of every fixed edge.

**Step 4 (Lefschetz calculation).** With only homology in dimensions zero and one, \(\operatorname{tr}(g\mid H_1)=1-(L_0-L_1+L_2)\). Using the preceding identities gives
\[
\operatorname{tr}(g\mid H_1)
=2-k+\sum_{g(v)=v}\binom{f_v}{2}-\sum_{g(v)=v}t_v
=\sum_{g(v)=v}\left(\frac{(f_v-1)(f_v-2)}2-t_v\right).
\]
The reduction uses \(\sum_v f_v=2(k-1)\). The cellular model has no cells above dimension two; the quoted dimension-one homotopy theorem is essential for interpreting this alternating trace as the first-homology trace, rather than only an Euler character.

**Step 5 (identifying the representation).** For a fixed vertex \(v\), \(\operatorname{tr}(g\mid W_v)=f_v-1\) and \(\operatorname{tr}(g^2\mid W_v)=f_v+2t_v-1\). The standard exterior-square character identity gives
\[
\operatorname{tr}\bigl(g\mid\bigwedge^2W_v\bigr)=\tfrac12\bigl((f_v-1)^2-(f_v+2t_v-1)\bigr)
=\tfrac12(f_v-1)(f_v-2)-t_v.
\]
A permutation of two different vertex summands contributes zero to the trace of their direct sum. Therefore the trace of \(g\) on \(\bigoplus_v\bigwedge^2W_v\) matches the topological trace for every \(g\in G\). Finite-dimensional rational representations of finite groups are semisimple in characteristic zero, and equality of all characters implies an isomorphism of rational \(G\)-representations. This establishes the claim.

## Verification
The accompanying `verify.py` builds the complete discrete cubical model independently for six trees (a four-arm star, five-arm star, balanced double star, balanced binary tree, six-vertex path, and tree with unequal branches). It explicitly enumerates all automorphisms of each original tree, lifts each to the once-subdivided tree, computes orientation-signed cell traces by direct vertex and edge permutations, independently computes the local branch formula, verifies mod-two boundary identities and connectedness, and checks the first Betti rank and the full cell counts. Across all tested automorphisms, the two characters match. The archived output in `verification_output.txt` is reproduced exactly by `python3 verify.py`. These finite computations corroborate the unrestricted argument but are not used as an induction or proof for arbitrary trees.

## Relationship to prior work
Farley and Sabalka's 2004 discrete-Morse framework and Barnett and Farber's 2009 two-particle graph theory support the one-dimensional topology and ordinary rank, but do not supply the character of all graph automorphisms. Farber's 2017 exposition, Theorem 11.1, gives a \(\mathbb Z_2\)-equivariant model for the **ordered** two-point configuration space under exchanging the *particle labels*. That action is not the arbitrary finite tree's full graph automorphism group. The later ordered-tree equivariant work of Aguilar-Guzmán, González, and Hoekstra-Mendoza likewise primarily treats permutations of particle labels. The present theorem determines the distinct full graph-automorphism representation uniformly for every finite tree. It encompasses the previously known two-particle star action as a special case, but does not claim that special case as original.

## Limitations
The conclusion is an isomorphism of rational representations, not an integral lattice decomposition, and no natural canonical splitting of topological cycles is asserted. The result does not address three or more particles or automorphisms of arbitrary graphs with cycles. Complete coverage of unindexed historical publications cannot be guaranteed. No independent mathematical audit has been performed.

## References
1. D. Farley and L. Sabalka, *Discrete Morse theory and graph braid groups*, arXiv:math/0410539v1 (October 25, 2004), https://arxiv.org/abs/math/0410539.
2. K. Barnett and M. Farber, *Topology of configuration space of two particles on a graph, I*, arXiv:0903.2180v1 (March 12, 2009), https://arxiv.org/abs/0903.2180; primary MSC 55R80.
3. M. Farber, *Configuration Spaces and Robot Motion Planning Algorithms*, arXiv:1701.02083v1 (January 9, 2017), https://arxiv.org/abs/1701.02083, especially Theorem 11.1.
4. J. Aguilar-Guzmán, J. González, and T. Hoekstra-Mendoza, *Farley-Sabalka's Morse-theory model and the higher topological complexity of ordered configuration spaces on trees*, arXiv:1911.12522v1 (November 28, 2019), https://arxiv.org/abs/1911.12522.
