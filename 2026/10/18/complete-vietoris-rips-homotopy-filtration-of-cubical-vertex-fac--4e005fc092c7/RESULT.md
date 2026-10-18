# Complete Vietoris–Rips homotopy filtration of cubical vertex–facet incidence graphs

## Finding
For every integer \(d\ge3\), the shortest-path Vietoris–Rips filtration of the vertex–facet incidence graph of the \(d\)-dimensional cube has the following complete integral homotopy types (with inclusive filtration convention):
\[
\operatorname{VR}_{\le r}(G_d)\simeq
\begin{cases}
\bigsqcup^{2^d+2d}\mathrm{pt},&0\le r<1,\\
\bigvee^{(d-1)2^d-2d+1}S^1,&1\le r<2,\\
S^{2^{d-1}-1},&2\le r<3,\\
S^{2^{d-1}+d-1},&3\le r<4,\\
\mathrm{pt},&r\ge4.
\end{cases}
\]
In the first line, the notation means a disjoint union of that many points. At scale two there is a **simplicial collapse** to the antipodal-pair cross-polytope boundary; at scale three there is an exact **simplicial join description**.

In particular, the reduced integral persistence barcode consists of \(2^d+2d-1\) degree-zero intervals \([0,1)\), \((d-1)2^d-2d+1\) degree-one intervals \([1,2)\), a single interval \([2,3)\) in degree \(2^{d-1}-1\), and a single interval \([3,4)\) in degree \(2^{d-1}+d-1\). There are no other reduced bars. Ordinary degree zero additionally has its single eternal connected-component class after scale one.

The three-dimensional instance is the fourteen-vertex rhombic-dodecahedral graph: its stages at scales one, two, and three are \(\bigvee^{11}S^1\), \(S^3\), and \(S^6\), respectively.

## Assumptions and scope
Write \(X=\{-1,1\}^d\) for the cube's vertex set and \(Y=\{(i,s):1\le i\le d,\ s\in\{-1,1\}\}\) for its signed-coordinate facets. Define the simple bipartite graph \(G_d\) on \(X\sqcup Y\) by \(x\sim(i,s)\) if and only if \(x_i=s\). Thus it has \(2^d+2d\) vertices and \(d2^d\) edges. Only shortest-path graph distance is considered; this is **not** Euclidean distance between polytope vertices, nor the Hamming metric on the cube vertices alone. Throughout \(d\ge3\), and all homotopy and homology groups are integral unless explicitly stated.

## Proof
**1. Complete metric description.** Any distinct cube vertices \(x,x'\in X\) have graph distance two if they agree at some coordinate and four if \(x'=-x\). Distinct facet vertices \((i,s),(j,t)\in Y\) have distance two unless \(i=j\) and \(t=-s\), in which case they have distance four. A cube vertex \(x\) is at distance one from an incident facet and distance three from a nonincident facet. The upper bounds follow by selecting an unconstrained second coordinate for a path, which is possible for \(d\ge3\); bipartiteness and the absence of common neighbors for opposite pairs give the matching lower bounds. Consequently the graph has diameter four.

**2. Scales zero and one.** The graph is connected and bipartite, so its first Rips complex is exactly its one-dimensional graph (it has no triangles). Its first Betti number is
\[
|E(G_d)|-|V(G_d)|+1=d2^d-(2^d+2d)+1=(d-1)2^d-2d+1.
\]
A connected graph collapses onto a wedge of that many circles. At scale zero there are \(2^d+2d\) isolated vertices.

**3. An explicit collapse at scale two.** Let \(K=\operatorname{VR}_{\le2}(G_d)\). On \(X\), its one-skeleton connects every pair except the \(2^{d-1}\) antipodal pairs. Thus the induced complex \(A=K[X]\) is the join of \(2^{d-1}\) zero-spheres and is homeomorphic to \(S^{2^{d-1}-1}\).

For a nonempty set \(F\subseteq Y\), a face containing exactly the facet vertices \(F\) exists if and only if \(F\) does not contain an opposite signed pair. Call such \(F\) compatible, and put
\[
X_F=\{x\in X:x_i=s\text{ for every }(i,s)\in F\}.
\]
Every face with facet part \(F\) has the form \(F\cup U\) for **an arbitrary** \(U\subseteq X_F\): all vertices in \(X_F\) agree on each constrained coordinate, so they are pairwise nonantipodal.

Fix \(a_F\in X_F\) by setting every unspecified coordinate to \(+1\). Order all nonempty compatible facet sets \(F\) by decreasing cardinality (breaking ties arbitrarily). For each such \(F\), order \(U\subseteq X_F\setminus\{a_F\}\) by decreasing cardinality and perform the elementary collapse
\[
F\cup U\quad\subset\quad F\cup U\cup\{a_F\}.
\]
This is a genuine free-face collapse, not merely a formal matching: at this point every strict coface obtained by adding another facet has already been deleted (its facet part was larger), and every strict coface obtained by adding a different cube vertex has already been deleted (its cube part was larger). Adding \(a_F\) is the unique remaining immediate coface. For any higher-dimensional coface, a surviving intermediate immediate coface would be necessary; hence none exists. The two displayed faces can therefore be deleted. Every face containing a facet appears in exactly one of these pairs. What remains is exactly \(A\), proving \(K\searrow A\cong S^{2^{d-1}-1}\).

The number of collapsed pairs is the finite identity
\[
N_d=\sum_{k=1}^{d}\binom dk 2^k\,2^{2^{d-k}-1},
\]
obtained by choosing \(k\) coordinate facets with signs, then choosing the optional subset of the \(2^{d-k}-1\) other compatible cube vertices.

**4. Exact join at scale three.** Every cube vertex is now adjacent in the distance-three graph to every facet vertex. On \(X\) the only missing edges join antipodes; on \(Y\) the only missing edges join opposite facets. Consequently the *entire* scale-three clique complex is
\[
K_3=A*B,\qquad A=\underbrace{S^0*\cdots*S^0}_{2^{d-1}\text{ factors}},\quad B=\underbrace{S^0*\cdots*S^0}_{d\text{ factors}}.
\]
Joins of simplicial spheres are spheres, so \(K_3\cong S^{2^{d-1}+d-1}\). At scale four, every pair of vertices is connected, giving the full simplex.

**5. Persistence.** The only reduced nonzero homology groups at successive nontrivial integer scales are in degrees one, \(2^{d-1}-1\), and \(2^{d-1}+d-1\). For \(d\ge3\) these degrees are pairwise distinct. Thus all maps between adjacent positive-dimensional groups necessarily vanish by degree, and the intervals stated in the finding follow; the connected-component map at scale one is surjective. This also verifies there are no hidden extension or coefficient-torsion qualifications.

## Verification
The included standalone Python 3 standard-library script `verify_incidence_rips.py` checks the complete graph-distance profile and the explicit face-pair collapse for \(d=3\) and \(d=4\), without relying on precomputed homology ranks. It requires no downloads or third-party dependencies. Execute `python verify_incidence_rips.py`.

For \(d=3\), independent brute-force enumeration of all vertex subsets verifies the scale-two and scale-three clique complexes, with exactly \(240\) and \(2186\) nonempty faces, respectively. The scale-two collapse has \(80\) free-face pairs and leaves exactly \(80\) nonempty faces of an \(S^3\) cross-polytope boundary. For \(d=4\), the scale-two complex has \(9152\) nonempty faces; \(1296\) free-face pairs leave \(6560\) nonempty faces forming an \(S^7\) cross-polytope boundary. The scale-three clique complex is combinatorially the join of two cross-polytope boundaries, as in the general proof. The complete all-dimensional result is proved symbolically above; the finite program is a reproducibility cross-check, not an extrapolation to arbitrary dimensions.

## Relationship to prior work
Adamaszek's foundational graph-power study [1] identifies clique complexes of distance powers with graph-metric Vietoris–Rips complexes and classifies several settings, including cycles and certain high-girth or total graphs. In particular its girth-based collapse hypothesis cannot apply here: the cubical vertex–facet incidence graph contains four-cycles. Its general universality statement does not classify the present canonical family.

Adamaszek and Adams [2] classify Rips complexes of circles and provide an important model of complete persistence calculations; the circular metric does not identify our incidence graph. Their work on hypercube graphs [3] uses the \(2^d\) cube **vertices only**, with Hamming distance, and proves a small-scale wedge of three-spheres. In contrast, this note uses the \(2^d+2d\) vertices **and facets** of a cube with incidence-graph distance; the two metric spaces and their sphere dimensions differ.

Other related indexed results concern the \(24\)-vertex rhombicuboctahedron rather than the \(14\)-vertex rhombic dodecahedron, or the rhombic-dodecahedral *matching* complex rather than the graph-metric Rips complex. Neither statement supplies the displayed homotopy filtration, even at \(d=3\). The concrete uniform coordinate-fiber collapse above is the distinguishing mechanism.

## Limitations
The theorem assumes \(d\ge3\) and the **graph** shortest-path metric. It does not concern Euclidean Vietoris–Rips complexes, arbitrary cubical face-poset ranks, or integral equivariant group actions. The breadth of published and unindexed literature means an equivalent prior formulation cannot be excluded by a finite search. The proof is self-contained conditional only on the usual elementary-simplicial-collapse and sphere-join facts; no software output is needed for the infinite-dimensional statement.

## References
[1] M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (first publicly posted 2011-04-03), especially sections 1–3 and the graph-power correspondence.

[2] M. Adamaszek and H. Adams, *The Vietoris–Rips complexes of a circle*, arXiv:1503.03669 (first publicly posted 2015-03-12).

[3] M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040 (first publicly posted 2021-03-01), especially Theorem 1 and its Hamming-metric definition.
