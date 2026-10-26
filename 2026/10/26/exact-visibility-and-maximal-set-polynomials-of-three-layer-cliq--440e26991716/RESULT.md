# Exact visibility and maximal-set polynomials of three-layer clique paths

## Finding

Let \(G_n=K_n\square P_3\) with \(n\ge2\). A set \(S\subseteq V(G_n)\) is a **mutual-visibility set** if every two distinct vertices in \(S\) have a shortest path with no selected internal vertices. Let \(\mathcal V_n(z)\) count all such sets by cardinality, including the empty set, and let \(\mathcal M_n(z)\) count their inclusion-maximal members. Then

\[
\boxed{\mathcal V_n(z)=(1+3z+z^2)^n+2nz^2(1+3z)^{n-1}}
\]
and
\[
\boxed{\mathcal M_n(z)=2n3^{n-1}z^{n+1}+z^n((1+z)^n-1).}
\]

In particular, all possible cardinalities of inclusion-maximal sets are exactly \(n+1,n+2,\ldots,2n\), with
\[
\mu^-(G_n)=n+1,\quad \mu(G_n)=2n,\quad
|\{S:S\text{ is inclusion-maximal}\}|=2n3^{n-1}+2^n-1.
\]
There is a unique maximum set; there are \(2n3^{n-1}+n\) inclusion-maximal sets of the smallest size. The value \(\mu(G_n)=2n\) was already implied by the 2022 Cartesian-product theorem [2]; the classification, both enumerators, and the lower maximality invariant are the proposed contributions here.

## Assumptions and scope

Graphs are finite, undirected, simple and unweighted. For each \(i\in\{1,\ldots,n\}\), write \(A_i,B_i,C_i\) for the three vertices in column \(i\), in the first, middle, and third path layers. Distinct vertices in the same layer are adjacent, and each column contains the edges \(A_iB_i\) and \(B_iC_i\) (but not \(A_iC_i\)). Every selected set falls into exactly one of the following disjoint types:

**Ordinary-column type:** independently for each \(i\), the selected vertices in column \(i\) are one of \(\varnothing,\{A_i\},\{B_i\},\{C_i\},\{A_i,C_i\}\).

**Single-pivot type:** for exactly one index \(i\), select either \(\{A_i,B_i\}\) or \(\{B_i,C_i\}\); in every other column select either nothing or one of the three individual vertices.

Moreover an ordinary-column set is inclusion-maximal exactly when every column contains either \(\{B_i\}\) or \(\{A_i,C_i\}\), and at least one column contains \(\{A_i,C_i\}\). A single-pivot set is inclusion-maximal exactly when each nonpivot column contains one selected vertex.

## Proof

The Cartesian distance formula implies
\[
d(A_i,C_i)=2,\quad d(A_i,B_j)=d(B_i,C_j)=2,\quad d(A_i,C_j)=3\quad (i\ne j).
\]
All other pairs in a common layer are adjacent. The unique shortest path from \(A_i\) to \(C_i\) has internal vertex \(B_i\); hence no mutual-visibility set contains a full column.

For distinct \(i,j\), the only possible internal vertices of a shortest \(A_i,B_j\)-path are \(A_j\) (through \(A_j\)) or \(B_i\) (through \(B_i\)). Thus, when both endpoints are selected, such a path exists avoiding the selected set precisely if \(A_j\notin S\) or \(B_i\notin S\). The analogous criterion for \(B_i,C_j\) is that \(C_i\notin S\) or \(B_j\notin S\). For \(A_i,C_j\) with \(i\ne j\), the only three shortest paths, written with their internal vertices, are
\[
(A_j,B_j),\qquad(B_i,B_j),\qquad(B_i,C_i).
\]
Consequently the pair is visible precisely if at least one of those three internal-vertex pairs is disjoint from \(S\). The reversed \(C_i,A_j\) case follows by symmetry.

Suppose that a selected column contains a pivot \(\{A_i,B_i\}\). Another column \(j\) cannot contain \(\{A_j,B_j\}\), since the selected endpoints \(A_i,B_j\) then have both of their length-two internal vertices selected. It cannot contain \(\{B_j,C_j\}\): the selected pair \(A_i,C_j\) has the internal vertices \(B_i\) on two of its three geodesics, and \(B_j\) on the third. It cannot contain \(\{A_j,C_j\}\): for the pair \(A_i,C_j\), two geodesics contain \(B_i\) and the remaining one contains \(A_j\). A full column was already excluded. The same argument with the path layers reversed applies to \(\{B_i,C_i\}\). Therefore a pivot occurs in precisely one column and all remaining columns contain at most one selected vertex.

Conversely, a single-pivot configuration is mutual-visible. For pairs in different columns with adjacent path layers, use whichever of the two length-two geodesics avoids the selected pivot coordinate; its other possible internal vertex is in a singleton column and therefore unselected when that vertex is not an endpoint. For pairs of vertices in the outermost layers and distinct columns, the middle-layer path \(A_i,B_i,B_j,C_j\) is clear whenever neither endpoint is in the pivot column. If the first endpoint is \(A_i\) in pivot \(\{A_i,B_i\}\) and the second is \(C_j\) in a singleton column, then \(A_i,A_j,B_j,C_j\) is clear because \(A_j,B_j\notin S\); if the second endpoint is \(A_j\) or \(B_j\), one of the two length-two geodesics is clear. The cases with the pivot in \(\{B_i,C_i\}\) follow by reflection. Pairs in the same column or layer are trivial or adjacent. Thus every listed pivot configuration works.

If no column contains a pivot, the exclusion of full columns leaves exactly the five ordinary-column states specified above. Every ordinary-column configuration is mutual-visible: for same-column \(A_i,C_i\), the middle vertex \(B_i\) is absent; for different columns with adjacent layers, one of the two length-two paths avoids all chosen middle vertices (indeed an outer endpoint's own column never contains the middle vertex); and for the outermost layers in distinct columns, \(A_i,B_i,B_j,C_j\) is clear because both corresponding columns containing the outer endpoints have no selected middle vertex. This proves the complete classification.

For maximality, an ordinary-column configuration with any empty column can be extended by a single outer-layer vertex. A column containing a lone \(A_i\) or \(C_i\) can be extended by selecting the opposite outer vertex in the same column, which remains ordinary type. Thus an inclusion-maximal ordinary configuration must choose \(B_i\) or \(\{A_i,C_i\}\) in every column. If every column is \(\{B_i\}\), adding \(A_i\) makes a valid single pivot. If some column is \(\{A_i,C_i\}\), every possible new vertex either makes that column full or would create a pivot in another column, which is forbidden by the classification. Exactly these configurations are maximal.

A single-pivot configuration with an empty nonpivot column is extended by one arbitrary vertex of that column. If all nonpivot columns contain one vertex, adding any remaining vertex would either complete the pivot column or create a second double-occupied column, both forbidden. This proves the claimed maximality classification.

For the enumerators, the five ordinary states contribute the per-column generating function \(1+3z+z^2\), independently in each of \(n\) columns. Choosing the unique pivot column, its orientation, and independently zero or one of three singletons in each other column contributes \(n\cdot2z^2(1+3z)^{n-1}\). For maximal ordinary sets, choosing \(k\ge1\) outer-pair columns and the remaining middle singletons contributes \(\binom nk z^{n+k}\), whose sum is \(z^n((1+z)^n-1)\). All maximal single-pivot sets have size \(n+1\), and their number is \(2n3^{n-1}\). The displayed formulas and their consequences follow for every \(n\ge2\). The unique maximum consists of every \(A_i,C_i\).

## Verification

The companion standalone Python program `verify.py` reconstructs the graph and computes shortest paths by breadth-first search, both in the original graph and after forbidding selected internal vertices. It exhaustively tests every subset for \(n=2,3,4,5\), compares the direct mutual-visibility and maximality predicates with the two structural classifications, and checks every generating-polynomial coefficient. In total it checks \(64+512+4096+32768=37440\) vertex subsets. Its terminal marker is `VERIFY_OK`. The program is a finite independent consistency test; the argument above establishes the statements for arbitrary \(n\).

## Relationship to prior work

Brešar and Yero [1] introduced and investigated the lower mutual-visibility number, including grids and complete-graph Cartesian products; the present invariant \(\mu^-\) is their definition. Cicerone, Di Stefano and Klavžar [2, Theorem 3.4] proved that \(\mu(K_n\square H)=n\mu(H)\) when \(\mu(H)=\mu_i(H)\), which **already implies** the scalar equality \(\mu(K_n\square P_3)=2n\). Their four-cycle criterion [2, Lemma 3.5] applies when both factors are complete graphs, and cannot by itself classify the hybrid product: two distance-three endpoints create additional obstructions. In fact, selecting \(\{A_i,B_i,A_j,C_j\}\) for distinct \(i,j\) meets each Cartesian four-cycle in at most three vertices but fails the visibility of \(A_i,C_j\). Bujtás, Klavžar and Tian [3] formalized visibility polynomials, but do not give the two enumerators for this three-layer clique path. The later Builder–Blocker game work [4] studies different, game-theoretic parameters and its Hamming graphs have two complete factors. The new contribution concerns all feasible sets, all maximal sets and the exact lower maximality distribution in the hybrid Cartesian product.

## Limitations

The theorem concerns ordinary (selected-pair) mutual visibility for \(K_n\square P_3\) only, not the stronger total/outer/dual variants, other path lengths or arbitrary Cartesian factors. The known scalar maximum \(2n\) must not be claimed as new. The original-paper and indexed-result comparisons cannot exclude unindexed, differently phrased or unpublished equivalent findings; independent priority review remains outstanding. Finite verification through \(n=5\) is not a substitute for the general proof.

## References

[1] B. Brešar and I. G. Yero, *Lower (total) mutual visibility in graphs*, arXiv:2307.02951, originally submitted 6 July 2023. https://arxiv.org/html/2307.02951v2

[2] S. Cicerone, G. Di Stefano and S. Klavžar, *On the mutual visibility in Cartesian products and triangle-free graphs*, arXiv:2112.13024, originally submitted 24 December 2021, especially Theorem 3.4 and Lemma 3.5. https://arxiv.org/html/2112.13024v2

[3] Cs. Bujtás, S. Klavžar and J. Tian, *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets*, arXiv:2412.03066, originally submitted 4 December 2024. https://arxiv.org/abs/2412.03066

[4] V. Iršič Chenoweth et al., *Builder-Blocker Mutual-Visibility Game*, Bulletin of the Malaysian Mathematical Sciences Society 49 (2026), article 89. https://doi.org/10.1007/s40840-026-02083-9
