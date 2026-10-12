# Three relabeling orbits of minimum total dominating sets in \(J(6,3)\)

## Finding
Let \(J(6,3)\) have the \(20\) triples of \([6]=\{1,2,3,4,5,6\}\) as vertices, adjacent when they share exactly two elements. A total dominating set \(D\) is a family of triples such that each of the \(20\) triples has a **different** member of \(D\) meeting it in exactly two elements (including when the triple itself belongs to \(D\)).

**Theorem (complete relabeling classification).** The smallest possible size of \(D\) is \(4\). There are exactly \(765\) minimum total dominating sets. Under the natural relabeling action of \(\mathfrak S_6\), they form exactly three orbits with the following representatives and sizes:

\[
\begin{array}{c|c|c}
\text{representative (triples)}&\text{orbit size}&\text{stabilizer order}\\\hline
\{123,235,245,456\}&360&2\\
\{124,125,236,346\}&360&2\\
\{146,156,234,235\}&45&16
\end{array}
\]

These orbits are distinguished by their multiset of intersections between the six unordered pairs of selected triples: respectively \(\{0,1,1,2,2,2\}\), \(\{0,1,1,1,2,2\}\), and \(\{0,0,1,1,2,2\}\). The total number is \(360+360+45=765\).

## Assumptions and scope
The graph is exactly \(J(6,3)\), with \(20\) *labeled* vertices indexed by three-element subsets of the six-element ground set. The group defining equivalence is precisely the relabeling group \(\mathfrak S_6\); no claim is made about different Johnson parameters. All total domination tests use **open** neighborhoods, not closed neighborhoods. This theorem refines the scalar minimum-size question by classifying every optimizer under the natural group action.

## Proof
The proof is a finite exhaustive classification with small, explicit search spaces. It is fully reproducible from `j63_orbit_verify.py` supplied below; the validity of the finite exhaustion follows from the next three assertions about its loops.

1. The script creates the \(\binom63=20\) triples in lexicographic order. For each such triple it constructs the open-neighborhood bit mask by directly testing cardinality-two intersection with every *other* triple. Its predicate `dominates(indices)` returns true exactly when **every** of these \(20\) masks has nonempty intersection with the mask of selected triples. Thus it implements the mathematical definition of total domination, without an optimization library or precomputed graph data.
2. The loops over `combinations(range(20),k)` for \(k=0,1,2,3\) cover every possible set of fewer than four vertices, and none passes. The loop over `combinations(range(20),4)` visits each of the \(\binom{20}{4}=4845\) four-vertex sets *once*; exactly \(765\) satisfy total domination. Therefore the minimum equals four and the total count of minimum sets equals \(765\).
3. The script acts on each of the three displayed families by *every one* of the \(6!=720\) ground-set permutations, sorting the image triple to recover its vertex index. Deduplication yields orbit sizes \(360,360,45\). It checks pairwise disjointness and equality of their union to the complete set of \(765\) four-vertex dominating sets computed in step 2. Thus the orbits are exhaustive and disjoint. Orbit–stabilizer gives the listed stabilizer orders.

This is an exact finite proof: the search loops traverse all mathematical cases within the defined finite domain. There is no inference from samples to infinite families. The reported pair-intersection fingerprints are calculated from the representatives; they are also invariant under relabeling.

## Verification
Execute `python3 j63_orbit_verify.py` (Python 3 standard library only). The program checks all \(\sum_{k=0}^3\binom{20}{k}=1351\) possibilities of size below four, all \(4845\) possibilities of size four, and \(720\) group permutations applied independently to each of the three representatives. Assertions compare the complete winning family against the union of the proposed orbits. The output `j63_orbit_verify.out` is included; the live execution matched the file exactly.

## Relationship to prior work
Cornet, Dravec, and Torres (arXiv:2610.04675, first public October 3, 2026) determine scalar total-domination numbers for Johnson graphs including \(J(n,3)\). Their accessible abstract establishes this scope, not the optimizer count or \(\mathfrak S_6\)-orbit classification asserted here. The paper's complete text could not be inspected, so equivalent orbit results in its details remain a substantial bibliographic risk; absence from the abstract is not used as conclusive novelty evidence. Lee and Oh (arXiv:2606.10326) treat **ordinary** domination in \(J(n,3)\), a different condition. Results on total dominating sets of triangular graphs \(J(n,2)\) do not cover the triple graph \(J(6,3)\).

## Limitations
This is a finite classification of exactly one natural graph. The group is the natural ground-set permutation group, not a claimed classification for all possible graph automorphisms. The number \(765\) is not asserted to follow from a general family formula. Independent external audit and full-text exclusion of every historical equivalent have not been performed. An accessible primary-source abstract alone cannot guarantee novelty of this finite case.

## References
- M. G. Cornet, T. Dravec, P. Torres, *Domination and Total Domination in Johnson graphs*, arXiv:2610.04675 (first posted October 3, 2026), https://arxiv.org/abs/2610.04675.
- S.-a. Lee, S. Oh, *Domination in Johnson graphs \(J(n,3)\) for odd \(n\)*, arXiv:2606.10326 (June 9, 2026), https://arxiv.org/abs/2606.10326.
