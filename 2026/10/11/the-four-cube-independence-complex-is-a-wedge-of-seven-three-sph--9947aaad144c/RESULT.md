# The four-cube independence complex is a wedge of seven three-spheres

## Finding

Let \(Q_4\) be the simple graph on the sixteen binary words \(\{0,1\}^4\), with two words adjacent exactly when their Hamming distance is one. Let \(\operatorname{Ind}(Q_4)\) be the abstract simplicial complex whose faces are the vertex subsets containing no adjacent pair. Then

\[
\bigl|\operatorname{Ind}(Q_4)\bigr|\simeq\bigvee^{7}S^3.
\]

Equivalently, this is the independence complex of the fully periodic four-by-four square grid \(C_4\mathbin{\square}C_4\), since \(C_4\cong K_2\mathbin{\square}K_2\). In particular the only nonzero reduced integral homology is \(\widetilde H_3\cong\mathbb Z^7\), and the fundamental group is trivial. The claim is an exact homotopy type, not merely a field-homology computation.

## Assumptions and scope

All complexes are finite and use the standard nonempty-face convention for their face posets. The statement concerns **only** the sixteen-vertex four-cube; no assertion is made about larger hypercubes or arbitrary periodic square grids. Number its vertices by the integers \(0,\ldots,15\), written as four-bit binary words. The neighbors of vertex \(v\) are \(v\oplus1\), \(v\oplus2\), \(v\oplus4\), and \(v\oplus8\), where \(\oplus\) is bitwise exclusive-or. A simplex is represented by its sixteen-bit membership mask.

## Proof

**Exact face universe.** Enumerate every integer mask from \(1\) through \(2^{16}-1\) and retain a mask precisely when no two selected vertices differ in exactly one bit. This is a direct exhaustive enumeration of *all* independent subsets: every vertex subset has exactly one mask, and the predicate is equivalent to the graph's edge definition. The face counts by dimensions zero through seven are

\[
(16,88,208,228,128,56,16,2),
\]

so the face poset contains exactly \(742\) members. Independent sets of eight vertices occur, and none has more than eight.

**Discrete-Morse matching.** Begin with all nonempty faces unmatched. For each pivot \(v=0,1,\ldots,15\), consider every currently unmatched face \(a\) omitting \(v\). If \(b=a\cup\{v\}\) is also currently unmatched, pair \((a,b)\); remove both from the unmatched set. At a fixed pivot the pairs are disjoint because each lower member omits the pivot and each upper member contains it. Their counts at the sixteen successive pivots are

\[
(176,134,10,4,5,5,13,4,0,3,4,3,3,1,1,1),
\]

which sum to \(367\). Exactly eight faces remain unmatched. Their decimal masks are \(1,1680,2400,10370,17028,24600,33064,33096\). Mask \(1\) has one selected vertex; the other seven masks each have four selected vertices. Thus the critical-cell dimensions are one zero and seven threes.

**Complete acyclicity certificate.** On the full Hasse diagram of the \(742\) nonempty faces, direct every dimension-one incidence from larger face to smaller face, *except* reverse an incidence in the matching. There are exactly \(2816\) directed incidences. The accompanying `morse_certificate.json` records all \(367\) matched incidences together with a linear ordering of **every** face. The independent checker reconstructs the entire Hasse diagram directly from the definition of \(Q_4\), confirms that every stored pair is exactly the pair selected by the pivot rule, and checks for **all \(2816\) arrows** that its tail precedes its head in the stored order. The existence of such a linear order proves the directed graph acyclic; no unexamined incidences or asymptotic extrapolations enter the argument.

By the acyclic-matching theorem of discrete Morse theory, \(\operatorname{Ind}(Q_4)\) is homotopy equivalent to a CW complex with one zero-cell and seven three-cells and no cells of other dimensions. Each three-cell is attached to the zero-skeleton by a map from \(S^2\) to a point, necessarily constant. The CW complex is therefore a wedge of seven three-spheres, proving the stated homotopy equivalence. In particular the integral homology is free abelian as claimed.

## Verification

The self-contained standard-library command is `python3 verify_q4.py morse_certificate.json`. The checker enumerates every independent set, validates the stored complete Morse matching and its acyclicity ordering, and independently computes exact binary simplicial boundary ranks

\[
\bigl(\operatorname{rank}_{\mathbb F_2}\partial_1,\ldots,
\operatorname{rank}_{\mathbb F_2}\partial_7\bigr)
=(15,73,135,86,42,14,2).
\]

This gives mod-two Betti numbers \((1,0,0,7,0,0,0,0)\) in dimensions zero through seven, consistent with the stronger Morse-based integral result. The verifier's successful terminal line is `VERIFY_OK independent_sets=743 nonempty_faces=742 pairs=367 critical=1x0+7x3 acyclic_edges=2816 mod2_b3=7`. The included topological ordering, not the boundary-rank check, is the complete acyclicity certificate.

## Relationship to prior work

Bousquet-Mélou, Linusson, and Nevo analyze independence complexes of **open and cylindrical** square grids using discrete Morse theory; toroidal boundary conditions are discussed through earlier alternating-count questions, but are not covered by their open/cylindrical homotopy classification [2]. Jonsson studies **periodic square-grid quotients** and constructs nontrivial cross-cycles, but explicitly limits the main result to cross-cycles and notes that full homology need not be generated by them [3]. Neither result gives the exact homotopy type of this particular fully periodic four-by-four grid. Matsushita and Wakatsuki determine homotopy types of rectangular **path-by-path** grid graphs, whose boundary conditions differ from the present graph [4]. Barmak's general theorem that triangle-free graph independence complexes are suspensions [5] applies here but does not determine the number or dimension of wedge summands. Kozlov's graph-complex simple-homotopy methods [1] provide historical methodological context, not this classification.

The finite count of independent sets and general discrete-Morse machinery are not claimed as new. The additional fact is the exact seven-sphere homotopy type, proved by a complete and independently checkable matching certificate.

## Limitations

This is one precise, naturally occurring finite periodic-grid case. It does not determine a family-wide formula for all toroidal grids or higher cubes, nor does it establish a canonical equivariant decomposition under graph automorphisms. The originality comparison cannot exclude an unindexed presentation of the same specific computation. Acyclic matching implies homotopy equivalence to a Morse CW complex; it is **not** asserted that the original complex simplicially collapses directly to an embedded wedge of spheres.

## References

[1] D. N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, arXiv:math/0503613, first posted 2005-03-28; explicitly primary MSC 57Q10. https://arxiv.org/abs/math/0503613

[2] M. Bousquet-Mélou, S. Linusson, E. Nevo, *On the independence complex of square grids*, arXiv:math/0701890, Journal of Algebraic Combinatorics 27 (2008), 423–450. https://arxiv.org/abs/math/0701890

[3] J. Jonsson, *Certain homology cycles of the independence complex of grid graphs*, author-hosted preprint dated 2008-10-19; published in Discrete & Computational Geometry 43 (2010), 927–950. https://people.kth.se/~jakobj/doc/papers/crosstorus.pdf

[4] T. Matsushita and S. Wakatsuki, *Independence complexes of (n × 4) and (n × 5)-grid graphs*, arXiv:2203.16391. https://arxiv.org/abs/2203.16391

[5] J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418, first posted 2010-07-02. https://arxiv.org/abs/1007.0418

[6] R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. https://doi.org/10.1006/aima.1997.1650
