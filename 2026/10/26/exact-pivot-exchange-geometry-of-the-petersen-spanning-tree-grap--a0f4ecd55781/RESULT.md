# Exact pivot-exchange geometry of the Petersen spanning-tree graph

## Finding

Let \(P=KG(5,2)\) be the Petersen graph. Its vertices are the ten two-element subsets of \(\{0,1,2,3,4\}\), adjacent exactly when disjoint. Let \(\mathscr T(P)\) be its spanning trees. Join \(T,U\in\mathscr T(P)\) when \(U=T-e+f\), where \(e\in T\), \(f\in E(P)\setminus T\), the edges \(e,f\) share a graph vertex, and \(U\) is again a tree. Denote this *pivot-exchange graph* by \(\mathcal P(P)\) and its shortest-path metric by \(d_{\rm piv}\).

The graph \(\mathcal P(P)\) is connected and 12-regular on 2,000 vertices. Its diameter is exactly \(8\); of its spanning trees, 1,040 have eccentricity \(7\), and 960 have eccentricity \(8\). Its exact unordered-pair distance enumerator is

\[
\sum_{\{T,U\}\subseteq\mathscr T(P),\;T\ne U}z^{d_{\rm piv}(T,U)}
=12000z+72000z^2+266940z^3+588060z^4+678350z^5
+327080z^6+52500z^7+2070z^8.
\]

Write \(b(T,U)=9-|E(T)\cap E(U)|\), the unrestricted spanning-tree exchange distance. Then
\[0\le d_{\rm piv}(T,U)-b(T,U)\le4.\]
The number of unordered pairs at excess \(0,1,2,3,4\), respectively, is
\[565010,\ 1045740,\ 363290,\ 24810,\ 150.\]
All 150 excess-four pairs are at distance \(8\). They form exactly two orbits of sizes \(30\) and \(120\) under \(\operatorname{Aut}(P)\cong S_5\), and their endpoints comprise a single orbit of 60 spanning trees. In contrast, the full tree set has 21 such symmetry orbits.

## Assumptions and scope

All graphs are finite, simple, and unweighted. Trees are distinct *edge subsets of the fixed labeled Petersen graph*, not isomorphism classes; shortest paths may use any intermediate spanning trees. Every pivot must replace exactly one edge with another edge incident at the same vertex, while preserving the spanning-tree property. Distances and orbit multiplicities count *unordered distinct* tree pairs unless otherwise stated. The graph, move set, and verification ranges are fully specified here, without embedding, drawings, or external data conventions.

## Proof

**Tree count.** The Petersen graph is strongly regular with parameters \((10,3,0,1)\). If \(A\) is its adjacency matrix and \(J\) the all-one matrix, then \(A^2=2I-A+J\). The constant vector has eigenvalue 3; on its orthogonal complement the eigenvalues are 1 and \(-2\), with multiplicities 5 and 4 by trace and dimension. Thus its Laplacian eigenvalues are \(0\), \(2\) (five times), and \(5\) (four times). By the matrix-tree theorem,
\[|\mathscr T(P)|=2^5 5^4/10=2000.\]
An independent exact 9-by-9 Laplacian cofactor and exhaustive tree enumeration verify the same count in the supplied program.

**Pivot neighborhoods.** Let \(T\) be any spanning tree in a connected simple graph, and \(f=xy\notin T\). There is a unique \(x\)-to-\(y\) path in \(T\), with at least two edges. For \(T-e+f\) to be a tree, \(e\) must lie on this path, since \(T+f\) has this path plus \(f\) as its unique cycle. If \(e\) is also incident to \(f\), then \(e\) must be one of the path's first or last edges; conversely each of those two removals gives a tree. Consequently a tree in \(P\) has exactly two pivot neighbors per omitted edge: \(2(15-9)=12\). No two such neighbors coincide because their edge symmetric differences with \(T\) identify the removed and inserted edges.

**Exact metric certificate.** The accompanying standalone program enumerates the \(\binom{15}{9}=5005\) nine-edge candidates and checks acyclicity and connectivity by disjoint-set union. It constructs every pivot in two independent ways: (i) all incident one-edge exchanges retaining a tree, and (ii) for each missing edge, deleting the first or last edge of its fundamental tree path. The 2,000 adjacency lists agree exactly; each has 12 distinct entries and all arcs are symmetric. Breadth-first search from all 2,000 sources yields distances to all 2,000 destinations. Counting each pair once proves the eight displayed distance coefficients, eccentricity counts, connectivity, diameter, and the complete exchange-excess profile. The code tests these as exact integer assertions and checks that the distance histogram sums to \(\binom{2000}{2}=1999000\).

**Symmetry certificate.** The natural permutations of the five underlying symbols yield 120 edge-preserving permutations of \(P\). These constitute its full automorphism group: the five maximal four-vertex independent sets of \(KG(5,2)\) are precisely the stars consisting of two-subsets containing a fixed symbol (a pairwise-intersecting family of four edges in \(K_5\) must be a star). Every graph automorphism permutes these five stars, faithfully. The program enumerates all 120 actions on trees, obtains 21 tree orbits, and independently recomputes the distance and excess tables by orbit-weighted breadth-first search using its second adjacency construction. Finally, it constructs the group orbits of all 150 excess-four unordered pairs. Their sizes are exactly 30 and 120, and their endpoints form one orbit of size 60. This proves the remaining assertions.

## Verification

Run `python3 verify_petersen_pivots.py` from the directory containing this document and the supplied program. No third-party libraries or input data are used. The program terminates with `VERIFY_OK` only after verifying two independent pivot-neighbor constructions, an exact Laplacian cofactor, every all-pairs graph distance, a second symmetry-reduced distance census, and the extreme-pair symmetry orbits. Tree enumeration is exhaustive over all 5,005 eligible edge subsets; the 2,000 trees are also independently certified by the matrix-tree theorem. Reproducibility is finite and exact, not statistical.

## Relationship to prior work

The count of 2,000 Petersen spanning trees and the general matrix-tree theorem are classical and are not claimed as new. Knuth's *The Art of Computer Programming*, Volume 4A (publicly published 12 January 2011), frames local-change spanning-tree generation; subsequent pivot-Gray-code work explicitly traces a related problem to this book. Cameron, Grubb and Sawada (first public preprint 20 August 2021) study pivot Gray codes for fan graphs, while Behrooznia and Mütze (2024 preprint; published 2025) establish pivot-exchange listings for outerplane triangulations. The Petersen graph is not in those families, and an existence theorem for a Hamilton path would not imply the exact shortest-path distribution. Unrestricted basis exchanges have distance \(b(T,U)\), but permit nonincident replacements and give only the lower bound used above. The present finite metric and symmetry census was not found in the inspected works or targeted research-record and literature searches.

## Limitations

This is a complete exact classification for one canonical ten-vertex graph, not a bound for all cubic graphs or a claim of a pivot Gray code/Hamilton cycle. The degree-12 argument is general and is not itself claimed as a new theorem. The finite computation is verified via two exact constructions and symmetry, but is not an independent external audit. Earlier unpublished or unindexed Petersen-specific pivot-distance computations cannot be ruled out merely by negative searches.

## References

1. D. E. Knuth, *The Art of Computer Programming*, Volume 4A, Addison-Wesley, 2011, Section 7.2.1.6 (publisher publication date: 12 January 2011). https://www.pearson.com/en-us/subject-catalog/p/art-of-computer-programming-the-combinatorial-algorithms-volume-4a-part-1/P200000009030?view=educator
2. B. Cameron, A. Grubb, and J. Sawada, *A Pivot Gray Code Listing for the Spanning Trees of the Fan Graph*, arXiv:2108.09363, first posted 20 August 2021. https://ar5iv.labs.arxiv.org/html/2108.09363
3. N. Behrooznia and T. Mütze, *Listing Spanning Trees of Outerplanar Graphs by Pivot-Exchanges*, STACS 2025, doi:10.4230/LIPIcs.STACS.2025.16, preprint arXiv:2409.15793. https://drops.dagstuhl.de/storage/00lipics/lipics-vol327-stacs2025/html/LIPIcs.STACS.2025.16/LIPIcs.STACS.2025.16.html
4. C. Tuffley, *Counting the Spanning Trees of the 3-Cube Using Edge Slides*, arXiv:1109.6393, first posted 29 September 2011. This studies a distinct cubical slide operation and is background only.
