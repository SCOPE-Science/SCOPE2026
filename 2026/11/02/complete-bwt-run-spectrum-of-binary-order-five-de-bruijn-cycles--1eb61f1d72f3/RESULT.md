# Complete BWT-run spectrum of binary order-five de Bruijn cycles

## Finding
For a binary de Bruijn **necklace** of order five—one circular binary word of length \(32\) containing each length-five binary word exactly once—let \(\mathcal B(w)\) denote the sentinel-free Burrows–Wheeler transform obtained by sorting all \(32\) cyclic rotations lexicographically and taking the preceding character of each row. Let \(r(w)\) be the number of maximal constant runs of the resulting **linear** transform string, with no wraparound run merger.

The exact, complete distribution over the \(2048\) different order-five necklaces is:

| \(r(w)\) | Number of necklaces |
|---:|---:|
| 20 | 38 |
| 22 | 426 |
| 24 | 840 |
| 26 | 608 |
| 28 | 130 |
| 30 | 6 |

Every other run count has multiplicity zero. In particular, the minimum is \(20\), the maximum is \(30\), and the mode is \(24\) (attained by \(840\) necklaces). This is an **exact finite classification**, not a claim for orders other than five.

## Assumptions and scope
The ordered alphabet is \(0<1\). A de Bruijn necklace of order \(5\) is an equivalence class modulo cyclic rotation of length-\(32\) binary words with pairwise distinct circular windows of length \(5\). Every such word is primitive, so its \(32\) cyclic rotations are distinct and their lexical sorting has no tie. Distinct indexed rotations of the same necklace are counted once, not \(32\) times. We do not insert an end marker. A *run* is a maximal nonempty contiguous block of identical letters in the **ordinary linear** BWT output; its first and last positions are not treated as adjacent.

## Proof
**Lemma 1 (block form).** Every relevant BWT string \(b=(b_0,\ldots,b_{31})\) is a concatenation of \(16\) two-bit blocks, each either \(01\) or \(10\). Indeed, two distinct length-five windows share every prescribed four-bit prefix, one followed by \(0\) and the other by \(1\). In the sorted rotation table these two rows are consecutive, and their preceding symbols are different: otherwise their preceding symbol followed by their common four-bit prefix would duplicate a five-bit circular window. Therefore the preceding symbols are exactly \(0\) and \(1\) in some order.

Write \(a=(a_0,\ldots,a_{15})\in\{0,1\}^{16}\) for the first bits of these blocks. Then \(b_{2i}=a_i\) and \(b_{2i+1}=1-a_i\). There are precisely \(2^{16}=65536\) candidate block orientations. The \(16\) transitions within blocks are all changes; the boundary from block \(i\) to block \(i+1\) is a change exactly when \(a_i=a_{i+1}\). Thus the linear run number is
\[
r(b)=17+\sum_{i=0}^{14}\mathbf1\{a_i=a_{i+1}\}.\tag{1}
\]

**Lemma 2 (single-necklace test).** For any candidate \(b\), its first-to-last-column map on zero-based row indices \(0,\ldots,31\) is
\[
\operatorname{LF}_b(j)=C_{b_j}+\#\{i<j:b_i=b_j\},\qquad C_0=0,\quad C_1=16.\tag{2}
\]
It is a permutation because \(b\) has exactly sixteen occurrences of each symbol. The candidate comes from a *single* order-five de Bruijn necklace if and only if \(\operatorname{LF}_b\) is one \(32\)-cycle. To justify the equivalence rather than merely invoke inversion: LF advances one position backward through each cyclic-rotation row. The inverse cyclic BWT therefore decomposes into one necklace per LF cycle. Moreover, the complementary-pair form and the uniqueness of the LF mapping force the length-five prefixes of the \(32\) sorted rows to be precisely the binary length-five dictionary; this is the standard de Bruijn-set inverse-BWT lemma, also proved in Higgins (2012), Section 3, Theorem 3.4 and Lemmas 3.6–3.7. Hence if LF has one cycle, those dictionary rows are rotations of one de Bruijn word. If it has several cycles, its inverse consists of multiple necklaces, not a single de Bruijn necklace. Distinct one-cycle columns invert to distinct necklaces.

**Exhaustive finite count.** The following fully specified finite algorithm counts all cases, with no sampling or truncation. Iterate the integer \(m\) over \(0\le m<65536\), set \(a_i=\lfloor m/2^i\rfloor\bmod 2\), construct \(b\) from the above blocks, and construct LF by (2). Beginning at row zero, apply LF until a row repeats; retain the orientation exactly if this orbit has length \(32\). For each retained orientation, evaluate (1) and increment its run-count bin. The complete executable `checker.py` carries out precisely this enumeration and uses integer-only operations. It checks that all 65536 masks are considered, yields \(2048\) accepted one-cycle columns, and exactly the six-bin table in the Finding. As all possible input masks have been exhausted and Lemmas 1–2 are biconditional, this finishes the finite proof.

As an algorithmically independent check, the same `checker.py` constructs **every Euler circuit** in the order-four binary de Bruijn digraph, rooting each at the unique all-zero five-bit edge. Each other length-five binary edge is used exactly once, and returning to the initial four-bit vertex yields exactly one representative per necklace. It directly verifies all \(32\) length-five cyclic windows and recomputes the BWT from sorted rotations without using the LF column generator. That second exhaustive path produces \(2048\) distinct necklaces, the identical six-bin histogram, and the exact same set of \(2048\) BWT last columns. The independent construction guards against indexing, orientation, or inversion implementation mistakes.

## Verification
Run `python3 checker.py` with standard-library Python 3. The program must print three PASS lines and exit with status zero; it internally asserts the complete distribution \(\{20:38,22:426,24:840,26:608,28:130,30:6\}\), the \(2048\) count, all de Bruijn window conditions, agreement of the two complete enumeration procedures and equality of their BWT-column sets. Both procedures were executed successfully from the embedded checker source. This is an exhaustive \(2^{16}\)-case certificate, not a statement inferred from small samples.

## Relationship to prior work
Higgins, *Burrows–Wheeler transformations and de Bruijn words* (2012), Section 3, gives the inverse-transform and complementary-block results on which the finite counting reduction depends. Ruskey, Sawada and Williams (online May 8, 2012), treat constructive de Bruijn cycles for fixed-weight words; their sequence-generation results do not classify BWT runs of the full binary order-five necklace set. Lipták and Parmigiani (2024) explicitly give random BWT-based de Bruijn generation and the order-five total but not this run histogram. Fici and coauthors (2025), Proposition 32, derive general upper and lower run bounds (for order five: \(18\) and \(30\)); their result does not determine the sharper **attained** minimum \(20\) or any exact multiplicity. Date and Zatesko (2025) study specially constructed LFSR de Bruijn strings with a minimal-run BWT pattern; this does not enumerate all order-five necklaces or the six class sizes. Searches for the precise array, BWT-run aliases, inverse LF formulations, and stronger dominating statements located no such full classification in the inspected primary texts. Absence of an indexed record is not a proof of historical novelty.

## Limitations
The theorem is an exact finite fact at order \(5\), not a uniform formula or asymptotic claim across de Bruijn orders. The number of BWT runs is for the sentinel-free **linear output of the circular-rotation** transform, not the sentinel-terminated transform and not cyclic wraparound merging of output runs. The proof uses a complete, reproducible finite enumeration with a mathematical correspondence; it does not replace that exhaustive check with a short closed-form symbolic multiplicity calculation. Uninspected literature or databases could contain an equivalent table; no independent expert audit has been performed.

## References
1. Peter M. Higgins, “Burrows–Wheeler transformations and de Bruijn words,” *Theoretical Computer Science* **457** (2012), 128–136. DOI: https://doi.org/10.1016/j.tcs.2012.07.019 . Full authorized author version: https://arxiv.org/pdf/1901.08392 , Section 3 (2019 re-upload of the 2012 article, not the first-public date).
2. Frank Ruskey, Joe Sawada, and Aaron Williams, “De Bruijn Sequences for Fixed-Weight Binary Strings,” *SIAM Journal on Discrete Mathematics* **26** (2012), 605–617. DOI: https://doi.org/10.1137/100808782 . Publisher records online publication on May 8, 2012.
3. Zsuzsanna Lipták and Luca Parmigiani, “A BWT-based algorithm for random de Bruijn sequence construction,” (2024). https://iris.univr.it/handle/11562/1120694 .
4. Gabriele Fici, Sabrina Mantaci, Antonio Restivo, Giuseppe Romana, Giovanna Rosone, and Marinella Sciortino, “BWT and Combinatorics on Words,” (2025), Proposition 32. https://doi.org/10.4230/OASIcs.Manzini.1 .
5. Vinicius T. V. Date and Leandro M. Zatesko, “On the near-tightness of \(\chi\le2r\): a general \(\sigma\)-ary construction and a binary case via LFSRs,” arXiv:2512.20598 (2025), Section 4. https://arxiv.org/abs/2512.20598 .
