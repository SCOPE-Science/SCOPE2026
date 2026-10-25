# The nonabelian six-symbol group-table partial-transversal complex is a mixed sphere wedge

## Finding

Let \(G=S_3\), the group of all permutations of three letters. Let \(K(G)\) be the simplicial complex with vertices \((r,c)\in G\times G\). Its faces are precisely the sets \(F\subseteq G\times G\) for which all rows \(r\), all columns \(c\), and all products \(rc\) occurring in \(F\) are pairwise distinct. Then

\[
K(S_3)\simeq \bigvee^{12} S^2\ \vee\ \bigvee^{163} S^3.
\]

In particular, its reduced integral homology is \(\widetilde H_2\cong\mathbb Z^{12}\), \(\widetilde H_3\cong\mathbb Z^{163}\), and zero in every other degree. This is an integral homotopy equivalence, not just equality of Betti numbers.

## Assumptions and scope

The group is exactly the nonabelian group of order six. Its elements are the six bijections of \(\{0,1,2\}\), in lexicographic order of their tuples. Composition uses \((r\circ c)(x)=r(c(x))\). A cell at group-row index \(r\in\{0,\ldots,5\}\) and group-column index \(c\in\{0,\ldots,5\}\) is encoded by bit \(6r+c\) in a 36-bit integer; thus no precomputed Latin-square database or choice of isomorphic labeling is needed. Faces include the empty set when defining the abstract complex, but the nonempty face enumeration and its Morse poset exclude that set.

The result is about the *entire* complex of partial transversals, not only maximal partial transversals, not the space of Latin trades, and not the ordinary rook/chessboard complex obtained by omitting the distinct-symbol constraint. The primary mathematical classification is MSC2020 55U10.

## Proof

**1. Exhaustive face model.** For each row, independently choose either no cell or one cell in that row, subject to using no column or product-symbol previously used. The accompanying `verify.py` implements this six-stage recursion without pruning a legal choice. After the sixth row every legal partial transversal occurs once, indexed by its chosen cell set. Enumeration gives precisely 3,054 nonempty faces, with dimension-wise face vector

\[
(f_0,f_1,f_2,f_3,f_4)=(36,360,1200,1242,216).
\]

Their inclusion-maximal members have cardinalities three, four, and five, with respective multiplicities 12, 324, and 216; there are no six-cell transversals. Thus the complex is nonpure.

**2. Explicit acyclic discrete-Morse matching.** Start with all nonempty faces unmatched. For each cell index \(v=0,1,\ldots,35\), in that order, match every currently unmatched face \(F\) omitting \(v\) with \(F\cup\{v\}\), provided both are unmatched at the start of that iteration. Never match the empty face. Each face is removed as soon as matched. This procedure makes exactly 1,402 face–coface pairs and leaves one critical vertex, 49 critical two-simplices, and 200 critical three-simplices. To certify the crucial acyclicity hypothesis, orient each matched incidence from the face to the coface and every other codimension-one incidence from the coface to the face. All 10,368 incidences are constructed explicitly; a topological sort visits all 3,054 nonempty faces, hence the matching is acyclic. Discrete Morse theory supplies a homotopy-equivalent CW complex with precisely these critical cells, and no one-cells or cells above dimension three.

**3. Signed Morse attaching matrix.** Orient simplices by ascending cell index. The sign of deleting cell \(v\) is \((-1)^j\), where \(j\) is its zero-based position in the ascending ordered simplex. For a matched pair consisting of a two-simplex \(F\) and a three-simplex \(U\), the incidence is a unit \(\varepsilon\in\{\pm1\}\). Eliminating \(F\) replaces its two-chain class by

\[
-\varepsilon\sum_{E\subset U,\ E\ne F,\ |E|=3}[U:E]\,[E].
\]

Iterating the substitution along the directed acyclic matching gives a well-defined integral vector for every two-simplex in the 49 critical two-simplices. Summing the signed vectors of the four faces of each of the 200 critical three-simplices gives the full integral Morse boundary matrix \(B\), of size \(49\times200\). The verifier reconstructs all coefficients directly and counts 8,547 zeros, 627 positive units, 593 negative units, 16 entries equal to two, and 17 equal to negative two.

Integer unimodular row/column elimination exhibits 37 pivots equal to \(\pm1\), after which the entire \(12\times163\) remaining submatrix is identically zero. The code checks the complete zero residual (not merely an estimated rank) and that the pivots are units. Hence the integral attaching map, in suitable homotopy bases, consists of 37 identity degrees followed by zero maps.

**4. Upgrade to the homotopy type.** The Morse CW complex has a single zero-cell, no one-cells, 49 two-cells, and 200 three-cells. Its two-skeleton is \(\bigvee^{49}S^2\). Because this space is simply connected, \(\pi_2\cong H_2\cong\mathbb Z^{49}\), and each three-cell attaching map is completely determined up to homotopy by its signed integral degree vector. Changing bases by unimodular matrices corresponds to homotopy self-equivalences of wedges of two-spheres and handle-slides of the three-cells. The 37 unit columns therefore cancel 37 two-/three-cell pairs. The other 163 three-cells attach by nullhomotopic maps to the 12 surviving two-spheres, yielding

\[
K(S_3)\simeq\bigvee^{12} S^2\vee\bigvee^{163} S^3.
\]

This step uses the explicit absence of one-cells and the integral unit pivots; rational homology or a partial finite census would not alone imply the claimed homotopy type.

## Verification

Run `python3 verify.py` (Python 3.9 or later, standard library only). `verification_output.txt` contains the recorded output. The executable reconstructs the six-element group law, exhaustively enumerates faces, checks maximal faces, validates every Morse pair, constructs and topologically sorts the *entire* directed face-incidence graph, computes every signed Morse-boundary entry, performs the integer unit elimination, and independently calculates the ranks \((35,325,863,216)\) of the original simplicial boundary matrices modulo two. It returns `VERIFY_OK` only after every asserted condition succeeds. These original-boundary ranks also imply mod-two Betti numbers 12 and 163 in dimensions two and three; the integer unit calculation excludes torsion.

The Euler characteristic provides a secondary check: \(36-360+1200-1242+216=-150=1+12-163\).

## Relationship to prior work

Paige's 1951 complete-mapping theorem and Wanless's 2002 and 2007 Latin-transversal work study the existence, nonexistence, and distribution of transversals in group tables. These results motivate the order-six example but do not themselves yield its attaching degrees or integral homotopy type. A Latin trade space considered by Hämäläinen (2009) has *trades* as vertices and intersection-based simplices, rather than individual cells with distinct rows, columns, and symbols; the constructions are not the same. Likewise, the ordinary chessboard complex ignores symbol collisions. The partial-transversal complex of the *cyclic* group of order six is a distinct object and its homotopy cannot be substituted for that of the nonabelian group.

## Limitations

The classification is for the full partial-transversal complex of this particular finite group only; no assertion is made for other Latin squares, quasigroups, or all order-six isotopy types. Computation is exact and finite, with its acyclicity and integer cancellation certified by a fully reproducible program, but there is no independent scientific audit of the computation. Bibliographic comparison cannot eliminate the possibility of an unindexed equivalent result under different terminology. The earliest relevant public work examined is older than the available day-precise dating evidence; the separately recorded day-precise reference date does not assert priority for this result.

## References

1. L. J. Paige, *Complete mappings of finite groups*, Pacific Journal of Mathematics **1** (1951), 111–116; https://msp.org/pjm/1951/1-1/pjm-v1-n1-p11-p.pdf (original article; month-level date evidence only).
2. I. M. Wanless, *A Generalisation of Transversals for Latin Squares*, Electronic Journal of Combinatorics **9** (2002), R12, published 2002-03-18; https://www.combinatorics.org/ojs/index.php/eljc/article/view/v9i1r12.
3. I. M. Wanless, *Transversals in Latin Squares*, Quasigroups and Related Systems **15** (2007), 169–190; open author manuscript at https://arxiv.org/pdf/0903.5142 (submitted 2009-03-30).
4. C. Hämäläinen, *Latin trades and simplicial complexes*, arXiv:0907.1481v1 (2009-07-09), https://arxiv.org/html/0907.1481v1.
