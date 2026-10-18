# Facet rigidity under one-edge subdivision of a complete-graph transportation ball

## Finding
Let \(n\ge5\) be an integer. Obtain \(G_n\) from the complete graph \(K_n\) by replacing one edge \(ab\) by the path \(a-z-b\), and equip its \(n+1\) vertices with shortest-path distances from unit edges. Let \(B_n\) be the closed unit ball of its real Lipschitz-free space, identified with the convex hull of all oriented unit-edge molecules \(e_u-e_v\) in the zero-sum hyperplane. Then \(B_n\) is \(n\)-dimensional, has precisely
\[
F_n=2^{n+1}-10
\]
facets, and these form exactly \(3(n-2)\) orbits under the graph automorphism group together with central inversion. The number of vertices on any facet is at most
\[
M_n=\left\lfloor\frac{n^2}{4}\right\rfloor+2,
\]
and this bound is attained. For \(n=5\) exactly \(18\) facets attain it; for \(m=n-2\ge4\), their number is
\[
T_m=\begin{cases}
4\binom{m}{m/2-1},&m\text{ even},\\
4\left[\binom{m}{(m-1)/2}+\binom{m}{(m-3)/2}\right],&m\text{ odd}.
\end{cases}
\]
A complete orbit-size classification is given below. This statement concerns facets of \(B_n\), not all of its faces.

## Assumptions and scope
Put \(m=n-2\ge3\). Label the \(m\) original vertices other than \(a,b\) by \(U=\{u_1,\ldots,u_m\}\). The graph edges are all pairs of \(U\), all pairs joining \(a\) or \(b\) to \(U\), and \(az,bz\); there is no edge \(ab\) and no edge \(zu_i\). All original graph edges have length one, with the induced path metric. The space is real. A potential is a function \(f:V(G_n)\to\mathbb R\) modulo additive constants, subject to \(|f(v)-f(w)|\le1\) for every graph edge.

For an integer-valued potential \(f\), call an edge tight when its endpoint values differ by exactly one. Its tight-edge graph is \(T_f\). Because the graph is connected, a potential determines a facet of \(B_n\) exactly when \(T_f\) is connected and spanning: an edge equality gives an oriented vertex of \(B_n\) on the supporting facet, and their differences span the \(n\)-dimensional zero-sum space exactly when those tight edges connect every vertex. Every extreme potential is integer-valued modulo constants: the connected tight edges propagate integral differences from a chosen root. Therefore all facets are captured by this criterion, with no assumption of integral potentials needed at the outset.

## Proof
**Classification.** Since \(U\) induces a clique, an integer-valued one-Lipschitz function on \(U\), shifted to minimum zero, is either constant zero or takes both values zero and one. In the latter case, let \(L\) and \(H\) be the zero and one subsets, with \(|L|=r\ge1\), \(|H|=k\ge1\), and \(r+k=m\). Every edge between \(L\) and \(H\) is tight, so the tight subgraph already connects all of \(U\). Both \(a\) and \(b\) are adjacent to every member of \(U\), forcing \(f(a),f(b)\in\{0,1\}\), and each has tight incident edges to \(U\). The new vertex \(z\) has exactly two neighbors \(a,b\). It must be connected by at least one tight edge. If \(f(a)=f(b)=0\), this leaves \(f(z)\in\{-1,1\}\); if \(f(a)=f(b)=1\), it leaves \(f(z)\in\{0,2\}\); if \(f(a)\ne f(b)\), it leaves \(f(z)\in\{0,1\}\). Thus for each nonempty proper subset \(L\subset U\) there are exactly eight facet potentials. Each is feasible, its tight edges span all vertices, and no other potential is possible.

If \(f\) is constant zero on \(U\), connectivity of \(T_f\) requires \(a\) or \(b\) to have value \(\pm1\), and requires the other endpoint also to have value \(\pm1\), since an endpoint with value zero would have no tight edge to \(U\) (its sole other possible tight neighbor is \(z\), which would leave disconnected components). More directly, any tight path from a zero-valued endpoint to \(U\) would have to pass through \(z\) and the opposite endpoint, and the two-edge path through \(z\) cannot be simultaneously tight if one endpoint equals zero and the opposite endpoint is \(\pm1\), because the permitted common value range of \(z\) is \(\{0,1\}\) or \(\{-1,0\}\). So both \(a,b\in\{-1,1\}\). Their possibilities for \(z\), requiring at least one tight edge, are exactly
\[
(-1,-1,-2),\ (-1,-1,0),\ (1,1,0),\ (1,1,2),\ (-1,1,0),\ (1,-1,0),
\]
where each triple lists \((f(a),f(b),f(z))\). All six give connected spanning tight-edge graphs. Hence the total number of facets is \(6+8(2^m-2)=2^{m+3}-10\), as asserted.

**Symmetry orbits.** The vertex \(z\) is the unique vertex of degree two because \(m\ge3\). Its two neighbors \(a,b\) are therefore setwise distinguished, while the clique \(U\) is permuted arbitrarily. Thus \(\operatorname{Aut}(G_n)\cong S_m\times C_2\). We additionally allow the antipodal map \(f\mapsto-f\) on potentials, normalizing the minimum of \(f|_U\) to zero after every action. The six constant-\(U\) potentials form three size-two orbits: outward same-sign endpoints, inward same-sign endpoints, and opposite-sign endpoints.

For the nonconstant case, classify the pair \(\{r,k\}\) with \(r+k=m\), \(r,k\ge1\). When \(r<k\), the endpoint-equal configurations split into four orbits, each of size \(2\binom mr\), and the endpoint-opposite configurations split into two orbits, each of size \(4\binom mr\). Here the factor two or four records the transformations by inversion, exchanging \(a,b\), and moving the two admissible \(z\)-heights. When \(m\) is even and \(r=k=m/2\), inversion exchanges the two equal-size height classes; there are instead two equal-endpoint orbits of size \(2\binom m{m/2}\) and one opposite-endpoint orbit of size \(4\binom m{m/2}\). Consequently the total number of orbits is \(3+6\lfloor(m-1)/2\rfloor+3\mathbf1_{2\mid m}=3m\). The listed orbit sizes sum to the facet count because they reproduce every one of the six or eight patterns associated with each choice of height class, with no overlap.

**Facet-vertex extremum.** Every oriented tight edge contributes exactly one vertex of \(B_n\) to its supporting facet. There are no other vertices on that facet, since every oriented unit-edge molecule is extreme: it is the only way to attain graph distance one between its two adjacent endpoints, and convex combinations of other edge molecules cannot reproduce it. Therefore the facet vertex number is the tight-edge count. With nonconstant \(U\) and \(r+k=m\), it is respectively
\[
rk+2k+2\quad(f(a)=f(b)=0),\qquad
rk+2r+2\quad(f(a)=f(b)=1),\qquad
rk+m+1\quad(f(a)\ne f(b)).
\]
The six constant-\(U\) configurations each give \(2m+2\) tight edges. The mixed-endpoint expression cannot exceed the maximum of the two equal-endpoint expressions because \(\max\{2r+2,2k+2\}\ge m+2>m+1\). The equal-endpoint maximum is therefore
\[
\max_{1\le k\le m-1}\bigl(k(m-k+2)+2\bigr)
=\left\lfloor\frac{(m+2)^2}{4}\right\rfloor+2.
\]
When \(m=3\), the six constant-\(U\) configurations tie this maximum; for \(m\ge4\), \(2m+2\) is strictly smaller. For even \(m=2s\ge4\), the maximum is realized by the unique favorable opposite-height class of size \(s+1\), giving \(4\binom m{s-1}\) maximizing facets. For odd \(m=2s+1\ge5\), the favorable class has either \(s+1\) or \(s+2\) vertices, giving \(4(\binom ms+\binom m{s-1})\) maximizing facets. The case \(m=3\) contributes \(12\) nonconstant and six constant maximizers. This proves all assertions.

## Verification
Run the standalone standard-library script `verify.py` using `python3 verify.py`. It directly enumerates every integer-valued 1-Lipschitz potential after fixing one clique value to zero and bounding all remaining values by graph distance. For \(m=3,4,5,6,7,8\), it computes the connected spanning tight-edge graphs, their tight-edge counts, and the full orbits generated by swapping the distinguished endpoints, adjacent permutations of \(U\), and sign reversal. For \(n=5,6,7,8,9,10\), the resulting facet counts are \(54,118,246,502,1014,2038\); the orbit counts are \(9,12,15,18,21,24\); and the maximal numbers of facet vertices are \(8,11,14,18,22,27\). The analytic argument above, rather than this finite enumeration, proves the formulas for all \(n\ge5\).

## Relationship to prior work
The tight-edge connectedness criterion and the identification of symmetric edge polytopes with finite graph-metric Lipschitz-free balls are established background. Higashitani–Jochemko–Michałek develop the facet criterion and treat complete and complete bipartite cases. D'Alì–Delucchi–Michałek develop further facets and graph gluing. Chen–Davis–Korchevskaia give general facet-subgraph correspondence, which supports but does not itself evaluate this particular infinite family. Braun–Bruegge tabulate and count facets of sparse graph families, so individual small numeric facet counts are not claimed as intrinsically new. Chen–Korchevskaia's work on **regular subdivisions of polytopes induced by edge contraction** is about a different subdivision operation, not replacing one graph edge by a two-edge path; the similarity of wording does not imply this enumeration. The contribution here is the simultaneously evaluated all-\(n\) facet count, complete signed symmetry-orbit classification, and sharp facial-incidence bound for one-edge subdivisions of complete-graph metrics.

## Limitations
All edges have equal length and exactly one edge of a complete graph is subdivided exactly once; the result does not cover arbitrary subdivisions or perturbations of edge lengths. It treats the indicated subgroup of linear symmetries induced by graph automorphisms and central inversion, not an unproved classification of every affine symmetry of the polytope. Computational checks cover only \(5\le n\le10\). A bibliographic search and examination of closely relevant sources cannot exclude an unindexed equivalent treatment or exact small-case tables. No independent mathematical audit is claimed.

## References
1. A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1 (first posted 2018-07-20); especially the facet criterion.
2. A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193v1 (first posted 2019-10-11).
3. T. Chen, R. Davis, E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315v1 (first posted 2021-07-26).
4. B. Braun, K. Bruegge, *Facets of symmetric edge polytopes for graphs with few edges*, arXiv:2201.13303v1 (first posted 2022-01-31).
5. T. Chen, E. Korchevskaia, *Graph edge contraction and subdivisions for adjacency polytopes*, arXiv:1912.02841v1 (first posted 2019-12-05).
