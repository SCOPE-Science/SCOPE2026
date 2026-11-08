# A mixed-dimensional sphere wedge for the bidirected complete bipartite graph with three vertices in each class

## Finding

Let \(D=\overleftrightarrow{K}_{3,3}\) be the digraph with vertex classes \(A=\{0,1,2\}\) and \(B=\{3,4,5\}\), containing both arcs between every vertex of \(A\) and every vertex of \(B\). Its multipath complex \(X(D)\) has directed arcs as vertices, and a subset is a face if the selected arcs form a disjoint union of simple directed paths and isolated vertices. Then there is an **integral homotopy equivalence**

\[
|X(D)|\simeq\left(\bigvee^{19}S^3\right)\vee\left(\bigvee^{12}S^4\right).
\]

In particular the integral reduced homology is free of rank \(19\) in degree \(3\), free of rank \(12\) in degree \(4\), and zero in all other degrees. This is a homotopy classification, not an inference from homology alone.

## Assumptions and scope

The statement concerns exactly the six-vertex, eighteen-arc bidirected graph above, not a one-way orientation, undirected matching complex, or a family of larger graphs. Fix the arc indexing as follows: first enumerate the nine arcs \((i,j)\) for \(i=0,1,2\) and \(j=3,4,5\) in lexicographic order; then enumerate the nine reverse arcs \((j,i)\) in the same nested-loop order. Identify a simplex with the nonzero integer bit mask recording its selected arcs.

A bit mask is admissible exactly when each vertex has at most one selected incoming arc, at most one selected outgoing arc, and the selected digraph has no directed cycle. The complex has dimension \(4\): six vertices cannot support a six-arc acyclic directed graph with in- and out-degree at most one.

## Proof

**1. Exact finite face description.** The admissibility conditions above are equivalent to being a disjoint union of directed paths: each weak component of a finite directed graph with in- and out-degree at most one is an isolated vertex, a path, or a directed cycle. Excluding the final possibility leaves precisely multipaths. A complete enumeration using the arc mask rules gives the face vector

\[
(f_0,f_1,f_2,f_3,f_4)=(18,108,264,252,72),
\]

or \(714\) nonempty simplices. Two distinct enumeration procedures in `verify.py` produce the same face set; their checks include excluding all directed cycles, not merely two-cycles.

**2. Complete discrete-Morse matching.** Define the ordered sequence of arc indices

`(17,15,14,2,7,3,10,11,0,4,8,16,12,5,9,6,13,1)`.

Initially every nonempty simplex is active. For each index \(e\) in this order, traverse the active simplices in increasing integer-mask order. Whenever both \(\sigma\) and \(\sigma\cup\{e\}\) are active and \(e\notin\sigma\), match this lower face to that upper face and delete both from the active set. Continue through all eighteen indices. This unambiguously specifies \(341\) disjoint codimension-one matching pairs and leaves precisely one critical zero-simplex, nineteen critical three-simplices, and twelve critical four-simplices.

For a full acyclicity certificate, orient each unmatched face incidence downward and each matched incidence upward. The verifier constructs all \(2376\) incidences on the \(714\) nonempty simplices and topologically sorts the resulting directed graph, successfully deleting all \(714\) vertices. Hence the matching is acyclic. Forman's discrete-Morse theorem supplies a homotopy-equivalent CW complex with exactly these critical cells.

**3. Integral attaching degrees.** Orient simplices by increasing arc index. For each matched pair \((\ell,u)\), the coefficient of \(\ell\) in \(\partial u\) is \(+1\) or \(-1\). The integer cellular differential on critical cells is determined by repeatedly substituting \(\ell=-\langle\partial u,\ell\rangle\sum_{v\ne\ell}\langle\partial u,v\rangle v\), or equivalently by integral unit-pivot cancellations of these pairs. Two independent implementations in `verify.py` produce identical critical boundary matrices. The entire \(19\)-by-\(12\) boundary from critical dimension four to critical dimension three is zero **over the integers**, not only modulo two.

**4. From the Morse model to the wedge.** Its CW model has one zero-cell, no one- or two-cells, nineteen three-cells, and twelve four-cells. Consequently its three-skeleton is \(\bigvee^{19}S^3\). By the Hurewicz isomorphism for this two-connected space, \(\pi_3(\bigvee^{19}S^3)\cong H_3(\bigvee^{19}S^3;\mathbb Z)\cong\mathbb Z^{19}\). Each four-cell attaching map is therefore determined by its signed degree vector, i.e. the corresponding column of the integral Morse differential. All these columns vanish, so all twelve attaching maps are nullhomotopic. Thus each four-cell contributes a wedge summand \(S^4\), proving the asserted equivalence.

## Verification

Run `python3 verify.py` using Python 3.10 or newer (standard library only). The executable independently enumerates multipaths by subsets and by outgoing-arc choices; checks every matching pair and every gradient edge; topologically sorts the complete modified Hasse diagram; computes critical integer incidence matrices by both recursive Morse projection and independent unit-pivot algebraic cancellation; and computes raw mod-two boundary ranks for comparison. It terminates with `ALL_VERIFY_OK`, as recorded in `verify_output.txt`.

Observed nonempty face vector: `(18,108,264,252,72)`; matched pairs: `341`; critical profile: `{0:1,3:19,4:12}`; complete Hasse incidences: `2376`; raw mod-two boundary ranks in positive cardinalities two through five: `(17,91,173,60)`. These finite calculations are exhaustive for the exactly specified six-vertex complex; no claim for arbitrary graph sizes is extrapolated.

## Relationship to prior work

Caputi, Collari and Smith's 2026 manuscript studies multipath complexes of bidirectional paths and polygons and proves connectivity and homology statements for those families. The complete bipartite graph here has multiple overlapping undirected four-cycles and is not one of the paths or polygons there. Its T-operation suspension theorem does not supply this classification.

Caputi, Collari, Di Trani and Smith's 2022 paper defines multipath complexes and evaluates complete bipartite digraphs with all arcs going from one bipartition class to the other. Those are alternating orientations; the present digraph has both orientations of every edge, admits directed cycles, and is not the one-way complex. Its Euler-characteristic formula therefore does not imply the present result. Published calculations of ordinary discrete-Morse complexes or two-matching complexes of the same underlying graph concern different simplicial complexes. Searches of equivalent formulations and available indexed records found no directly covering classification, but this cannot rule out unindexed work.

## Limitations

The classification is specific to fully bidirected \(K_{3,3}\). It does not establish a general formula for \(\overleftrightarrow{K}_{a,b}\), determine an automorphism representation, or imply shellability. The proof and executable verify an exact finite claim; they are not an independent external review. Literature coverage has the usual residual risk from unindexed or inaccessible mathematical sources.

## References

1. L. Caputi, C. Collari and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1 (first public posting 2026-01-09), https://arxiv.org/abs/2601.05670 .
2. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1 (2022), https://arxiv.org/abs/2208.04656 .
3. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
