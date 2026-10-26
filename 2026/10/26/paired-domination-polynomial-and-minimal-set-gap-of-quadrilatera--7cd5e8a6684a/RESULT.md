# Paired-domination polynomial and minimal-set gap of quadrilateral books

## Finding
For every integer \(r\ge2\), let \(B_r=K_{1,r}\square K_2\). Define \(P_r(z)=\sum_S z^{|S|}\), summed over all paired dominating vertex sets \(S\) of \(B_r\). Then
\[
P_r(z)=z^2(1+z^2)^r+r(r-1)z^4(1+z^2)^{r-2}+(2r+1)z^{2r}.
\]
Every inclusion-minimal paired dominating set belongs to one of four explicitly described types below. The polynomial recording only those inclusion-minimal sets is
\[
M_r(z)=z^2+(2r+1)z^{2r}.
\]
In particular, the smallest and largest sizes of minimal paired dominating sets are \(2\) and \(2r\), respectively, and no minimal such set has any intermediate size. There are precisely \(2r+2\) minimal sets and \(2^r+r(r-1)2^{r-2}+2r+1\) paired dominating sets in total.

## Assumptions and scope
The graph is finite, simple, undirected, and has vertex set
\[
V(B_r)=\{u,v\}\cup\{x_i,y_i:1\le i\le r\},
\]
with precisely the edges \(uv\), \(ux_i\), \(x_iy_i\), and \(y_iv\) for every page index \(i\). Distinct pages have no additional edges. This is the Cartesian product of a star with one edge, and also the graph formed by putting \(r\) internally disjoint three-edge paths in parallel with the direct edge \(uv\).

A subset \(S\subseteq V(B_r)\) is *dominating* if each vertex outside \(S\) has a neighbor in \(S\). It is *paired dominating* if it is dominating and the induced subgraph \(B_r[S]\) has a perfect matching. *Inclusion-minimal* means that no strict subset is paired dominating, not merely that one-vertex deletion fails. The polynomials count vertex subsets, not perfect matchings (a subset is counted only once even if it has multiple perfect matchings). The page and vertex labels are fixed; no quotient by automorphisms is taken.

## Proof
Fix \(r\ge2\). Partition all paired dominating sets by how many of the two hubs \(u,v\) they contain.

**Both hubs chosen.** A page may contribute zero, one, or both of \(x_i,y_i\). A page contributing only \(x_i\) has that vertex adjacent, among selected vertices, only to \(u\); a page contributing only \(y_i\) has it adjacent only to \(v\). Consequently, there can be at most one single-vertex page of each orientation. The total selected cardinality is two plus twice the number of complete pages plus the number of singleton pages. The perfect-matching parity condition excludes exactly one singleton page, while two singleton pages must have opposite orientations and occur on different pages. Conversely, all such configurations are paired dominating: match the hubs to one another if there are no singleton pages; otherwise match \(u\) to its unique \(x\)-singleton and \(v\) to its unique \(y\)-singleton. Match each complete page internally. Since both hubs are present, domination is automatic. The two disjoint subclasses contribute
\[
z^2(1+z^2)^r\quad\text{and}\quad r(r-1)z^4(1+z^2)^{r-2}.
\]

**Exactly one hub chosen.** By symmetry take \(u\in S\), \(v\notin S\). For every page \(i\), \(x_i\) must belong to \(S\): if \(y_i\notin S\), domination of \(y_i\) requires \(x_i\), while if \(y_i\in S\), its only possible selected matching partner is \(x_i\). Every selected \(y_i\) is forced to match \(x_i\). Any remaining \(x_i\) must match the single chosen hub \(u\), so *exactly one* \(y_j\) is omitted. Conversely, these \(r\) selections have perfect matchings and dominate. The case with only \(v\) gives another \(r\) selections. Together they contribute \(2rz^{2r}\).

**Neither hub chosen.** If any page \(i\) is empty, its two page vertices are undominated. If just one of its vertices is selected, that vertex has no selected neighbor and cannot be matched. Therefore every page must be complete. Conversely, the \(r\) internal page edges form a perfect matching and dominate both hubs. This gives exactly one set, contributing \(z^{2r}\).

Summing the disjoint cases proves the formula for \(P_r(z)\). Their sum at \(z=1\) is the asserted total count.

For inclusion-minimality, every paired dominating set containing both hubs contains the paired dominating pair \(\{u,v\}\); hence only that pair is minimal in this case. With exactly one hub, the foregoing classification gives exactly \(r\) sets for each orientation. They are inclusion-minimal: any strict paired dominating subset would still have the same single hub (the hub-free case requires *every* page vertex, while each such set omits one), and the one-hub characterization forces every selected vertex. Finally, the all-page-vertex set is inclusion-minimal because it is the sole paired dominating set with neither hub. Therefore the minimal sets are exactly
\[
\{u,v\},\quad \bigcup_{i=1}^r\{x_i,y_i\},\quad
\{u\}\cup\{x_i:1\le i\le r\}\cup\{y_i:i\ne j\},\quad
\{v\}\cup\{y_i:1\le i\le r\}\cup\{x_i:i\ne j\},
\]
with \(j\in\{1,\ldots,r\}\) in each of the last two types. Thus \(M_r(z)=z^2+(2r+1)z^{2r}\). Every even cardinality \(2,4,\ldots,2r+2\) occurs among general paired dominating sets because the first term in \(P_r\) has a positive coefficient at each such degree. By contrast, for \(r\ge3\), the even sizes \(4,6,\ldots,2r-2\) cannot occur among inclusion-minimal sets, proving the gap. The graph is planar (draw the internally disjoint \(u\)-to-\(v\) paths in nested order), bipartite (alternating positions along each length-three path), and two-vertex-connected: deleting either hub leaves all pages connected through the other, while deleting any page vertex leaves the common hub edge and all remaining vertices connected. 

## Verification
The accompanying standard-library Python program `verify_paired_book.py` independently constructs the adjacency graph, checks the original domination definition, and searches for perfect matchings by bitmask recursion. It exhaustively enumerates all vertex subsets for \(r=2,3,4,5,6,7,8\) (349,504 subsets in total), compares the resulting paired-dominating families—not only their sizes—with the structural description, checks every polynomial coefficient, and tests inclusion-minimality against every proper feasible subset. All checks pass. Its recorded output is in `verification_output.txt`. This is finite corroboration; the universal conclusion follows from the case proof above.

## Relationship to prior work
Alizadeh and Gözüpek (2021, arXiv:2104.02446, later DMTCS 23:3) investigate upper paired domination and its relation to upper ordinary domination, proving structural results for equality cases and giving general bounds. The present statement determines the **full paired-domination subset enumerator** and **all inclusion-minimal sets** of a specific planar bipartite graph family, neither of which follows from the cited general bounds. Jiang and collaborators (2021/2022) study complexity of upper paired domination in bounded-degree bipartite graphs; their published abstract does not state an exact enumeration for this family. Andreev and collaborators (2024) study algorithms for paired domination and a parameterized counting version rather than this closed family-specific polynomial. The definitions agree with these sources. Searches for the graph under the names *quadrilateral book*, *square-page book*, *star prism*, and *parallel length-three paths with a spine* did not identify a stronger covering enumeration. This negative search observation is not a proof of first discovery.

## Limitations
The theorem addresses the specific graph \(K_{1,r}\square K_2\) with \(r\ge2\), not arbitrary graph Cartesian products, books with triangular pages, or all generalized theta graphs. It enumerates sets, not the numbers of perfect matchings inside those sets. Bibliographic searches may miss unindexed equivalent results. The displayed experimental range cannot certify the universal theorem. Independent mathematical validation has not been performed.

## References
1. H. Alizadeh and D. Gözüpek, *Upper paired domination versus upper domination*, 2021 preprint arXiv:2104.02446, DMTCS 23:3 (2021), article 17. https://arxiv.org/abs/2104.02446 ; https://doi.org/10.46298/dmtcs.7331
2. H. Jiang, P. Wu, J. Zhang, and Y. Rao, *Upper paired domination in graphs*, AIMS Mathematics 7 (2022), 1185–1197. https://doi.org/10.3934/math.2022069
3. N. Andreev, I. Bliznets, M. Kundu, S. Saurabh, V. Tripathi, and S. Verma, *Parameterized Complexity of Paired Domination*, IWOCA 2024, pp. 523–536. https://doi.org/10.1007/978-3-031-63021-7_40
