# Exact two-or-three isometric-path covers of three-arm theta graphs

## Finding
Let \(\Theta(a,b,c)\) be the simple graph consisting of three internally vertex-disjoint paths of lengths \(2\le a\le b\le c\), joining the same two hubs. Let \(\operatorname{ip}(G)\) be the minimum number of shortest paths whose vertex sets cover \(V(G)\). Then
\[
\operatorname{ip}(\Theta(a,b,c))=
\begin{cases}
2,&(a,b)=(2,2)\text{ or }(2,3),\\
2,&(a,b)=(2,4)\text{ and }c\text{ is even},\\
2,&(a,b)=(3,3)\text{ and }c\text{ is odd},\\
3,&\text{otherwise}.
\end{cases}
\]
The numerical classification includes all boundary cases, with no restriction on the third length beyond \(c\ge b\).

## Assumptions and scope
All graphs are finite, simple, unweighted and undirected. A path is *isometric* precisely if its number of edges equals the graph distance between its endpoints. The covering paths may overlap; vertices (not edges) are required to be covered. Every theta arm has at least two edges, so the graph has \(a+b+c-1\) vertices and two hubs of degree three. A path of length zero is allowed, but never improves the stated minimum.

Write the hubs as \(u,v\); write arm \(X\) of length \(\ell\) as \(u=X_0,X_1,\ldots,X_{\ell}=v\). Subscripts and comparisons in the proof refer to the chosen orientation.

## Proof
**One path is impossible.** Every pair of vertices lies on a cycle formed by two of the arms. The length of that cycle is at most \(b+c\), so the shorter arc gives
\(\operatorname{diam}(G)\le\lfloor(b+c)/2\rfloor\).
But the number of vertices is \(a+b+c-1>1+\lfloor(b+c)/2\rfloor\). Hence no geodesic contains all vertices.

**Three paths always suffice.** Take the whole shortest arm \(A\), an isometric \(u\)-to-\(v\) path. Set \(x=\lfloor b/2\rfloor\), \(y=\lfloor c/2\rfloor\). Take the path from \(B_x\) to \(C_y\) through \(u\), and the path from \(B_{x+1}\) to \(C_{y+1}\) through \(v\). Every endpoint is on the appropriate nearest-hub half of its arm, so neither path is longer than any alternative routing through the other hub (including a route using arm \(A\)). Both are geodesics. These three paths cover all vertices.

**Structure of a hypothetical two-path cover.** Suppose geodesics \(P,Q\) cover the graph. Each has at most \(1+\lfloor(b+c)/2\rfloor\) vertices, so
\[
|P\cap Q|\le 2+2\lfloor(b+c)/2\rfloor-(a+b+c-1)\le3-a\le1.
\]
In particular, \(a\le3\) and the paths share at most one vertex.

If a geodesic visits both hubs, its hub-to-hub section is an entire shortest arm. Suppose it also has endpoints internal to *both* other arms, of lengths \(p,q\), at positions \(P_i\) and \(Q_j\) from \(u\), with the path proceeding through \(u\), then the middle arm of length \(s\), then \(v\). Comparing the path to a route staying on the \(p\)-arm near \(v\), and to one staying on the \(q\)-arm near \(u\), respectively yields \(2i\le p-s\) and \(2j\ge q+s\). As \(s\ge2\), necessarily \(i\le p-2\) and \(j\ge2\). Hence **both** uncovered tails, \(P_{i+1},\ldots,P_{p-1}\) and \(Q_1,\ldots,Q_{j-1}\), are nonempty. They lie in distinct components after removing the geodesic: the first tail attaches at \(v\), the second at \(u\). Any single path covering vertices of both tails must meet the geodesic in at least two distinct vertices, contradicting the overlap bound. Thus a geodesic visiting both hubs can extend into at most one other arm.

If it does not extend at all, the other geodesic must cover all internal vertices of the two remaining arms and can meet the first path at most once. It must run through one hub with endpoints the vertices adjacent to the opposite hub. Its length is the sum of the two arm lengths minus two; going through the opposite hub has length two. Therefore both remaining arms have length two, and \((a,b)=(2,2)\).

If a hub-to-hub geodesic uses a shortest arm of length \(s\) and extends along a different arm of length \(t\), write its endpoint on that arm as \(T_{h+1}\) (with its extension from \(v\) toward \(u\)). The other geodesic must cover the remaining internal vertices \(T_1,\ldots,T_h\), plus all internal vertices of the third arm of length \(q\). Since at most one vertex is shared, this other geodesic runs through \(u\), from \(T_h\) to the vertex adjacent to \(v\) on the \(q\)-arm. Shortest-path comparisons give
\[
 s+(t-h-1)\le h+1\quad\Longrightarrow\quad 2h\ge s+t-2,
\]
\[
 h+(q-1)\le(t-h)+1\quad\Longrightarrow\quad2h\le t-q+2.
\]
Consequently \(s+q\le4\). Since \(s,q\ge a\ge2\), both have length two and again \((a,b)=(2,2)\). The case of extension at \(u\) is symmetric. Hence, provided \((a,b)\ne(2,2)\), neither covering path visits both hubs.

One path now visits \(u\) but not \(v\), and the other visits \(v\) but not \(u\). If either path uses only one arm, the other must cover the full interiors of the other two arms by running through its own hub. A comparison with the two-edge route through the opposite hub again forces both those arms to have length two. Thus outside \((a,b)=(2,2)\), each path runs through its own hub and has its endpoints in two distinct arms.

The two arm supports must share exactly one arm \(r\): let \(p\) be used exclusively by the \(u\)-path and \(q\) exclusively by the \(v\)-path. The first path runs from the vertex next to \(v\) on arm \(p\), through \(u\), to \(R_h\). The second runs from the vertex next to \(u\) on arm \(q\), through \(v\), to \(R_j\). Coverage of the shared arm and the at-most-one-overlap bound imply \(j=h\) or \(j=h+1\). Comparing each geodesic to its opposite-hub alternative gives
\[
2h\le r-p+2,\qquad 2j\ge q+r-2.
\]
If \(j=h\), these inequalities imply \(p+q\le4\), contradicting \((a,b)\ne(2,2)\). Thus \(j=h+1\) and
\[
q+r-4\le2h\le r-p+2,
\]
which forces \(p+q\le6\). Since the two smallest arm lengths are \(a,b\), we have \(a+b\le6\). The only possible smallest-length pairs other than \((2,2)\) are \((2,3)\), \((2,4)\), and \((3,3)\). For \((2,4)\), necessarily the exclusive arms have lengths \(2,4\) and the shared arm length is \(c\); the bounds collapse to \(2h=c\), requiring \(c\) even. For \((3,3)\), the exclusive arms both have length three and the shared arm length \(c\); the bounds collapse to \(2h=c-1\), requiring \(c\) odd. This proves the necessary conditions.

**Sharp two-path constructions.** In every case listed as two, select \(h\) such that
\[
\left\lceil\frac{b+c-4}{2}\right\rceil\le h\le\left\lfloor\frac{c-a+2}{2}\right\rfloor.
\]
Such an integer exists for \((a,b)=(2,2),(2,3)\), and respectively for the asserted parity of \(c\) for \((2,4),(3,3)\). Take the path \(A_{a-1},\ldots,A_0=u,C_1,\ldots,C_h\) and the path \(B_1,\ldots,B_b=v,C_{c-1},\ldots,C_{h+1}\), omitting empty segments. They are disjoint and cover all vertices. The two inequalities above guarantee shortestness versus opposite-hub routes, while \(b\le a+2\) in all four cases rules out a still shorter detour via the unused short arm. Thus both are geodesics. Combining the lower bounds and constructions completes the proof.

## Verification
The standalone `verify.py` constructs the original labelled theta graphs, computes every pairwise graph distance by breadth-first search, enumerates all geodesic vertex sets, and searches for a pair covering all vertices. It compares the result against the claimed closed classification for every unordered length triple with \(2\le a\le b\le c\le14\) (455 triples) and for 80 wider deterministically sampled triples with arm lengths up to 56. Both tests pass. Separate direct checks of the explicit two- and three-path constructions were performed for all 1,140 unordered triples through length 19. These are finite checks, not the proof of the general theorem.

## Relationship to prior work
Chakraborty, Defrain, Foucaud, Mari and Tale introduced new complexity results for *Isometric Path Cover* in their October 15, 2026 preprint, but do not give this all-length theta classification. The full open-access 2025 version of Chakraborty, Foucaud and Hakanen establishes an edge-geodesic-cover bound and a vertex-isometric-path-partition upper bound of \(2c(G)+\ell(G)\), equal to four for these theta graphs. Neither bounds nor algorithms determine the exact two-versus-three cover minimum. Manuel and Klavžar treat equal-arm theta graphs in the study of *general position* sets, a distinct invariant; their inequalities involving isometric covers do not determine the present result. Dumas and collaborators (2024) prove that a graph covered by a fixed number of shortest paths has bounded pathwidth; the necessary pathwidth bound cannot decide the exact theta threshold. The isometric-path covering/partition literature also contains grid, network, chordal and torus results, which neither state nor imply this classification. No historical priority beyond the inspected literature is asserted.

## Limitations
The result is restricted to exactly three simple internally disjoint arms, each of length at least two. It does not classify all optimal covering pairs, edge-geodesic covers, path partitions, weighted shortest paths or generalized theta graphs with four or more arms. The originality comparison is provisional against unindexed sources and the complete text of Manuel (2021), which was not accessible during this review; no independent mathematical audit has been performed.

## References
1. D. Chakraborty, O. Defrain, F. Foucaud, M. Mari and P. Tale, *Parameterized Complexity of Isometric Path Cover: Treewidth and Diameter* (first public version October 15, 2026), https://arxiv.org/abs/2610.22010 .
2. D. Chakraborty, F. Foucaud and J. Hakanen, *Distance-based graph covering problems for graphs of given cyclomatic number* (FCT 2023); expanded journal version *Distance-based (and path-based) covering problems for graphs of given cyclomatic number*, Discrete Mathematics (2025), open-access full text https://arxiv.org/html/2509.00383v1 and https://doi.org/10.1016/j.disc.2025.114595 .
3. P. Manuel and S. Klavžar, *Graph theory general position problem*, https://users.fmf.uni-lj.si/klavzar/preprints/Graph%20Theory%20General%20Position%20Problem%203%20April%202018.pdf .
4. P. Manuel, *On the Isometric Path Partition Problem*, Discussiones Mathematicae Graph Theory 41 (2021), 1077–1089, https://geodesic.mathdoc.fr/item/DMGT_2021_41_4_a13/ .
5. D. Chakraborty, A. Dailly, S. Das, F. Foucaud, H. Gahlawat and S. K. Ghosh, *Complexity and Algorithms for Isometric Path Cover on Chordal Graphs and Beyond*, ISAAC 2022, https://doi.org/10.4230/LIPIcs.ISAAC.2022.12 .
6. M. Dumas, F. Foucaud, A. Perez and I. Todinca, *On graphs coverable by k shortest paths*, SIAM Journal on Discrete Mathematics 38 (2024), 1840–1862, https://arxiv.org/abs/2206.15088 .
