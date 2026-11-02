# Outer-independent Roman rigidity and exact minimum-labeling multiplicities on clique chains and cylinders

## Finding

Let \(m\ge3\). On Cartesian products of the clique \(K_m\) with a path \(P_n\) or cycle \(C_n\), every outer-independent Roman dominating function is also an outer-independent total Roman dominating function. In particular the two weight enumerators, and hence their minima, coincide.

For every \(n\ge1\), the common minimum on the clique-path graph is
\[
\gamma_{oiR}(K_m\square P_n)=\gamma_{oitR}(K_m\square P_n)=mn-\left\lfloor\frac{2n}{3}\right\rfloor.
\]
For every \(n\ge4\), the common minimum on the clique-cycle graph is
\[
\gamma_{oiR}(K_m\square C_n)=\gamma_{oitR}(K_m\square C_n)=mn-\left\lfloor\frac{2n}{3}\right\rfloor,
\]
and the common minimum on \(K_m\square C_3\) is \(3m-1\).

The main extremal-structure refinement counts **every minimum-weight function**, with all graph vertices distinguishable and label values \(0,1,2\) fixed. For all \(q\ge1\), the number of minimum functions on \(K_m\square P_{3q}\) is
\[
M_P(m,3q)=m(m-1)^{2q-1}.
\]
For all \(q\ge2\), the number on \(K_m\square C_{3q}\) is
\[
M_C(m,3q)=3(m-1)^q\big((m-1)^q+(-1)^q(m-1)\big).
\]
In both families every minimum function at these lengths has exactly one zero in each column, exactly \(q\) vertices labeled \(2\), and a forced tiling into three-column blocks. In each block the sole vertex labeled \(2\) lies in the middle column and shares its row with the zeros at the two ends. Middle-column zeros are chosen in different rows; adjacent blocks have different defender rows.

## Assumptions and scope

Graphs are finite, simple, and undirected. The product \(K_m\square H\) has vertices \((a,j)\), where \(a\in\{0,\ldots,m-1\}\) is the clique row and \(j\) is the path or cyclic column. Two vertices are adjacent if they share a column and have different rows, or share a row and have adjacent second coordinates. The path has \(n\ge1\) vertices; the cycle is simple and has \(n\ge3\) vertices.

An outer-independent Roman dominating function \(f:V\to\{0,1,2\}\) has an independent zero set and gives every zero-labeled vertex a neighbor labeled \(2\). An outer-independent total Roman dominating function additionally requires the subgraph induced by all positively labeled vertices to have no isolated vertices. The weight is \(\sum_v f(v)\). Distinct labelings, rather than automorphism orbits, are counted.

## Proof

**1. Equivalence of the two requirements.** A column is a clique, so its zero vertices, if any, consist of exactly one vertex. Consequently each column has at least \(m-1\ge2\) positively labeled vertices, all pairwise adjacent. Every positive vertex therefore has a positive neighbor in its own column. Thus outer-independent Roman and outer-independent total Roman feasible functions coincide, for these graph families, at every weight.

**2. Universal lower bound.** Write \(z\) for the total number of zeros and \(t\) for the number of twos. There is at most one zero per column, so \(z\le n\). Each vertex labeled \(2\) can defend at most three zero vertices: at most one in its own clique, and at most one in each of its two adjacent columns, where only its same-row neighbor can be defended. Counting the covered zeros gives \(z\le3t\). Since every other vertex has label \(1\), the weight is \(mn-z+t\). In particular
\[
z-t\le z-\left\lceil\frac z3\right\rceil
=\left\lfloor\frac{2z}{3}\right\rfloor
\le\left\lfloor\frac{2n}{3}\right\rfloor.
\]
This proves the asserted common lower bound in every case.

**3. General constructions attaining the bound.** We describe every column's unique zero row and the selected defender centers. Put \(k=\lceil n/3\rceil\). For a path with \(n\ge2\), choose center columns \(1,4,7,\ldots\) below \(n\), adding column \(n-1\) when \(n\equiv1\pmod3\). For \(n=1\), choose center \(0\). Consecutive centers are two or three columns apart, and each path endpoint lies within one step of a center. Assign consecutive centers alternating defender rows \(0,1\).

For a cycle of length \(n\ge4\), choose \(k\ge2\) center columns separated around the circle by gaps of length two or three. Such gaps exist because \(2k\le n\le3k\): choose \(3k-n\) gaps of two and \(n-2k\) gaps of three. Assign defender rows \(A_1,\ldots,A_k\) so adjacent centers, including the cyclic last-first pair, have distinct rows. Two rows suffice for even \(k\); for odd \(k\), use three rows.

Between consecutive centers \(c,c'\), place the zero of the first intervening column in row \(A_c\). If the gap is three, place the zero of the second intervening column in row \(A_{c'}\). At path boundaries, give every column before the first or after the last center the nearest center's defender row. At center \(c\), put a label \(2\) in row \(A_c\), and place its column zero in a row \(B_c\) unequal to \(A_c\) and to the zero rows in its at most two neighboring columns. The latter rows include \(A_c\) on the right and either \(A_c\) or the preceding center's row on the left, so at most two row values are forbidden. Since \(m\ge3\), \(B_c\) always exists. Put label \(1\) at every remaining vertex.

The resulting one-zero-per-column zero set is independent: zero rows differ across each pair of consecutive columns by the chosen row restrictions. Every zero is adjacent to a labeled-2 vertex either in its own center column or at a neighboring center in the same row. Thus the labeling is feasible, has \(z=n\) and \(t=k\), and has weight \(mn-n+\lceil n/3\rceil=mn-\lfloor2n/3\rfloor\).

For the exceptional three-cycle, this construction cannot attain a saving of two. Attaining \(3m-2\) would force three zeros and one two, with that two defending a zero in each column. Both zeros in its two neighboring columns would then occupy its row, but those columns are adjacent in \(C_3\), contradicting zero independence. A labeling of weight \(3m-1\) exists: set \(f(0,0)=0\), \(f(1,1)=0\), \(f(1,0)=2\), and all remaining values to \(1\). Both zeros are defended and nonadjacent.

**4. Forced three-column rigidity.** Let \(n=3q\), and suppose an optimum has weight \(mn-2q\). With \(z\le3q\) and \(z\le3t\), the identity \(z-t=2q\) yields \(t\ge q\) and \(t\le q\). Hence \(z=3q\) and \(t=q\). Every column has exactly one zero and every two-labeled vertex must defend exactly three distinct zeros. Therefore its own column and both neighboring columns have zeros, and both neighbors' zeros have the same row as the two-labeled vertex. The defended three-column neighborhoods are disjoint and partition all columns.

On a path, the only partition of its consecutive columns into such centered three-intervals has center columns \(1,4,\ldots,3q-2\). On a cycle with \(q\ge2\), centers have cyclic spacing exactly three, giving exactly three disjoint choices of cyclic phase. Write \(A_j\) for the two-labeled vertex's row in block \(j\) and \(B_j\) for the center zero row. Then \(B_j\ne A_j\). Across successive blocks, their boundary zeros are adjacent and occupy rows \(A_j\) and \(A_{j+1}\), so \(A_j\ne A_{j+1}\); this condition is cyclic for a cycle. Conversely, these choices satisfy all local conditions and give optimum functions. Thus they characterize every minimum labeling.

**5. Exact multiplicities.** The defender rows on a path of \(q\) blocks can be assigned in \(m(m-1)^{q-1}\) ways, and the middle zeros in \((m-1)^q\) independent ways. The product is \(m(m-1)^{2q-1}\). In the cycle case the defender rows are a proper coloring of the cycle of \(q\) blocks. The number is \((m-1)^q+(-1)^q(m-1)\); this expression also correctly counts the two-center case as a pair of distinct defender rows. Multiply by \((m-1)^q\) choices of \(B_j\) and by three cyclic phases to get the stated formula. No two choices produce the same labeled function, because center positions and defender rows can be recovered from the values \(2\).

## Verification

The standalone graph-checking program in `CHECKER.py` is standard-library Python 3. It builds the actual graph, validates every supplied optimum construction against all graph edges and zero defenders, and compares small instances to unrestricted column-state dynamic programming. The program also directly enumerates all three-valued labelings for four small graphs. Execute `python3 CHECKER.py`. The final reproducible output contains `VERIFY_OK`: 936 separately graph-checked constructed witnesses, 20 exact dynamic-programming minima/counts, and four direct all-label graph enumerations. Its cycle count checks include \(m=3,n=6\) and \(m=3,n=9\), and its path count checks include \(m=3,n=3,6,9\). Computation supports but is not substituted for the infinite proof.

## Relationship to prior work

Cabrera Martínez, Kuziak, and Yero (arXiv:2112.05476v1, 2021-12-10) introduced and bounded the total variant and explicitly studied Cartesian products of complete factors. Their complete-factor result includes the cases \(P_2=K_2\) and \(C_3=K_3\). Gao, Liu, Guo, and Yang (Mathematics 2022, DOI 10.3390/math10183361) established outer-independent Roman minima for certain toroidal grids including \(C_3\square C_n\); these include the \(m=3\) cyclic scalar cases. Gao, Qiu, Du, Zhao, and Yang (arXiv:2410.06486v1, 2024-10-09) established the outer-independent Roman minimum of \(P_n\square C_3\), which coincides with the \(m=3\) path scalar formula above.

Accordingly those scalar special cases are **not claimed as new**. The distinguishing contribution is the exact classification and multiplicity of all minimum-weight labelings for every divisible-by-three length and every clique order \(m\ge3\), simultaneously for the ordinary and total outer-independent Roman variants, along with the explicit full-family comparison. None of the inspected prior statements furnishes the extremal multiplicities or forced three-column coloring structure; absence of a match from searches is not a proof of worldwide publication priority.

## Limitations

The multiplicity formulas require \(n=3q\), with \(q\ge1\) for paths and \(q\ge2\) for cycles; the numbers of optimal functions for other length residues are not determined here. The path or cycle and clique-factor hypotheses are essential to the presented proof. The three-cycle scalar case is exceptional. The 2022 torus article was accessible through publication information and relevant indexed results rather than a reliably fetchable complete text; its full uninspected portions and unindexed literature remain a residual priority uncertainty. Independent mathematical assessment has not been performed.

## References

1. A. Cabrera Martínez, D. Kuziak, I. G. Yero, *Relating the outer-independent total Roman domination number with some classical parameters of graphs*, arXiv:2112.05476v1 (first posted 2021-12-10), https://arxiv.org/abs/2112.05476 .
2. H. Gao, X. Liu, Y. Guo, Y. Yang, *On Two Outer Independent Roman Domination Related Parameters in Torus Graphs*, Mathematics **10** (2022), 3361, https://doi.org/10.3390/math10183361 (published 2022-09-16).
3. H. Gao, D. Qiu, S. Du, Y. Zhao, Y. Yang, *Outer Independent Roman Domination Number of Cartesian Product of Paths and Cycles*, arXiv:2410.06486v1 (first posted 2024-10-09), https://arxiv.org/abs/2410.06486 .
