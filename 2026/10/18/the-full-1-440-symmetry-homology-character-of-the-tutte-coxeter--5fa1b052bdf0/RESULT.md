# The full 1,440-symmetry homology character of the Tutte–Coxeter independence complex

## Finding

Let \(T\) be the Tutte–Coxeter graph in its canonical six-letter duad–syntheme model and set \(X=\operatorname{Ind}(T)\). Its full graph-automorphism group \(G=\operatorname{Aut}(T)\) has order \(1440\). The known nonequivariant homotopy equivalence \(X\simeq\bigvee^9 S^8\) implies that the only nonzero reduced rational homology of \(X\) occurs in degree \(8\) and has dimension \(9\).

**The new conclusion is the full rational homology character of all \(1440\) automorphisms.** On the canonical, color-preserving \(S_6\) subgroup,
\[
\widetilde H_8(X;\mathbb Q)\big|_{S_6}\cong S^{(2,2,1,1)}\cong S^{(4,2)}\otimes\operatorname{sgn},
\qquad
\chi(\sigma)=\operatorname{sgn}(\sigma)\bigl(f_2(\sigma)-f_1(\sigma)\bigr),
\]
where \(f_1(\sigma)\) counts fixed letters and \(f_2(\sigma)\) counts setwise fixed duads (unordered pairs) of the six letters. If \(f\) is the number of fixed letters and \(t\) the number of \(2\)-cycles, then \(f_2=\binom{f}{2}+t\).

The character values on the eleven \(S_6\) classes, in cycle-type order, are:

| Cycle type on six letters | Character |
| --- | ---: |
| \((1^6)\) | \(9\) |
| \((2,1^4)\) | \(-3\) |
| \((2^2,1^2)\) | \(1\) |
| \((2^3)\) | \(-3\) |
| \((3,1^3)\) | \(0\) |
| \((3,2,1)\) | \(0\) |
| \((3^2)\) | \(0\) |
| \((4,1^2)\) | \(1\) |
| \((4,2)\) | \(1\) |
| \((5,1)\) | \(-1\) |
| \((6)\) | \(0\) |

The remaining \(720\) automorphisms interchange the duad and syntheme classes. Their exact character is:

| Permutation cycle type on all 30 graph vertices | Number of elements | Character |
| --- | ---: | ---: |
| \((2^{15})\) | \(36\) | \(-1\) |
| \((4^6,2^3)\) | \(180\) | \(-1\) |
| \((8^3,4,2)\) | \(360\) | \(+1\) |
| \((10^3)\) | \(144\) | \(-1\) |

Hence a color-swapping involution acts with \(4\) positive and \(5\) negative eigenvalues on \(\widetilde H_8(X;\mathbb Q)\). The complete \(G\)-module is irreducible over \(\mathbb C\), since its restriction to \(S_6\) is already irreducible.

## Assumptions and scope

Fix \(\Omega=\{0,1,2,3,4,5\}\). A **duad** is a two-element subset of \(\Omega\); a **syntheme** is a partition of \(\Omega\) into three duads. There are \(15\) of each. The vertex classes of \(T\) are the duads and synthemes; adjacency means containment of a duad in a syntheme. Thus \(T\) is a \(30\)-vertex cubic bipartite graph with \(45\) edges. The independence complex \(X\) contains precisely the vertex subsets spanning no graph edge. All homology representations in the finding use characteristic zero. A cycle type stated for an outer automorphism refers to its permutation of the \(30\) graph vertices, not to an arbitrary identification of the outer coset with a six-letter permutation class.

## Proof

**1. Full automorphism group.** A bipartition-preserving graph automorphism sends the duad class to itself. Two duads share a syntheme neighbor if and only if they are disjoint subsets of \(\Omega\), so the induced action preserves the Kneser graph \(KG(6,2)\). Its automorphism group is \(S_6\): the only intersecting families of five duads are the six stars of all pairs containing a fixed letter (a direct \(2\)-subset Erdős–Ko–Rado argument). Thus the induced action permutes these stars, hence the six letters. The action on synthemes is uniquely determined by duad incidence. Every letter permutation gives such an automorphism, so this subgroup has exactly \(720\) elements.

The verifier gives an explicit color-interchanging order-two graph automorphism \(d\). Numbering duads lexicographically by \(0,\ldots,14\), followed by the lexicographically sorted synthemes numbered \(15,\ldots,29\), its image array is

`[15,22,20,28,24,27,25,19,23,16,26,18,21,29,17,0,9,14,11,7,2,12,1,8,4,6,10,5,3,13]`.

The code checks bijectivity, \(d^2=1\), bipartition exchange, and preservation of all \(45\) edges. Every automorphism either preserves or swaps the two color classes; the latter coset is \(dS_6\). Hence \(|G|=1440\) exactly.

**2. Topological premise, independently verified.** The checker builds every nonempty independent face as a \(30\)-bit mask. Its face vector in dimensions \(0\) through \(14\) is
\[
(30,390,2890,13515,41736,86610,120690,111225,66090,24948,6420,1370,240,30,2).
\]
It constructs the element-toggle discrete-Morse matching in increasing vertex order, with exactly \(238088\) matched cover pairs, one critical vertex and nine critical eight-dimensional cells. Rather than infer acyclicity from counts, it orients all \(3461400\) nonempty-face Hasse covers downward except the matched edges upward and topologically sorts the entire directed graph. All \(476186\) faces are processed, proving there is no directed cycle. Forman's theorem yields a CW model with exactly one \(0\)-cell and nine \(8\)-cells. Since all intervening skeleta are a point, all attaching maps are constant and \(X\simeq\bigvee^9 S^8\). This checks the published homotopy premise without claiming it as a new result.

**3. Exact equivariant Lefschetz formula.** Fix any automorphism \(g\in G\), viewed as a permutation of the \(30\) vertices. Decompose that permutation into disjoint cycles. A cycle is **eligible** if its vertex set contains no edge of \(T\). Form a conflict graph \(C_g\) on eligible cycles, joining two if any edge of \(T\) runs between them. A \(g\)-invariant independent face of \(T\) is exactly a union of cycles corresponding to an independent set \(S\) in \(C_g\). Each selected cycle of length \(\ell\) changes the orientation of its vertex wedge by \((-1)^{\ell-1}\). On reduced simplicial chains, the resulting signed alternating contribution for \(S\), including the empty face in degree \(-1\), is \((-1)^{|S|+1}\). Thus the reduced Lefschetz trace is
\[
L_{\mathrm{red}}(g)=-\sum_{S\in\operatorname{Ind}(C_g)}(-1)^{|S|}.
\]
Because all reduced homology is concentrated in even degree \(8\), this is precisely \(\operatorname{tr}(g\mid\widetilde H_8(X;\mathbb Q))\). The finite sum is evaluated exactly by the independence-polynomial deletion recurrence, memoized on the graph's vertex mask. No homology-basis selection or floating-point arithmetic is used.

**4. Complete character computation.** For each of the \(720\) permutations \(\sigma\) of \(\Omega\), the checker constructs its induced action on duads and synthemes, verifies every incidence edge, and computes the Lefschetz trace from the independent-cycle recursion in Step 3. On every one of these \(720\) elements, it separately verifies the closed formula \(\operatorname{sgn}(\sigma)(f_2(\sigma)-f_1(\sigma))\). The resulting values and eleven class counts are exhaustively checked. The squared-character sum is \(\sum_{\sigma\in S_6}\chi(\sigma)^2=720\), so the character is irreducible over \(\mathbb C\).

The familiar degree-\(15\) permutation module on duads contains the degree-\(6\) letter permutation module via the injective equivariant map sending a letter to the sum of the five duads that contain it (injectivity follows because \(a_i+a_j=0\) for every pair forces all coefficients to vanish). Its degree-\(9\) quotient has character \(f_2-f_1\) and is the standard \(S^{(4,2)}\) Specht module; applying the sign twist gives \(S^{(2,2,1,1)}\), as claimed.

For each of the same \(720\) letter permutations, the checker additionally composes with the explicit color-exchanging involution \(d\), verifies the resulting automorphism, computes the signed Lefschetz trace, and classifies its permutation-cycle type on all \(30\) vertices. Every color-exchanging element lies in exactly one of the four rows of the table; within each row all traces agree. The four counts sum to \(720\), covering the whole coset. A color-exchanging involution has trace \(-1\) on a \(9\)-dimensional vector space, hence \(4\) eigenvalues \(+1\) and \(5\) eigenvalues \(-1\).

## Verification

Run `python verify.py` with Python \(3\); only the standard library is needed. The program rebuilds graph incidence from the six-letter definitions, checks all graph automorphisms, enumerates every independent face, verifies the complete acyclic matching using all Hasse covers, and evaluates the exact signed character on all \(1440\) group elements. It also checks every stated character equality, each outer-cycle-class count, and the squared character norm. The expected final output markers are `INTEGRAL_MORSE_OK`, `S6_IRREDUCIBLE_OK`, and `VERIFY_OK`. The verifier was run successfully against the independently staged source code. Exhaustive computations here are finite proofs for the specified \(30\)-vertex complex; they are not extrapolations to general incidence graphs.

## Relationship to prior work

Linusson, Shareshian, and Welker classify the homotopy type of the no-perfect-matching complex \(\mathrm{NPM}_6\), a natural Alexander-dual object for the duad–syntheme incidence construction. Their Theorem 1.12 determines an \(S_5\)-restricted homology representation; their Conjecture 1.13 asks for a full \(S_6\)-module identification, and their Question 1.14 asks a broader representation question. Their inspected paper does not compute the present \(1440\)-element incidence-graph automorphism character, particularly the bipartition-interchanging coset.

Tsukuda's incidence-graph/Alexander-duality theorem describes a general homotopy relationship but its available abstract does not supply the exceptional outer-automorphism action; the full text could not be obtained for direct inspection, so its precise equivariant consequences remain a bibliographic risk. The existing exact Tutte–Coxeter independence-complex calculation already proves \(X\simeq\bigvee^9 S^8\); that conclusion and the nine-dimensional Betti number are **not** asserted new. The separate published \(S_6\) computation for the scale-three graph-metric Vietoris–Rips complex concerns \(\widetilde H_3\) of a different, \(256\)-dimensional space, and therefore does not determine the degree-eight representation here. Classical expositions of the Tutte–Coxeter outer automorphism determine the graph symmetry group, not its action on independence-complex homology. The contribution here is the complete top-homology character, including the previously unaddressed bipartition-swapping automorphisms and explicit irreducibility.

## Limitations

The result concerns rational or characteristic-zero representations; no integral lattice isomorphism or modular decomposition is asserted. It uses the already known nonequivariant homotopy type as a premise, also independently reconstructed by a finite exact certificate. The displayed outer character is indexed by permutation cycle types on the \(30\)-vertex graph rather than by an abstract character-table label for \(\operatorname{Aut}(S_6)\). An equivalent character calculation in unindexed or inaccessible sources may have been missed, and the full text of Tsukuda's paper was inaccessible; these are genuine originality limitations. No family-wide theorem is claimed.

## References

1. S. Linusson, J. Shareshian, V. Welker, *Complexes of graphs with bounded matching size*, arXiv:math/0410345, first public 2004-10-15; relevant Theorem 1.1, Corollary 1.2, Theorem 1.12, Conjecture 1.13, Question 1.14. https://www.mathematik.uni-marburg.de/~welker/preprints/lsw.pdf
2. S. Tsukuda, *Independence complexes and incidence graphs*, Contributions to Discrete Mathematics 12(1) (2017), DOI:10.55016/ojs/cdm.v12i1.62277. https://cdm.ucalgary.ca/article/view/62277
3. *The Tutte–Coxeter independence complex is a wedge of nine eight-spheres*, published technical result, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-tutte-coxeter-independence-complex-is-a-wedge-of-nine-eight--374e87ce82da
4. *The natural \(S_6\)-homology representation of the scale-three Tutte–Coxeter Vietoris–Rips complex*, published technical result, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-natural-s-6-homology-representation-of-the-scale-three-tutte--df31ab97e550
5. J. Baez, *The Tutte–Coxeter Graph*, American Mathematical Society blog, 2015-08-15. https://blogs.ams.org/visualinsight/2015/08/15/tutte-coxeter-graph/
