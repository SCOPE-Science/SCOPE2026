# Seven certified circular-ladder total three-cut homotopy types

## Finding
For the circular ladder \(L_n=C_n\square K_2\), put \(X_n=\Delta_3^t(L_n)\), the total three-cut complex. For every integer \(4\le n\le10\), its complete **homotopy type** is
\[
|X_n|\simeq
\begin{cases}
\bigvee^{9}S^{2},&n=4,\\
\bigvee^{14}S^{4},&n=5,\\
\bigvee^{1+\binom{n+1}{2}}S^{2n-6},&6\le n\le10.
\end{cases}
\]
In particular these seven complexes have torsion-free reduced integral homology concentrated in degree \(2n-6\) with respective ranks \(9,14,22,29,37,46,56\). As each is pure of dimension \(2n-4\), none of the seven is shellable.

## Assumptions and scope
The graph has vertex set \(\{(j,a):j\in\mathbb Z/n\mathbb Z,\ a\in\{0,1\}\}\) and edges joining cyclic consecutive vertices within each row and the two corresponding vertices across rows. It has exactly \(2n\) vertices and \(3n\) edges. An independent triple is a three-element set of pairwise nonadjacent graph vertices. The simplicial complex \(\Delta_3^t(L_n)\) has one facet \(V(L_n)\setminus T\) for each independent triple \(T\). The theorem applies precisely to the seven integers \(n=4,5,6,7,8,9,10\); it makes no statement for larger widths, for ordinary three-cut complexes, or for arbitrary Cartesian products.

## Proof
This is a finite, complete computational proof by explicit acyclic discrete Morse matchings, with executable pseudocode supplied as the complete standard-library program `verify.py`. The program enumerates every three-element vertex subset and uses the adjacency matrix of \(L_n\) to retain exactly the independent triples; it then generates every nonempty subface of every complementary facet. Since every face is a subset of a facet, this is the complete nonempty face poset, without sampling. Each face is encoded by a \(2n\)-bit nonnegative integer.

For each \(v=0,1,\ldots,2n-1\), in this order, pair each still-unmatched face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\), provided both faces remain unmatched. Remove both from further stages. This is a matching of cover relations: every face belongs to at most one pair. The complete verifier independently constructs the directed Hasse graph of the resulting matching, orienting unmatched cover relations from larger to smaller face and reversing every paired relation. It calculates the indegree of every face using every codimension-one incidence and applies Kahn's exhaustive topological sorting algorithm. All faces are removed in all seven cases, proving the directed Hasse graph is acyclic. In particular, no assumption that a numerical search found all critical faces is used: the code constructs and inspects the full face poset.

The output consists of one critical zero-simplex and exactly \(9,14,22,29,37,46,56\) critical simplices in dimensions \(2,4,6,8,10,12,14\), respectively, with no other critical simplices. Discrete Morse theory gives a CW complex with one zero-cell and exactly that many cells, all in a single positive dimension. Every attaching map of these higher-dimensional cells has image in the unique zero-cell, so this CW complex is the displayed wedge of spheres. The argument proves homotopy equivalence, not just equality of Betti numbers.

## Verification
Execute `python3 verify.py` with Python 3 and its standard library. For \(n=4,5,6,7,8,9,10\), the exact numbers of facets are \(8,30,76,154,272,438,660\), the numbers of nonempty faces are \(134,805,3761,15906,64890,261305,1047519\), and the numbers of Morse pairs are \(62,395,1869,7938,32426,130629,523731\). The largest case independently checks all \(10{,}467{,}920\) Hasse cover incidences and obtains a full directed acyclic graph. The expected critical vectors are hard-coded for assertion, but each is recomputed solely from the graph definitions and exhaustive face enumeration. Successful output ends in `VERIFY_OK 7 complete complexes; every Hasse incidence checked`. The executable does not rely on any data file, external package, or previous calculation.

## Relationship to prior work
Chauhan, Shukla and Vinayak (2025), Section 4, Table 4, **already tabulate precisely the same integral homology groups and ranks for this seven-case subfamily** and state Conjecture 4.5 covering all circular ladders; these numerical Betti numbers are not claimed as new. Their proved Theorem 3.14 treats the total **two**-cut complex, not the total three-cut complex. The new claim here is the explicit, rigorously checked **homotopy equivalence** for the initial seven nonvoid circular-ladder cases. Homology ranks alone, even torsion-free and concentrated in one degree, do not imply a wedge-of-spheres homotopy type. Agarwal and Basak (2026), Problem 26, explicitly ask for the topology of cut and total cut complexes of Möbius and circular ladders; their theorems instead classify independence and perfect matching complexes. Bayer and collaborators (2022/2024) provide the definitions and classifications for other graph families; Carnero Bravo (2026) establishes other families and connectivity bounds, not these seven homotopy equivalences.

## Limitations
The result proves seven finite instances and does **not** prove Conjecture 4.5 for unrestricted circumference or more than two rows. The already published numerical homology entries must not be interpreted as original numerical discoveries. The proof uses finite exhaustive discrete Morse certification, not a uniform symbolic description of critical cells for all \(n\). There is no claim about equivariant homotopy, degreewise symmetry characters, or a complete general classification. Additional prior or unpublished equivalent homotopy computations are possible.

## References
1. Pratiksha Chauhan, Samir Shukla and Kumar Vinayak, *Total 2-cut complexes of powers of cycle graphs and Cartesian products of certain graphs*, arXiv:2512.04486v1 (first public 4 December 2025), especially Theorem 3.14, Table 4 and Conjecture 4.5. https://arxiv.org/abs/2512.04486
2. Anshu Agarwal and Biplab Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601 (first public 31 August 2026), Problem 26. https://arxiv.org/abs/2608.30601
3. Margaret Bayer, Mark Denker, Marija Jelić Milutinović, Rowan Rowlands, Sheila Sundaram and Lei Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503 (first public 27 September 2022), especially Definition 2.3 and discrete Morse appendix. https://arxiv.org/abs/2209.13503
4. Andrés Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427 (first public 24 February 2026). https://arxiv.org/abs/2602.21427
