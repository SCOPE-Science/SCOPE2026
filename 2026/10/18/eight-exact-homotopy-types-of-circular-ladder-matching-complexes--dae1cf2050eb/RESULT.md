# The ten-rung circular-ladder matching complex is a wedge of forty six-spheres

## Finding

For the circular ladder \(P_{10}=C_{10}\square K_2\), its ordinary matching complex satisfies
\[
\mathcal M(P_{10})\simeq\bigvee^{40}S^6.
\]
In particular it is 5-connected, but not 6-connected. The exact type advances the initial classification of the ordinary circular-ladder matching complex from the covered range \(3\le n\le9\) to the next order. Because the smaller types have nonzero reduced integral homology in degree at most five [2, 3], this is the first circular ladder (among simple cycles, \(n\ge3\)) whose matching complex is 5-connected. No novelty is claimed for those smaller types.

## Assumptions and scope

A simplicial vertex is a graph edge; a face is any set of mutually vertex-disjoint graph edges, with no required extendibility to a perfect matching. The two rims are simple ten-cycles on \(0,\ldots,9\) and \(10,\ldots,19\), with rungs \(\{i,10+i\}\) for \(0\le i<10\). Homotopy is integral, with neither localization nor equivariance. The new exact calculation is only for ten rungs.

## Finite certificate and proof

Sort the 30 graph edges lexicographically by their ordered endpoint pair (smaller endpoint first), with indices \(0,\ldots,29\). Process the indices in order \(20,21,\ldots,29,0,1,\ldots,19\). Start with every face, including the empty face, unmatched. At each index \(i\), pair each available face \(F\) not containing \(i\) with \(F\cup\{i\}\) whenever both are available. Within this stage the pairs are disjoint. Delete the empty face and its pair, leaving its former partner as an unmatched vertex.

The resulting matching on the nonempty face poset is acyclic, by the following argument. Orient matched covers up and others down. In a directed cycle, up and down steps must be equally numerous, and successive up steps are impossible because matched pairs are disjoint. Thus the cycle alternates. Let \(i\) be the processing index of the earliest matched stage used on that cycle. A step adding \(i\) must be balanced by a step removing \(i\). Both faces of that downward step would have been available at stage \(i\), because every face in the cycle is incident to a matched up step used at stage \(i\) or later. The two faces would therefore have been paired at stage \(i\), contradicting the downward orientation. Dropping the empty-face pair does not invalidate the argument for the nonempty poset: the former partner is unmatched and cannot be in an alternating directed cycle.

For reproducibility, the face and matching count can be obtained by the following exact procedure, using bitsets of graph-edge indices. Start with \(L=[0]\). Scan the thirty edges in index order. For the current edge append \(F\cup\{i\}\) for each face in the list **before** this iteration that uses no endpoint of edge \(i\). The new face has largest index \(i\), so is unique; induction proves that this lists all faces. Form the set of live faces from \(L\), then delete the two live faces of each pair in the stated stages. The counts are:

| Quantity | Count |
|:--|--:|
| All faces, including the empty face | 117,732 |
| Cover incidences in the nonempty face poset | 714,010 |
| Matched covers in the nonempty face poset | 58,845 |
| Unmatched vertices | 1 |
| Unmatched six-dimensional faces | 40 |
| Other unmatched faces | 0 |

Discrete Morse theory gives a homotopy-equivalent CW complex with these unmatched cells. There are no positive-dimensional cells below dimension six, so every six-cell attaches to the unique vertex. This proves the claimed wedge without needing any arithmetic test of a boundary matrix as a substitute for the attaching-map argument.

## Reproduction and literature

Run the accompanying `python3 verify_prism.py` and inspect the `n 10` row. It reconstructs all faces, recomputes this matching, checks acyclicity directly and counts every unmatched face, and performs an independent mod-two homology check. Its smaller rows are context and redundant checks, not new claims here. The decisive evidence for the integral homotopy type is the acyclic matching and the dimensions of its critical cells.

The general ordinary matching-complex problem for circular ladders is identified in [1, Problem 26]. Neither the independence complex of the ladder nor its perfect matching complex determines the ordinary matching complex; the ordinary one is the independence complex of the **line graph**. Open-grid estimates address different graphs [4]. The covered exact types through nine rungs [2, 3] include mixed-dimensional cases and do not force the critical cell dimensions or sphere multiplicity at ten rungs. This finite certificate gives a test for proposed general formulas; it does not assert a recurrence.

1. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, [arXiv:2608.30601v2](https://arxiv.org/abs/2608.30601v2), §6.
2. [*Initial integral homotopy types of circular-ladder matching complexes*](https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-initial-integral-homotopy-types-of-circular-ladder-matching-comp--94cb26be0034/RESULT.md), Finding.
3. [*Twist-sensitive five-sphere wedges in nine-rung cubic ladder matching complexes*](https://github.com/Resultary/2026/blob/main/2026/11/17/SCOPE-twist-sensitive-five-sphere-wedges-in-nine-rung-cubic-ladder-mat--217ee7d98ffe/RESULT.md), Finding (untwisted case).
4. B. Braun and W. K. Hough, *Matching and Independence Complexes Related to Small Grids*, [arXiv:1606.01204](https://arxiv.org/abs/1606.01204).
