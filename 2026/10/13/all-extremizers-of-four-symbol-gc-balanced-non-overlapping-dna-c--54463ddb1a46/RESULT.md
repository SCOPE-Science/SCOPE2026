# All extremizers of four-symbol GC-balanced non-overlapping DNA codes

## Finding
Fix the DNA alphabet \(\Sigma=\{\mathrm A,\mathrm T,\mathrm C,\mathrm G\}\), with \(E=\{\mathrm A,\mathrm T\}\) and \(H=\{\mathrm C,\mathrm G\}\). Every codeword has length four and contains exactly two letters of \(H\). A code is non-overlapping if a proper nonempty prefix of one codeword never equals a suffix of another codeword, including itself.

**Equality-classification theorem.** There are exactly **twelve labeled codes of maximum size**, each with twenty words. They are precisely the following codes. Choose one of the two ordered pairs \((L,R)=(E,H)\) or \((L,R)=(H,E)\), and write \(Q=L\times R\) for the four possible two-letter blocks, with concatenation understood. For any two-element subset \(P\subset Q\), put \(S=Q\setminus P\). Then

\[
C_{L,R,P}=L^2R^2\;\cup\;\{ps:p\in P,\ s\in S\},
\qquad |C_{L,R,P}|=16+4=20.
\]

All twelve codes are distinct and every maximum code is one of them. The fact that twenty is the maximum size was already addressed by the polarity-balanced small-parameter searches of Stanovnik, Moškon and Mraz (2024 preprint, 2025 article); it is *not* claimed as a new numerical optimum. The claim here is the complete equality structure, number of optimal labeled codebooks, and symmetry classification.

Let \(G\) consist of the eight alphabet permutations that either preserve the two sets \(E,H\) or exchange them. Permit in addition reversing all four-letter words simultaneously. Under this sixteen-element action, the twelve maximum codebooks form exactly two orbits, of sizes four and eight. The smaller orbit corresponds to selecting two opposite corners of the \(2\times2\) grid \(L\times R\), and the larger to selecting two cells sharing one coordinate.

## Assumptions and scope
The four symbols are individually labeled, and the two groups \(E,H\) are fixed. The balance condition is exact: each word has precisely two GC bases, not merely approximately half. There is no Hamming-distance, reverse-complement separation, homopolymer, or error-correction requirement. All overlaps of lengths one, two and three are forbidden, for every ordered pair of codewords including identical words. A code is **maximum** when its number of words is globally largest within this constrained class; it is not merely inclusion-maximal.

## Proof
**Endpoint separation and candidate bounds.** For a nonempty code \(C\), let \(L_0\) be the set of all first letters and \(R_0\) that of all last letters. Overlap length one forces \(L_0\cap R_0=\varnothing\). Let \(e_L,h_L,e_R,h_R\) denote the numbers of letters from \(E,H\) in the corresponding endpoint sets. Because the middle two positions together must contribute the remaining high-GC letters, the number of balanced four-letter words with endpoints in \(L_0\times R_0\), before other overlaps are forbidden, is

\[
N(L_0,R_0)=4(h_Lh_R+e_Le_R)+8(h_Le_R+e_Lh_R).
\]

Indeed, two middle GC letters contribute four choices, as do two middle AT letters, while one of each gives eight. The endpoints are distinct groups of actual letters, so \(|L_0|,|R_0|\ge1\) and \(|L_0|+|R_0|\le4\). Evaluating the displayed expression over the finitely many possible compositions yields maxima \(8,16,16,20,32,20\) for endpoint sizes \((1,1),(1,2),(2,1),(1,3),(2,2),(3,1)\), respectively. Thus an optimal code with twenty words could only have endpoint sizes \((1,3)\), \((3,1)\) or \((2,2)\).

If the sizes are \((1,3)\), the candidate bound twenty is attained only when the first endpoint is a letter of one GC class and the three remaining letters are allowed last endpoints. For example, with first letter A and other endpoints C,G,T, both `ACAC` and `AGAG` are balanced candidates and each has a two-letter border. Both must be discarded, leaving at most eighteen words. If the first letter is C, the forbidden balanced candidates `CACA` and `CTCT` similarly suffice; GC-class-preserving relabelings cover the other choices. Reversal handles \((3,1)\).

For endpoint sizes \((2,2)\), three compositions exist up to exchanging the two GC classes: (i) the first endpoints are exactly \(E\), the last exactly \(H\), or conversely; (ii) both endpoint sets contain one letter of each GC class. In case (ii), the candidate count is twenty-four. After relabeling within the two GC classes, take \(L_0=\{\mathrm A,\mathrm C\}\), \(R_0=\{\mathrm T,\mathrm G\}\). The self-overlapping candidates `AGAG` and `CTCT` are prohibited. Of the remaining twenty-two candidates, at least one word must be omitted from each of the following three disjoint incompatible pairs:

`AACG` / `ACGT` (overlap length three), `AAGG` / `AGGT` (overlap length three), and `ACAG` / `AGCT` (overlap length two).

Thus there can be at most \(24-2-3=19\) words. Every twenty-word code must therefore have \((L_0,R_0)=(E,H)\) or its reversal in GC-class orientation.

**Uniform endpoints and all equality cases.** Suppose \((L_0,R_0)=(L,R)=(E,H)\), or symmetrically \((H,E)\). Exact balance permits only two patterns of GC-class membership among the four positions: \(LLRR\) and \(LRLR\). There are exactly sixteen words of each pattern. Every word of pattern \(LLRR\) is compatible with every other such word and with every word of pattern \(LRLR\): their one-, two- and three-letter prefix/suffix group patterns cannot agree. Consequently an optimal code may, and for equality must, include all sixteen words of \(L^2R^2\).

Identify an \(LRLR\)-pattern word with a directed edge \(p\to s\), where its first and last two-letter blocks \(p,s\) lie in the four-element set \(Q=L\times R\). Overlap length two occurs exactly when a suffix block \(s\) is an allowed prefix block of an included alternating word. The length-one and length-three overlaps never occur within this group pattern. Thus the selected edges must have disjoint sets of initial vertices \(P\) and terminal vertices \(S\). With \(P\cap S=\varnothing\) and \(|Q|=4\), the number of edges is at most

\[
|P|\,|S|\le\left\lfloor\frac{|Q|^2}{4}\right\rfloor=4.
\]

Equality requires \(|P|=|S|=2\), \(P\cup S=Q\), and the inclusion of **all** four edges from \(P\) to \(S\). Therefore every maximum code is exactly the stated \(C_{L,R,P}\); conversely the construction has no forbidden overlap and contains twenty balanced words. There are two endpoint orientations and \(\binom42=6\) choices of \(P\) in each, giving exactly twelve distinct maximum codes.

**Symmetry.** For each fixed orientation, the four-element block grid is \(L\times R\). Its six two-element subsets split into the two diagonals and the four pairs occupying a common row or column. Independent swaps inside the two letter classes move each subset within its type. Exchanging the GC classes exchanges endpoint orientations, while global reversal sends a prefix-block choice to the transposed complementary suffix-block choice; this preserves the diagonal/adjacent distinction. The corresponding labeled orbits therefore have sizes \(2\cdot2=4\) and \(2\cdot4=8\). No other equivalences occur because these exhaust the stated action on the twelve codebooks.

## Verification
The standalone `verify.py` uses only the Python standard library. Run `python3 verify.py` from a directory containing the extracted file. It first constructs the twelve codebooks by the theorem, checks all 20-codeword sets directly against all three forbidden overlap lengths, then separately enumerates every balanced unbordered four-letter word and computes all maximum cliques in the pairwise-compatibility graph by a branch-and-bound coloring algorithm. It independently confirms that the maximal clique size is twenty, that the complete list of maximum cliques equals the twelve constructed codes, and that the allowed alphabet/reversal symmetry action has orbits of sizes four and eight.

Expected check: `VERIFY_OK: 96 balanced words; 72 unbordered words; optimum 20;` followed by `12 labeled optimal codes; two symmetry orbits of sizes 4 and 8.` The proof above is an unrestricted finite combinatorial argument; computer enumeration corroborates it and is not substituted for the proof. The displayed classification concerns only the stated four-letter parameter set.

## Relationship to prior work
Blackburn's 2013 preprint defines non-overlapping codes, provides general constructions and cardinality bounds, and does not classify GC-balanced optimal codebooks of this size. Yazdi, Kiah and Milenkovic's January 2016 preprint constructs GC-balanced weakly mutually uncorrelated codes, but does not enumerate length-four equality structures. The much closer **Stanovnik–Moškon–Mraz** 2024 preprint (2025 journal paper), Section 3, specifically studies polarity-balanced non-overlapping codes and reports optimal cardinalities at alphabet size four and lengths four, six, and eight. Thus the *size* twenty is prior-covered; the present statement is solely its explicit classification into twelve labeled codebooks and two symmetry types, not a new general construction or improvement of that published bound. The authors' more general maximality and partition constructions describe allowable structures but do not supply these twelve extremizers or their equivalence classes in the inspected text. Their earlier 2023 preprint/2024 article establishes analogous but **unconstrained** size and counting formulas for length four; those formulas cannot be restricted to the GC-balanced equality census by merely intersecting with balanced words, since optimization under intersection changes the maximizers.

## Limitations
This is a finite, four-symbol, length-four structural classification, not an asymptotic rate theorem and not a claim of biological validation or error-correction capability. No uniqueness among all unindexed writings is asserted. Although the closest polarity-balanced paper's full public text was inspected, an unindexed equality enumeration, or an unpublished specialization of the general partition method, remains a bibliographic originality risk. Some applications may require additional constraints that these twenty-word codebooks do not satisfy.

## References
1. S. R. Blackburn, *Non-overlapping codes*, arXiv:1303.1026, first publicly available 2013-03-05; IEEE Transactions on Information Theory 61 (2015), 4890–4894.
2. S. M. H. T. Yazdi, H. M. Kiah and O. Milenkovic, *Weakly Mutually Uncorrelated Codes*, arXiv:1601.08176, first publicly available 2016-01-29, especially Section 4.
3. L. Stanovnik, M. Moškon and M. Mraz, *In search of maximum non-overlapping codes*, arXiv:2307.12593, 2023; Designs, Codes and Cryptography 92 (2024), 1299–1326. DOI:10.1007/s10623-023-01344-z.
4. L. Stanovnik, M. Moškon and M. Mraz, *On maximal almost balanced non-overlapping codes and non-overlapping codes with restricted run-lengths*, arXiv:2410.18458, 2024; Computational and Applied Mathematics 44 (2025), 109. DOI:10.1007/s40314-024-03055-0.
