# Dodecahedral transportation ball: facet census and incenter locus

## Finding

Let \(D\) be the 20-vertex dodecahedral graph with unit-edge shortest-path metric and let \(P\) be the unit ball of its real Lipschitz-free space in the canonical zero-sum Euclidean realization. The 19-dimensional polytope \(P\) has precisely **3,678,208 facets**. The number of facets containing exactly \(j\) vertices of \(P\) is

| \(j\) | 19 | 20 | 21 | 22 | 23 | 24 |
|:--:|--:|--:|--:|--:|--:|--:|
| Number | 411,840 | 934,968 | 1,103,600 | 801,000 | 352,440 | 74,360 |

In the intrinsic Euclidean geometry, the largest inscribed ball has radius \(r=1/\sqrt{29}\). The ball centered at the origin touches exactly 20 facets; their outward normals are the centered distance functions from the 20 vertices of \(D\). The affine hull of **all** centers of maximum-radius Euclidean balls has dimension **9**. In particular, the center is not unique.

## Assumptions and scope

Use the canonical generalized Petersen labeling \(V(D)=\{u_0,\ldots,u_9,v_0,\ldots,v_9\}\), all suffixes modulo 10, and edges \(u_iu_{i+1},u_iv_i,v_iv_{i+2}\) for every \(0\le i<10\). This graph has 20 vertices, 30 edges, and is connected. For distinct vertices \(a,b\), write \(d(a,b)\) for the shortest-path length. The Lipschitz-free ball equals
\[
P=\operatorname{conv}\{\pm(e_a-e_b):ab\in E(D)\}\subset H,\qquad H=\{z\in\mathbb R^{20}:\sum_a z_a=0\}.
\]
The displayed identification follows because every normalized molecule \((e_a-e_b)/d(a,b)\) is an average of edge molecules along a shortest path. The Euclidean metric is the restriction of the ordinary \(\ell_2^{20}\) inner product to \(H\); no other embedding is intended. A facet is a codimension-one face of \(P\), and the contact assertion concerns the origin-centered largest Euclidean ball.

## Proof

**Facet criterion and completeness.** The polar is the 19-dimensional Lipschitz polytope of real functions \(f\) on \(V(D)\) modulo additive constants with \(|f(a)-f(b)|\le1\) on edges. Normalize \(f(u_0)=0\). A vertex of this polar must have saturated edge constraints whose normals span \(H\); the incidence matrix of those edges has rank 19 precisely when the tight-edge graph is connected (and then automatically spanning). Thus facets of \(P\) correspond bijectively to normalized extreme potentials with connected tight-edge graph. Each such potential is integer-valued, since the tight connected graph includes a spanning tree whose successive signed edge differences are \(\pm1\). Conversely any normalized integer potential with connected tight-edge graph defines a polar vertex, hence one facet. All integer 1-Lipschitz potentials can therefore be enumerated without omitting any facet.

**Finite exact enumeration.** The standalone program `verify.cpp` lists the 30 edges, constructs a vertex order in which each newly visited vertex has an earlier neighbor, and recursively assigns every possible integer value in the intersection of its adjacent previously assigned unit intervals. It fixes \(f(u_0)=0\); the connected order bounds every variable and makes the recursion exhaustive. The program visits exactly 14,607,387 normalized integer 1-Lipschitz potentials. For each it checks connectivity of saturated edges by breadth-first search, yielding 3,678,208 extreme potentials. The six counts by number of saturated edges are respectively 411,840; 934,968; 1,103,600; 801,000; 352,440; and 74,360 at 19 through 24 edges. Each saturated edge contributes exactly one vertex to the supported facet, proving the incidence table. The enumeration is finite and exhaustive by the preceding integrality and recursion arguments, not an inference from a sample.

**Sharp Euclidean norm and contacts.** For a potential \(f\), let \(\bar f=f-\frac1{20}(\sum_a f(a))\mathbf1\in H\). Its facet has inequality \(\langle z,\bar f\rangle\le1\), so its supporting plane lies at distance \(1/\|\bar f\|_2\) from the origin. Its exact squared-normal numerator is
\[
T(f)=20\sum_a f(a)^2-\left(\sum_a f(a)\right)^2=20\|\bar f\|_2^2.
\]
The exhaustive checker determines \(\max T(f)=580\), attained at exactly 20 extreme potentials, and checks set equality of these maximizers with \(f_w(a)=d(w,a)-d(w,u_0)\) for the 20 choices of \(w\). Independently, breadth-first search gives distance-layer multiplicities \((1,3,6,6,3,1)\) at every vertex; hence \(\sum_a d(w,a)=50\), \(\sum_a d(w,a)^2=154\), and \(\|\bar f_w\|_2^2=154-50^2/20=29\). Therefore \(r=1/\sqrt{29}\) and the centered ball touches exactly those 20 facet planes. To see this is the global, not merely centered, inradius, note that every facet occurs with its centrally reflected partner. If a translated ball of radius \(r'\) centered at \(c\) lies in \(P\), the opposite inequalities imply \(r'\|\bar f\|_2+|\langle c,\bar f\rangle|\le1\). Using a maximizer with norm \(\sqrt{29}\) forces \(r'\le1/\sqrt{29}\).

**Complete affine dimension of optimal centers.** Every optimal center \(c\in H\) must annihilate all 20 maximizer normals. Their linear span has dimension exactly ten. For an upper bound, the graph antipode of \(u_i\) is \(u_{i+5}\), and similarly for \(v_i\), with \(d(w,a)+d(w',a)=5\) for all \(a\); consequently \(\bar f_{w'}=-\bar f_w\), giving at most ten independent normals. For a matching lower bound, use the distance-difference matrix \(M_{i,j}=d(i,j)-d(0,j)\) in the numeric order \((u_0,\ldots,u_9,v_0,\ldots,v_9)\). The submatrix with rows \((1,2,3,4,5,10,11,12,13,14)\) and columns \((0,1,2,3,4,10,11,12,13,14)\) has exact determinant \(-2\); the accompanying `verify_rank.py` constructs all distances and computes this minor with an integer Bareiss algorithm. Every distance row has sum 50, so every row of this difference matrix already belongs to \(H\) and is the difference of two centered distance normals. The nonzero minor therefore gives ten linearly independent directions in their span. Hence the annihilator in the 19-dimensional \(H\) has dimension nine. At the origin all other 3,678,188 facet inequalities have strictly positive radius slack, so some neighborhood of zero inside this nine-dimensional annihilator consists entirely of optimal centers. No optimal center lies outside it. This establishes the asserted affine dimension.

## Verification

The sources `verify.cpp` and `verify_rank.py` are standalone and require a C++17 compiler and Python 3 standard library, respectively. From their containing directory run `g++ -std=c++17 -O3 verify.cpp -o verify && ./verify` and `python3 verify_rank.py`. The C++ program exhaustively checks all integral 1-Lipschitz assignments in the canonical \(GP(10,2)\) representation, the connected-tight-subgraph criterion, the exact incidence counts, \(T\)-maximizers and equality with distance profiles. The Python program independently checks the graph distance layers and antipodes, and computes the specified integer minor determinant. They report `ALL EXACT CHECKS PASSED` and `ALL EXACT RANK CHECKS PASSED` when their assertions are met. These calculations have been executed successfully against the embedded source versions. The proof above specifies why these finite loops cover all required candidates.

## Relationship to prior work

Higashitani, Jochemko and Michałek (2018), Theorem 3.1, provide the general integral tight-edge facet criterion for symmetric edge polytopes; the criterion is **not** a new result here. D'Alì, Delucchi and Michałek (2019) analyze graph symmetric edge polytopes and established families; Chen, Davis and Korchevskaia (2021) develop facet-subgraph characterizations; Braun and Bruegge (2022) tabulate certain small graphs and families. Alexander et al. (2019) explain the general Lipschitz-free and symmetric-edge-polytope connection. The inspected portions and full-text searches of these sources did not produce the evaluated dodecahedral census, complete contact set, or nine-dimensional optimal-center locus. A separately searchable dodecahedral *cut* polytope has different coordinates, dimension, and defining inequalities and does not itself imply these conclusions.

## Limitations

This is an exact calculation for the one graph \(GP(10,2)\), not an infinite-family theorem or a claim about other Euclidean realizations. The computational enumeration is essential to the displayed facet statistics and largest-normal comparison; an elementary closed-form symbolic enumeration is not supplied. The affine dimension characterizes the full center locus, but its complete face lattice and metric volume are not computed. The literature comparisons cannot exclude an unindexed exact-object table or a differently worded previously published result.

## References

1. A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of symmetric edge polytopes* (first public 2018-07-20), arXiv:1807.07678, https://arxiv.org/abs/1807.07678.
2. A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes* (2019), arXiv:1910.05193, https://arxiv.org/abs/1910.05193.
3. M. Alexander and coauthors, *Geometry and volume product of finite dimensional Lipschitz-free spaces* (2019), arXiv:1911.10642, https://arxiv.org/abs/1911.10642.
4. T. Chen, R. Davis, D. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes* (2021), arXiv:2107.12315, https://arxiv.org/abs/2107.12315.
5. B. Braun, C. Bruegge, *Facets of Symmetric Edge Polytopes for Graphs with Few Edges* (2022), arXiv:2201.13303, https://arxiv.org/abs/2201.13303.
