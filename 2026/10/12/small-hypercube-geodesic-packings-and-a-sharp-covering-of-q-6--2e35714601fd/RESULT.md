# Small-hypercube geodesic packings and a sharp covering of \(Q_6\)

## Finding

Write \(Q_d\) for the graph of binary strings of length \(d\), with edges changing exactly one bit. A **geodesic packing** is a family of pairwise vertex-disjoint geodesics that are maximal under path extension. Its size is denoted \(\operatorname{gpack}(Q_d)\). The exact small-cube profile is
\[
\operatorname{gpack}(Q_4)=2,\qquad \operatorname{gpack}(Q_5)=5,\qquad \operatorname{gpack}(Q_6)=9.
\]
For \(d=4\), the polynomial enumerating all unordered geodesic packings, including the empty packing, by their number of paths is
\[
F_4(t)=1+192t+2976t^2.
\]
Moreover the minimum number of diameter-geodesics whose union covers every vertex of \(Q_6\) is
\[
\operatorname{gvc}_6(Q_6)=10.
\]
Thus the natural vertex-volume packing bound is **not** always attained in Cartesian powers of \(K_2\): its first nontrivial failure occurs at \(Q_4\), whereas it is attained in \(Q_5\) and \(Q_6\). The near-perfect nine-path packing of \(Q_6\) leaves one vertex and yields the matching cover construction by adding one more geodesic.

## Assumptions and scope

All graphs are finite simple undirected graphs. Use the integer encoding \(0,\ldots,2^d-1\) for the bit strings in \(Q_d\); an edge \(uv\) exists precisely when the binary XOR of \(u\) and \(v\) is a positive power of two. All path sequences displayed below use this encoding. A geodesic is a shortest path between its endpoints; it is maximal if it is not a proper subpath of a longer geodesic. The packing polynomial counts families of **distinct unoriented paths** with disjoint vertex sets, including the empty family; different orientations of the same path are not counted twice. For covering, paths may intersect one another, but each must have length \(d\). All numerical assertions concern exactly \(d\in\{4,5,6\}\); no general formula for other dimensions is asserted.

## Proof

**1. Maximal paths and volume bounds.** In the cube, graph distance is Hamming distance. Along any shortest path each flipped coordinate is distinct. A shortest path of length smaller than \(d\) has a coordinate not yet flipped and can be extended at its endpoint by flipping that coordinate. Thus every maximal geodesic has exactly \(d\) edges and \(d+1\) vertices, with complementary endpoints. Therefore
\[
\operatorname{gpack}(Q_d)\le\left\lfloor\frac{2^d}{d+1}\right\rfloor,
\qquad \operatorname{gvc}_d(Q_d)\ge\left\lceil\frac{2^d}{d+1}\right\rceil.
\]
These bounds give \(3\), \(5\), and \(9\) for the packing numbers at dimensions four, five, six, and a lower covering bound of \(10\) in dimension six. For \(d=1,2,3\), the same volume upper bound is attained: one edge in \(Q_1\), any two-edge path in \(Q_2\), and the two disjoint geodesics `(0, 1, 3, 7)` and `(2, 6, 4, 5)` in \(Q_3\). Thus the strictness at \(Q_4\) is indeed the first strict dimension.

**2. Complete four-dimensional obstruction and count.** Every length-four geodesic in \(Q_4\) is determined by its initial vertex and an ordering of the four coordinate flips. Reversing its orientation identifies two descriptions of the same vertex set. No other descriptions coincide: the vertex-induced subgraph of a diameter geodesic is a path on five vertices, with its unique linear ordering up to reversal. Hence there are \(16\cdot4!/2=192\) distinct maximal geodesics. Cube automorphisms, consisting of bit translations and coordinate permutations, act transitively on these geodesics. Fix
\[
P_0=(0,1,3,7,15).
\]
The complete enumeration in the accompanying `verify.py` generates the \(192\) vertex masks in two mathematically different ways: by all initial-vertex/flip-order pairs, and by all five-vertex subsets whose induced graph is a five-vertex path with complementary endpoints. The two sets agree. Filtering to geodesics disjoint from \(P_0\) gives precisely \(31\) masks, and **each pair of these \(31\) masks intersects**. Consequently three vertex-disjoint diameter geodesics cannot exist: map the first member of any hypothetical triple to \(P_0\) by a cube automorphism, leaving two disjoint members of its \(31\)-element compatible list, a contradiction. An explicit pair is

```text
(0, 1, 3, 7, 15); (13, 5, 4, 6, 2)
```

It follows that \(\operatorname{gpack}(Q_4)=2\). Every one of the \(192\) maximal geodesics has \(31\) compatible partners by transitivity, so there are \(192\cdot31/2=2976\) unordered two-path packings, proving the polynomial. The verifier additionally checks the no-triple assertion directly without symmetry reduction. This is an exhaustive **finite proof**, not a claim that sampling suggests impossibility.

**3. Witnesses in dimensions five and six.** Each line below is an ordered diameter geodesic, and the lines in each displayed group have disjoint vertex sets. For \(Q_5\) the five paths are

```text
(1, 0, 4, 6, 22, 30)
(2, 18, 16, 24, 28, 29)
(5, 13, 15, 31, 27, 26)
(11, 3, 7, 23, 21, 20)
(14, 12, 8, 9, 25, 17)
```

They cover \(30\) of the \(32\) vertices, omitting exactly \(\{10,19\}\). Thus \(\operatorname{gpack}(Q_5)=5\) by the volume upper bound. For \(Q_6\) the nine paths are

```text
(0, 1, 3, 7, 15, 31, 63)
(4, 6, 2, 34, 42, 43, 59)
(17, 16, 20, 52, 60, 62, 46)
(5, 13, 9, 8, 24, 56, 58)
(23, 21, 29, 61, 45, 44, 40)
(25, 57, 41, 33, 32, 36, 38)
(12, 14, 10, 11, 27, 19, 51)
(28, 30, 22, 54, 55, 39, 35)
(26, 18, 50, 48, 49, 53, 37)
```

They cover \(63\) of the \(64\) vertices, omitting only \(47\). Thus \(\operatorname{gpack}(Q_6)=9\), attaining the volume upper bound.

**4. Sharp diameter-geodesic covering in dimension six.** Starting at the sole uncovered vertex \(47\), successively flip coordinates \(0,1,2,3,4,5\) to obtain one further geodesic

```text
(47, 46, 44, 40, 32, 48, 16)
```

Its endpoints are complementary and it includes vertex \(47\). The nine pairwise disjoint paths in the preceding display plus this tenth path cover the entire cube. Since nine paths can cover at most \(9\cdot7=63<64\) vertices, ten is minimal.

## Verification

`verify.py` is a complete, dependency-free Python 3 verification program supplied alongside this document; execute it from the extracted package with `python3 verify.py`. It verifies that each displayed path has \(d+1\) distinct valid vertices, consists of \(d\) distinct coordinate flips, and has complementary endpoints. It checks pairwise disjointness, exact uncovered-vertex lists, and the ten-geodesic cover. In dimension four it performs independent constructions of the complete mask set, an exhaustive compatibility count, a pairwise-intersection test for every path compatible with the canonical path, and a further direct exhaustive no-triple check. The supplied `verification_output.txt` is the result of an actual run; the output ends with `VERIFY_OK`. No heuristic random search or unexplained solver bound is used in the proof.

## Relationship to prior work

Manuel, Brešar and Klavžar (2022; revised 2023) introduced geodesic packing as vertex-disjoint maximal geodesics. Their Lemma 2.3 and Corollary 2.8 yield the general packing volume bound for Cartesian products of uniform-geodesic graphs, including all hypercubes. They do not state the small-cube packing values or the complete packing polynomial given here. The new \(Q_4\) value is a strictness example for that bound; the \(Q_5\) and \(Q_6\) packings are exact witnesses of sharpness.

Sharma, Guragain and Srivastava (public preprint, January 2026) define the minimum number of diameter-geodesics covering all vertices. For \(Q_n\), their Theorem 11 supplies general lower and upper bounds \(\lceil 2^n/(n+1)\rceil\) and \(2^{n-2}\). At dimension six their bounds allow \(10\) through \(16\); the explicit ten-path cover here closes that gap. Their covering invariant is not the same as the maximum vertex-disjoint packing invariant. Anick and Ramras (2013) study **edge** decompositions of hypercubes by paths, a different notion from the vertex-disjoint geodesic packing and minimum vertex-covering problems proved here. Goldwasser and Hansen (2020) study extremal densities of perfect-path configurations in high-dimensional subcubes, not a vertex-disjoint family of diameter paths in a fixed cube.

## Limitations

The result is confined to dimensions four, five, and six; it does not determine the general-dimension packing or covering sequences. The exact \(Q_4\) obstruction relies on complete executable finite enumeration; the remaining sharpness cases have checkable constructive witnesses and elementary volume bounds. The numerical verifier is a proof certificate for a finite search space but has not undergone independent audit. The publicly accessible abstract for older disjoint-shortest-path routing literature concerns a different, prescribed-terminal routing setting, although its full text was not inspected, leaving some historical overlap risk. Equivalent results under other descriptions (such as vertex-disjoint antipodal paths) cannot be excluded merely from unsuccessful searches.

## References

1. P. Manuel, B. Brešar and S. Klavžar, *Geodesic packing in graphs*, arXiv:2210.15325 (first posted 2022-10-27), https://arxiv.org/html/2210.15325v3 .
2. A. Sharma, S. Guragain and R. Srivastava, *On k-geodetic vertex traceable graphs*, preprint publicly uploaded 2026-01-28, DOI 10.13140/RG.2.2.13477.36320, https://www.researchgate.net/publication/400141455_On_k-geodetic_vertex_traceable_graphs .
3. D. Anick and M. Ramras, *Edge Decompositions of Hypercubes by Paths*, arXiv:1308.4949 (2013), https://arxiv.org/html/1308.4949v1 .
4. J. Goldwasser and R. Hansen, *Maximum density of vertex-induced perfect cycles and paths in the hypercube*, arXiv:2009.09037 (2020), https://arxiv.org/html/2009.09037v1 .
5. *Disjoint and Shortest Paths Routing in Hypercubes*, *Congressus Numerantium* 233 (2019), abstract at https://combinatorialpress.com/cn-articles/volume-233/disjoint-and-shortest-paths-routing-in-hypercubes/ .
