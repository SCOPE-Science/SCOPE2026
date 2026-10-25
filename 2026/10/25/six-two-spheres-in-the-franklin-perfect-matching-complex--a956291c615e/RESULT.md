# Six two-spheres in the Franklin perfect-matching complex

## Finding
Let \(F\) be the twelve-vertex Franklin graph, defined by the labeled edge set below. Let \(\mathcal P(F)\) be the simplicial complex on the eighteen graph edges whose faces are precisely the edge sets extendible to perfect matchings. Then
\[
\boxed{\mathcal P(F)\simeq\bigvee^{6}S^2.}
\]
Furthermore, all matching sets of one or two graph edges extend to a perfect matching of \(F\), but exactly 72 three-edge matchings do not. Thus the ordinary matching complex \(\mathcal M(F)\) and \(\mathcal P(F)\) have identical one-skeleta but different homotopy types: the previously computed ordinary complex is \(\mathcal M(F)\simeq\bigvee^{12}S^3\), whereas the perfect-matching complex is a wedge of six two-spheres.

## Assumptions and scope
Number the graph vertices \(0,1,\ldots,11\), with residue indices modulo twelve. Include all cycle edges \(\{i,i+1\}\). For each even \(i\) include the chord \(\{i,i+5\}\); for each odd \(i\) include \(\{i,i-5\}\). Duplicate unordered edges are identified. This is the Franklin graph in LCF notation `[5,-5]^6`, also known as the six-crossed prism and the Knödel graph `W(3,12)`. It has twelve vertices and eighteen edges.

A graph matching is a set of edges with disjoint endpoints; a perfect matching covers all twelve graph vertices, hence has six graph edges. The finite simplicial complex \(\mathcal P(F)\) contains the empty face and every subset of each perfect matching. Its geometric realization is the object of the homotopy-equivalence claim. The claim is integral and nonequivariant; it is not a classification of all crossed prisms or Knödel graphs.

For reproducibility label the graph's edges \(0,1,\ldots,17\), in lexicographic order of their increasing endpoint pairs:

```
0:(0,1)   1:(0,5)   2:(0,11)  3:(1,2)   4:(1,8)   5:(2,3)
6:(2,7)   7:(3,4)   8:(3,10)  9:(4,5)  10:(4,9)  11:(5,6)
12:(6,7) 13:(6,11) 14:(7,8) 15:(8,9) 16:(9,10) 17:(10,11)
```

## Proof
First enumerate perfect matchings without omission or duplication. For any set of currently unmatched graph vertices, choose its least vertex \(u\), branch over every neighbor \(v\) still unmatched, and recurse after deleting \(u,v\). At an empty set, record the chosen six graph edges. This exhaustive recurrence identifies **exactly 17 perfect matchings**. Insert every one of their subsets into a set of graph-edge bitmasks. The resulting complex has the following numbers of nonempty faces by dimension:
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(18,117,264,243,102,17),
\]
for a total of 761 nonempty simplices.

Construct a partial matching on the nonempty face poset by processing graph-edge labels in the following fixed order:
```
16,5,17,14,7,8,6,0,12,10,15,11,2,1,9,3,13,4
```
At a label \(j\), for each still-unpaired simplex \(\sigma\) not containing \(j\) for which \(\sigma\cup\{j\}\) is also still unpaired, pair the two and remove both from subsequent consideration. Because the pair membership test uses the current unpaired set, no face is paired twice. Each pair is a genuine codimension-one face–coface incidence.

This procedure constructs 377 disjoint pairs. Precisely seven cells are critical: the vertex with graph-edge label 16, and the six two-simplices with label triples
```
(0,8,13), (1,6,8), (1,7,17), (1,10,14), (2,8,12), (3,8,12).
```
The 761 nonempty simplices have 2,610 codimension-one incidences. Direct each incidence from its higher to its lower simplex, **except** direct the 377 matched incidences upward. The supplied standalone verifier explicitly builds this finite directed graph, computes every indegree, and exhausts its vertices using Kahn's topological-sort algorithm. All 761 face vertices are removed. Therefore the directed graph is acyclic; the partial pairing is an acyclic discrete-Morse matching.

Discrete Morse theory yields a homotopy equivalent CW complex with precisely one zero-cell, six two-cells and no other cells. Every attaching map of a two-cell lands in the unique zero-cell, so this CW complex is a wedge of six copies of \(S^2\), proving the boxed homotopy equivalence. No field-homology inference is used for the homotopy conclusion.

For the extension boundary, enumerate **all** graph matchings independently by checking endpoint disjointness for each of the \(2^{18}\) graph-edge subsets. The ordinary matching-complex face counts are
\[
(18,117,336,417,186,17).
\]
The equality of the first two entries with those of \(\mathcal P(F)\) proves that every one-edge and every two-edge graph matching extends. At dimension two there are 336 ordinary matching triangles but only 264 extendible triangles, so exactly 72 distinct three-edge matchings are nonextendible; all are minimal such obstructions. This finishes the claim.

## Verification
The standalone file `verify_franklin_perfect_matching.py` requires only the Python 3 standard library. Run `python3 verify_franklin_perfect_matching.py` in its directory. It reconstructs the chord-and-cycle edge set; checks the 17 perfect matchings and both face vectors; independently enumerates all ordinary matchings; checks the 72 minimal obstructions; performs the complete 377-pair matching; verifies all 2,610 oriented incidences are acyclic; and prints the seven critical faces. A successful execution ends with `VERIFY_OK`. The recorded output in `verification_output.txt` comes from a direct execution of that packaged source.

## Relationship to prior work
The Franklin graph is a classical twelve-vertex, nonplanar cubic graph (Franklin, 1934), also called the six-crossed prism; Knödel-graph literature records the equivalent family description. Published work on the **ordinary** Franklin matching complex establishes \(\mathcal M(F)\simeq\bigvee^{12}S^3\), including its two edge-deletion/link profiles; that statement concerns all matchings and does not give the homotopy type of the strict perfect-matching subcomplex. Here the first missing simplices are the 72 three-edge matching obstructions.

Bayer, Jelić Milutinović and Vega study perfect-matching complexes of planar honeycomb patches. Chandrakar and Singh treat polygonal line tilings. Their family hypotheses do not include the nonplanar Franklin graph. Agarwal and Basak classify circular and Möbius ladder families; the twelve-vertex instances have respectively 20 and 18 perfect matchings, whereas \(F\) has 17, so neither is the graph classified here. These comparisons address exact objects and statements rather than merely dissimilar titles.

## Limitations
This is one finite graph, not an infinite-family formula, classification of embeddings or symmetry representation. The proof is a fully finite, reproducible acyclic-matching certificate coupled with the standard discrete-Morse theorem. It is not an independent formal certification. An equivalent result in unindexed or inaccessible literature remains possible. The 1934 historical graph paper is recorded with its verified **month**, not an invented exact day; the dated Knödel-graph survey of 1 March 2004 supplies the precise archive source date used in metadata.

## References
1. P. Franklin, *A Six Color Problem*, Journal of Mathematics and Physics 13 (1934), 363–369, DOI:10.1002/sapm1934131363 (first published April 1934; day not verified).
2. G. Fertin and A. Raspaud, *A survey on Knödel graphs*, Discrete Applied Mathematics 137 (2004), 173–195, DOI:10.1016/S0166-218X(03)00260-9 (publisher lists publication 1 March 2004).
3. M. Bayer, M. Jelić Milutinović and J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803 (2022), DOI:10.37236/11525.
4. H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809 (2024).
5. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601 (2026).
6. *Edge-orbit matching-complex splitting for the Franklin graph*, published mathematical finding, 11 October 2026, `https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-edge-orbit-matching-complex-splitting-for-the-franklin-graph--be4888fadcca`.
