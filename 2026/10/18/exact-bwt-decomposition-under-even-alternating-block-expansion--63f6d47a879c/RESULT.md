# Exact BWT decomposition under even alternating block expansion

## Finding
For a binary circular word \(w\) containing both symbols and any integer \(h\ge2\), define the uniform alternating expansion \(\Phi_h\) by \(\Phi_h(0)=(01)^h\) and \(\Phi_h(1)=(10)^h\). For the cyclic-rotation Burrows–Wheeler transform (BWT), sorted with \(0<1\), **the number of linear maximal equal-letter runs in \(\operatorname{BWT}(\Phi_h(w))\) is independent of \(h\)**. More strongly, the entire BWT admits an explicit decomposition in which \(h\) changes only lengths of positive monochromatic padding blocks.

For a parent index \(i\) (modulo the parent length \(n\)), let \(d_i\ge1\) be the number of consecutive copies of \(w_i\) beginning at \(i\) before the next opposite symbol. For \(c\in\{0,1\}\) and \(r\ge1\), form \(L_c(r)\) by listing the symbols \(1-w_{i-1}\) for exactly those indices with \(w_i=c\) and \(d_i=r\), in the lexicographic order of the cyclic parent rotations beginning at those indices. Let \(N_c(r)\) be the length of this list, let \(R_c\) be the maximum \(d_i\) among indices with \(w_i=c\), and let \(n_c\) be the number of occurrences of \(c\) in \(w\). Then the precise string equality is

\[
\operatorname{BWT}(\Phi_h(w)) =
1^{h n_1}\left(\prod_{r=R_0}^{1} L_0(r)1^{(h-1)N_0(r)}\right)
\left(\prod_{r=1}^{R_1} 0^{(h-1)N_1(r)}L_1(r)\right)0^{h n_0}.
\]

Here a descending product means concatenate factors for \(r=R_0,R_0-1,\ldots,1\), and an ascending product means concatenate for \(r=1,2,\ldots,R_1\). Tied parent rotations may be sorted arbitrarily: identical rotations have identical preceding characters, so the strings \(L_c(r)\) are well defined. Every \(N_c(r)\) is positive in its indicated range.

## Assumptions and scope
The parent \(w\) is any nonempty finite binary *circular* word containing at least one zero and at least one one; no primitivity, aperiodicity, balance, or restriction on run lengths is required. Cyclic rotations are counted with multiplicity, and their preceding characters are read cyclically. The resulting BWT is a linear word, and its run statistic counts maximal constant blocks in that linear word, not circular runs. The integer expansion parameter obeys \(h\ge2\). The theorem does not assert invariance between \(h=1\) and \(h=2\).

## Proof
**1. First doubled letter.** In the expanded circular word \(s=\Phi_h(w)\), every code block alternates. Adjacent equal symbols occur only where consecutive parent symbols differ. For a rotation starting at offset \(t\in\{0,\ldots,2h-1\}\) in the expanded block for parent index \(i\), the first equal-adjacent pair is encountered after \(D=2h d_i-t\) symbols. In other words, positions \(D-1,D\) of that rotation (zero-indexed) are equal; all earlier adjacent positions differ. Positivity follows from \(d_i\ge1\) and \(t<2h\). The starting bit is \(w_i\) if \(t\) is even, and \(1-w_i\) if \(t\) is odd.

**2. Lexicographic order by the first defect.** Two rotations starting in the same bit each agree with the uniquely determined alternating infinite prefix up to their first doubled letter. If their first-double distances differ, the rotation with the smaller \(D\) has, at position \(D\), the opposite symbol to the continuing alternating rotation. Starting in zero, first-double distances of odd parity sort before every even distance, and among even distances larger \(D\) sorts first. Starting in one, the even distances sort first, in increasing \(D\), followed by all odd distances. This comparison is strict whenever \(D\) differs. Among equal \(D\), the starting offset modulo \(2h\) is fixed and, as the image morphism is order-preserving on aligned parent rotations (the expanded images of zero and one begin with zero and one respectively), aligned starts follow the lexicographic order of parent rotations. Ties cause no change in BWT symbols.

**3. The zero-starting half.** Odd-offset starts whose first symbol is zero necessarily occur in expanded blocks of parent ones. Every such start is preceded by a one; hence these contribute the initial \(1^{h n_1}\). The remaining zero-starts occur at even offsets in blocks of parent zeros. For any fixed \(r=d_i\), their first doubled-letter distances are \(2hr,2hr-2,\ldots,2h(r-1)+2\). The boundary-aligned starts at \(t=0\) therefore sort before all other even offsets in this layer, and the layers sort in decreasing \(r\). The preceding symbols of boundary-aligned starts are \(1-w_{i-1}\), yielding \(L_0(r)\). Every other even-offset start in a zero-parent block has preceding bit one, giving \(1^{(h-1)N_0(r)}\).

**4. The one-starting half.** Its even-offset starts are in parent-one blocks, and layers sort by increasing \(r\). For each layer, the \(h-1\) nonzero even offsets precede the boundary-aligned offset. Their preceding symbols are zero, so the layer reads \(0^{(h-1)N_1(r)}L_1(r)\). Finally, the odd-offset starts in parent-zero blocks all have predecessor zero and yield \(0^{h n_0}\). Joining the two halves proves the displayed exact BWT identity.

**5. Positive separators and run invariance.** Within every circular maximal run of symbol \(c\), the values \(d_i\) include every integer from one to that maximal run length. Since the parent contains both symbols, every \(N_c(r)>0\) for \(1\le r\le R_c\). For \(h\ge2\), each displayed padding block has strictly positive length. Replacing \(h\) by any other integer at least two changes only the *positive length* of already-present monochromatic padding runs. It never changes any boundary between adjacent nonpadding list words and separators. Consequently the run count of the entire linear BWT is independent of \(h\).

The threshold is sharp: for \(w=001\), \(\operatorname{BWT}(\Phi_1(w))=101100\) has four runs, while \(\operatorname{BWT}(\Phi_2(w))=110111010000\) has six. Thus the result is not a trivial invariance valid for all positive expansion parameters.

## Verification
The included `verify.py` independently constructs cyclic BWTs by full rotation sorting and by cyclic suffix-doubling. It checks the exact block formula and run invariance exhaustively for every mixed binary parent of lengths \(2\) through \(9\), each with \(h\in\{2,3,4\}\), for \(3012\) cases. It additionally tests \(180\) seeded larger inputs with lengths up to \(305\) and parameters \(h\in\{2,3,5\}\); larger cases use a separate cyclic doubling BWT algorithm. Finally it checks the sharp \(h=1\) example. Run with `python3 verify.py`. This finite test is independent corroboration; the proof in the preceding section establishes all lengths and all \(h\ge2\).

## Relationship to prior work
Burrows–Wheeler run minimization is a central text-indexing and compression invariant; for example, Prezza and Policriti (2015) study run-compressed-space algorithms. Brlek and collaborators (2019) compute BWTs of selected morphic families including Thue–Morse. Fici, Romana, Sciortino, and Urbina (2023) analyze morphism-dependent run sensitivity, including a distinct family \(0\mapsto 0 1^p\), \(1\mapsto 1 0^q\) with constant additive effects. The latter does not supply the present full-BWT identity for \(0\mapsto(01)^h\), \(1\mapsto(10)^h\), or the cross-\(h\) invariance for every mixed parent. Fici and collaborators (2025) develop general sensitivity bounds and bounded-additive classifications but not this exact decomposition. No general novelty claim beyond comparisons with inspected sources and indexed searches is warranted.

## Limitations
The theorem requires a mixed binary parent and \(h\ge2\). The unexpanded parent BWT may have a different run count; no claim is made of equality with it. It concerns cyclic-rotation BWT without a unique endmarker, not the sentinel BWT. Literature coverage may be incomplete, and independent mathematical review has not occurred. The code is a finite check, not an exhaustive proof of the unbounded theorem.

## References
- Prezza, N., and Policriti, A. *Computing LZ77 in Run-Compressed Space* (first public preprint, 2015-10-21), arXiv:1510.06257. https://arxiv.org/abs/1510.06257
- Brlek and collaborators, *Burrows–Wheeler transform of words defined by morphisms* (2019), full open text: https://flore.unifi.it/retrieve/e398c380-dd2e-179a-e053-3705fe0a4cff/BWT-morphism_%20Last.pdf
- Fici, G., Romana, G., Sciortino, M., and Urbina, C. *On the Impact of Morphisms on BWT-Runs* (2023), DOI:10.4230/LIPIcs.CPM.2023.10. https://drops.dagstuhl.de/storage/00lipics/lipics-vol259-cpm2023/LIPIcs.CPM.2023.10/LIPIcs.CPM.2023.10.pdf
- Fici and collaborators, *Morphisms and BWT-Run Sensitivity* (2025), DOI:10.4230/LIPIcs.MFCS.2025.49. https://drops.dagstuhl.de/storage/00lipics/lipics-vol345-mfcs2025/html/LIPIcs.MFCS.2025.49/LIPIcs.MFCS.2025.49.html
