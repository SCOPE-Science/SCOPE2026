# The half-exchange graph of minimum dominating sets of the seven-cube

## Finding
Let \(Q_7\) be the graph on binary words of length seven, with edges joining words that differ in one coordinate. Let \(\mathcal D\) be its family of minimum dominating vertex sets. For an integer \(t\geq1\), join distinct \(A,B\in\mathcal D\) when \(|A\setminus B|=|B\setminus A|\leq t\). The following assertions hold.

1. Every minimum dominating set has size \(16\) and is an efficient dominating set; there are exactly \(240\) such sets.
2. No two distinct minimum sets share more than eight vertices. Consequently the reconfiguration graph has no edges for \(t\leq7\).
3. At \(t=8\), the reconfiguration graph has \(240\) vertices, \(1680\) edges, and is connected, vertex-transitive, fourteen-regular, and triangle-free. Its radius and diameter both equal \(4\).
4. From **each** vertex the shortest-path distance spheres have sizes \((1,14,63,106,56)\) at distances \(0,1,2,3,4\), respectively.

Thus half of the sixteen selected vertices must sometimes move simultaneously, but any two minimum dominating sets can be connected by at most four such half-exchanges; the four-step bound is attained. The classical classification of perfect length-seven binary codes, and the minimum possible nonempty perfect-code bitrade size, are prior facts. The retained contribution is the complete exchange-graph geometry, especially its uniform distance profile and diameter.

## Assumptions and scope
All graphs are finite, undirected, and simple. A dominating set \(D\) contains or neighbors every vertex. Its size is minimum if it is as small as possible. A dominating set is **efficient** if every vertex is contained in exactly one closed neighborhood of a member of \(D\). The term half-exchange refers only to replacing eight selected vertices by eight unselected vertices at once; intermediate subsets within a single exchange need not dominate. A reconfiguration edge preserves minimum domination at both endpoints. Binary words are encoded in the verification programs by integers \(0\) through \(127\), with bit \(i\) recording coordinate \(i\) for \(0\leq i\leq6\). The main classification is for \(Q_7\), not for general hypercubes.

## Proof
**Minimum size and equality.** Each vertex of \(Q_7\) has a closed neighborhood of size eight. To cover all \(128\) vertices, any dominating set has at least \(16\) members. The binary Hamming \([7,4,3]\) code, obtained by taking words whose parity-check syndrome vanishes for columns \(1,\ldots,7\), contains sixteen words with pairwise distance at least three. Its closed neighborhoods are disjoint and cover the cube. Hence the domination number is \(16\), and any minimum dominating set must have its sixteen closed neighborhoods partition the cube, so is efficient.

**Exhaustive structural description.** Translate an efficient sixteen-set \(D\) by one of its members so that the zero word belongs to it. No other word of weight one or two can belong to the translated set. Each of the \(21\) weight-two words must be covered by one of the weight-three codewords. A weight-three codeword covers precisely three weight-two words, so exactly seven weight-three words occur, and their supports cover each pair of coordinates exactly once: a Steiner triple system \(\operatorname{STS}(7)\). These seven triples are the lines of a Fano plane.

The \(28\) weight-three words not in the code must each be covered by a selected weight-four word, because selected weight-two words are forbidden. Every selected weight-four word is adjacent to four weight-three words. Moreover, the weight-four word cannot contain any selected weight-three line, or the efficient closed neighborhoods would intersect. Precisely seven four-subsets contain no Fano line: the complements of the seven lines. Therefore all seven complements are forced into the code. At this point the selected set has fifteen words (zero, seven triples, seven complements). The seven weight-six cube vertices still require coverage, and the one remaining selected word must be the all-one word; no word of weight at most six covers all seven weight-six vertices. Thus each code containing zero is uniquely determined by its Fano plane and equals the linear sixteen-word Hamming code associated to that plane.

There are exactly \(30\) labelled Steiner triple systems on seven fixed points: any such system is isomorphic to the Fano plane, whose coordinate-permutation stabilizer has order \(168\), so \(7!/168=30\). This count is also directly reproduced by the independent exact-cover enumerator. Each associated linear code has eight distinct translates (cosets) in the \(128\)-element binary group. Different underlying linear subspaces cannot have the same affine translate. Consequently \(|\mathcal D|=30\cdot8=240\).

**First possible exchange.** Every member of \(\mathcal D\) is an affine four-dimensional binary subspace of the seven-dimensional binary space. Two distinct affine four-flats have intersection either empty or an affine space of dimension at most three, hence at most eight common vertices. An exchange between two distinct sixteen-sets therefore replaces at least eight vertices. The enumeration below exhibits exchanges replacing exactly eight.

**Complete finite exchange analysis.** The accompanying exact-cover program lists all seven-triple pair partitions, constructs the corresponding sixteen-word subspaces, and forms all their translates. It verifies perfect closed-neighborhood coverage separately for each of the 240 resulting sets. Two such sets are joined exactly if their intersection has eight members. It examines all \(\binom{240}{2}=28680\) unordered pairs and obtains intersection multiplicities \(12600,7680,6720,1680\) for intersection sizes \(0,2,4,8\), respectively. These four values exhaust all pairs. Therefore the eight-exchange graph has \(1680\) edges. Each of its vertices has fourteen neighbors.

The program then performs breadth-first search starting at **every** vertex, not merely one selected vertex. It confirms that all 240 vertices are reached, with distance counts \((1,14,63,106,56)\) for every start. Its explicit count of common adjacent pairs is zero, proving triangle-freeness. The second standalone verifier constructs all codes instead by independently permuting the seven parity-check columns and translating the resulting subspaces. It compares all 240 code lists, the 1680-edge list, all pair intersections, and all 240 distance profiles to the first certificate. Thus the finite graph properties, including radius and diameter \(4\), follow from exhaustive reproducible integer operations over a domain proven complete by the structural reduction.

**Vertex transitivity.** Every labelled Fano-plane structure is obtained from every other by a coordinate permutation, and every coset is obtained by a cube translation. These are automorphisms of \(Q_7\), and they act transitively on \(\mathcal D\). They preserve intersections, hence act transitively on vertices of the exchange graph.

## Verification
Run the two standard-library Python 3 programs from the directory containing all files:

```sh
python3 verify_steiner.py certificate.json
python3 verify_permutation.py certificate.json
```

The first program constructs the sorted certificate deterministically and overwrites `certificate.json`; the second regenerates all 240 configurations independently and validates the certificate and distance spheres. Both emit the identical certificate SHA-256 digest `c781514e90db3505a668f3b39a284e8072605fb2d9967fa9504a7b913b21d89d`. Saved expected outputs are `steiner.log` and `permutation.log`. The certificate explicitly contains the 240 codeword lists and all 1680 exchange edges. All graph properties are checked as integer assertions; no heuristic graph-isomorphism software is needed. The two implementations use different generation methods (pair exact cover versus parity-check permutations). No probabilistic tests are used.

## Relationship to prior work
Perfect binary one-error-correcting codes, Hamming parity-check constructions, and their Fano-plane connection are classical. Östergård and Weakley classified small optimal binary covering codes up to equivalence. Malyugin studied coordinate-component switches for perfect codes, especially length fifteen. Potapov studied perfect colorings and lower bounds on components/bitrades, while subsequent work on Hamming graph bitrades explains why nontrivial trades have a minimum size. These results cover foundations such as the sixteen-codeword optimum, the familiar classification by Fano structures, and minimum switch support; those are not presented here as new. The exact 240-state half-exchange graph, its common distance spheres and sharp diameter are the specific additional assertions.

## Limitations
This is a complete **finite** result for \(Q_7\). It does not imply any analogous diameter in higher-dimensional cubes or uniqueness of such a reconfiguration structure among graphs. The exchange notion permits a simultaneous eight-vertex substitution without requiring feasible intermediate subsets. Earlier switching and covering-code studies are substantial, and unindexed or inaccessible detailed tables could already contain some exchange-graph statistics. Scientific publication priority and independent external validation are not certified by the finite computation itself.

## References
1. I. J. Dejter, “Symmetry of factors of the 7-cube Hamming shell,” *Journal of Combinatorial Designs* 5 (1997), 301–309, DOI: 10.1002/(SICI)1520-6610(1997)5:4<301::AID-JCD5>3.0.CO;2-J (online first-publication metadata dated 1998-12-07).
2. P. R. J. Östergård and W. D. Weakley, “Classification of binary covering codes,” *Journal of Combinatorial Designs* 8 (2000), 391–401, DOI: 10.1002/1520-6610(2000)8:6<391::AID-JCD1>3.0.CO;2-R.
3. S. A. Malyugin, “On enumeration of the perfect binary codes of length 15,” *Discrete Applied Mathematics* 135 (2004), 161–181, DOI: 10.1016/S0166-218X(02)00303-7.
4. V. N. Potapov, “On perfect 2-colorings of the q-ary n-cube,” arXiv:1104.1293, first submitted 2011-04-07, *Discrete Mathematics* 312 (2012), 1269–1272.
5. A. Valyuzhenich, “Eigenfunctions and minimum 1-perfect bitrades in the Hamming graph,” arXiv:2003.01571, first submitted 2020-03-03, *Discrete Mathematics* 344 (2021), article 112228.
