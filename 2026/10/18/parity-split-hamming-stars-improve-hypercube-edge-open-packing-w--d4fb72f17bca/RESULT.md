# Parity-split Hamming stars improve hypercube edge-open packing, with an exact five-cube census

## Finding

Let \(Q_d\) be the graph with vertex set \(\{0,1\}^d\), where two vertices are adjacent precisely when their Hamming distance is one. An **edge-open packing** is a set \(F\) of edges for which the subgraph induced by the endpoints of \(F\) is a disjoint union of stars, and \(F\) consists of all edges in those stars. Write \(\rho_e^{\mathrm{o}}(Q_d)\) for its maximum cardinality.

**Theorem (parity-lift bound and first odd-dimensional exact census).** For every pair of integers \(k\ge 2\) and \(d\ge 2^k-1\),
\[
\rho_e^{\mathrm{o}}(Q_d)\ \ge\ (2^k-1)\,2^{d-k-1}.
\]
Every bound is realized by an explicit family of disjoint induced stars, using only \(2^k-1\) of the available coordinate directions. In particular,
\[
\rho_e^{\mathrm{o}}(Q_9)\ge224.
\]
For the five-dimensional cube, the exact value and complete extremal count are
\[
\rho_e^{\mathrm{o}}(Q_5)=12,\qquad
\bigl|\{F\subseteq E(Q_5):F\text{ is an edge-open packing},\ |F|=12\}\bigr|=80.
\]
All eighty maximum packings consist of four induced three-edge stars. They form one automorphism orbit and have the constructive classification given below.

## Assumptions and scope

All graphs are finite, undirected and simple. In a star, the edge set contains every edge between its center and its chosen leaves; a one-edge star is permitted. The standard characterization by induced star forests is used with the original edge-open-packing definition: for two different selected edges, no third graph edge may connect their endpoint sets. These formulations agree for hypercubes, which are triangle-free.

The infinite lower bound is asserted only for integers \(k\ge2\) and \(d\ge2^k-1\); it is not presented as an equality formula in general. The five-dimensional statement is exact for every edge subset of that graph, not merely for symmetric subsets. Vertices of \(Q_5\) are intrinsically labelled by binary strings, so the number eighty is a labelled-subset count; quotienting by automorphisms yields a single class.

## Proof

### 1. Parity-split perfect Hamming code

Fix \(k\ge2\), put \(h=2^k-1\), and let \(H\) be the \(k\)-by-\(h\) binary matrix whose columns are all nonzero vectors of \(\mathbb F_2^k\), in any fixed order. Define the binary linear code
\[
C=\ker(H)\subseteq\mathbb F_2^h.
\]
The matrix has rank \(k\), so \(|C|=2^{h-k}\). No column is zero and no two are equal, so no nonzero codeword has Hamming weight one or two. Thus distinct codewords are at distance at least three.

Every radius-one closed Hamming ball in \(Q_h\) contains \(h+1=2^k\) vertices. The balls \(B_1(c)\), \(c\in C\), are pairwise disjoint by the distance bound, and their total size is \(2^{h-k}2^k=2^h\). Consequently these balls **partition** the entire cube.

Write \(C_0\) and \(C_1\) for the even-weight and odd-weight codewords. Both sets have the same size. To see this, take any two distinct nonzero columns \(a,b\) of \(H\). The distinct nonzero column \(a+b\) also occurs in \(H\), so the three corresponding positions support a weight-three codeword. Translation by that codeword interchanges the two parities. Hence
\[
|C_0|=|C_1|=2^{h-k-1}.
\]
Two distinct codewords of the same parity have even Hamming distance, necessarily at least four. Therefore the sets of all \(h\) coordinate edges around the centers \(c\in C_p\), with \(p=0\) or \(1\), form pairwise disjoint **induced** \(h\)-stars: if distinct stars had a vertex overlap, or had a graph edge between their endpoint sets, the corresponding centers would have distance at most two or three, contradicting distance at least four. The endpoint sets of these stars are exactly the balls \(B_1(c)\). Since the full code is perfect, the endpoint sets from the two different parity classes are complementary subsets of \(\mathbb F_2^h\).

### 2. Cartesian parity lift

Identify the vertices of \(Q_d\) with pairs \((x,y)\in\mathbb F_2^h\times\mathbb F_2^{d-h}\). For each fixed \(y\), let \(p(y)\in\{0,1\}\) be its Hamming-weight parity. In the fiber \(\{(x,y):x\in\mathbb F_2^h\}\), select every coordinate edge in the first \(h\) directions incident to every center \((c,y)\) with \(c\in C_{p(y)}\). Select no edges in any of the final \(d-h\) directions.

Inside one fiber the selected edges induce disjoint stars by step 1. Fibers differing in at least two coordinates of \(y\) have no connecting graph edges. If \(y\) and \(y'\) differ in exactly one coordinate, their parities are opposite. The supports selected in their fibers are the complementary unions of Hamming balls from \(C_0\) and \(C_1\). A connecting cube edge would have to join \((x,y)\) to \((x,y')\) with the **same** first coordinate \(x\), which is impossible when those supports are disjoint. Thus the full selected endpoint subgraph is the disjoint union of the asserted induced stars.

There are \(2^{d-h}\) fibers, \(2^{h-k-1}\) selected centers per fiber, and exactly \(h\) selected edges per center. Their disjointness gives the exact number of edges in this construction:
\[
2^{d-h}\cdot2^{h-k-1}\cdot h
=h2^{d-k-1}
=(2^k-1)2^{d-k-1}.
\]
Taking \(k=3\) and \(d=9\) yields \(7\cdot2^5=224\), as claimed. This is a **lower bound**; it makes no assertion that an even larger packing of \(Q_9\) cannot exist.

### 3. The explicit five-cube family

For \(Q_5\), choose any three of its five coordinate positions as **active**, and let the other two be **passive**. Choose any active three-bit template \(t\in\mathbb F_2^3\). In the fiber indexed by a passive two-bit string \(y\), put a full induced three-edge star centered at the active string \(t\oplus(p(y),p(y),p(y))\). The other three coordinate directions carry no selected edges. In each fiber, its star occupies four vertices; adjacent passive fibers have complementary four-vertex supports. Thus these four stars are mutually induced-disjoint and form an edge-open packing of \(4\cdot3=12\) edges.

The ten active-coordinate triples and eight templates give \(\binom53\cdot2^3=80\) distinct selected edge sets: the directions of selected edges recover the active triple, and a star in the passive-zero fiber recovers the template. Coordinate permutations and independent bit flips take one construction to any other, so they form one automorphism orbit.

### 4. Exhaustive upper bound and complete count for the five-cube

The remaining finite step is certified by the attached standalone program `verify.py`, whose complete search algorithm and recursion are present in the package. The five-cube has \(80\) graph edges. Define a graph \(A\) on these \(80\) objects: two distinct cube edges are adjacent in \(A\) exactly when selecting them together creates no prohibited third cube edge. In the triangle-free cube this is equivalent to: they share an endpoint, or all four cross-endpoint pairs are nonadjacent in the cube. The edge-open packings in \(Q_5\) are **exactly** the cliques in \(A\).

The automorphism group of \(Q_5\) acts transitively on its graph edges. Consequently, to determine the largest clique and to count maximum cliques, it suffices to search cliques containing one prescribed cube edge \(e_0\). The program constructs the full \(80\)-vertex compatibility graph directly from binary Hamming distances and performs two exact searches. The first is bitset branch-and-bound for the maximum clique containing \(e_0\). A greedy proper vertex coloring of each remaining candidate graph supplies a rigorous clique-size upper bound for branch pruning. The program proves that the largest anchored clique contains precisely twelve vertices; this search visits \(96\) recursive nodes. The second recursion enumerates **each** twelve-clique containing \(e_0\) once, selecting candidate vertices in increasing index order and using only cardinality and properly colored clique upper bounds for pruning. It finds exactly twelve anchored maximizers, visiting \(1,393\) recursive nodes.

For clarity, this is a finite **exhaustive computational proof** of the upper bound and the enumeration, not a probabilistic experiment or extrapolation. The code gives the complete algorithm rather than merely a solver log. Edge transitivity makes the number of maximum edge sets equal to the incidence double count
\[
\frac{|E(Q_5)|\cdot\#\{\text{maximum sets containing }e_0\}}{12}
=\frac{80\cdot12}{12}=80.
\]
The eighty explicit packings in step 3 meet that count, so no other maximizing type exists. Therefore \(\rho_e^{\mathrm{o}}(Q_5)=12\) and every optimizer has the asserted shape.

## Verification

Execute `python3 verify.py` with the Python standard library. The program reconstructs the complete cube edge lists, constructs the compatibility graph, checks symmetry of compatibility, performs the full anchored maximum search and full anchored counting search, constructs all eighty explicit maximizers and verifies pairwise edge-open-packing feasibility, and directly verifies the Hamming-lift packings for dimension/parameter pairs \((k,d)=(2,3),(2,5),(3,7),(3,9)\).

The observed transcript is:

```
PASS: Q5 maximum = 12; optimal subsets = 80
PASS: anchored maximum nodes = 96 ; anchored counting nodes = 1393
PASS: all maxima belong to the 80-member parity-lift family
PASS: Hamming constructions Q3=3, Q5=12, Q7=56, Q9=224
```

The infinite lower bound is proved in steps 1–2; these finite checks are illustrations and regression checks. The exact five-cube upper bound and enumerator do depend on the exhaustive finite search, but every search and bound is expressed in auditable source code, without a black-box solver.

## Relationship to prior work

Brešar, Dravec, Hedžet and Samadi [1], Section 5.1, investigate hypercube edge-open packings. Their Table 1 records the five-cube **lower** bound \(\rho_e^{\mathrm{o}}(Q_5)\ge10\), their subsequent paragraph records \(\rho_e^{\mathrm{o}}(Q_9)\ge153\), and their Theorem 5.10 determines the exact value in dimensions that are powers of two. The present result sharpens those displayed lower bounds to an exact five-cube value and an improved nine-cube construction, and determines every five-cube maximizer. Earlier general product and packing inequalities in that article neither provide this explicit parity-lift family nor resolve its five-cube exact extremal structure.

Das and Santra [2] develop algorithms for edge-open packing on AT-free, chordal, and convex bipartite graphs. Their accessible complete text treats these algorithmic classes and does not state the hypercube Hamming-parity lift or an exact five-cube enumeration. Their formulation as induced star forests agrees with the present structural definition, but does not by itself imply the extremal cardinalities.

## Limitations

The inequality for dimensions other than five is not asserted sharp. In particular, the value of \(\rho_e^{\mathrm{o}}(Q_9)\) is not determined; only the constructive improvement \(\rho_e^{\mathrm{o}}(Q_9)\ge224\) is established. The code provides a complete exact certificate at dimension five and explicit feasibility checks at higher dimensions, not an exhaustive search in those higher dimensions. The complete five-cube optimizer census is computationally exhaustive rather than a solver-free structural upper-bound proof. Priority against all inaccessible or unpublished research cannot be guaranteed.

## References

1. B. Brešar, T. Dravec, J. Hedžet, and B. Samadi, *Induced matching vs edge open packing: trees and product graphs*, arXiv:2406.04020v2 (first posted 2024). Particularly Section 5.1, Table 1, Proposition 5.9, and Theorem 5.10. https://arxiv.org/pdf/2406.04020
2. G. K. Das and K. Santra, *Maximum Edge Open Packing on AT-Free, Chordal, and Convex Bipartite Graphs*, arXiv:2610.02275v1, first posted 2026-10-01. https://arxiv.org/abs/2610.02275
