# Exact eleven-petal local-rigidity census
## Finding
Consider eleven-petal words in the convention of Vernitski, with cyclic rotation of positions identified. There are
\[
10!=3{,}628{,}800
\]
such words. Exactly \(393{,}410\) admit no trivial petal deletion \(\mathsf T^-\), exactly \(1{,}971{,}006\) admit no crossing exchange \(\mathsf X\), and exactly \(325{,}398\) admit neither move.

Call a word *dihedrally locally rigid* if every word in its orbit under the height rotation \(\mathsf R\) and half-turn \(\mathsf S\) admits neither \(\mathsf T^-\) nor \(\mathsf X\). Exactly \(270{,}630\) eleven-petal words are dihedrally locally rigid. They form exactly \(12{,}786\) \(\langle\mathsf R,\mathsf S\rangle\)-orbits, with orbit-size distribution
\[
8\text{ orbits of size }1,\qquad
954\text{ orbits of size }11,\qquad
11{,}824\text{ orbits of size }22.
\]

## Assumptions and scope
A petal word is a cyclic permutation of the heights \(0,1,\ldots,10\), and one representative is chosen by rotating positions so that \(0\) is first. The moves \(\mathsf T^-\), \(\mathsf X\), \(\mathsf R\), and \(\mathsf S\) are exactly those in Sections 3.1--3.4 of Vernitski's preprint.

The claim is a finite combinatorial census. It does not classify the knot type represented by any eleven-petal word, and it does not assert that any of the counted words is a hard unknot. Dihedral local rigidity is only a local obstruction to simplification inside the fixed-petal layer.

## Proof
Every cyclic class of an eleven-letter permutation has a unique representative beginning with \(0\). Thus exhaustive enumeration of permutations of \(1,\ldots,10\) visits each eleven-petal word exactly once.

For \(\mathsf T^-\), the source criterion is exact: the move applies precisely when two cyclically adjacent letters are consecutive integers \(m,m+1\). Testing all eleven cyclic adjacencies therefore decides \(\mathsf T^-\)-applicability.

For \(\mathsf X\), fix each of the eleven possible basepoint positions \(b\). The remaining ten positions split into five cyclically consecutive pairs. For every \(m\) and \(w\) with \(w\ge m+2\), the verifier checks whether two of these pairs have endpoint sets
\[
\{m,w+1\}\quad\text{and}\quad\{m+1,w\},
\]
and then checks the published nesting condition: every other pair is either contained in or disjoint from \([m+2,w-1]\). This exhausts exactly the source definition of a crossing exchange.

The first pass over all \(10!\) normalized words gives the three local counts. For the stronger count, the verifier applies the source formulas
\[
\mathsf R(p_0,\ldots,p_{10})=(p_0+1,\ldots,p_{10}+1)\pmod {11}
\]
and
\[
\mathsf S(p_0,\ldots,p_{10})=(10-p_{10},\ldots,10-p_0),
\]
renormalizing by cyclic position rotation after each operation. It generates the full dihedral orbit and retains an orbit exactly when every member fails both local moves. Orbit-stabilizer then allows only sizes dividing \(22\), and direct enumeration gives the stated \(1\), \(11\), and \(22\) strata. The identity
\[
8+954\cdot11+11{,}824\cdot22=270{,}630
\]
checks the word total against the orbit decomposition.

## Verification
Compile and run `artifacts/petal11_verify.cpp` with a C++17 compiler, for example:

`g++ -O3 -std=c++17 artifacts/petal11_verify.cpp -o petal11_verify && ./petal11_verify`

A successful replay prints:

`VERIFY_OK total=3628800 no_Tminus=393410 no_X=1971006 local_rigid=325398 dihedrally_local_rigid_words=270630 dihedral_orbits=12786 orbit_sizes=1:8,11:954,22:11824`

The verifier also checks the published seven-petal crossing-exchange example and verifies that the three named nine-petal hard representatives in the source admit neither local move. The finite enumeration is exhaustive for eleven-petal words and is not used to claim anything about knot type.

## Relationship to prior work
Vernitski exhaustively classifies petal words only through \(N=9\), where the paper identifies \(108\) hard unknot words. Its computation section states that the reported table stops at \(N=9\), while the only eleven-petal statement there is a random move-preservation test. The paper explicitly asks how common hard diagrams are for larger \(N\). The present census addresses the first combinatorial filter at the next odd size \(N=11\): it counts all words on which the simplifying local moves are absent, and then counts the subset for which this remains true throughout the natural dihedral symmetry orbit.

Colton, Glover, Hughes, and Sandberg define trivial petal moves and crossing exchanges and prove their Reidemeister-type completeness theorem, but do not give an eleven-petal enumeration or a local-rigidity census.

Two earlier calculations on Vernitski's preprint concern shortest move distances for two named nine-petal words and the dihedral quotient of the capped move component of a third named nine-petal word. Neither calculation counts the global eleven-petal word space, and neither implies the counts above.

## Limitations
Local rigidity is not the same as hardness. A counted word may represent a nontrivial knot, and even a locally rigid unknot may interact with moves after increasing the petal number. No eleven-petal knot-type census is claimed. The result also does not give an asymptotic density as the petal number grows.

The originality comparison covers the inspected primary papers, targeted searches for the exact counts and equivalent local-rigidity formulations, and the available prior calculations. An unindexed independent enumeration remains a residual risk.

## References
1. A. Vernitski, *Some petal diagrams of the unknot are hard*, arXiv:2610.01596v1, 2026.
2. L. Colton, C. Glover, M. Hughes, S. Sandberg, *A Reidemeister type theorem for petal diagrams of knots*, arXiv:1812.08930v1; *Topology and its Applications* 267 (2019), 106896.
