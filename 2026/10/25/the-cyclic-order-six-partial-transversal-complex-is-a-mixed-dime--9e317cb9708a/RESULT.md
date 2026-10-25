# The cyclic order-six partial-transversal complex is a mixed-dimensional sphere wedge

## Finding
For the cyclic Latin square of order six, the simplicial complex \(\mathcal T_6\) of its partial transversals has the exact homotopy type
\[
\mathcal T_6\simeq\left(\bigvee^{14}S^2\right)\vee\left(\bigvee^{75}S^3\right).
\]
In particular its reduced integral homology is free of rank \(14\) in degree \(2\), free of rank \(75\) in degree \(3\), and zero otherwise. This is a statement about the *homotopy type*, not just the Betti numbers.

## Assumptions and scope
Fix \(\mathbb Z/6\mathbb Z=\{0,1,2,3,4,5\}\). The Latin square is \(L_{r,c}=r+c\pmod6\). Its \(36\) cells are indexed by \(v=6r+c\) in \(\{0,\ldots,35\}\). A set of cells is a face of \(\mathcal T_6\) if no two have the same row, column, or symbol \(r+c\pmod6\). We include the empty face as usual, but count only nonempty faces in all enumerations. All homotopy spaces are geometric realizations. No assertion is made for other squares or orders.

There can be no complete transversal: a hypothetical six-cell face would contain every row, column and symbol once. Its sum of symbols would be both \(\sum_{s=0}^{5}s\equiv3\pmod6\) and \(\sum_{r=0}^{5}r+\sum_{c=0}^{5}c\equiv0\pmod6\), contradiction. A five-cell face exists by the explicit enumeration below.

## Proof
**Step 1: Exhaustive face model.** Process rows \(r=0,\ldots,5\). At each row either choose no cell, or choose one column not previously used such that \(r+c\pmod6\) has not appeared previously. Induction on the processed rows proves this gives each face *exactly once*: every face has at most one cell per row, and the two masks enforce precisely the other compatibility requirements. The resulting face counts by cardinality \(1,\ldots,6\) are
\[
(36,360,1200,1224,288,0).
\]
Thus there are exactly \(3108\) nonempty simplices and their total Euler characteristic is \(-60\).

**Step 2: Explicit acyclic matching.** Encode every nonempty face as its 36-bit vertex mask. In the following order of cell indices, repeatedly pair any currently unpaired face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\), provided both are still unpaired:

`22,26,7,34,3,15,19,24,1,5,33,14,13,32,8,10,29,23,4,20,2,18,28,35,27,30,25,16,0,11,17,31,12,9,21,6`.

The procedure creates \(1500\) disjoint codimension-one matching pairs. Its remaining critical faces are one vertex, \(23\) triangles (dimension \(2\)), and \(84\) tetrahedra (dimension \(3\)). Acyclicity is **checked rather than presumed**: orient matched codimension-one incidences upward, all other incidences downward. There are \(10656\) directed incidences and a complete Kahn topological-sort removes all \(3108\) vertices, proving the directed Hasse graph has no cycle. Therefore the complex has a Morse CW model with precisely these cells; in particular its one-skeleton has one vertex and no edges.

**Step 3: Exact integral attaching matrix.** Order vertices increasingly and give faces increasing-vertex orientation. Write \(\partial[v_0,\ldots,v_k]=\sum_i(-1)^i[v_0,\ldots,\widehat{v_i},\ldots,v_k]\). Each noncritical dimension-two face \(t\) matched upward with a dimension-three face \(u\) is recursively replaced by \(-\epsilon\sum_{f\subset u,\ f\ne t}[u:f]P(f)\), where \(\epsilon=[u:t]\in\{\pm1\}\) and \(P(f)\) is the already determined projection of the other dimension-two face; matched-upper dimension-two faces project to zero, and critical dimension-two faces to their own basis elements. Acyclicity guarantees termination. Apply this projection to the ordinary oriented boundary of each critical three-face. This constructs an *exact integer* \(23\times84\) Morse boundary matrix \(B\). Its \(327\) nonzero entries have absolute value at most \(3\). Complete integer row and column Euclidean reductions (all unimodular) put \(B\) into Smith form
\[
\operatorname{diag}(\underbrace{1,\ldots,1}_{9},0,\ldots,0).
\]
The included standalone verification program reconstructs every face, pair, orientation, Morse coefficient and integer elementary operation from the original 36-cell definition; no external numerical logs or undisclosed intermediate data are needed.

**Step 4: From the Morse CW complex to homotopy.** The Morse complex has one zero-cell, no one-cells, \(23\) two-cells and \(84\) three-cells. Hence its two-skeleton is \(\bigvee^{23}S^2\). The attaching maps of three-cells belong to \(\pi_2(\bigvee^{23}S^2)\cong\mathbb Z^{23}\), so they are *completely* determined by their integral degree vectors, namely the columns of \(B\). Integral invertible row changes are realized by homotopy self-equivalences of the wedge of two-spheres and integral invertible column changes by changing the three-cell attaching generators. With nine unit pivots the resulting CW complex cancels nine two-cell/three-cell pairs; 14 two-spheres and 75 three-spheres remain. Thus the displayed homotopy equivalence follows.

## Verification
Run `python3 verify.py` using Python 3.9+ and only its standard library. The checker independently enumerates all faces, confirms the \(1500\) pairs and \(10656\) incidences, checks the complete directed acyclicity test, constructs the exact Morse matrix and performs unimodular integer diagonalization. Its success marker is `VERIFY_OK`, with counts and degrees printed. No probabilistic or floating-point steps occur. The code is a finite proof of this *one* specified complex, not an extrapolation to all cyclic Latin squares.

## Relationship to prior work
Wanless's 2002 paper [1] treats transversals and plexes, including Cayley tables and obstructions to their existence; the 2018 work [2] treats covers and maximal partial transversals. Neither source's inspected conclusions provides an integral homotopy classification for the complex of *all* partial transversals of this cyclic square. By contrast, Cioabă and Mim [3] compute homology of the **clique complex** of the Latin square graph that joins cells sharing a row, column or symbol. Here the same graph's **independence complex**, equivalently the clique complex of its complement, is used: the two homotopy functors are not interchangeable. Searches for cyclic order-six rainbow-matching, partial-transversal and Latin-square-graph independence complexes identified no covering homotopy statement; this is evidence from a bounded search, not an exhaustive uniqueness proof.

## Limitations
This finite calculation determines the homotopy type for exactly the cyclic group table of order six; it does not provide an infinite-family formula, equivariant homology, or homotopy maps under inclusions. The originality assessment depends on accessible indexed and inspected sources and may miss an unindexed equivalent statement. The proof and verification are self-review; independent scientific validation has not been performed.

## References
[1] I. M. Wanless, *A Generalisation of Transversals for Latin Squares*, Electronic Journal of Combinatorics **9** (2002), #R12, https://doi.org/10.37236/1629 (first public date 2002-03-18).

[2] D. Best, T. Marbach, R. J. Stones and I. M. Wanless, *Covers and partial transversals of Latin squares*, Designs, Codes and Cryptography (2018), https://doi.org/10.1007/s10623-018-0499-9.

[3] S. M. Cioabă and M. Mim, *On the homology groups of clique complexes of strongly regular graphs*, arXiv:2606.27328 (2026), https://arxiv.org/abs/2606.27328.
