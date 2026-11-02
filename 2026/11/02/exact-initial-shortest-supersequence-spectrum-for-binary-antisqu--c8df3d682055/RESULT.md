# Exact initial shortest-supersequence spectrum for binary antisquares

## Finding
For \(k\ge1\), an **order-\(k\) antisquare** is a binary word \(x\overline{x}\) of length \(2k\), with \(|x|=k\) and bitwise complement \(\overline{x}\). A host covers this language when every one of its \(2^k\) antisquares occurs as a **scattered subsequence** (not necessarily as a contiguous factor).

The minimum host length is exactly \(4k-1\) **for every integer \(1\le k\le8\)**. For \(1\le k\le7\), an exhaustive classification gives the complete numbers of indexed hosts at this minimum, the palindromic-host counts, their reversal/complement symmetry-orbit counts, and the distribution of the ordinary subsequence-universality index (the maximum length for which *every* binary pattern is a scattered subsequence):

| \(k\) | shortest length | number of hosts | palindromic hosts | symmetry orbits | universality-index distribution |
|---:|---:|---:|---:|---:|---|
| 1 | 3 | 2 | 2 | 1 | \(1: 2\) |
| 2 | 7 | 10 | 2 | 3 | \(3: 10\) |
| 3 | 11 | 44 | 8 | 13 | \(4: 2\), \(5: 42\) |
| 4 | 15 | 190 | 10 | 50 | \(6: 28\), \(7: 162\) |
| 5 | 19 | 800 | 32 | 208 | \(7: 6\), \(8: 200\), \(9: 594\) |
| 6 | 23 | 3,266 | 38 | 826 | \(9: 58\), \(10: 1,102\), \(11: 2,106\) |
| 7 | 27 | 13,018 | 118 | 3,284 | \(11: 412\), \(12: 5,316\), \(13: 7,290\) |

For \(k=8\), length \(30\) admits no covering word, while the alternating word of length \(31\) covers all order-eight antisquares. The count of minimum-length hosts at \(k=8\) is **not claimed**.

## Assumptions and scope
The alphabet is the fixed, labeled binary alphabet \(\{0,1\}\). Host words are indexed, not identified under cyclic rotation. The symmetry-orbit column, separately, quotients by reversal and bitwise complementation. An occurrence is any strictly increasing list of host positions. No restriction is imposed on non-antisquare subsequences. All numerical classification results are finite and apply only within the stated ranges; there is no assertion of the minimum-length formula for \(k\ge9\).

## Proof
**Universal upper bound.** The alternating binary word starting and ending in \(0\) with length \(4k-1\) contains every binary word of length \(2k\) that has exactly \(k\) zeros and \(k\) ones, hence in particular every antisquare. To see this, greedy embedding of a binary target \(u\) in an alternating host starts at position \(1\) or \(2\), depending on the first symbol. Each subsequent change of target letter advances one position, while each repeated letter advances two positions. A balanced binary target has at least one change, hence no more than \(2k-2\) equal-adjacent pairs. Its last greedy position is therefore at most \(2+(2k-1)+(2k-2)=4k-1\).

**Exact finite lower bounds and counts.** For a fixed \(k\), index the \(2^k\) target antisquares by the integer \(j\) encoding their first halves. For a host prefix \(v\), define \(g_j(v)\) as the length of the longest prefix of the \(j\)-th antisquare that can be embedded in \(v\). A greedy leftmost embedding proves the exact recursion
\[
g_j(vb)=g_j(v)+\mathbf1\bigl[g_j(v)<2k\ \text{and}\ b=t_j[g_j(v)]\bigr],
\]
where target letters \(t_j[r]\) have zero-based indexing. Initially all values are zero. This recursion follows because an appended symbol can only extend the maximum embeddable target prefix by one, and the greedy earliest completion of each prefix never loses an embedding opportunity. A host of length \(L\) covers the language exactly when all \(g_j\) equal \(2k\).

An exhaustive depth-first enumeration visits both binary extensions of every viable prefix of length less than \(L\). At depth \(d\), the branch is discarded only if some target has \(g_j(v)+(L-d)<2k\). This test is **necessary for future completion** and therefore cannot prune a valid host: even if every remaining symbol matched, that target would remain incomplete. Induction on the binary prefix tree proves that every length-\(L\) covering word is counted exactly once. The source file `verify_antisquares.c` implements this recurrence and branch test with fixed-size arrays sufficient for \(k\le8\). For every \(1\le k\le8\), running it with \(L=4k-2\) returns zero; monotonicity under appending letters excludes all smaller lengths. At \(L=4k-1\), the same exhaustive algorithm returns the host counts in the table for \(k\le7\). The alternating construction above completes the finite minimum-length proof through \(k=8\).

**Refinement by universality and symmetry.** For every qualifying terminal host of length \(4k-1\), scan its characters left to right, increment an arch counter when both symbols have appeared since the preceding reset, and reset the seen-symbol set. The number of complete arches is exactly the ordinary scattered-subsequence universality index: concatenating one arbitrary symbol choice from each arch proves sufficiency, while choosing the final symbol of each completed arch followed by an absent symbol in the residual suffix proves that one further universal level is impossible. (This is the standard arch characterization.) The program accumulates the index histogram for each row. It also tests equality with the reversed word, yielding the palindromic-host count.

Reversal and bitwise complementation both map antisquares to antisquares, hence preserve covering hosts. Since every host length \(4k-1\) is odd, complement and reverse-complement have no fixed points. Burnside's lemma therefore gives \((H_k+P_k)/4\) orbits from the number \(H_k\) of covering hosts and the number \(P_k\) of palindromic covering hosts, as displayed in the table.

## Verification
The reproducible C11 verifier in `verify_antisquares.c` explicitly explores the entire surviving binary prefix tree. In the range \(1\le k\le7\), it checks both lengths \(4k-2\) and \(4k-1\), and prints all exact counts and index distributions. Its order-eight check at length \(30\) examines \(30{,}965{,}979\) prefix-tree nodes and returns no covering host. The verification does **not** attempt to count order-eight hosts of length \(31\).

A separate program, `verify_literal.c`, scans each complete binary host against every literal order-\(k\) antisquare independently of the prefix-state recurrence. Direct exhaustive checks at lengths \(4k-2\) and \(4k-1\) for \(1\le k\le5\) agree with all host counts, palindrome counts, and universality-index histograms from the first verifier. The exact algorithmic invariant above, not a sample of its outputs, supplies exhaustiveness.

## Relationship to prior work
Baranwal, Currie, Mol, Ochem, Rampersad, and Shallit study **contiguous** antisquare factors and their avoidance/critical exponents. Their definition motivates the pattern family, but a contiguous-factor statement does not imply this scattered-subsequence covering census. Adamson's work counts and ranks words universal for **all** fixed-length patterns; its ordinary universality index and arch method are used only for the index refinement. It does not enumerate hosts covering exactly the antisquare target language. General shortest-common-supersequence algorithms for arbitrary target sets do not supply the stated numerical or symmetry spectra without an additional exhaustive calculation.

## Limitations
The equality of minimum length with \(4k-1\) is proved only through order eight. It is not inferred for all orders from the eight tested values. Complete minimum-host enumerations and index spectra are proved only through order seven. The proof is an exhaustive finite computation justified by an exact recurrence and sound pruning; no closed form or asymptotic for the counts is established. An unlocated equivalent finite table or a broader theorem on restricted-language supersequences remains an originality risk. No independent mathematical audit has been performed.

## References
1. A. Baranwal, J. Currie, L. Mol, P. Ochem, N. Rampersad, J. Shallit, *Antisquares and Critical Exponents*, arXiv:2209.09223, initial public version September 19, 2022; Discrete Mathematics & Theoretical Computer Science 25:2 (2023).
2. D. Adamson, *Ranking and Unranking k-subsequence universal words*, arXiv:2304.04583, April 10, 2023. See especially definitions and the arch characterization in Sections 2–3.
3. K.-J. Räihä and E. Ukkonen, *The shortest common supersequence problem over binary alphabet is NP-complete*, Theoretical Computer Science 16 (1981), 187–198 (background on unrestricted SCS).
