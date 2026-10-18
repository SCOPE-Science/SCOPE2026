# Exactly 96 minimum two-dominating sets in long triangular cylinders

## Finding

For every integer \(n\ge 7\), the graph \(G_n=C_3\square P_n\) has precisely \(96\) minimum two-dominating vertex sets. Every such set has \(n+2\) vertices. Moreover, all minimum sets are classified as follows: exactly one of columns \(1,2\) has two selected vertices, exactly one of columns \(n-1,n\) has two selected vertices, and every other column has one selected vertex. Each of these four column-size profiles admits exactly \(24\) sets. The isolated selected vertices between the two double columns form a three-periodic rainbow pattern.

## Assumptions and scope

The graph \(C_3\) is the simple three-vertex cycle, isomorphic to \(K_3\); \(P_n\) is the path with columns indexed \(1,\ldots,n\). Vertices of \(G_n\) are pairs \((i,j)\) with \(i\in\{0,1,2\}\) and \(1\le j\le n\). Two vertices are adjacent when their columns agree and their row indices differ, or their rows agree and their columns are consecutive. A two-dominating set \(S\) satisfies \(|N(v)\cap S|\ge2\) for every \(v\notin S\); vertices belonging to \(S\) are not subject to this condition. Let \(S_j=\{i:(i,j)\in S\}\) and \(s_j=|S_j|\). All sets are counted on the fixed, labeled vertex set, not modulo graph automorphisms. The result concerns every integer \(n\ge7\), with no bound on \(n\).

## Proof

**Column constraints.** If \(S_j=\varnothing\), then \(1<j<n\): an empty end column cannot two-dominate any of its vertices. Every row in an empty interior column must have its horizontal neighbors selected on both sides, so \(S_{j-1}=S_{j+1}=\{0,1,2\}\). If an end column contains just one selected vertex, then its neighboring column must contain both other rows. If a column has two selected vertices, its sole unselected vertex already has two selected neighbors inside that column.

**Empty columns are too costly.** Join empty-column indices that differ by two and consider a maximal component of \(k\ge1\) such indices. It consists of \(k\) empty columns at consecutive distance-two positions, forcing the \(k+1\) neighboring columns between and immediately outside them to be full. Distinct components cannot share a forced full column: otherwise the corresponding empty positions differ by two and would be in the same component. All remaining columns contribute at least zero to the excess \(\sum_{j=1}^n(s_j-1)\). Therefore each empty-column component contributes \(-k+2(k+1)=k+2\ge3\). In particular, if any column is empty, \(|S|\ge n+3\).

**The sharp lower bound and rigidity.** If every column is nonempty, the end-column rule gives \(s_1+s_2\ge3\) and \(s_{n-1}+s_n\ge3\). Since \(n\ge7\), these pairs of columns are disjoint, and all other columns have at least one selected vertex. Hence \(|S|\ge n+2\). In case of equality, each of the two end pairs contributes exactly one unit above one vertex per column, and no other column contributes excess. Thus precisely two columns have size two, at positions \(a\in\{1,2\}\) and \(b\in\{n-1,n\}\), and all others have size one. This also rules out full columns in a minimum set.

**The middle colors.** Fix such \(a,b\). All columns strictly between them are singleton columns, and there are at least three of these because \(n\ge7\). Let \(c_j\) be the selected row of a singleton column. If columns \(j-1,j,j+1\) are all singleton, the two unselected vertices in column \(j\) have one selected neighbor within the triangle, so each requires a selected horizontal neighbor. Consequently \((c_{j-1},c_j,c_{j+1})\) is a permutation of the three rows. This property for every internal middle column implies that the middle labels repeat with period three. There are exactly \(3!=6\) possible middle sequences.

**Two choices at each boundary.** At the first middle singleton column, its next singleton column contains one of the two missing row labels, and the left double column must contain the other missing label. Its second selected row can independently be either of the remaining two labels. Thus the left double column has exactly two possibilities. The right double column likewise has two possibilities. If the left double column lies at position \(2\), the singleton at position \(1\) is forced to be the unique row omitted by the double column, because its two missing rows must both be selected in column \(2\). The analogous condition uniquely determines column \(n\) if the right double column lies at position \(n-1\). There are no additional constraints: a double column already dominates its one unselected vertex vertically; the middle singleton vertices satisfy the rainbow rule or their one boundary condition; and any outside endpoint singleton is covered by both selected vertices of its neighboring double column.

The two boundary choices are independent because the middle singleton interval has length at least three. For each of the \(2\times2=4\) possible pairs of double-column positions, precisely \(6\times2\times2=24\) valid sets arise. They all have \(n+2\) selected vertices, so the lower bound is attained. These profiles exhaust all minimum sets, and their total number is \(4\times24=96\), as claimed. \(\square\)

## Verification

The standalone `verify.py` provides reproducible and logically independent finite checks. Run `python verify.py` with Python 3.9 or later. Its direct neighborhood-enumeration method checks every vertex subset up to the first valid cardinality for \(2\le n\le7\); its eight-mask-column dynamic program computes the exact minimum and multiplicity for \(1\le n\le200\), obtaining \(n+2\) and \(96\) throughout \(7\le n\le200\). A third routine constructs all four boundary families, independently checks all domination conditions, and verifies uniqueness for \(7\le n\le40\) and \(n\in\{100,150,200\}\). These are finite checks of the self-contained proof above, not substitutes for its infinite quantifiers.

## Relationship to prior work

Garzón, Martínez, Moreno, and Puertas (first publicly posted 22 September 2021; published 2022) determined the minimum **size** \(\gamma_2(C_3\square P_n)=n+2\) for \(n\ge4\) using min-plus matrix methods, but did not state the number or complete structural classification of the minimum sets. Martínez, Castaño-Fernández, and Puertas later established additional general cylindrical size bounds and constructions, including longer cycle circumferences divisible by three. Related studies by Garzón et al. of small-path cylinder sizes and by Žerovnik of weak and rainbow two-domination address different numerical quantities. The present theorem adds the exact multiplicity and characterization of **all** optimizers. Literature searches found no directly covering enumeration; absence of a search hit is not a uniqueness proof.

## Limitations

The theorem makes no claim about the enumeration for \(n<7\) or about cylinders with circumference greater than three. It enumerates labeled subsets, not equivalence classes under automorphisms. Literature coverage cannot rule out unindexed or inaccessible equivalent results. The proof does not depend on numerical output or on any conjectural general-cylinder formula.

## References

1. E. M. Garzón, J. A. Martínez, J. J. Moreno, and M. L. Puertas, *On the 2-domination Number of Cylinders with Small Cycles*, Fundamenta Informaticae **185** (2022), 185–199, DOI `10.3233/FI-222107`, first arXiv submission `2109.10549v1` (2021-09-22), open full text `https://arxiv.org/pdf/2109.10549`.
2. J. A. Martínez, A. B. Castaño-Fernández, and M. L. Puertas, *The 2-domination number of cylindrical graphs*, Computational and Applied Mathematics **41** (2022), article 424, DOI `10.1007/s40314-022-02137-1`; lawful open preprint `https://arxiv.org/pdf/2409.16703`.
3. E. M. Garzón, J. A. Martínez, J. J. Moreno, and M. L. Puertas, *HPC acceleration of large (min,+) matrix products to compute domination-type parameters in graphs*, The Journal of Supercomputing **78** (2022), 17826–17843, DOI `10.1007/s11227-022-04574-5`.
4. J. Žerovnik, *On 2-domination and 2-rainbow domination of cylindrical graphs*, Computational and Applied Mathematics (2025), DOI `10.1007/s40314-025-03201-2`.
