# First finite two-list insertion–deletion separation for binary two-error codes

## Finding
For integers \(2\le n\le5\), let \(D_n\) and \(I_n\) be the largest sizes of binary length-\(n\) codes with at most two candidates after exactly two deletions and exactly two insertions, respectively. Then
\[
(D_2,D_3,D_4,D_5)=(2,3,4,4),\qquad
(I_2,I_3,I_4,I_5)=(2,3,4,6).
\]
Thus \(n=5\) is the first admissible length at which the two-list **maximum code sizes** separate for an equal two-error budget. At this length the insertion optimum is six codewords, versus four for deletions. The numbers of distinct *labeled optimal codebooks* for lengths \(n=2,3,4,5\) are, respectively, \((6,6,33,3089)\) for deletions and \((6,6,43,185)\) for insertions. The \(185\) length-five insertion-optimal codebooks form exactly \(52\) orbits under bit complementation and word reversal: \(41\) orbits of size four, ten of size two, and one of size one.

## Assumptions and scope
All alphabets are \(\{0,1\}\), the transmitted codeword length is \(n\), exactly two symbols are inserted or deleted, and received words are regarded as distinct strings regardless of the number of edit histories. The list limit is two *different source codewords*, not two edit histories. Let \(x\preceq y\) mean that \(x\) occurs in \(y\) as a scattered subsequence. A codebook \(C\subseteq\{0,1\}^n\) is insertion-admissible when
\[
\#\{x\in C:x\preceq y\}\le2\quad\text{for every }y\in\{0,1\}^{n+2};
\]
it is deletion-admissible when
\[
\#\{x\in C:y\preceq x\}\le2\quad\text{for every }y\in\{0,1\}^{n-2}.
\]
Lengths below two are not considered because the two-deletion output length would be negative. No claim is made for \(n\ge6\), other list sizes, or mixed error budgets.

## Proof
Encode each length-\(n\) word as an integer \(x\in\{0,\ldots,2^n-1\}\), with the leftmost binary symbol most significant. Represent any codebook by its \(2^n\)-bit characteristic mask \(K\). For each received word \(y\), define the exact integer incidence mask \(M_y\): its bit \(x\) is one if and only if \(x\preceq y\) in the insertion channel, or \(y\preceq x\) in the deletion channel. The two-list requirement is **equivalent**, without relaxation, to
\[
\operatorname{popcount}(K\mathbin{\&}M_y)\le2\quad\text{for every received }y.
\]
The predicate \(u\preceq v\) is computed exactly by scanning \(v\) left to right and advancing a pointer into \(u\) on each matching symbol; the scan reaches the end of \(u\) exactly when a subsequence embedding exists.

The standalone finite enumerator `insdel_exact.cpp` constructs *every* received-word incidence mask for each \(n\in\{2,3,4,5\}\), in both channels, and then enumerates every codebook of cardinality \(k\) by the standard increasing fixed-popcount bit-mask successor. Its exhaustive counts at the candidate maximum \(k\) and the immediately next cardinality are:

| Length | Channel | \(k\) | Admissible codebooks of size \(k\) | Admissible codebooks of size \(k+1\) |
|---|---|---:|---:|---:|
| 2 | deletion | 2 | 6 | 0 |
| 2 | insertion | 2 | 6 | 0 |
| 3 | deletion | 3 | 6 | 0 |
| 3 | insertion | 3 | 6 | 0 |
| 4 | deletion | 4 | 33 | 0 |
| 4 | insertion | 4 | 43 | 0 |
| 5 | deletion | 4 | 3089 | 0 |
| 5 | insertion | 6 | 185 | 0 |

In each line, a nonzero count proves attainability. A zero count at cardinality \(k+1\), together with the downward-closed nature of the list constraint, excludes all larger codebooks. This establishes both complete optimum vectors and all displayed labeled-optimum counts. For explicit size-optimal length-five examples, take the deletion-admissible codebook
\[
\{00000,00111,01000,01011\}
\]
and the insertion-admissible codebook
\[
\{00000,00001,01110,01111,10011,11000\}.
\]
Each received-word list for these examples has size at most two by direct incidence checking.

The file `maxima_n5_ins.csv` lists **all** \(185\) length-five optimal insertion codebooks as eight-hex-digit incidence masks in increasing order. For each mask \(K\), reverse each five-bit codeword, complement each five-bit codeword, or do both. These commuting involutions generate at most four masks. Direct application of these transformations to each listed mask gives precisely \(41\) four-element orbits, ten two-element orbits and one singleton orbit, with no mask outside the list. Since the actions preserve the subsequence relation, they preserve admissibility.

## Verification
Compile and run `insdel_exact.cpp` with a C++17 compiler. It directly scans all possible received words and enumerates all relevant constant-weight codebook masks. Compile and run `insdel_dp_verify.cpp` independently. This second checker **does not use received-word incidence masks**: it tests whether each three-word set has a shortest common supersequence of length at most \(n+2\) or a longest common subsequence of length at least \(n-2\), then enumerates forbidden-triple-free codebooks. The second route yields the identical eight optimum and next-level counts. Its forbidden-triple totals at length five are \(2776\) for deletions and \(2696\) for insertions. The full mask list is in `maxima_n5_ins.csv`. The standalone `verify_orbits.py` checks every listed codebook against all 128 possible insertion outputs, confirms 185 distinct codebooks and complete closure under reversal and complement, and verifies the 52-orbit partition. Since the independent fixed-weight enumerators find exactly 185 admissible size-six codebooks, this checked list is exhaustive.

The finite enumeration is exhaustive: at length five, there are \(32\) possible codewords, \(128\) possible two-insertion outputs, and \(8\) possible two-deletion outputs. Only finite claims are made; no extrapolation to arbitrary lengths is used. Both C++17 checkers, the complete witness list, and the Python 3 orbit/list checker are embedded with this result. They use only standard-language libraries.

## Relationship to prior work
The inequality between two-list insertion and deletion decodability is established in the general literature. Con, Doron and Ribeiro (2026) determine an asymptotic binary insertion list-decoding capacity, while Kiah, Wei and Zeng (2026) give constant-list bounds and insertion–deletion budget conversion. Banerjee, Con, Wachter-Zeh and Yaakobi (2026) investigate average list sizes for Varshamov–Tenengolts codes after two errors. These results concern asymptotic capacities, bounds or average behavior of restricted code families, not the exact all-codebook length-two-through-five enumeration above. An existing published length-six binary two-list two-deletion optimum concerns one different length and only the deletion channel; it does not determine this first finite separation or the insertion extremizers.

## Limitations
The result is a finite exact census, not an asymptotic improvement. Exhaustiveness depends on the supplied finite bit-mask enumeration and its independently implemented subsequence/supersequence recurrences. Independent external mathematical review has not been performed. A previously unindexed all-codebook table or computational search could contain overlapping values, so historical priority beyond the examined primary literature and mathematical-record searches is not certified.

## References
1. R. Con, D. Doron and J. Ribeiro, *The Insertion List-Decoding Capacity and an Improved Bound on the Deletion List-Decoding Capacity*, arXiv:2607.03989 (first posted 2026-07-04), https://arxiv.org/abs/2607.03989.
2. H. M. Kiah, H. Wei and R. Zeng, *Constant-List Insertion–Deletion Codes: New Bounds and an Improvement of Levenshtein's Lower Bound*, arXiv:2609.21395 (first posted 2026-09-18), https://arxiv.org/abs/2609.21395.
3. A. Banerjee, R. Con, A. Wachter-Zeh and E. Yaakobi, *On the Average List Size of VT Codes under Two Insertions or Two Deletions*, arXiv:2610.15767 (first posted 2026-10-11), https://arxiv.org/abs/2610.15767.
4. B. Haeupler, A. Shahrasbi and M. Sudan, *Synchronization Strings: List Decoding for Insertions and Deletions*, arXiv:1802.08663 (2018), https://arxiv.org/abs/1802.08663.
