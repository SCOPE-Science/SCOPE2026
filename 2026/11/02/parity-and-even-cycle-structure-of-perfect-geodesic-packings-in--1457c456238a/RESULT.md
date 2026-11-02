# Parity and even-cycle structure of perfect geodesic packings in binary-slab Hamming graphs

## Finding

Let \(H_n=K_2\square K_2\square K_n\), where \(n\ge2\). A *maximal geodesic* means a shortest path that is not properly contained, as a consecutive subpath, in another shortest path. A *geodesic packing* is a collection of pairwise vertex-disjoint maximal geodesics. Then
\[
\boxed{\operatorname{gpack}(H_n)=2\left\lfloor\frac n2\right\rfloor.}
\]
In particular, the universal volume bound \(\operatorname{gpack}(H_n)\le n\) is attained exactly for even \(n\); odd \(n\) has an unavoidable deficit of one entire four-vertex path.

Every perfect packing (a packing with \(n\) paths) determines a loopless, two-regular *multigraph of column incidences* on the \(n\) labeled \(K_2\square K_2\) fibers: each maximal geodesic contributes an edge between the two fibers that it meets, with parallel edges retained. **Every cycle of this multigraph has even length. Conversely, every loopless two-regular multigraph on the labeled fibers whose components are even cycles, including doubled edges as cycles of length two, is realized by a perfect geodesic packing.**

If \(h_n\) is the number of distinct labeled column-incidence multigraphs that occur among perfect packings, with \(h_0=1\), then
\[
\boxed{\sum_{n\ge0}\frac{h_n}{n!}z^n
 =\exp(z^2/4)(1-z^2)^{-1/4}.}
\]
Thus \(h_n=0\) for odd \(n\), and \(h_2=1\), \(h_4=6\), \(h_6=120\), \(h_8=5250\). This counts **incidence multigraphs**, not the generally larger number of path packings.

## Assumptions and scope

Graphs are finite, simple, undirected, unweighted Cartesian products. The vertices of \(H_n\) are triples \((a,b,c)\) with \(a,b\in\{0,1\}\) and \(c\in\{1,\ldots,n\}\); two vertices are adjacent when exactly one coordinate differs. Call the four vertices with a fixed \(c\) a *column*. The underlying four-cycle \(Q=K_2\square K_2\) has two edge directions, corresponding to changes of \(a\) and of \(b\). A cycle of length two in a multigraph consists of two parallel edges, not a loop. A geodesic is counted up to reversal, and each path in a packing is counted once.

The finding concerns the maximum number of disjoint maximal geodesics and the possible incidence multigraphs of *perfect* packings; it does not enumerate the packings themselves, classify all non-perfect packings, or address arbitrary three-factor Hamming graphs.

## Proof

**1. Maximal geodesics and column footprints.** In a Cartesian product of complete graphs, distance is the number of unequal coordinates. A shortest path cannot change any coordinate twice. A shortest path of length less than three can be extended at an endpoint by changing an as-yet unchanged coordinate; the resulting path is still shortest. Therefore the maximal geodesics of \(H_n\) are exactly the paths of length three, changing each of the three coordinates once. Each has four vertices and meets exactly two columns, with footprint sizes either \((1,3)\), \((2,2)\), or \((3,1)\). An occupied two-vertex footprint is an edge of \(Q\); an occupied three-vertex footprint is a two-edge path of \(Q\).

**2. Two incidences per column in a perfect packing.** A packing of \(n\) paths would use all \(4n\) vertices. Each path meets exactly two columns; hence the sum of the numbers of path incidences over the columns is \(2n\). No path can fill a column of four vertices, so each column must meet at least two paths. Consequently every column meets exactly two paths, whose disjoint footprints partition \(Q\). The footprint sizes are therefore \((2,2)\) or \((1,3)\). Call the columns of these two kinds \(E\)-columns and \(T\)-columns, respectively. Since the footprint sizes of a single path at its two columns sum to four, a path joins two \(E\)-columns or two \(T\)-columns; it never joins different kinds. The column-incidence multigraph is loopless and two-regular, so its components are cycles (parallel-edge two-cycles allowed).

**3. Evenness of the \(E\)-cycles.** The two edges of \(Q\) arising as footprints in an \(E\)-column are disjoint; in a four-cycle, two disjoint edges are parallel. Label each \(E\)-column by their common coordinate direction (the first or second binary coordinate). A path that meets two \(E\)-columns spends one binary-coordinate change in each of them; since a geodesic changes each binary coordinate exactly once, these two edges have perpendicular directions. Thus the labels alternate along every \(E\)-component cycle. Every such cycle has even length.

**4. Evenness of the \(T\)-cycles.** Orient a path between two \(T\)-columns from the column containing its three-vertex footprint to the column containing its singleton footprint. Every \(T\)-column has exactly one incoming and one outgoing path, making each \(T\)-component a directed cycle. For each column \(c\), write \(s_c\in\{0,1\}^2\) for its incoming singleton's binary coordinate. The outgoing three-vertex footprint is \(Q\setminus\{s_c\}\), a two-edge path. The binary coordinate \(t_c\) of the endpoint at which this path changes column is adjacent in \(Q\) to its missing vertex \(s_c\): both endpoints of a three-vertex path of \(Q\) are neighbors of the missing vertex. The column change preserves the two binary coordinates, so if \(d\) follows \(c\) in the directed incidence cycle, then \(s_d=t_c\). Consequently \(s_c\) and \(s_d\) are adjacent in the bipartite square \(Q\). These coordinates form a closed walk of length equal to the incidence-cycle length. Every closed walk in a bipartite graph has even length. Therefore every \(T\)-cycle is even. Combining steps 3 and 4 proves the claimed necessary even-cycle property and, in particular, that \(n\) must be even for a perfect packing.

**5. Realization of every even-cycle multigraph.** Fix a labeled loopless two-regular multigraph whose components are even cycles. Orient each of its cycles arbitrarily, and alternately designate its columns as direction-\(a\) and direction-\(b\) columns. At each column, assign one of its two disjoint, parallel edges of \(Q\) to the incoming incidence and the other to the outgoing incidence. An incidence between two columns now receives a direction-\(a\) edge in one column and a direction-\(b\) edge in the other. These two edges, viewed in \(Q\), intersect at exactly one binary-coordinate pair \(x\). Traverse the first edge toward \(x\), change the column coordinate while at \(x\), and traverse the second edge away from \(x\). This is a shortest three-edge path: it changes \(a\), \(b\), and \(c\) exactly once. Across all incidences, every column's four vertices are partitioned by its two assigned edges, so these maximal geodesics are pairwise disjoint and cover all \(4n\) vertices. This works equally for a doubled-edge two-cycle. Hence every stated multigraph is realizable, and for even \(n\) there is a perfect packing (take \(n/2\) doubled-edge cycles).

**6. Optimality for odd \(n\).** No packing contains more than \(n\) paths because each maximal geodesic uses four vertices. For odd \(n\), steps 2–4 rule out \(n\) paths, yielding the upper bound \(n-1\). Pair any \(n-1\) columns and on each pair take the two disjoint geodesics supplied by step 5; the remaining column is unused. This gives \(n-1\) paths. For even \(n\), step 5 gives \(n\) paths. The packing-number formula follows.

**7. Enumeration of incidence multigraphs.** On a fixed labeled pair, there is precisely one doubled-edge component, giving exponential-generating-function contribution \(z^2/2\). For every even \(\ell\ge4\), the number of unoriented simple cycles on \(\ell\) given labels is \((\ell-1)!/2\), yielding contribution \(z^\ell/(2\ell)\). By the exponential formula for labeled disjoint components,
\[
\sum_{n\ge0}h_n\frac{z^n}{n!}
=\exp\!\left(\frac{z^2}{2}+\sum_{j\ge2}\frac{z^{2j}}{4j}\right)
=\exp(z^2/4)(1-z^2)^{-1/4}.
\]
The correspondence in step 5 shows that every multigraph counted here is actually realized, completing the enumeration proof.

## Verification

The accompanying standalone `verify.py` reconstructs graph adjacency and all diameter-three shortest paths directly from the vertex triples. It uses an independent exact subset recursion to compute the optimum for \(n=2,3,4\), obtaining \(2,2,4\), respectively. It checks the explicit paired-column construction and realizations of a single even incidence cycle for \(n=2,4,6,8,10,12\). The accompanying `verify_extra.py` exhaustively enumerates perfect packings; this supplementary enumeration for \(n=2,3,4\) yielded respectively \(12,0,720\) perfect packings and checked every resulting incidence cycle for even length. These are finite corroborations only; the all-\(n\) proof is in the preceding section.

To replay the main standalone checks with Python 3, run `python3 verify.py`. No third-party packages or data are needed.

## Relationship to prior work

Manuel, Brešar, and Klavžar introduced maximal-geodesic packing and proved that Cartesian products of uniform-geodesic graphs are uniform-geodesic; their resulting volume bound gives \(\operatorname{gpack}(H_n)\le n\). Their 2022 preprint studies rook graphs and diagonal grids, but the inspected material does not establish the parity obstruction, the exact value for \(K_2\square K_2\square K_n\), or the realizable even-cycle incidence structures. The new contribution is the sharp deficit for odd \(n\), the all-parameter equality classification, and the incidence-multigraph characterization and generating function.

Brešar, Klavžar, and Rall's later work on packings in bipartite prisms and hypercubes studies *vertex* two-packings and *open* neighborhood packings. Those are different from collections of vertex-disjoint maximal shortest paths and do not imply the result here. The independent older census of maximal-geodesic packings in the two-factor graph \(K_2\square K_n\) likewise does not imply this three-factor parity obstruction.

## Limitations

The result does not give a count of path packings sharing one incidence multigraph, nor any formula for general \(K_a\square K_b\square K_c\) with both \(a,b>2\). Its originality is assessed against accessible indexed literature and available prior claims, not established as global publication priority. In particular, unindexed work on induced four-vertex path factors or isometric path decompositions may require further expert comparison. Some later sections of the main 2022 preprint were unavailable on a repeat retrieval; the relevant Cartesian-product propositions and surrounding sections were inspected.

## References

1. P. Manuel, B. Brešar, and S. Klavžar, *Geodesic packing in graphs*, arXiv:2210.15325, first posted 2022-10-27. https://arxiv.org/abs/2210.15325 . See especially Proposition 2.7, Corollary 2.8, and the discussion of rook graphs.
2. B. Brešar, S. Klavžar, and D. F. Rall, *Packings in bipartite prisms and hypercubes*, arXiv:2309.04963, first posted 2023-09-10. https://arxiv.org/abs/2309.04963 . This paper concerns different packing invariants.
