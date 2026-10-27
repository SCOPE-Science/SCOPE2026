# Minimum identifying-code exchanges in three-row rook graphs

## Finding
For every integer \(m\ge4\), consider the Cartesian product \(G_m=K_3\square K_m\), with vertex set \(\{0,1,2\}\times\{0,\ldots,m-1\}\). Two distinct vertices are adjacent if and only if they share their row or their column. A set \(C\) is an identifying code if the signatures \(N[v]\cap C\), over all vertices \(v\), are nonempty and pairwise distinct.

All *minimum* identifying codes have size \(2m-3\). They are exactly the matrices with one singleton column containing \((i,j_i)\) for each \(i\in\{0,1,2\}\), where \(j_0,j_1,j_2\) are distinct, and exactly two selected cells in every other column. Thus the exact number of minimum codes is
\[
|\mathcal C_m|=m(m-1)(m-2)\,3^{m-3}.
\]

Let \(X_m\) be the graph on \(\mathcal C_m\) in which two codes are adjacent precisely when one selected vertex is removed and one previously unselected vertex is added. Then \(X_m\) is **connected and \(6(m-3)\)-regular**, with exactly
\[
|E(X_m)|=3(m-3)m(m-1)(m-2)\,3^{m-3}
\]
edges. Every possible exchange belongs to one of the two types specified in the proof below. The natural action of row permutations and column permutations partitions \(\mathcal C_m\) into orbits indexed by integer partitions of \(m-3\) into at most three parts (zeros permitted).

The scalar optimum \(\gamma^{\rm ID}(G_m)=2m-3\) is an earlier result of Goddard and Wash; the claim here is the full equality-case description and the resulting exact reconfiguration graph, counting, regularity, connectivity, and natural symmetry orbits.

## Assumptions and scope
The graph is simple, undirected, and *Cartesian* (not the direct/tensor product). All rows and columns are labeled. A row is a set \(\{i\}\times\{0,\ldots,m-1\}\); a column is \(\{0,1,2\}\times\{j\}\). The exchange rule is **token jumping**, so the removed and added vertices need not be adjacent in \(G_m\). The result holds for every integer \(m\ge4\), without an upper bound. It does not assert a classification of all identifying codes, nor a formula for exchange-graph diameter.

## Proof
**1. Same-row separation bound.** For a proposed code \(C\), let \(R_i\) denote its selected cells in row \(i\), and \(B_j\) those in column \(j\). The identifying signature of \((i,j)\) is precisely
\[
I(i,j)=R_i\cup B_j.
\]
For different columns \(j\ne k\), the sets \(B_j\setminus R_i\) and \(B_k\setminus R_i\) are disjoint, and hence \(I(i,j)=I(i,k)\) exactly when *both* are empty. In an identifying code, therefore, for each \(i\), at most one column has all its selected cells confined to row \(i\).

If a column is empty, every other column must contain at least two selected cells; otherwise an empty and a singleton column violate this condition for the singleton's row. Two empty columns are impossible. Consequently an identifying code with an empty column has size at least \(2(m-1)>2m-3\). If there are no empty columns, at most three columns are singletons (at most one in each of the three distinct rows). Every other column contains at least two selected cells, giving \(|C|\ge 2m-3\). Equality is possible only with precisely three singleton columns, one in each row, and exactly two selected cells in each other column.

**2. Sufficiency of the equality patterns.** Now fix any such pattern. Every column is nonempty, so all signatures are nonempty. The same-row argument separates any two different cells in one row, since exactly one singleton column is supported in that row. Suppose signatures of cells \((i,j)\) and \((h,k)\) in different rows \(i\ne h\) coincide. Let \(x_i\) and \(x_h\) be the unique selected cells in the respective singleton columns \(j_i\) and \(j_h\). Since \(x_i\) belongs to the first signature, it can enter the second only via its column, forcing \(k=j_i\). Similarly \(j=j_h\). Equality then forces
\[
R_i\setminus\{x_i\}=R_h\setminus\{x_h\}.
\]
The two sides lie in different rows and are disjoint, so both must be empty. But \(m\ge4\) guarantees a double column, and its two selected rows include at least one of \(i,h\). This contradiction establishes pairwise distinctness. Hence every equality pattern is an identifying code, proving the minimum size and complete classification without assuming the old numerical theorem.

**3. Exact enumeration.** Choose the columns \(j_0,j_1,j_2\) for the three distinct singleton-row labels injectively, in \(m(m-1)(m-2)\) ways. Each of the other \(m-3\) columns has three possible missing rows. This proves the code count.

**4. Complete move rule.** Write \(S_i\) for a column containing only row \(i\), and \(D_a\) for a column containing both rows other than \(a\). Every valid word contains exactly one of each \(S_0,S_1,S_2\) and \(m-3\) letters from \(D_0,D_1,D_2\). A one-selected/one-unselected exchange stays within this class if and only if it is one of the following:

* A **double recoloring** \(D_a\to D_b\) in one column, where \(a\ne b\), by replacing the selected cell in row \(b\) with the formerly unselected cell in row \(a\). Each double column admits two such moves.
* A **singleton relocation** between a column \(S_i\) and a column \(D_a\), where \(a\ne i\): change the former \(D_a\) to \(S_i\), and the former \(S_i\) to \(D_b\) for any \(b\ne i\). This is realized by removing the other selected cell in \(D_a\) and adding one of the two available cells in the old singleton column. The two choices of \(b\) give two distinct exchanges.

Indeed, any move either preserves the counts of selected cells in each column, in which case it is a double recoloring (recoloring a singleton would duplicate its row label), or changes the count in two columns. The equality-case description then forces an old double to become a singleton and an old singleton to become a double, with the singleton's row label preserved. Moves involving a triple or empty column cannot be optimal. For each double column there are two double recolorings and \(2\times2=4\) singleton relocations, which are all distinct. Thus every code has degree \(6(m-3)\). Half the product of vertex count and degree gives the edge count.

**5. Connectivity.** A double column \(D_a\) can be freely recolored to either other double type while maintaining optimality. A marker \(S_i\) can be moved to any double column: first recolor that double column to \(D_a\) with \(a\ne i\), then perform a singleton relocation. At least one double column always exists. Choose any three distinct target columns for \(S_0,S_1,S_2\). Fix the singleton markers sequentially. If the next target is occupied by another, as yet unfixed, singleton marker, first move that marker into an available double-column buffer. Then move the desired marker into its target. This never dislodges a marker previously fixed at its *different* target, and a double buffer remains after each move. Once the three markers occupy their target columns, recolor all remaining double columns independently. Hence any two codes are connected by exchanges.

**6. Symmetry classes.** The natural group \(S_3\times S_m\) permutes row labels and column labels. The multiset of multiplicities of missing-row labels among double columns is invariant, up to row relabeling. Conversely, equal unordered multiplicity triples can be matched by a row permutation and then a column permutation, including the three singleton positions. These are exactly the natural-group orbits, indexed by partitions of \(m-3\) into at most three parts. This does not purport to classify orbits under the full automorphism group of \(X_m\).

## Verification
The bundled `verify.py` independently generates closed neighborhoods directly from graph adjacency. For each \(4\le m\le7\), it tests *all* subsets of cardinality at most \(2m-3\) for distinct nonempty signatures, comparing the resulting optimum codes against the explicit column-word classification. It then independently reconstructs all one-for-one set exchanges and compares them to the two move rules, computes degrees/edge totals, and checks connectivity by breadth-first search. It also performs a complete configuration-level exchange check for \(m=8\). Results for \(m=4,5,6,7,8\) respectively are \(72,540,3240,17010,81648\) code vertices, with \(216,3240,29160,204120,1224720\) exchange edges. Run `python3 verify.py` from the directory containing this document.

## Relationship to prior work
Goddard and Wash's Theorem 2.2 already gives the numerical identifying-code optimum for arbitrary Cartesian products of two cliques, including the \(3\)-by-\(m\) family. Their proof develops lower bounds and an explicit construction, not the set of *all* optimum codes nor their token-jumping transitions. Foucaud, Gravier, Naserasr, Parreau and Valicov study identifying codes in line graphs, including the line-graph interpretation of complete bipartite graphs and results on equal part sizes. That general machinery does not state the present optimum-exchange classification. Teshima's work on identifying-code reconfiguration investigates a vertex-slide variant and realization constructions for arbitrary target graphs, rather than the explicit token-jumping graph of this Cartesian product. A search for alternate terms, including *edge-identifying code of \(K_{3,m}\)* (the equivalent line-graph formulation), did not locate a stronger coverage theorem. This is not an assertion of absolute priority.

## Limitations
The result is restricted to \(m\ge4\); the three-by-three case has a different optimum size. The connectivity theorem does not give a diameter formula, a mixing-time estimate, or an explicit Hamilton cycle. Numerical verification is finite and not a substitute for the proof. Earlier equivalent descriptions under uncommon terminology, or unindexed references, remain possible; independent mathematical review has not been performed.

## References
1. W. Goddard and K. Wash, *ID Codes in Cartesian Products of Cliques*, Journal of Combinatorial Mathematics and Combinatorial Computing 85 (2013), 97–106, Theorem 2.2 and Sections 2.1–2.2. Public journal record: https://combinatorialpress.com/jcmcc-articles/volume-085/id-codes-in-cartesian-products-of-cliques/ ; author PDF: https://people.computing.clemson.edu/~goddard/papers/idCodeProduct.pdf .
2. F. Foucaud, S. Gravier, R. Naserasr, A. Parreau, and P. Valicov, *Identifying codes in line graphs*, arXiv:1107.0207 (first submitted July 1, 2011), especially Sections 1–2. https://arxiv.org/abs/1107.0207 .
3. L. E. Teshima, *The i-Graph and Other Variations on the Gamma-Graph*, University of Victoria dissertation (2022), Chapter 2, Section 2.1. https://dspace.library.uvic.ca/items/740e5c10-d1aa-4992-970b-3711b397f7f5 .
