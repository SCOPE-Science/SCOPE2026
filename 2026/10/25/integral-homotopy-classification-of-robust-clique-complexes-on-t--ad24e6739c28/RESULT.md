# Integral homotopy classification of robust clique complexes on the \(4\times4\) grid

## Finding

Let \(G=P_4\square P_4\) be the Cartesian grid graph with sixteen vertices. For the robust clique complex
\[
\mathsf{Cliq}_k(G)=\{W\subseteq V(G):\alpha(G[W])<k\},\qquad k\ge2,
\]
the following are homotopy equivalences of geometric realizations over the integers:
\[
|\mathsf{Cliq}_k(G)|\simeq\bigvee^{b_k}S^{2k-3},\quad
(b_2,b_3,b_4,b_5,b_6,b_7,b_8)=(9,36,84,122,102,29,1).
\]
For every \(k\ge9\), the complex is the full simplex and is contractible. The new content is the integral homotopy decomposition for \(k=4,5,6,7\); neither the numerical Betti ranks nor the smaller parameters are claimed as new.

## Assumptions and scope

The vertices are labeled by pairs \((i,j)\in\{0,1,2,3\}^2\), with an edge exactly when their Manhattan distance equals one. The bit index of \((i,j)\) is \(4i+j\). For any induced graph, \(\alpha\) is its maximum independent-set cardinality. Faces may have any size, including the empty face; the discrete-Morse face poset omits only the empty face. The theorem concerns this single, specified graph for **every integer** \(k\ge2\), and integral homotopy equivalence, not merely field homology or a numerical Euler characteristic.

## Proof

**Exact face generation.** Let \(N[v]\) denote the closed neighborhood of vertex \(v\). For every vertex mask \(S\ne\varnothing\), take the least-indexed \(v\in S\). The exact recurrence
\[
\alpha(S)=\max\bigl(\alpha(S\setminus\{v\}),\;1+\alpha(S\setminus N[v])\bigr),\qquad\alpha(\varnothing)=0,
\]
follows by separating independent sets that omit or contain \(v\). Every smaller mask is evaluated before the larger mask, so this integer recurrence enumerates the complete \(2^{16}\)-element power set, with no search cutoff. A second face-recognition implementation first enumerates independent subsets by direct adjacency tests, then uses a subset-zeta sweep to mark all supersets of each independent \(k\)-set; it agrees on all masks, for each \(2\le k\le8\), with the predicate \(\alpha(S)\ge k\). The full graph has independence number eight.

**A specified finite Morse matching.** Fix any one of \(k=2,3,4,5,6,7,8\), and start with all nonempty faces of \(\mathsf{Cliq}_k(G)\) unmatched. Visit the sixteen vertices in the fixed order \(0,1,\dots,15\). At vertex \(v\), pair every still-unmatched face \(S\) that omits \(v\) to \(S\cup\{v\}\) when the latter also remains unmatched; then delete both from further stages. At any one stage, these pairs are disjoint, because each upper face contains \(v\) and has one uniquely determined lower face with \(v\) removed. Thus the construction gives a legitimate face-poset matching. It can be reproduced completely from `verify_grid4_robust.py` using only Python's standard library.

**Acyclicity and critical-cell counts.** For each of the seven complexes, enumerate every nonempty face and every codimension-one inclusion \(S\subset T\), excluding the empty face. Orient each incidence from \(T\) to \(S\), except that the matched incidences are reversed. A complete indegree-based topological sort removes **every** face, proving that the entire directed Hasse graph has no directed cycle. This independently verifies acyclicity, not simply an alternating-sum constraint. The exact face counts, paired-face counts, critical degrees and critical multiplicities are:

| \(k\) | Nonempty faces | Matched pairs | Critical cell dimensions and multiplicities |
| ---: | ---: | ---: | --- |
| 2 | 40 | 15 | one zero-cell; nine one-cells |
| 3 | 635 | 299 | one zero-cell; 36 three-cells |
| 4 | 4,811 | 2,363 | one zero-cell; 84 five-cells |
| 5 | 19,305 | 9,591 | one zero-cell; 122 seven-cells |
| 6 | 43,309 | 21,603 | one zero-cell; 102 nine-cells |
| 7 | 60,532 | 30,251 | one zero-cell; 29 eleven-cells |
| 8 | 65,024 | 32,511 | one zero-cell; one thirteen-cell |

The exact directed-Hasse incidence totals are respectively \(48,1952,21992,114644,305904,469316,518144\), and every topological-sort traversal exhausts the corresponding face set. These are exhaustive finite certificate facts, not samples. They can be checked anew from the included source, rather than trusted as unexplained log values.

**Passage to homotopy type.** Forman's acyclic matching theorem (also stated as Theorem 7.2 in Bayer et al. [2]) provides a CW complex with exactly the unmatched cells. Since the only critical cells are one zero-cell and cells all in one strictly positive dimension \(2k-3\), their attaching maps have a point as target, so this CW complex is precisely a wedge of that many spheres of the asserted dimension. This is an integral homotopy assertion. When \(k\ge9\), the maximum independent-set size eight makes every subset a face, producing a contractible fifteen-simplex.

## Verification

With Python 3, in the same directory as the supplied file, execute `python3 verify_grid4_robust.py`. The program terminates successfully only after comparing both exact face predicates on all masks, verifying each claimed critical-cell distribution and full directed-Hasse acyclicity, and checking the reduced Euler characteristics. Its final line is `VERIFY_OK`. The accompanying `MORSE_LOG.txt` records an actual completed run. The executable finite exhaustion, together with the cited discrete-Morse theorem, supplies the proof; the log alone is not a proof.

## Relationship to prior work

Filakovský [1], Theorem 1, already proves the wedge-of-spheres assertion for all rectangular grids at \(k=2,3\); its Corollary 3 covers all \(k\) for edge-gluing-only square sequences, but the full grid here has a square-attachment structure involving corners. Its Conjecture 5 asks for the wedge-of-spheres description across square-sequence graphs for higher parameters. The present theorem verifies this conjectured conclusion for this natural grid at all its parameters, including the four previously unresolved interior levels \(k=4,5,6,7\).

Bayer et al. [2], Table 3, **already report exactly** the relevant Betti numbers \(84,122,102,29\) for the total cut complexes of the \(4\times4\) grid. Alexander duality explains the corresponding robust-clique numerical ranks, but **does not by itself imply the claimed unstable integral homotopy types**. The 2022 work also mentions using lexicographic sequences of Morse element matchings for its tabulated data; it does not publish the specific perfect critical-cell certificates needed here or state these homotopy equivalences. The new contribution is therefore the explicit acyclic perfect matchings and resulting homotopy classifications, not a recomputation of the table's numbers. Chandrakar et al. [3] focus their principal grid homotopy results on two-row and three-row families, rather than the present higher-parameter four-row case.

## Limitations

This is a finite, exactly reproducible classification of one canonical grid, not a proof of Filakovský's conjecture for arbitrary square-sequence graphs or larger grids. The computational certificate is a mathematical finite exhaustion and depends on the correctness of the supplied transparent integer operations and standard discrete-Morse theorem. No independent mathematical audit has been performed. Older work's explicit mention of Morse computations leaves a residual priority risk that analogous unpublished matching certificates could exist; the published Betti numbers are not new.

## References

[1] Marek Filakovský, *The Topology of \(k\)-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365, first publicly submitted February 11, 2026, especially Theorem 1, Corollary 3, Conjecture 5, and Example 10. https://arxiv.org/abs/2602.11365

[2] Margaret Bayer, Mark Denker, Marija Jelić Milutinović, Rowan Rowlands, Sheila Sundaram, and Lei Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503, initially submitted September 27, 2022; version 2 (January 30, 2024), Table 3 (page 22) and Appendix Theorems 7.2 and 7.5. https://arxiv.org/abs/2209.13503

[3] Himanshu Chandrakar, Nisith Ranjan Hazra, Debotosh Rout, and Anurag Singh, *Topology of Total Cut and Cut Complexes of Grid Graphs*, arXiv:2408.07646, initially submitted August 14, 2024. https://arxiv.org/abs/2408.07646
