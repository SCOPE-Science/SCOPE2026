# Homotopy types of the two twelve-vertex Archimedean 2-independence complexes

## Finding
Let \(T\) be the truncated-tetrahedral graph and \(C\) the cuboctahedral graph. For a finite graph \(G\), its two-independence simplicial complex \(\operatorname{Ind}_2(G)\) has faces the vertex subsets whose induced connected components have at most two vertices. Then there are **integral homotopy equivalences**
\[
\left|\operatorname{Ind}_2(T)\right|\simeq
\bigvee^{3}S^{3}\vee\bigvee^{3}S^{4},\qquad
\left|\operatorname{Ind}_2(C)\right|\simeq\bigvee^{32}S^{3}.
\]
In particular, the first complex has integral reduced homology of rank three in each of degrees three and four, while the second has rank thirty-two only in degree three; both have zero reduced integral homology otherwise. They are nonpure but homotopy equivalent to wedges of spheres, of different dimension patterns.

## Assumptions and scope
All graphs are finite, simple and undirected. Label the twelve vertices of \(T\) by ordered pairs \((i,j)\) of distinct elements of \(\{0,1,2,3\}\), in lexicographic order. Two distinct vertices are adjacent exactly when their first coordinates agree or they are \((i,j)\) and \((j,i)\). This describes the skeleton of the truncated tetrahedron (four triangles joined along the six edges of the underlying tetrahedron).

Label the twelve vertices of \(C\) by the twelve edges of the cube \(Q_3\). Two such vertices are adjacent exactly when their cube edges share an endpoint; thus \(C=L(Q_3)\) is the cuboctahedral graph. In the checker, cube vertices are integers from zero to seven, edges connect binary words differing in one position, and the twelve edges are ordered first by their lower binary endpoint and then by coordinate position.

The assertion is about the indicated two-independence complex, not the ordinary independence complex, ordinary matching complex, or a graph-metric Rips or Čech complex. No family-wide result beyond these two graphs is claimed.

## Proof
**1. Enumerating the face posets.** A vertex subset is a face of \(\operatorname{Ind}_2(G)\) if and only if it contains no three-element subset inducing a connected graph. Indeed, any induced connected component of order at least three contains a path on three distinct vertices (possibly with its endpoints also adjacent). Enumerating the three-element subsets gives 28 forbidden triples for \(T\) and 56 for \(C\). The numbers of nonempty faces by dimensions zero onward are
\[
 f(T)=(12,66,192,303,228,62),\qquad
 f(C)=(12,66,164,177,36).
\]
For \(T\), there are three maximal dimension-three simplices and 62 maximal dimension-five simplices. For \(C\), there are 45 maximal dimension-three simplices and 36 maximal dimension-four simplices. Hence neither complex is pure.

**2. Acyclic matchings.** Number vertices zero through eleven as above and take the vertex order
\[
(10,3,0,2,7,11,1,9,5,4,6,8).
\]
Starting with all *nonempty* faces unmatched, process each indicated vertex \(v\): pair every currently unmatched face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\), provided both faces remain unmatched. Every face belongs to at most one pair. This rule is deterministic, as in `verify_polyhedra.py`, and its union is acyclic. Independently of the general sequential-element-matching argument, the checker explicitly orients each codimension-one Hasse incidence downwards, reverses every matched incidence and visits **all** cells by a topological sort. The oriented graph has 3432 incidences over 863 nonempty faces for \(T\), and 1512 incidences over 455 nonempty faces for \(C\); in both instances all vertices are visited.

There are 428 matching pairs for \(T\), with precisely one critical vertex, three critical three-cells and three critical four-cells. There are 211 matching pairs for \(C\), with precisely one critical vertex and 32 critical three-cells. By the acyclic discrete-Morse theorem, the original simplicial complexes are homotopy equivalent to CW complexes with precisely these cell counts.

**3. Integral attaching degrees.** The cellular boundary of the Morse CW complex can be calculated exactly from signed gradient paths. The checker uses the orientation of a simplex given by ascending vertex labels and incidence \((-1)^p\) upon deleting the vertex in zero-based position \(p\). A critical cell projects to itself, the upper cell of any matching pair projects to zero, and the lower cell \(a\) of a pair \((a,b)\) projects to the negative signed sum of the projections of all other facets of \(b\), divided by the unit incidence coefficient \([b:a]\). Acyclicity guarantees that these equations terminate recursively. Taking the signed facets of each critical cell and projecting them gives the integral Morse boundary.

For \(T\) the exact three-by-three Morse boundary from the critical four-cells to the critical three-cells is the zero matrix; the checker verifies all its integer entries, rather than merely their reduction modulo two. There are no other possible positive-dimensional cellular differentials. The three-skeleton of the Morse CW complex is a wedge of three three-spheres. Since
\(\pi_3(\bigvee^3 S^3)\cong\mathbb Z^3\) with the three Hurewicz degrees as coordinates, each zero-boundary attaching map of a four-cell is nullhomotopic. The result is \(\bigvee^3S^3\vee\bigvee^3S^4\).

For \(C\), all nonzero-dimensional critical cells have dimension three, so no positive-dimensional attaching map can occur: the CW complex is \(\bigvee^{32}S^3\). This proves the asserted integral homotopy types, not merely rational or mod-two homology.

## Verification
Run `python3 verify_polyhedra.py` with Python 3.9 or newer; only the standard library is needed. The program constructs both graphs from the above canonical descriptions, enumerates every one of their 4095 nonempty vertex subsets and checks face recognition both by forbidden connected triples and independently by induced-component flood fill. It computes all maximal facets, performs the deterministic matching, tests the whole directed Hasse graph for acyclicity, calculates signed integral Morse boundaries by memoized exact recursion, and independently computes all mod-two simplicial boundary ranks. The observed output is in `verification_output.txt`, finishing with `VERIFY_OK`.

All finite assertions in the proof are exhaustive and reproducible; the topological step from the Morse CW decomposition to the wedge type is a mathematical argument. There are no interpolated infinite-parameter claims.

## Relationship to prior work
Deshpande and Singh introduced systematic homotopy calculations for higher-independence complexes, giving formulas for complete multipartite graphs, fully whiskered graphs, paths, cycles and perfect arity trees [1]. Ghosh and Selvaraja study chordality and shellability of higher-independence complexes, proving criteria for forests, block graphs and graph modifications [2]. The two Archimedean graphs here belong to none of those explicitly classified homotopy families. The published 2021 results of Abdelmalek et al. establish shellability and decomposability for some chordal classes [3], whereas both examples here contain induced cycles and do not satisfy the cited chordal hypotheses.

The computational records closest to these two graph names concern ordinary matching complexes, three-cut complexes and graph-metric constructions, which are different simplicial functors; none of the examined statements gives the two homotopy types above. These comparisons are evidence of a distinct claim, not a proof of worldwide novelty. A relevant database or unindexed exact computation could still establish priority.

## Limitations
The theorem concerns only the two specified graphs and the parameter two; it does not classify all Archimedean graphs or all higher-independence parameters. The computer proof uses complete finite enumeration and an explicitly reproducible acyclic matching; a short conceptual matching proof is not supplied. There is no independent scientific audit. Bibliographic priority has residual uncertainty despite the targeted database and primary-literature comparisons.

## References
[1] P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448 (first submitted 2020-01-15), https://arxiv.org/abs/2001.05448.

[2] A. Ghosh and S. Selvaraja, *Chordality and Shellability of Higher Independence Complexes*, arXiv:2505.06614 (first submitted 2025-05-10), https://arxiv.org/abs/2505.06614.

[3] F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863 (first submitted 2021-06-21), https://arxiv.org/abs/2106.10863.
