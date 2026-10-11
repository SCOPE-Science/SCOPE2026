# Equivariant top homology of balanced complete-bipartite Morse complexes

## Finding
Let \(m\ge 2\) be an integer and let \(\mathfrak M(K_{m,m})\) be the ordinary discrete-Morse-matching complex of the complete bipartite graph. Write \(u_1,\dots,u_m\) and \(v_1,\dots,v_m\) for the two vertex classes, and let \(\tau\) exchange \(u_i\leftrightarrow v_i\) for every \(i\). The induced involution on its unique nonzero reduced integral homology group has trace
\[
\operatorname{tr}\!\left(\tau_*\mid\widetilde H_{2m-2}(\mathfrak M(K_{m,m});\mathbb Z)\right)=(-1)^m(m-1)^{m-1}.
\]
In fact, if \(R_m=(2m-1)(m-1)^{2m-2}\) and \(T_m=(-1)^m(m-1)^{m-1}\), then the positive and negative eigenspaces over \(\mathbb Q\) have dimensions \((R_m+T_m)/2\) and \((R_m-T_m)/2\), respectively.

For \(m=4\), the entire degree-\(6\) rational character under the natural graph-automorphism group \(G=(S_4\times S_4)\rtimes C_2\) is given by the following complete table. The side-preserving classes are indexed by *unordered pairs* of cycle types in \(S_4\). For side-exchanging classes, the label is the cycle type of the permutation obtained by squaring and restricting to either bipartition class.

| Automorphism class | Class size | Top-homology trace |
|---|---:|---:|
| Side-preserving \( (4),(4) \) | 36 | 7 |
| Side-preserving \( (4),(3,1) \) | 96 | 0 |
| Side-preserving \( (4),(2,2) \) | 36 | 3 |
| Side-preserving \( (4),(2,1,1) \) | 72 | 3 |
| Side-preserving \( (4),(1,1,1,1) \) | 12 | 3 |
| Side-preserving \( (3,1),(3,1) \) | 64 | 0 |
| Side-preserving \( (3,1),(2,2) \) | 48 | 0 |
| Side-preserving \( (3,1),(2,1,1) \) | 96 | 0 |
| Side-preserving \( (3,1),(1,1,1,1) \) | 16 | 0 |
| Side-preserving \( (2,2),(2,2) \) | 9 | 63 |
| Side-preserving \( (2,2),(2,1,1) \) | 36 | 3 |
| Side-preserving \( (2,2),(1,1,1,1) \) | 6 | -9 |
| Side-preserving \( (2,1,1),(2,1,1) \) | 36 | 15 |
| Side-preserving \( (2,1,1),(1,1,1,1) \) | 12 | -45 |
| Side-preserving \( (1,1,1,1),(1,1,1,1) \) | 1 | 5103 |
| Side-exchanging; squared permutation type \( (4) \) | 144 | -1 |
| Side-exchanging; squared permutation type \( (3,1) \) | 192 | 0 |
| Side-exchanging; squared permutation type \( (2,2) \) | 72 | 3 |
| Side-exchanging; squared permutation type \( (2,1,1) \) | 144 | -1 |
| Side-exchanging; squared permutation type \( (1,1,1,1) \) | 24 | 27 |


There are exactly \(20\) conjugacy classes. Their sizes sum to \(1152\), and the class-size-weighted sum of the displayed characters is \(6912\). In particular,
\[
\operatorname{rank}_{\mathbb Z}\!\left(\widetilde H_6(\mathfrak M(K_{4,4});\mathbb Z)^G\right)=6.
\]
The full homology rank is \(5103\), which is already determined by the published nonequivariant homotopy theorem. The new information is the *group action* on this homology, not the number of spheres.

## Assumptions and scope
For a finite graph \(H\), the vertices of \(\mathfrak M(H)\) are pairs consisting of an endpoint and an incident edge; a simplex is an acyclic partial matching of vertices with edges in the Hasse graph. Identify such pairs with oriented arcs pointing from the matched vertex to its opposite endpoint. Then a face is an oriented rooted forest in which each graph vertex has at most one outgoing arc and there are no directed cycles. All graphs are finite and simple, and the homology coefficients are integral except when discussing the rational isotypic decomposition. The topological action is the natural simplicial action of graph automorphisms on these arcs.

Jojić's directed-tree convention orients arcs *away* from roots, whereas the endpoint-to-edge convention here orients arcs *toward* roots. Arc reversal is an automorphism-equivariant simplicial isomorphism between the two conventions for a bidirected graph, so Jojić's nonequivariant shelling theorem applies without a sign or dimension change.

## Proof
**1. Homology concentration.** Jojić's 2012 shellability theorem and Corollary 3.1 apply to bidirected complete bipartite graphs. After reversing all arcs if needed, they give
\[
\mathfrak M(K_{m,m})\simeq \bigvee^{R_m} S^{2m-2},\qquad R_m=(2m-1)(m-1)^{2m-2}.
\]
Thus its reduced integral homology is free, concentrated in the even degree \(2m-2\), and its equivariant reduced Lefschetz number equals the trace on that group.

**2. The diagonal exchange and fixed forests.** Under \(\tau\), the two arcs \(u_i\to v_j\) and \(v_i\to u_j\) form one orbit. If \(i=j\), selecting this orbit gives a directed two-cycle, which is forbidden. For \(i\ne j\), selecting this orbit can be denoted by the arrow \(i\to j\) on the \(m\) index vertices. Every invariant face is a union of whole arc orbits, and the at-most-one-outgoing-arc condition becomes the same condition on these index arrows. A directed cycle among the index arrows lifts to a directed cycle in the bipartite graph, and any bipartite directed cycle projects to a directed cycle among the index arrows. Hence invariant faces correspond *bijectively* to rooted forests of the complete graph \(K_m\).

**3. Signed Lefschetz enumeration.** On a fixed simplex made of \(r\) selected two-element arc orbits, \(\tau\) acts on its \(2r\) vertices as \(r\) transpositions, so its orientation sign is \((-1)^r\). The augmented simplicial-chain Lefschetz identity gives the reduced Lefschetz number as the negative of the alternating signed sum over all invariant faces, including the empty face. Since each face has \(2r\) arcs, this is
\[
\widetilde L(\tau)=-\sum_{F\text{ a rooted forest on }K_m}(-1)^{|E(F)|}.
\]
The rooted-forest matrix-tree identity gives, for the graph Laplacian \(L_{K_m}\),
\[
\sum_F t^{|E(F)|}=\det(I+tL_{K_m})=(1+mt)^{m-1}.
\]
One proof of the first equality expands the determinant into principal Laplacian minors and applies the all-minors matrix-tree theorem, with the complementary vertices marked as forest roots. Evaluation at \(t=-1\) yields \(\widetilde L(\tau)=-(1-m)^{m-1}=(-1)^m(m-1)^{m-1}\), proving the trace formula. The two involution eigenspace multiplicities follow from their sum \(R_m\) and difference \(T_m\).

**4. The complete character for \(m=4\).** The group \((S_4\times S_4)\rtimes C_2\) has fifteen side-preserving conjugacy classes (unordered pairs of partitions of four) and five side-exchanging classes (indexed by the cycle type of the product of the two side permutations). For each representative, enumerate all oriented partial functions from the eight graph vertices to an opposite-side vertex or to a root, and discard cyclic assignments. This gives exactly \(140625\) rooted-forest faces, including the empty face, with cardinalities
\[
(1,32,432,3200,14080,36864,53248,32768).
\]
For the induced permutation on the \(32\) oriented arcs, a face is fixed precisely when its mask is a union of full arc orbits. If such a face contains \(r\) arc orbits, the product of its alternating chain sign and orientation sign is \((-1)^r\). Its contribution to the top-homology trace is consequently \(-(-1)^r\). Summing exact integers for every representative gives the displayed twenty values. The accompanying program specifies every representative, tests every possible face, reproduces the table, and checks the conjugacy-class-weighted average \(6912/1152=6\).

## Verification
Run `python3 verify_equivariant_k44.py`. The dependency-free program checks the complete face enumerator, all twenty conjugacy-class trace values, all class sizes, the rank-six invariant subspace, and the diagonal-swap trace for \(m=2,3,4\); successful completion prints `VERIFY_OK`. These finite checks validate the character table but are **not** offered as a proof of the general all-\(m\) formula, which follows symbolically above.

## Relationship to prior work
Jojić (2012) proves shellability and the ordinary nonequivariant wedge-of-spheres decomposition of the directed-tree complex for complete multipartite graphs. In particular, its \(5103\)-sphere count at \(K_{4,4}\) is prior work. Knudson and Owens–White (2026) review the original discrete-Morse-matching complex and distinguish it from their *strong* Morse complex; the latter is not used in this character calculation. Kozlov's earlier study of complete bidirected graph complexes includes symmetric-group phenomena, but it does not directly state the diagonal bipartition-exchange character or the twenty-class character for the complete bipartite subgraph.

## Limitations
The formula concerns only the specified diagonal swap for arbitrary \(m\). The exhaustive full character table is proved only for \(K_{4,4}\), not for every balanced complete bipartite graph. Character values determine the complexified representation, but do not classify integral lattices or equivariant homotopy types. No statement is made about strong discrete Morse complexes. Earlier unindexed equivalent equivariant formulas remain a bibliographic possibility; independent validation has not been performed.

## References
1. K. P. Knudson and A. Owens–White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844v1 (first public 2026-09-06), primary MSC2020 57Q70; https://arxiv.org/html/2609.06844v1.
2. D. Jojić, *Complexes of directed trees of complete multipartite graphs*, Publications de l'Institut Mathématique 92(106) (2012), 43–51, DOI:10.2298/PIM1206043J; especially Definition 1.1, Theorem 2.1, Corollary 3.1, and Theorem 3.2.
3. D. N. Kozlov, *Complexes of Directed Trees*, Journal of Combinatorial Theory A 88 (1999), 112–122, DOI:10.1006/jcta.1999.2984.
4. P. Chebotarev and E. Shamis, *Matrix-Forest Theorems*, arXiv:math/0602575v1 (2006); the determinant identity is also an application of the all-minors matrix-tree theorem.
