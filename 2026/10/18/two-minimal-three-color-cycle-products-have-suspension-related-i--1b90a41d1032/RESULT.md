# Two minimal three-color cycle products have suspension-related integral homotopy types

## Finding

Let \(G_m=C_m\times K_3\) denote the categorical (tensor, direct) graph product and let \(X_m=\operatorname{Ind}(G_m)\) be its ordinary independence complex. For the two cycle lengths \(m\in\{7,8\}\),
\[
X_7\simeq S^3\vee\bigvee^{3}S^4,
\qquad
X_8\simeq S^4\vee\bigvee^{3}S^5.
\]
Consequently there is an abstract pointed homotopy equivalence \(X_8\simeq\Sigma X_7\). In particular, the reduced integral homology of \(X_7\) is \(\mathbb Z\) in degree three and \(\mathbb Z^3\) in degree four, whereas that of \(X_8\) is \(\mathbb Z\) in degree four and \(\mathbb Z^3\) in degree five, with all other reduced groups zero. Both complexes have torsion-free integral homology. The suspension equivalence is an existence statement derived from their homotopy types; no natural graph-induced suspension map is asserted.

## Assumptions and scope

For \(m\in\{7,8\}\), define the simple graph \(G_m\) on vertices \(v_{i,a}\), where \(i\in\mathbb Z/m\mathbb Z\) and \(a\in\{0,1,2\}\). The distinct vertices \(v_{i,a}\) and \(v_{j,b}\) are adjacent precisely when \(j-i\equiv\pm1\pmod m\) and \(a\ne b\). A face of \(X_m\) is a nonempty independent vertex set; the empty face is included in standard augmented chain conventions but is not a CW cell in the matching computation. The claim concerns exactly these two cycle lengths at three colors, not arbitrary cycle products or a uniform recurrence in the number of colors.

## Proof

Index the vertices by the integers \(3i+a\) from zero to \(3m-1\). A face is represented by its corresponding nonzero integer bitmask. Exhaustive recursion, always considering the least eligible vertex next and removing its neighbors when it is included, generates each independent set once. The exact totals are **5,281** nonempty faces for \(m=7\), and **18,721** for \(m=8\). In dimensions starting at zero, their respective face vectors are
\[
(21,168,658,1365,1554,1022,402,84,7)
\]
and
\[
(24,228,1112,3042,4848,4652,2880,1305,472,132,24,2).
\]

Construct a matching on each face poset as follows. Use the explicit permutation of all vertex indices given in `check_morse.py` under the key for the corresponding cycle length. For each vertex \(v\), inspect the currently unmatched faces \(\sigma\) not containing \(v\). Whenever both \(\sigma\) and \(\sigma\cup\{v\}\) are still unmatched, pair them and remove both from further matching consideration. As the two faces in a pair differ by exactly one vertex, this is a matching on cover relations in the face poset, with no repeated face. This deterministic construction makes **2,638** pairs for \(m=7\) and **9,358** pairs for \(m=8\). The unmatched critical cells have dimensions \((0,3,4,4,4)\) and \((0,4,5,5,5)\), respectively.

Acyclicity is not presumed from the choice of toggles. The verifier explicitly builds the entire cover-relation Hasse digraph, orients every unmatched incidence downward and every matched incidence upward, and checks all faces are removed by a topological sort. It confirms **5,281 of 5,281** and **18,721 of 18,721** faces in this sort. Thus there are no directed cycles and Forman's discrete-Morse theorem gives a homotopy-equivalent CW complex with exactly the critical cells listed above.

The only potentially nonzero positive-dimensional cellular differential is from the three higher critical cells to the unique lower positive-dimensional critical cell. To calculate its signed integer coefficients, orient each original simplex by the increasing vertex indices. For a lower matched face \(\tau\subset\eta\) with upper partner \(\eta\), let \(\epsilon(\tau,\eta)\in\{+1,-1\}\) be the oriented incidence. Define the projection \(P(\tau)\) to critical faces of the same dimension by
\[
P(\tau)=-\epsilon(\tau,\eta)
\sum_{\substack{\tau'\subset\eta,\ \dim\tau'=\dim\tau\\\tau'\ne\tau}}
\epsilon(\tau',\eta)P(\tau').
\]
For a critical face its projection is itself, and for a face matched as an upper face its projection is zero. The acyclic matching guarantees recursion terminates, and no nonunit division occurs. Applying \(P\) to every oriented boundary of a critical upper cell, `check_morse.py` calculates the **entire Morse differential over \(\mathbb Z\)** as the zero \(1\times3\) matrix for each \(m\). Independent integer chain-unit cancellation in `check_chain.py` yields the same critical ranks and zero surviving differentials.

For each cycle length, the Morse CW model has one zero-cell, one cell in dimension \(d=m-4\ge3\), and three cells in dimension \(d+1\), with no other cells. The \(d\)-skeleton is \(S^d\). Each \((d+1)\)-cell attaches by a map \(S^d\to S^d\), whose degree is its cellular boundary coefficient, here zero. Such a map is nullhomotopic because \(\pi_d(S^d)\cong\mathbb Z\) by degree when \(d\ge2\). Therefore the three higher cells split as wedged \((d+1)\)-spheres, yielding \(X_m\simeq S^d\vee\bigvee^3S^{d+1}\). Substituting \(m=7,8\) proves the finding and the suspension equivalence.

## Verification

Using only Python's standard library, execute `python3 check_morse.py` and `python3 check_chain.py`. Their exact outputs are embedded as `morse_output.txt` and `chain_output.txt`. The first independently enumerates each face, checks all toggle matching pairs, tests the full gradient orientation for cycles, and computes every signed integral gradient-path boundary. The second separately enumerates the two graph complexes, constructs their signed boundary matrices, and performs integral unit-coefficient chain cancellations until no units remain. Both reproduce the claimed ranks. The full computation is finite and exhaustive for the stated graphs, not a sampled experiment or extrapolation to larger graphs.

## Relationship to prior work

Antolín Camarena and Carnero Bravo (arXiv:2307.12401, first public July 23, 2023), Theorem 23 and Question 24, study exactly these categorical products. They establish severe restrictions on the possible homology degrees and allow sphere and Moore-space summands, explicitly naming both \(C_7\times K_3\) and \(C_8\times K_3\) as examples with nontrivial free homology in two consecutive degrees. That observation does **not** determine the multiplicities, eliminate additional integral torsion, or provide the exact homotopy equivalences proved here. Their question whether these products are always torsion-free motivates a finite answer for the first two named three-color examples. An existing published computation of \(\operatorname{Ind}(C_7\times K_4)\) has different color count and does not imply the two cases here; no monotonic or suspension theorem across color counts is assumed. The 2025 paper *On independence complexes of graph products* studies products with path factors, not the two stated cycle-times-complete-graph complexes.

## Limitations

These are exact finite classifications, not an all-parameter resolution of the torsion-freeness question, nor evidence of a natural suspension map. An earlier paper explicitly reported nontrivial free homology in both relevant dimensions, so that qualitative observation is not new. The added information is the full integral torsion-free homotopy type for each of the two particular examples and their abstract suspension relation. An unpublished computation or unindexed equivalent source may exist.

## References

- O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401, first public 2023-07-23, Theorem 23 and Question 24. https://arxiv.org/html/2307.12401v2
- A. Carnero Bravo, *On independence complexes of graph products*, arXiv:2505.06457, first public 2025-05-09, Section 3 on products with path factors. https://arxiv.org/html/2505.06457v2
- *A torsion-free mixed-dimensional sphere wedge for the seven-cycle categorical product with four colors*, published published-finding corpus record, 2026-10-11 (different three-versus-four-color parameter). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-torsion-free-mixed-dimensional-sphere-wedge-for-the-seven-cycl--50b8be4e4c8f
