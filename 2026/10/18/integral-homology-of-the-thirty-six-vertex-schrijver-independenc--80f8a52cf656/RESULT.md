# Integral homology of the thirty-six-vertex Schrijver independence complex

## Finding
Let \(G=SG_{5,2}\) be the stable Kneser (Schrijver) graph on the thirty-six cyclically stable five-subsets of a twelve-element cycle, with two vertices adjacent when their five-subsets are disjoint. Its independence complex has reduced integral homology
\[
\widetilde H_i(\operatorname{Ind}(G);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{6},&i=6,\\
\mathbb Z^{2},&i=8,\\
0,&\text{otherwise}.
\end{cases}
\]
More strongly, it is homotopy equivalent to a CW complex consisting of one point, six six-dimensional cells, and two eight-dimensional cells. Consequently it is five-connected. **The attaching maps of the eight-cells have not been classified**; this is not a claim that the complex is a wedge of spheres.

## Assumptions and scope
Write \(C=\{0,1,\ldots,11\}\) with consecutive residues modulo twelve. A five-subset \(A\subset C\) is *stable* if it contains no cyclically consecutive pair. Let \(A_0,\ldots,A_{35}\) be the thirty-six stable five-subsets ordered lexicographically, and connect \(A_i\) to \(A_j\) exactly when \(A_i\cap A_j=\varnothing\). Then \(\operatorname{Ind}(G)\) consists of collections of pairwise-intersecting stable five-subsets. This statement concerns that one exact finite simplicial complex, not all Schrijver graphs, not its open-neighborhood complex, and not an equivariant representation.

## Proof
**Complete face enumeration.** Encode every face \(F\) by the integer \(\sum_{i\in F}2^i\). Let \(N[i]\) be the bit mask containing vertex \(i\) and its graph neighbors. Beginning from the full vertex mask, a recursion records the currently chosen face and then, for each available vertex in increasing order, recurses with that vertex included and all its closed neighbors excluded. This generates each independent set once, because its selected vertices must occur in strictly increasing order. The total is exactly **1,519,600** faces counting the empty face. As an independent enumeration check, the recurrence
\[
P_T(t)=P_{T\setminus\{v\}}(t)+tP_{T\setminus N[v]}(t),\quad P_\varnothing(t)=1
\]
for the independence polynomial of the induced vertex set \(T\) gives coefficients, indexed by face cardinality zero through fifteen,
\[
(1,36,540,4476,22941,77256,177884,288696,338652,292700,188196,89484,30586,7092,996,64).
\]

**Explicit acyclic matching.** Process graph-vertex indices in the following fixed order (zero-based lexicographic labeling):
```
1,3,4,6,7,8,10,11,12,13,16,18,19,21,22,23,25,26,27,28,31,32,33,34,
0,2,5,9,14,15,17,20,24,29,30,35
```
For each index \(v\), among faces not already matched, pair every \(F\) avoiding \(v\) with \(F\cup\{v\}\) whenever both are still unmatched. Remove all pairs for that pass simultaneously. The rule defines **759,796** disjoint cover-relation pairs on the augmented face poset, leaving precisely these eight face masks:
```
446791680,6722945024,11045175296,11950113312,
19549913088,23636475904,25849593856,47857696768
```
Six have cardinality seven, and two have cardinality nine. The empty face is paired with the singleton corresponding to index one. An ordinary face-poset Morse matching can instead leave that singleton critical; this produces one critical vertex and does not introduce a cycle.

**Acyclicity certificate.** Orient every codimension-one face incidence from higher face to lower face, reversing each matched incidence to point upward. Compute the indegree of every one of the **1,519,600** faces and topologically sort this directed graph with Kahn's algorithm. The standalone verifier visits **all 1,519,600 nodes**, across **12,264,696** codimension-one incidences. Thus there is no directed cycle, and the listed matching is acyclic, with the incidence graph checked exhaustively rather than sampled. For the ordinary matching obtained by freeing the empty face and its singleton, the empty face is a sink after edge reversal and cannot participate in a directed cycle, proving its restriction to nonempty faces is also acyclic.

**Topological conclusion.** Forman's discrete Morse theorem yields a CW model with one zero-cell, six six-cells and two eight-cells, and no other cells. Every cellular boundary map is therefore zero, even over the integers. Its reduced integral homology is exactly the displayed pair of free groups. Since the CW model has no positive-dimensional cells below degree six, it is five-connected. This argument makes no assertion about unstable attaching maps from seven-spheres into the six-skeleton.

## Verification
The included `verify.py` is self-contained and uses only the Python standard library. Run `python verify.py` from the extracted package directory. It independently checks the face-count polynomial by deletion–closed-neighborhood recurrence, enumerates all independent faces, reconstructs the stated disjoint matching, verifies the eight critical masks and their dimensions, and topologically sorts the complete oriented incidence graph. It exits with an assertion failure on any discrepancy; its reported PASS was obtained by executing the included file.

## Relationship to prior work
Braun's *Independence Complexes of Stable Kneser Graphs* (arXiv:0912.0720v1, made public 2009-12-03) defines the exact stable Kneser family and explicitly describes the homotopy types of \(\operatorname{Ind}(SG_{n,2})\) as unknown in its Introduction, while treating the family \(SG_{2,k}\) and the distinct auxiliary graphs \(E_{2n+2}\). Braun and Zeckner (arXiv:1102.1984v1) concern the **neighborhood complex**, not this independent-set complex. Published work on \(SG_{4,2}\) supplies a homotopy type for a different, twenty-five-vertex case and does not imply the present thirty-six-vertex calculation. Feng and Wang (arXiv:2404.10566v1) study independence complexes of **ordinary** Kneser graphs, not this induced stable Kneser graph. No previously verified source in those comparisons states the claimed exact integral homology of \(SG_{5,2}\).

## Limitations
The homology result is exhaustive for this finite graph, not an infinite-parameter theorem or a complete homotopy-type classification. In particular, the potential attaching-map information between the six- and eight-dimensional cells has not been computed; rational or integral homology alone cannot establish a sphere wedge. The verification requires memory sufficient to enumerate 1,519,600 face masks and directed incidence degrees. Literature comparisons reduce but do not eliminate the risk of an unindexed earlier computation.

## References
- B. Braun, *Independence Complexes of Stable Kneser Graphs*, arXiv:0912.0720v1 (2009), https://arxiv.org/abs/0912.0720 ; published in *Electronic Journal of Combinatorics* 18 (2011), #P118, Theorems 1.4–1.5 and Section 4.
- B. Braun and M. Zeckner, *Deformation Retracts of Neighborhood Complexes of Stable Kneser Graphs*, arXiv:1102.1984v1 (2011), https://arxiv.org/abs/1102.1984 .
- Z. Feng and G. Wang, *Exploring Homological Properties of Independent Complexes of Kneser Graphs*, arXiv:2404.10566v1 (2024), https://arxiv.org/abs/2404.10566 .
- R. Forman, *Morse theory for cell complexes*, *Advances in Mathematics* 134 (1998), 90–145.
