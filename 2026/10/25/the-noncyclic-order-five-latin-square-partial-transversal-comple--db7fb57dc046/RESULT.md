# The noncyclic order-five Latin-square partial-transversal complex is a wedge of 48 two-spheres

## Finding
For a Latin square \(L\) of order five, define \(\mathcal T(L)\) to be the abstract simplicial complex with one vertex for each of the twenty-five cells of \(L\). A set of cells is a simplex exactly when no two chosen cells share a row, column, or symbol (a partial transversal). **New theorem.** If \(L\) belongs to the noncyclic order-five isotopy class (the unique class not isotopic to the addition table of \(\mathbb Z/5\mathbb Z\)), then
\[
\boxed{\mathcal T(L)\simeq\bigvee^{48}S^2.}
\]
This is a complete integral homotopy-type statement for that natural isotopy class: its fundamental group is trivial, its reduced integral second homology is \(\mathbb Z^{48}\), and all other reduced integral homology groups vanish. A separate earlier computation of the cyclic-class/Paley-25 complex already determines the cyclic case; **that case is not asserted as a new contribution here**.

## Assumptions and scope
A Latin square of order five is a matrix on five symbols, with each symbol appearing exactly once in each row and column. Two squares are **isotopic** if one is obtained from the other by independent permutations of rows, columns, and symbols. Isotopies preserve the partial-transversal simplicial complex by relabeling its vertices.

Represent the cyclic class by \(C_{r,c}=r+c\pmod 5\), for \(r,c\in\{0,1,2,3,4\}\). Represent the other class by the following rows, indexed from zero:
```
0 1 2 3 4
1 0 3 4 2
2 3 4 0 1
3 4 1 2 0
4 2 0 1 3
```
The latter square is not isotopic to the cyclic one: the cyclic representative has 15 full transversals, the latter has 3. Every permutation of rows, columns, and symbols carries simplices bijectively to simplices. The new theorem concerns only the noncyclic isotopy class; cyclic-class computations included in the verifier serve solely as consistency and context checks. Nothing is asserted about different orders or equivariant homotopy types.

## Proof
**Step 1: an exhaustive classification certificate.** Fix the first row and the first column to the order \((0,1,2,3,4)\); such Latin squares are called reduced. Backtracking over possible rows, pruning repeated symbols in any column, yields exactly 56 reduced Latin squares. For either displayed representative, iterate all \(5!\) permutations of rows and all \(5!\) permutations of columns, then normalize symbols to make the first row increasing and permute rows to make the first column increasing. The two resulting sets of reduced squares have 6 and 50 elements, have empty intersection, and their union equals all 56 reduced squares. Since every Latin square can be normalized to reduced form by an isotopy, these two representatives exhaust all order-five cases. The accompanying verifier performs and checks all these exact enumerations.

**Step 2: enumerate the noncyclic complex and construct its discrete-Morse matching.** Encode the cell in row \(r\), column \(c\) by bit \(5r+c\). Enumerate a face by adjoining the next cell only when its row, column, and symbol have not appeared. For the noncyclic representative the face vector, counting nonempty faces by cardinality, is
\[
(f_0,f_1,f_2,f_3,f_4)=(25,150,250,79,3).
\]
Including the empty face there are 508 faces. Starting with every face unmatched, process the 25 vertex bits in increasing order; match any still-unmatched face not containing the bit to its bit-adjoined coface if that coface is also unmatched, in order of face cardinality and then integer bitmask. This yields 226 pairs. The matching includes a pair involving the empty face and leaves four critical edges and 52 critical triangles; there are no other unmatched nonempty faces. Interpret the empty-face pair in the usual reduced discrete-Morse convention: the ordinary Morse CW model has one base vertex, along with the remaining critical cells.

For every face–coface incidence, orient the gradient edge from face to coface if matched and from coface to face otherwise. A full topological sort visits all 508 faces, verifying that no directed cycle exists. Thus the matching is acyclic, and Forman's discrete Morse theorem supplies a homotopy-equivalent CW model with exactly the indicated cells.

**Step 3: compute the exact integral Morse boundaries.** Orient a simplex by increasing cell-bit indices. For each cell matched upward, eliminate that cell using the signed boundary of its matched coface; matched upper cells project to zero and unmatched lower-dimensional critical cells project to themselves. The acyclic matching makes this recursive signed projection finite. Applying it to the noncyclic complex produces the integral matrix \(\partial_2^{M}:\mathbb Z^{52}\to\mathbb Z^4\). The matrix's first four columns form a four-by-four matrix of determinant \(-1\), so its image is the entire critical one-chain group. Hence reduced integral homology is concentrated in degree two with rank \(52-4=48\), without torsion.

**Step 4: check simple connectivity, then upgrade homology to homotopy.** A spanning tree of the complex's one-skeleton has 24 edges. Its 150 edges give 126 non-tree generators of the edge-path presentation of \(\pi_1\), and its 250 triangles provide the relators. The verifier repeatedly finds a triangular relator in which a remaining generator occurs exactly once, solves that relator for the generator, substitutes in all relators, and freely and cyclically reduces. For the noncyclic complex it successfully eliminates all 126 generators, leaving no nontrivial relators. Every step is a valid Tietze move, so each fundamental group is trivial. The acyclic Morse models are connected two-dimensional CW complexes and have free second homology of the stated rank. The Hurewicz theorem represents an integral homology basis by sphere maps, and the homology version of Whitehead's theorem makes the induced map from the corresponding wedge of two-spheres a homotopy equivalence. This proves the asserted noncyclic homotopy type for every square in that isotopy class.

## Verification
Run the standalone standard-library checker with `python3 verify.py`. It constructs both representatives and their Latin-square properties, enumerates all 56 reduced squares and both complete isotopy orbits, and then verifies the noncyclic 508 faces and all signed incidences, its complete acyclic matching, the integral Morse boundary and unimodular minor, and the elimination of all 126 fundamental-group generators. The verifier also computes the cyclic reference case to enable direct comparison, but its homotopy type is not a newly asserted result. The output is recorded verbatim in `verify_output.txt` and ends with `VERIFY_OK`. The verification is exhaustive for order five but does not establish results for larger orders. No independent external audit has been conducted.

## Relationship to prior work
McKay, Meynert, and Myrvold [1] classify small Latin squares and give the order-five isotopy count two and the reduced count 56; that is prior combinatorial knowledge and is not claimed as new. Work on Latin transversals, for example Aharoni, Berger, Kotlar, and Ziv [2] and the survey [3], identifies partial transversals as rainbow matchings in properly edge-colored bipartite graphs and studies their existence and size. Neither classification of isotopy classes nor counts or lower bounds for partial transversals imply the **integral homotopy type of the noncyclic class** obtained here. The ordinary chessboard complex permits at most one cell per row and column, without the third uniqueness condition on symbols, so matching-complex results for it do not imply the present noncyclic homotopy type. Indexed results for colorful assignment complexes on fewer coordinate groups concern different simplicial complexes with different vertex sets and face rules.

## Limitations
The claim is exhaustive for the noncyclic order-five isotopy class and is nonequivariant. The proof uses exact finite exhaustive computations with a fully specified replayable algorithm, rather than a uniform construction for arbitrary order. Although the listed literature and indexed comparisons did not yield a theorem covering the two stated homotopy types, equivalent older, unindexed, or inaccessible results remain a possibility. The existence of this finite certificate, and the numerical distinction between the two cases, do not by themselves establish originality; the originality assessment depends on the stated literature comparisons. No independent audit has been performed.

## References
[1] B. D. McKay, A. Meynert, W. Myrvold, *Small Latin Squares, Quasigroups and Loops*, Journal of Combinatorial Designs 15 (2007), 98–119; first published online 2006-03-02, DOI `10.1002/jcd.20105`. Lawful author full text: https://cs.anu.edu.au/people/Brendan.McKay/papers/ls_final_corr.pdf .

[2] R. Aharoni, E. Berger, D. Kotlar, R. Ziv, *On a conjecture of Stein*, first public arXiv version 2016-05-06, https://arxiv.org/abs/1605.01982 .

[3] R. Montgomery, *Transversals in Latin Squares*, survey, https://rhmontgomery.warwick.ac.uk/papers/37transversalssurvey.pdf .
