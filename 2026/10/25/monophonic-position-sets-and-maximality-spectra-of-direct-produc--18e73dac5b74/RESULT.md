# Monophonic position sets and maximality spectra of direct products of complete graphs

## Finding

For integers \(p,q\ge 3\), let \(G=K_p\times K_q\) denote the **categorical (tensor/direct) graph product**. Its vertices are cells \((i,j)\), and distinct cells are adjacent exactly when they differ in both coordinates. A vertex set is in *monophonic position* when no induced path of \(G\) contains three of its vertices.

**Classification.** Every monophonic-position set of size at least three is a clique, and conversely every clique is in monophonic position. All sets of size at most two are in monophonic position. The full cardinality enumerator is therefore
\[
 P_{p,q}(z)=1+pqz+\binom{pq}{2}z^2
 +\sum_{k=3}^{\min(p,q)}\binom pk\binom qk k!\,z^k.
\]
In particular, the monophonic position number is \(\operatorname{mp}(G)=\min(p,q)\), and the number of maximum sets is \(\binom p m\binom q m m!\), where \(m=\min(p,q)\).

**Inclusion maximality.** An inclusion-maximal monophonic-position set is exactly (i) a pair of nonadjacent vertices, or (ii) a clique of size \(m\). Thus the complete enumerator of inclusion-maximal sets is
\[
 P_{p,q}^{\mathrm{max}}(z)=
 \left[p\binom q2+q\binom p2\right]z^2
 +\binom pm\binom qm m!\,z^m.
\]
In particular, the smallest inclusion-maximal size equals \(2\), while the largest equals \(m\). The difference \(m-2\) is unbounded as both factors grow. Moreover, every pair of nonadjacent vertices is a **monophonic interval generator**: every other vertex lies on an induced path joining that pair. In the terminology of Brešar, Cornet and Dravec, these categorical products are *strongly 2-monophonic*. This covering property is distinct from the monophonic-position condition being counted. Furthermore, a whole coordinate row is a *geodesic* general-position set of cardinality \(q\); hence for \(p=3\) and arbitrary \(q\ge3\), the difference \(\operatorname{gp}(G)-\operatorname{mp}(G)\) is at least \(q-3\), an unbounded separation between the geodesic and induced-path notions on connected diameter-two graphs.

## Assumptions and scope

The graph is finite, simple and undirected. The categorical product here is **not** the Cartesian product: its adjacency condition is \((i,j)\sim(i',j')\) precisely when \(i\ne i'\) and \(j\ne j'\). Every quantifier above holds for all integers \(p,q\ge3\), with no assumption of equal factor sizes. The coefficient of \(z^k\) counts distinct vertex subsets, not orderings or symmetry orbits. A maximal set means maximal under inclusion, whereas a maximum set has largest cardinality. The notation \(\binom nk\) has its usual combinatorial meaning.

## Proof

**Lemma (induced-path witnesses for every nonclique triple).** Suppose three different cells of \([p]\times[q]\) do not form a clique. Permuting row and column symbols, and possibly exchanging the two coordinates, reduces the triple to one of the following three configurations. Each configuration has an induced path containing all three cells, where the displayed arrows specify the vertex order.

1. **Three cells in a single row:** the triple \((0,0),(0,1),(0,2)\) lies on
\[
 (0,0)\to(1,1)\to(0,2)\to(1,0)\to(0,1).
\]
2. **A repeated row and a third cell sharing a column with one of the repeated-row cells:** the triple \((0,0),(0,1),(1,0)\) lies on
\[
 (0,0)\to(2,1)\to(1,0)\to(0,1).
\]
3. **A repeated row and a third cell with a different column from both repeated-row cells:** the triple \((0,0),(0,1),(1,2)\) itself induces a length-two path
\[
 (0,0)\to(1,2)\to(0,1).
\]

Every displayed consecutive pair differs in both coordinates, while every nonconsecutive pair shares at least one coordinate; hence each displayed path has no chord. These paths require only three symbols per coordinate, which exist by assumption. The corresponding repeated-column configurations follow by interchanging coordinates. In every configuration the two repeated-row (or repeated-column) vertices are the **endpoints** of the displayed induced path, while the third vertex appears internally. This also proves that every nonadjacent pair has every other vertex in its monophonic interval. Every nonclique triple falls into one of these configurations: if all three row coordinates and all three column coordinates are distinct, it is a clique; otherwise some row or column is repeated, and the cases above exhaust the multiplicities. This proves the lemma.

A clique is monophonic-position, because an induced path cannot include three pairwise adjacent vertices: the edge joining its first and last of those vertices would be a chord of the intervening subpath. Conversely, if a monophonic-position set has at least three vertices but is not a clique, it contains a nonclique triple; the lemma gives an induced path through that triple, a contradiction. Sets of at most two vertices satisfy the definition vacuously. Therefore the classification holds.

A clique of \(k\) cells uses \(k\) distinct rows and \(k\) distinct columns, together with a bijection between those selected row and column sets. This gives exactly \(\binom pk\binom qk k!\) cliques when \(3\le k\le m\), and none larger. The full polynomial and maximum-size count follow.

For inclusion maximality, a nonadjacent pair cannot be extended because every admissible triple must be a clique. Every adjacent pair can be extended to a triangle by choosing a fresh row and fresh column (possible since \(p,q\ge3\)). Every clique of size less than \(m\) can similarly be extended; every clique of size \(m\) is inclusion-maximal. The nonadjacent pairs are exactly the pairs sharing a row or sharing a column, without double counting, giving \(p\binom q2+q\binom p2\). This proves the second polynomial and cardinality-spectrum statements.

Finally, vertices in one coordinate row are pairwise nonadjacent and have graph distance two (because both factor sizes are at least three). A geodesic between any such pair has one internal vertex outside that row, so the complete row is a geodesic general-position set. The graph has diameter two because any two nonadjacent cells share a common neighbor, and it is connected. Taking \(p=3\) proves the unbounded separation stated above.

## Verification

The standalone file `verify.py` enumerates all induced paths directly from the adjacency condition, constructs all forbidden triples, checks all vertex subsets and all inclusion-maximal subsets, and compares both complete coefficient dictionaries with the formulas. Execution using `python3 verify.py` returned `VERIFY_OK` for factor sizes \((3,3),(3,4),(3,5),(4,4)\). The program separately verifies adjacency and absence of chords in all three canonical witness paths and their transposes. The finite tests are checks of the implementation and edge cases; the proof above establishes the universal claim.

The resulting monophonic-position polynomial coefficients in those instances are respectively \((1,9,36,6)\), \((1,12,66,24)\), \((1,15,105,60)\), and \((1,16,120,96,24)\). Their inclusion-maximal size profiles are respectively \(18z^2+6z^3\), \(30z^2+24z^3\), \(45z^2+60z^3\), and \(48z^2+24z^4\).

## Relationship to prior work

Thomas, Ullas Chandran, Tuite and Di Stefano introduced monophonic position, established general structural lemmas and considered unicyclic, complement-of-bipartite, split, join and corona families. Their Lemma 3.1 implies that an induced subgraph on a monophonic-position set is a disjoint union of cliques; the present induced-path witnesses strengthen this to a **single clique for sets with three or more vertices in the specified direct products**, and yield an exact enumeration.

Di Stefano, Klavžar, Krishnakumar, Tuite and Yero established the lower **geodesic** general-position number of the same direct products, \(\operatorname{gp}^{-}(K_p\times K_q)=\min\{p,q,4\}\). This concerns shortest paths, not induced paths, and does not enumerate monophonic-position sets. Iršič, Klavžar, Rus and Tuite studied the geodesic general-position polynomial of related direct products, again a distinct family of feasible sets. Chandran, Klavžar, Neethu and Tuite studied *Cartesian* and *lexicographic* products for monophonic position; those adjacency relations differ from the categorical product treated here. Brešar, Cornet and Dravec introduced the strongly 2-monophonic condition in the sense of induced-path **coverage**, proved general sufficient conditions and studied Kneser, Johnson and Cartesian-product Hamming graphs. Their 2025 paper asks which vertex-transitive graphs have that property. The categorical products treated here are different from their Hamming graphs; our path witnesses establish an additional vertex-transitive family and then its distinct **monophonic-position** enumerators. These earlier definitions and results are credited; no claim is made to have invented monophonic position or graph-product enumerators in general.

## Limitations

The result is restricted to \(p,q\ge3\). The two-row or two-column boundary is not classified here. The exact formulas do not assert any analogous statement for arbitrary categorical products of noncomplete factor graphs. Prior-literature comparisons cannot exclude every unindexed or inaccessible source. No independent mathematical audit has been performed.

## References

1. E. J. Thomas, S. V. Ullas Chandran, J. Tuite and G. Di Stefano, *On monophonic position sets in graphs*, arXiv:2012.10330, first posted 2020-12-18, https://arxiv.org/abs/2012.10330.
2. G. Di Stefano, S. Klavžar, A. Krishnakumar, J. Tuite and I. Yero, *Lower General Position Sets in Graphs*, arXiv:2306.09965, first posted 2023-06-16, https://arxiv.org/abs/2306.09965.
3. V. Iršič, S. Klavžar, G. Rus and J. Tuite, *General position polynomials*, arXiv:2401.05696, first posted 2024-01-11, https://arxiv.org/abs/2401.05696.
4. S. V. Ullas Chandran, S. Klavžar, P. K. Neethu and J. Tuite, *Monophonic position sets of Cartesian and lexicographic products of graphs*, arXiv:2412.09837, first posted 2024-12-13, https://arxiv.org/abs/2412.09837.
5. B. Brešar, M. G. Cornet and T. Dravec, *Monophonic number of Kneser graphs and strongly 2-monophonic graphs*, arXiv:2509.18784, first posted 2025-09-23, https://arxiv.org/abs/2509.18784.
